# Viewing and Extracting Game Assets with FModel

*FModel* is a powerful *UE4/5* asset viewer and unpacker. In my opinion, its importance in modding comes second only to *UE4SS*. For *R-Type Final 2*, both the *AES key* and *.usmap mapping files* are required to unpack assets properly.

## Selecting the Directory

1. Open *FModel* and click `Settings` in the top menu.
2. Configure the following two settings:
   - `Archive Directory`: Set this to the `RTypeFinal2` folder inside the game directory.  
     (Example: `D:\Program Files (x86)\Steam\steamapps\common\R-Type Final 2\RTypeFinal2`)
   - `UE_Versions`: Select `GAME_UE4_26`
3. Click `OK` to save the changes.

If set up correctly, you should see the game's `.pak` files listed on the left. However, they will still appear gray, which means they are encrypted and cannot yet be unpacked.

Currently, the `Directory -> Selector` option in *FModel*’s menu seems to offer automatic game detection and setup—it might be worth trying.

## Loading the AES Key

1. Open the top menu `Directory -> AES`.
2. Try the AES keys exported using *AESKeyFinder*, one by one.
3. Once the correct key is entered, the `.pak` filenames on the left will turn from gray to white, indicating successful decryption.

At this point, you can start unpacking the basic content. Change the `Loading Mode` to `ALL`, click `Load`, then switch to the `Folders` tab. You will see the game's assets and directory structure. However, previewing or exporting will still result in errors at this stage.

## Loading the `.usmap` Mapping Files

1. Click `Settings` from the menu.
2. In the `ADVANCED` section, check the `Local Mapping File` option.
3. Set the `Mapping File Path` to the location where you exported the `.usmap` files earlier.

You should now be able to preview and extract assets without issues.
