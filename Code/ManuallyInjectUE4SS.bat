@echo off
set GAME_EXE="RTypeFinal2-Win64-Shipping.exe"
set MOD_DLL="UE4SS.dll"
set BACKUP_FILE="RTypeFinal2-Win64-Shipping.exe~"

echo Checking for backup file...
if exist %BACKUP_FILE% (
    echo Backup file detected: %BACKUP_FILE%
    echo Injection skipped to avoid overwriting the backup file.
    pause
    exit
)

echo Injecting DLL...
setdll.exe -d:%MOD_DLL% %GAME_EXE%

if %errorlevel% neq 0 (
    echo Injection failed! Please check the file paths and permissions.
) else (
    echo Injection successful! Launching the game...
    start %GAME_EXE%
)

echo Press any key to exit...
pause