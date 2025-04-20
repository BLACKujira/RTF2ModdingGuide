import struct
import os
import gzip
from io import BytesIO

def extract_files(dat_path, fat_path, output_dir, extracted_files):
    """ 解包 dat/fat 文件（支持 FAT 内含数据，修正 XIM/XMO 处理） """
    # Unpack dat/fat files (supports embedded data in FAT and fixes for XIM/XMO)

    with open(fat_path, "rb") as fat_file:
        fat_data = fat_file.read()

    # 读取 file_info_end (0xF8) 和 文件内容偏移量 (0xFC)
    # Read file_info_end (at 0xF8) and file data offset (at 0xFC)
    file_info_offset = 0x100
    file_info_end = struct.unpack("<I", fat_data[0xF8:0xFC])[0]
    file_data_offset = struct.unpack("<I", fat_data[0xFC:0x100])[0]

    # 如果 FAT 是空文件夹（大小 == 0x100）
    # If FAT file is an empty folder (size == 0x100)
    if len(fat_data) == 0x100:
        print(f"Skipping empty folder: {fat_path}")
        return

    # 如果 FAT 里没有直接存储文件数据（file_data_offset == 0），需要 DAT 文件
    # If FAT does not contain file data directly (file_data_offset == 0), DAT file is needed
    need_dat = file_data_offset == 0

    # 如果需要 DAT，但 DAT 不存在，直接跳过
    # If DAT file is needed but missing, skip this entry
    if need_dat and not os.path.exists(dat_path):
        print(f"Missing DAT file: {dat_path}, skipping {fat_path}")
        return

    # 读取 DAT 文件（如果需要）
    # Read DAT file if needed
    dat_data = b""
    if need_dat:
        with open(dat_path, "rb") as dat_file:
            dat_data = dat_file.read()

    entry_size = 16
    file_entries = []

    # 解析 FAT 文件
    # Parse FAT file for file entries
    for i in range(file_info_offset, file_info_end, entry_size):
        entry = fat_data[i:i + entry_size]
        if len(entry) < entry_size:
            break

        offset, size, _, name_offset = struct.unpack("<I I I I", entry)

        # 读取文件名
        # Read file name string from offset
        name_start = name_offset
        name_end = fat_data.find(b'\x00', name_start)
        file_name = fat_data[name_start:name_end].decode('utf-8', errors='ignore')

        # 替换文件名中的 / 和 \ 为 _ 避免路径错误
        # Replace slashes to avoid path issues
        file_name = file_name.replace("/", "_").replace("\\", "_")

        file_entries.append((offset, size, file_name))

    # 创建输出目录
    # Create the output directory
    os.makedirs(output_dir, exist_ok=True)


    # 提取文件
    # Extract files from data sources
    for offset, size, file_name in file_entries:
        if need_dat:
            # 从 DAT 里读取数据
            # Read data from DAT file
            file_data = dat_data[offset:offset + size]
        else:
            # 从 FAT 里读取数据（偏移量相对于 file_data_offset）
            # Read data from FAT file (offset is relative to file_data_offset)
            file_data = fat_data[file_data_offset + offset:file_data_offset + offset + size]

            # 解压缩文件数据（如果是 GZIP 压缩的）
            # Try decompressing if data is GZIP-compressed
            try:
                with gzip.GzipFile(fileobj=BytesIO(file_data), mode='rb') as gzip_file:
                    file_data = gzip_file.read()
            except Exception as e:
                print(f"Failed to decompress {file_name}: {e}")

        # XIM 处理：重命名为 .gim
        # XIM handling: rename to .GIM
        if file_name.lower().endswith(".xim"):
            file_name = file_name[:-4] + ".GIM"

        # XMO 处理：解压 GZIP 并重命名为 .gmo
        # XMO handling: extract GZIP and rename to .GMO
        elif file_name.lower().endswith(".xmo"):
            if len(file_data) > 4:
                gzip_offset = struct.unpack("<I", file_data[4:8])[0]  # 读取 4h 位置 Read offset from byte 0x04
                if 0 <= gzip_offset < len(file_data):
                    try:
                        with gzip.GzipFile(fileobj=BytesIO(file_data[gzip_offset:]), mode='rb') as gzip_file:
                            file_data = gzip_file.read()
                            file_name = file_name[:-4] + ".GMO"  # 修改扩展名 Change extension to .GMO
                    except Exception as e:
                        print(f"Failed to decompress XMO {file_name}: {e}")

        # 写入文件
        # Write extracted file to disk
        output_path = os.path.join(output_dir, file_name)

        with open(output_path, "wb") as out_file:
            out_file.write(file_data)

        print(f"Extracted: {output_path} ({len(file_data)} bytes)")

        # 记录解包出的文件
        # Record extracted file path
        extracted_files[file_name] = output_path


def process_folders(output_dir, extracted_files):
    """ 递归处理所有 FAT 文件 """
    # Recursively process all FAT files found during extraction

    # 创建字典的副本来避免在迭代时修改字典
    # Create a copy of the dictionary to avoid modification during iteration
    for fat_file, fat_path in list(extracted_files.items()):
        if fat_file.upper().endswith(".FAT"):
            new_output_dir = os.path.join(output_dir, fat_file.replace(".FAT", ""))
            dat_file_name = fat_file.replace(".FAT", ".DAT")

            # 可能没有 DAT 文件
            # DAT file might be missing
            dat_path = extracted_files.get(dat_file_name, "")

            extract_files(dat_path, fat_path, new_output_dir, extracted_files)

# 主程序
# Main program
dat_dir = r"E:\Games\hr-rtt2\PSP_GAME\USRDIR\CMN\CMN.DAT"
fat_dir = r"E:\Games\hr-rtt2\PSP_GAME\USRDIR\CMN\CMN.FAT"
output_dir = r"E:\Games\hr-rtt2\Output1"

# 记录所有已解包的文件
# Store all extracted file paths
extracted_files = {}

# 第一步：解包根目录 FAT/DAT
# Step 1: Extract root FAT/DAT
extract_files(dat_dir, fat_dir, output_dir, extracted_files)

# 第二步：递归处理子 FAT
# Step 2: Recursively extract nested FATs
process_folders(output_dir, extracted_files)

print("All files extracted successfully!")
