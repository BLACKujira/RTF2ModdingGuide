# Resource Packing Method Analysis

This article covers the technical details of *R-Type Tactics II*'s resource packing and unpacking. It's intended for those who are curious about the inner workings. If you're only looking to unpack the files, using the `extract_rtt2_dat.py` script is sufficient—you don’t need to understand these details.

Since a lot of time has passed between the research and the writing of this document, some parts may be incomplete or inaccurate. To help verify or correct information, I’ve shared the [original conversation with ChatGPT during script development](https://chatgpt.com/share/680303d4-fa94-800e-b3fb-d1c977266b5e).

## Main DAT/FAT Files

These refer to the `CMN.DAT` and `CMN.FAT` files located in `PSP_GAME\USRDIR\CMN`.  
`CMN.FAT` contains file names, sizes, and positions. `CMN.DAT` stores the actual file data.

### Main FAT File

This file consists of a `256-byte header` + `file info section` + `file name section`.

#### Header

- Starts with the fixed string `FAT `
- At offset `0xF8` is a 32-bit integer marking the end of the file info section.

#### File Info Section

Each file takes up 16 bytes and is represented by four 32-bit integers:

`File start offset in .DAT`, `File size`, `0000`, `Filename offset in .FAT`

#### File Name Section

File names are null-terminated (`0x00`), with no separate length variable.

### Main DAT File

A single file made up of many concatenated resources. Start offsets and sizes are recorded in `CMN.FAT`.

## Sub DAT/FAT Files

These refer to *DAT/FAT files* extracted from the *main DAT/FAT file*. They work similarly to folders or compressed archives.

### Sub FAT Files

Similar to the *main FAT file*, but with key differences:

- Only a few *sub FAT files* have corresponding `.DAT` files. Most include a `file content section` appended after the `filename section`.
- If a `.FAT` file contains file content, offset `0xFC` stores the starting point of that content (not 0).
- File names may contain `/`. The script does not create folders for performance reasons.
- Actual file position = content section start + file start offset
- Files in `.FAT` are **GZIP-compressed**

### Sub DAT Files

Identical in format to the *main DAT file*.

## XIM and XMO Files

These are texture, animation, and model files extracted from the archives and require a bit of processing.

### XIM Files

`.XIM` files are actually `.GIM` files. Simply rename the extension to `.GIM` for easier reading.

### XMO Files

`.XMO` files are GZIP-compressed `.GMO` files with an extra 4-byte header. The GZIP data begins at offset `0x04`.
