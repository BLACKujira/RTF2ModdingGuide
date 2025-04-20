# Identifying Enemy IDs via BydoLab Images

- First, open FModel and locate `Content/Design/texture/Bydolabo/img_bydo`. Extract all the images in this folder.

- Next, go to the folder where the images were extracted. By comparing the enemy appearances, find the one you're looking for. The middle part of the file name contains the enemy's ID.

Using this ID, you can locate the following assets:

- `/Content/Enemy/ID/IDParamAsset.uasset`: This is the enemy definition object. It contains the enemy's class and parameters, and is used for creating object pools in stages.
- `/Content/character/Enemy/ID/`: This folder contains the enemy’s models, animations, textures, and materials. (For Route Y, Route Z, and newer stages, they are found in corresponding plugins.)
- Searching this image in `/Content/Data/BydoData.uasset` reveals the localized key name of the enemy.

## Example: Floating turret from Stage 3.0 and Stage X6.0
![E386](../image/E386.png)

- From the image, we identify the ID as E386.
- Its corresponding definition file is `/Content/Enemy/E386/E386ParamAsset.uasset`.
- The bullets it fires are defined in `/Content/Enemy/E386/S386ParamAsset.uasset`.
- Its model is located at `/Content/character/Enemy/E386/E386_01.uasset`.
- In `/Content/Data/BydoData.uasset`, its ID is `102`, and the localization key name is `NAME_103_SourceString`.

# Postscript

Although the game does have ID-enemy mappings, there is no global enemy list. *BydoLab* only records enemies that have appeared in officially released stages. Therefore, this method cannot identify enemies from unreleased stages.
