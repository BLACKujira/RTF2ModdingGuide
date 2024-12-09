# Installing UE4SS
Before developing or using mods for *R-Type Final 2*, installing UE4SS is an essential first step.

`UE4SS` is a powerful tool that provides support for two main types of mods—`LUA Mods` and `Blueprint Mods`. It also includes features like viewing and editing in-game objects, exporting map files, and generating header files. Most of the following content relies on UE4SS as a foundation.

In this tutorial, we will learn how to install the developer version of `UE4SS v3.0.0`, upgrade it to `v3.0.1`, verify the installation, and troubleshoot potential issues.

## Downloading UE4SS
First, visit the [UE4SS-RE/RE-UE4SS](https://github.com/UE4SS-RE/RE-UE4SS) repository. Click on the [Releases](https://github.com/UE4SS-RE/RE-UE4SS/releases) section on the right side of the page and download `zDEV-UE4SS_v3.0.1.zip`. Scroll down and also download `zDEV-UE4SS_v3.0.0.zip`.

Note: Both versions need to be downloaded because `v3.0.0` must be installed before upgrading to `v3.0.1`.

## Locating the Installation Directory
For the Steam version, right-click the game icon, select `Manage` -> `Browse Local Files` from the menu. This will open the game’s installation directory. You should see an executable named `RTypeFinal2.exe` and folders like `Engine` and `RTypeFinal2`. If you purchased the OST, there will also be an OST folder.

![GameDir](../image/GameDir.png)

Open the `RTypeFinal2` **folder**, then navigate to the `Binaries` folder, and finally to the `Win64` folder. Here, you should see a file named `RTypeFinal2-Win64-Shipping.exe`. This is the installation directory for UE4SS.

## Installing UE4SS v3.0.0
Extract all the contents of `zDEV-UE4SS_v3.0.0.zip` into the installation directory. If done correctly, the folder should look like the image below.

![AfterInstall](../image/AfterInstall.png)

Now, launch the game. If the installation was successful, you should see the UE4SS console launch alongside the game. If not, double-check the steps above. If everything seems correct and it still doesn’t work, please refer to the [Manual Injection of UE4SS](ManualInjectionUE4SS.md) guide for a solution.

If the console appears blank, don't worry. This issue can be resolved after upgrading to `v3.0.1`.

## Upgrading to UE4SS v3.0.1
Extract the contents of `zDEV-UE4SS_v3.0.1.zip` into the same directory, overwriting any files with the same name. This upgrades UE4SS to version `v3.0.1`.

## Resolving Console Display Issues
If the UE4SS console is entirely black or white, locate the `UE4SS-settings.ini` file in the UE4SS installation directory.

Open the file with any text editor. Find the line `GraphicsAPI = opengl` and change it to `GraphicsAPI = dx11`.

![FixGuiConsole](../image/FixGuiConsole.png)

## What’s Next...
If UE4SS is installed successfully, you can now start installing mods. The installation method varies depending on the type of mod. Refer to the following tutorials to install different types of mods:
- [Installing Blueprint Mods](InstallingBlueprintMods.md)
- [Installing LUA Mods](InstallingLUAMods.md)

Some mods may require the installation of both `LUA Mods` and `Blueprint Mods` components to work correctly.

## Additional Reading: Why Use the Developer Version of the Latest UE4SS
The developer version has the console enabled by default, making it easier for beginners to verify whether UE4SS is functioning correctly without modifying configuration files. The console also outputs information useful for determining if a mod is properly installed.

Additionally, since weapon, unit, and level data are stored in data tables in the game, adding these elements with multiple mods requires runtime additions to the data tables to avoid conflicts rather than overwriting the original data.

Although this feature is not yet available in the current version of UE4SS, it may be introduced in a future release. To prepare for future upgrades, it’s recommended to use the latest version (`v3.0.1`) for mod development and loading.