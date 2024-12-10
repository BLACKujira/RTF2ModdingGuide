# Manually Injecting UE4SS

If UE4SS does not launch alongside the game despite being installed correctly, check if there is a UE4SS.log file in the UE4SS installation directory. If it is missing, UE4SS has failed to automatically inject into the game process. In this case, you need to manually inject the DLL.

This issue is known to occur on Windows 7 and earlier systems, but there is no evidence to suggest that it is exclusively related to the operating system.

## Preparing a DLL Injector

I recommend using `setdll.exe` from Microsoft's `Detours` project to inject the DLL. Since `Detours` is officially maintained by Microsoft, it won't be flagged as a virus.

`setdll.exe` injects the DLL into the game's executable, allowing it to automatically run with the game on startup without requiring manual injection every time.

If you trust me, you can download the precompiled `setdll.exe` from the [Releases](https://github.com/BLACKujira/RTF2ModdingGuide/releases) section. Alternatively, you can clone the [detours](https://github.com/microsoft/detours) repository and compile it yourself. The compiled `setdll.exe` can be found in the `bin.X64` folder.

## Alternative: Using Commands to Inject the DLL

Since the injector, DLL, and target file are fixed, I have created a batch script to simplify the injection process.

1. First, download `setdll.exe` and `ManuallyInjectUE4SS.bat` from the [Releases](https://github.com/BLACKujira/RTF2ModdingGuide/releases) section.
2. Move both `setdll.exe` and `ManuallyInjectUE4SS.bat` into the `RTypeFinal2\Binaries\Win64` folder, which is where `RTypeFinal2-Win64-Shipping.exe` and `UE4SS.dll` are located.
3. Double-click to run `ManuallyInjectUE4SS.bat`. This will open the **Command Prompt**, which will execute the manual injection of `UE4SS.dll`.

- If the injection is successful, the **Command Prompt** will display a long list of DLL names, followed by `Injection successful! Launching the game...`, and then it will launch the game. All other outputs indicate injection failure.
- If the message `Injection skipped to avoid overwriting the backup file.` is shown, it means the script detected an existing backup file from a previous injection, and injection has been skipped to avoid overwriting it.

## Using Commands to Inject the DLL

If the injection script fails, you can try injecting the DLL manually using the following method.

For **Windows 10** and later, press `Win + X` and select **Command Prompt** or **PowerShell** from the menu.

For **Windows 7** and earlier, open the Start menu, choose **Run**, and type `CMD` to open the **Command Prompt**.

In the **Command Prompt** or **PowerShell**, input the following command:
```
"(location_of_setdll.exe)/setdll.exe" d:"(game_directory)/RTypeFinal2/Binaries/Win64/UE4SS.dll" "(game_directory)/RTypeFinal2/Binaries/Win64/RTypeFinal2-Win64-Shipping.exe"
```
- Replace `(location_of_setdll.exe)` and `(game_directory)` with the corresponding directories on your computer.
- Do not remove the double quotes from the command unless you are sure of what you are doing.

Press Enter. If the injection is successful, the `RTypeFinal2-Win64-Shipping.exe` file will be updated, and a backup file named `RTypeFinal2-Win64-Shipping.exe~` will be created.

If you see a permission error, run the **Command Prompt** or **PowerShell** as an administrator.

**Important: Do not inject multiple times**, as it will overwrite the `RTypeFinal2-Win64-Shipping.exe~` backup file with the already injected executable.

## Verifying the Installation

Start the game. If the UE4SS console window launches alongside the game, the manual injection was successful.

To remove UE4SS, simply overwrite `RTypeFinal2-Win64-Shipping.exe` with the backup file `RTypeFinal2-Win64-Shipping.exe~`.

