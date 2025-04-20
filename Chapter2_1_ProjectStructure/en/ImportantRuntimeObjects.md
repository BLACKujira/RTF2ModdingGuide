# Important Runtime Objects

### E28GameInstance  
This is the main game instance object. It seems to contain functions for entering stages. There are also many deprecated variables inside.

### GameFlag  
Used to set the state of in-game flags. Flag names and IDs can be found in `RTypeFinal2/Content/Data/FlagNumber.uasset`.

### GamePoint  
Controls the amount of R-Points (in-game currency).

### GameResource  
Controls the amount of Solar Ore, Ether Ore, and Bydo Ore.

### (Important) PlayerSettings  
Manages hangar R-ships, custom stage routes, and custom titles.

### (Important, Non-Instance) ConfigGame  
Runtime configuration file for ConfigGame. Used to change the entry stage of each route.

### (Important) ScrollManager  
Manages scroll speed, stops scrolling, and handles scroll info and events.

### (Important) E28GameMode_Shooter  
The game mode object after entering a stage. Contains references to stage control objects, controls UI display, and can directly trigger stage completion.

### ShooterPlayerController  
Controls the player and parts of the stage logic. Can reset the stage and change camera FOV.

### Savedata1  
Represents the game's save data. **Modifying its variables has no effect on gameplay.** Variable names correspond to their respective control objects.

### FadeDriver  
Manages stage fade-in/fade-out. If a black screen occurs when entering a stage, use this to locate `UMG_Fade_C` and call `SetAlpha` to remove the black screen.

### (Important) EnemyManager  
Manages the enemy and bullet object pools. Acts as the parent object for enemies and projectiles.
