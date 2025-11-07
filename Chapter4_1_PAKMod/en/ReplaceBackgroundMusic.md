# Replace Background Music

In Unreal Engine, `.pak` files are used to package various resources. When the game runs, it loads these `.pak` files according to a specific priority order. If two `.pak` files contain assets with the same path, the one loaded later will override the earlier one.

To facilitate patches and DLCs, Unreal Engine automatically gives `.pak` files with a `_P` suffix the **highest priority**. Therefore, by creating a replacement file with the same asset path as the original and packaging it as `_P.pak`, you can override the game’s audio without modifying the original files.

---

### About CUE Files

In *R-Type Final 2*, both music and sound effects are controlled by **Sound Cue** assets.  
A Sound Cue can be thought of as an “audio logic blueprint” that defines how an audio file is played—for example, playback order, looping, fade in/out, and volume control.

The BGM (background music) Sound Cues are located in  
`RTypeFinal2/Content/Sound/Cue`

Our task is to create a replacement Sound Cue with the same path and name as the original, but make it play our own music instead. Then, we package it into a `_P.pak` file to override the in-game resource.

## Step 1: Create the Project

1. Launch *Unreal Engine 4.26.2*.

   ![Create new project window](../image/ReplaceBGM/NewProject_UE.png)

2. Choose **New Project Type → Games**, then click **Next**.

   ![Select game project type](../image/ReplaceBGM/NewProject_TypeGame.png)

3. Set the project template to **Blank**, then click **Next**.

   ![Choose blank template](../image/ReplaceBGM/NewProject_NoTemplate.png)

4. Set the project type to **Blueprint**.

   ![Select Blueprint type](../image/ReplaceBGM/NewProject_BP.png)

5. Set the save path and name the project **RTypeFinal2**.

   ![Set project name and path](../image/ReplaceBGM/NewProject_Name.png)

6. Click **Create Project** and wait for it to initialize.

## Step 2: Create a Dummy Sound Class

Sound CUEs depend on **Sound Classes** to control playback behavior such as global volume, fading, etc.  
To ensure the game recognizes our replacement CUE while still using the original logic, we need to create a “dummy” sound class—essentially a placeholder with the same name and path as the original. It won’t change how audio behaves but ensures the reference remains valid.

1. In the Unreal Content Browser, right-click to create a new folder named `Sound`.

   ![Create Sound folder](../image/ReplaceBGM/SoundClass_Folder.png)

2. Inside the `Sound` folder, create a subfolder named `Mix`.  
   The directory should now look like this:

   ![Sound folder structure](../image/ReplaceBGM/SoundClass_Path.png)

3. In the `Mix` folder, right-click → **Sounds → Class → Sound Class**.

   ![Create sound class menu](../image/ReplaceBGM/SoundClass_Type.png)

4. Name the new sound class **Sound_BGM**.

   ![Name it Sound_BGM](../image/ReplaceBGM/SoundClass_SoundBGM.png)

> This `Sound_BGM` will not be included in the final PAK.  
> It only exists in the editor so that the Sound Cue can correctly find its reference.

## Step 3: Edit the Audio Files

1. Use any audio editor (or a video editor capable of exporting audio) to open the track you want to replace.
2. Split the track into two parts: an **intro segment** and a **loop segment** (it’s fine if the intro includes part of the loop).

   ![Split audio segments diagram](../image/ReplaceBGM/SoundEdit_Split.png)

3. Use waveform comparison to precisely mark the start and end of the loop to ensure a seamless transition.

   ![Waveform alignment example](../image/ReplaceBGM/SoundEdit_Trim.png)

4. Export the intro and loop segments separately. WAV or OGG formats are recommended (use a higher bitrate if possible).

   ![Export audio window](../image/ReplaceBGM/SoundEdit_Output.png)

## Step 4: Locate the Target Sound Cue

1. Open **FModel** and load all the game’s `.pak` files.
2. Navigate to `RTypeFinal2/Content/Sound/Cue` to find the target `Sound Cue`.

   ![FModel directory view](../image/ReplaceBGM/FModel_Path.png)

3. Double-click the Sound Cue asset. In the JSON view on the right, scroll down to find nodes with `Type` = `SoundNodeWavePlayer` or `SoundNodeOggPlayer`.

   ![FModel node view](../image/ReplaceBGM/FModel_Node.png)

