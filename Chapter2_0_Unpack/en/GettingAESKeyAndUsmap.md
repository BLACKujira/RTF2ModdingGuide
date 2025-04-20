# Obtaining AES Key and .usmap Mapping Files

Like many UE4/5 games, *R-Type Final 2* encrypts its resource files and uses a custom mapping format. To unpack or modify in-game resources, you'll typically need both the *AES key* and the *.usmap mapping files*.

## Obtaining the AES Key

Download [AESKeyFinder](https://github.com/GHFear/AESKeyFinder-By-GHFear), and follow the first method described in [this guide](https://github.com/Dmgvol/UE_Modding/blob/main/TheBasics/AesKey.md). Copy `RTypeFinal2-Win64-Shipping.exe` into the *AESKeyFinder* folder, then run the script to extract the key.

In the current version, four keys will be extracted—only one of them is valid.

## Extracting `.usmap` Mapping Files

There are two ways to do this. The simpler way is to use *UE4SS* to export `.usmap` mapping files. Follow [this tutorial](https://github.com/Dmgvol/UE_Modding/blob/main/TheBasics/Extractingusmap.md) for instructions.

Alternatively, you can use [Dumper-7](https://github.com/Encryqed/Dumper-7). Download or clone the project and compile it. Then use *any DLL injector* to inject it into the game process. The exported content will include the `.usmap` files.

## Tool Requirements for These Files

| Tool       | Requires AES Key | Requires `.usmap` Mapping File |
|------------|------------------|-------------------------------|
| FModel     | ✅                | ✅                             |
| UModel     | ✅                | ❌                             |
| UAssetGUI  | ❌                | ✅                             |
