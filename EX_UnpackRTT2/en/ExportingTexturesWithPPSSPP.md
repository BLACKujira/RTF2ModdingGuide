# Exporting Textures Using PPSSPP

This is an alternative method for extracting textures. If you only need a **small number of textures** and **already have a completed save file**, using PPSSPP is a simpler and more intuitive solution.

However, if you need a large number of textures, or both models and textures, it’s recommended to use the unpacking script as described in [Unpacking the Main Resource File](UnpackingMainResourceFile.md).

## Steps

1. Open `PPSSPP` and go to the settings menu.
2. Navigate to `Tools` -> `Developer Tools`.
3. Enable `Save new textures`.
4. Run the game and enter a level that contains the textures you want.

The textures from that level will be saved in the `memstick\PSP\TEXTURES\NPJH50119\new` folder inside your PPSSPP directory.

### Note:
One downside of this method is that if the texture’s width and height are not equal, the shorter side will be padded with extra data, so cropping may be necessary.

## Transferring Save Data

Many people may choose to play this game on mobile devices. While *PPSSPP* on Android can also save textures, transferring your save data to a PC makes the extraction process easier.

By default, save data on Android devices can be found in `storage/emulated/0/PSP`. You can also check the save data location in the *PPSSPP* settings. To use the save data on your PC, simply copy the desired save folder to `memstick\PSP\SAVEDATA` under your PC's *PPSSPP* directory.