4. Click the `AssetPathName` or `ObjectPath` of those nodes—FModel will open an audio player.
5. Play it to confirm whether it’s the BGM you want to replace.

## Step 5: Create the Replacement Sound Cue

1. Go back to Unreal Engine, and create a subfolder named `Cue` inside the `Sound` folder.

   ![Create Cue folder](../image/ReplaceBGM/CreateCue_Folder.png)

2. Import the two audio files you exported earlier into any content folder (preferably inside the Cue folder).

   ![Import audio files](../image/ReplaceBGM/CreateCue_Input.png)

3. In the `Cue` folder, right-click → **Sounds → Sound Cue**, and name it exactly the same as the target CUE.

   ![Create Sound Cue](../image/ReplaceBGM/CreateCue_Cue.png)

4. Open the new Sound Cue and set its **Sound Class** to the `Sound_BGM` created earlier.

   ![Set Sound Class](../image/ReplaceBGM/CreateCue_SoundClass.png)

5. In the Sound Cue editor graph, add a **Concatenator** node and connect its output to the speaker output node.

   ![Connect nodes](../image/ReplaceBGM/CreateCue_Connector.png)

6. Drag both imported audio files into the graph. This will create two sound nodes automatically.  
7. Connect the **intro segment** to the first input of the concatenator and the **loop segment** to the second input.

   ![Connect intro and loop segments](../image/ReplaceBGM/CreateCue_Nodes.png)

8. Select the loop segment node and enable the **Looping** option in the properties panel.

   ![Set loop property](../image/ReplaceBGM/CreateCue_Loop.png)

## Step 6: Assign to a Specific Chunk

1. From the top menu, select **Edit → Project Settings**.

   ![Open project settings](../image/ReplaceBGM/AssignChuck_Menu.png)

2. Under the **Packaging** section, enable **Generate Chunks**.

   ![Enable chunk generation](../image/ReplaceBGM/AssignChuck_GenerateChuck.png)

3. Next, go to **Edit → Editor Preferences**.  
4. Enable **Experimental → User Interface → Allow Assigning Chunk IDs**.

   ![Allow chunk ID assignment](../image/ReplaceBGM/AssignChuck_AllowAssign.png)

5. In the Content Browser, select **the Sound Cue and both audio files**.  
6. Right-click → **Asset Actions → Assign to Chunk**.

   ![Assign to chunk menu](../image/ReplaceBGM/AssignChuck_AssignTo.png)

7. Set the **Chunk ID** to a nonzero number, ensuring all three share the same ID.

   ![Set chunk ID](../image/ReplaceBGM/AssignChuck_ChuckID.png)

> ⚠️ Do **not** assign `Sound_BGM` to the same chunk as the Sound Cue.  
> Keep it in the default chunk (ID 0), or it may override the game’s global sound class and break all BGM playback.

> You can verify asset assignments via **Right-click → Audit Asset**.

## Step 7: Package the PAK and Install It in the Game

1. From the top menu, select **File → Package Project → Windows (64-bit)**.

   ![Select package project](../image/ReplaceBGM/Pack_Win64.png)

2. Choose an output path (for example, your project folder). The first packaging may take a while.

   ![Select output path](../image/ReplaceBGM/Pack_OutputFolder.png)

3. In the output directory, navigate to  
   `WindowsNoEditor\RTypeFinal2\Content\Paks`.

4. Locate the file named `pakchunk{your_chunk_ID}-WindowsNoEditor.pak`.  
   It should contain your Sound Cue and audio files.

   ![Generated PAK file](../image/ReplaceBGM/Pack_Paks.png)

5. Rename it to `{any_name}_P.pak`.  
   The `_P` suffix is **mandatory**.

   ![Rename to _P suffix](../image/ReplaceBGM/Pack_Rename.png)

6. Place the file in the game’s Paks folder using the [Install PAK Mod](../../Chapter1_TheBasics/zhs/安装PAKMod.md) method.

   ![Place in game Paks folder](../image/ReplaceBGM/Pack_Installed.png)

7. Launch the game and check if your custom BGM successfully replaced the original.