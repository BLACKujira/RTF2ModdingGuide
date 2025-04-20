import json
import re

# 加载 JSON 数据（假设这些数据已经作为 Python 对象载入）
with open(r"C:\Users\KUROKAWA_KUJIRA\Desktop\8\PlayerDefs.json", encoding="utf-8") as f:
    player_defs_data = json.load(f)

with open(r"C:\Users\KUROKAWA_KUJIRA\Desktop\8\playerParam_ship_ja.json", encoding="utf-8") as f:
    player_param_data = json.load(f)

with open(r"C:\Users\KUROKAWA_KUJIRA\Desktop\8\EBODY_NO.cpp", encoding="utf-8") as f:
    enum_text = f.read()

# 解析 EBODY_NO 枚举
enum_id_map = {}
pattern = re.compile(r'\bBD_([A-Z0-9_]+)\b')
id_counter = 0
for line in enum_text.splitlines():
    match = pattern.search(line)
    if match:
        key = match.group(1)
        if key not in enum_id_map:
            enum_id_map[key] = id_counter
            id_counter += 1
    elif "BD__" in line:
        enum_id_map["255"] = 255  # 特殊处理

# 解析 PlayerDefs
player_entries = player_defs_data[0]["Properties"]["PlayerDefs"]["Tables"]
name_map = player_param_data[0]["Rows"]

markdown_lines = [
    "| ID | 枚举名 | Code | 机体名 |",
    "|----|--------|------|--------|"
]

for entry in player_entries:
    enum_full_key = entry["Key"]  # e.g., "EBODY_NO::BD_R9A"
    enum_name = enum_full_key.split("::")[1]  # BD_R9A
    code = entry["Value"].get("Code", "")
    name_key = entry["Value"].get("NameKey", "")
    name_entry = name_map.get(name_key, {})
    localized_name = name_entry.get("SourceString", {}).get("LocalizedString", "")
    id_val = enum_id_map.get(enum_name.replace("BD_", ""), "")  # match C++ enum style

    markdown_lines.append(f"| {id_val} | {enum_name} | {code} | {localized_name} |")

# 输出 Markdown 表格
markdown_output = "\n".join(markdown_lines)
print(markdown_output)
