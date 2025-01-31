# UE4 Version Selection

By checking the properties of the game's executable file, you will find that it uses the *UE4* version `4.26.0.0`. Naturally, using the same engine version as the game for *Blueprint Mod* development is the best choice. However, the *Epic Launcher* no longer offers older versions for download, only the latest `4.26.2` and `4.26 Chaos`.

In fact, both of these versions can be used for *Blueprint Mod* development, but I strongly advise against using `4.26 Chaos`. In this version, any 3D models imported from external sources, whether in `.fbx` or `.obj` format, will cause the game to crash. Strangely, it seems that *Mesh* in Unreal Engine project templates doesn't have this issue, but exporting and re-importing these files still leads to a crash.

It seems that part of the Chaos system is also used in the game, but the header files compile fine in the standard `4.26.2`, so I may have misunderstood. For now, let's proceed as is. If I can get `4.26.0`, that might be the best option.
