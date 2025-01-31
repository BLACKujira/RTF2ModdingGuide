# In-Game Console Commands

Unreal Engine provides an in-game console that allows developers to control the game or display useful information, making it easier to debug. Normally, this console is disabled in the final version of the game. However, *UE4SS* includes a feature to unlock the in-game console.

This tutorial lists some known console commands that can be used in *R-Type Final 2* and their functions. These are not all of the available commands, as some commands from other tutorials may not work in *R-Type Final 2*.

By default, pressing `F10` once will open the console for command input, and pressing it again will display the console output.

## Command List

- `slomo <game speed>`: Adjust the game's speed. It works like the slowdown feature in Easy Mode. For example, `slomo 0.5` sets the game speed to half of the normal speed. The speed resets when the game is paused.
- `r.SetRes <resolution>`: Set the game resolution. Adding `f` makes it fullscreen, and adding `w` sets it to windowed mode. For example, `r.SetRes 1920x1080f`, `r.SetRes 1600x900`. It allows you to bypass the *16:9* aspect ratio limit.
- `FOV <FOV size>`: Change the camera's field of view. The default value is 32.
- `Stat LEVELS`: Displays the current level and the maps it consists of.
- `GAMMA <gamma value>`: Adjust the scene's brightness.
- `r.TonemapperFilm <0,1>`: Enable/Disable post-processing effects in the map.
