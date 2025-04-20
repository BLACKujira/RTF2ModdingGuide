# Resolving Issues with Custom Materials Not Displaying or Crashing

When creating *Blueprint Mods* or *PAK Mods*, you may encounter an issue where custom materials do not display properly, instead showing as the default gray checkerboard pattern.

In fact, this is a very common issue, and people ask about it almost every month in the UE4 modding community. In some games, this issue cannot be resolved at all, but fortunately, *R-Type Final 2* is not one of them.

## Solution

As with the *Animation Blueprint Update Event crash*, the first step is to replace the configuration files in the project's `Config` folder with the game's default configuration files.

Next, go to `Project Settings` -> `Packaging` and uncheck `Shared Material Shader Code`.

If you only *replace the configuration files* without unchecking *Shared Material Shader Code*, the custom materials will still not display correctly.

If you only uncheck *Shared Material Shader Code* without *replacing the configuration files*, the game will crash after generating an *Actor* with custom materials.

If both are confirmed to be correct but custom materials still do not display, check if the *Material* and *Material Instances* are properly packaged into the correct PAK file.
