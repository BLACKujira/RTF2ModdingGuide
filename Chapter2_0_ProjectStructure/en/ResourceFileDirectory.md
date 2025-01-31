# Resource File Directory

When you load all the pak files in the game using *FModel* or similar *Pak extractors*, you'll first see two folders: `Engine` and `RTypeFinal2`. The `Engine` folder only contains resources that come with Unreal Engine, while `RTypeFinal2` is where the game content is stored. Expanding this folder, you will find the following three subfolders:

| Folder Name  | Description                                  |
|--------------|----------------------------------------------|
| Config       | Folder containing game configuration files  |
| Content      | Folder containing the main game content     |
| Plugins      | Folder containing DLC and additional level content |

## Config Folder
Just like in Unreal Engine projects, there are three main configuration files: `DefaultEngine`, `DefaultGame`, and `DefaultInput`. For some reason, each configuration file has several variants, but the variants of `DefaultGame` and `DefaultInput` don’t seem to differ much. The true variant of `DefaultEngine` has not been determined yet.

It’s worth noting that `DefaultGame` defines the starting level for each route. You can modify these definitions to make the game start from different levels, which is useful for custom levels.

These configuration files can be dynamically modified in *UE4SS* debugging tools, but note that they are not instances.

## Content Folder
This is the main resource folder for the game. The folders here serve the following purposes. The bolded rows indicate folders that are especially important for data mining and mod development.

| Folder Name  | Description                                  |
|--------------|----------------------------------------------|
| Animations   | Poses for the pilot on the personal profile page |
| **character** | **Almost all 3D models, bones, animations, and materials** |
| Credit       | Credits for the developers                     |
| Data         | Other important encrypted data from BydoLab |
| Debug        | Developer debug content, including level lists and debug UI |
| Demo         | Cutscenes during takeoff (real-time rendered) |
| **Design**   | **UI and textures used in UI, many high-resolution artworks** |
| Developers   | Developer content, including three test enemy levels |
| DynamicVolumetricSky | Likely an external library related to the sky |
| **Enemy**    | **Definitions and parameters for enemies**   |
| Fade         | Likely related to fade-in and fade-out effects |
| FX           | Special effects related meshes, materials, and Niagara particles |
| item         | Five types of in-game items                  |
| **Level**    | **Levels and museum maps**                   |
| Localization | Possibly deprecated localization content     |
| map          | Models, materials, and textures for map objects |
| Movies       | Possibly deprecated animations               |
| MoviesPak    | Opening animations (video)                   |
| MWRedwoodForest | Likely an external library                |
| Object       | Objects that can be placed on the personal profile page |
| PadShakes    | Likely related to controller vibration effects |
| plan         | Part of blueprint function library           |
| **Player**   | **Definitions for planes, weapons, forces, etc.** |
| **Sound**    | **Audio files and CUE**                      |
| **System**   | **Core blueprint function libraries**        |
| **Text**     | **Localized content in various languages**   |
| Vibrations   | Unknown                                      |
| Waterline    | Unknown                                      |
| WaterMaterials | Likely materials related to water surfaces |
| WaterVolume  | Unknown                                      |

Here are some folders worth checking out for beginners:

- Each folder in `character` is worth exploring. It contains the majority of the 3D models for the player, enemies, and warships. You can even find models of the three Bydo warships from *R-Type Tactics*. Occasionally, you may even find unreleased content.

- `Design/texture/Bydolabo/img_bydo` contains images of enemies from *BydoLab*, though the resolution is still somewhat low.

- `Design/texture/gallery/img_gallery` contains high-resolution versions of all images from the *Gallery*, perfect for exporting as wallpapers.

- In `Enemy`, you can find detailed parameters for each enemy, such as health, attack speed, etc.

## Plugins Folder
Some folders in `Plugins` only contain placeholder files marking that a plugin is installed, while others contain their own `Content` folder, which is structured similarly to the `Content` folder mentioned above, storing resources for DLC and additional levels.

Note that for the *X route*, only the map is stored in `Plugins`, while the enemy models and definitions remain in the `Content` folder. For other routes, while the enemy models are stored in `Plugins`, the enemy parameters and definitions are still in the `Enemy` folder inside the `Content` folder.
