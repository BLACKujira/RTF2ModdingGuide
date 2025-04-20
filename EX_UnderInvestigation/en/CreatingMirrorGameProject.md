# Creating a Mirror Game Project

If there is a *Mirror Game Project* available for the current game version in the community, it’s best to use that instead of creating a new one.

Before learning this chapter, you need to be familiar with the *Blueprint Mod* development process; understand how to create *virtual copies (Dummy)* for different types of code and resources in the game during the *Blueprint Mod* development process, and have some experience with *C++* development and debugging.

For mods that rely heavily on game resources and code, manually creating virtual copies (Dummies) of various resources becomes a difficult task. To better understand and utilize the game resources, we can use some tools to automatically create a *Mirror Game Project* that includes most of the virtual code and resources.

This involves a lot of knowledge and can be complex, but once a *Mirror Game Project* is successfully created, it can be used by the entire modding community for a long time, until the next major version update.

Since the interval between creating a *Mirror Game Project* is quite long, this guide is written as my own research notes for future reference. Additionally, if I ever leave the community, I hope someone can quickly complete this research and take over my position using this guide.

## Step 1: Export UHT and Use UHT to Create the Project

- Use the `Unreal Header Tool (UHT) Dumper` in *UE4SS*'s `Dumpers` to export the virtual code (UHT) of the game itself and the plugins it uses. There is no need to configure this feature at this stage.
- Use *FModel* to unpack the `RTypeFinal2\RTypeFinal2.uproject` and `RTypeFinal2\Plugins\RTypeFinal2.upluginmanifest` files.
- Download the [UE4GameProjectGenerator](https://github.com/Buckminsterfullerene02/UE4GameProjectGenerator) project.
- Run *UE4GameProjectGenerator* once in `UE4.26` to check the version and the necessary files for the generated version.
- Use the command prompt to generate the project file with the following command:

```
"(Unreal Engine installation location)\UE_4.26\Engine\Binaries\Win64\UE4Editor-Cmd.exe" "(UE4GameProjectGenerator location)\UE4GameProjectGenerator\GameProjectGenerator.uproject" -run=ProjectGenerator -HeaderRoot="(Game installation location)\R-Type Final 2\RTypeFinal2\Binaries\Win64\UHTHeaderDump" -ProjectFile="(FModel installation location)\FModel\Output\Exports\RTypeFinal2\RTypeFinal2.uproject" -PluginManifest="(FModel installation location)\FModel\Output\Exports\RTypeFinal2\Plugins\RTypeFinal2.upluginmanifest" -OutputDir="(Output folder)" -stdout -unattended -NoLogTimes
```

Note: The `(Output folder)` must exist, or the project will not be generated.

## Step 2: Transfer Project Files

Running the game project directly using the method from [UE4GameProjectGenerator](https://github.com/Buckminsterfullerene02/UE4GameProjectGenerator) will result in a compilation error, as the project does not generate a `.sln` file. This issue must be solved in a special way.

- Similar to when creating a Blueprint Mod, create a new `C++` project named `RTypeFinal2`.
- Replace the newly created project files with the project files generated earlier. At this point, it will still not compile or open Unreal Engine.
- Since there will be many steps to follow, it's recommended to create a git repository for the project to make backup and recovery easier.

## Step 3.1: Fix Compilation Errors - Basic

In the following text, *delete non-basic content* refers to *only retaining references to header files in the `.cpp` files* and *removing all members except `GENERATED_BODY()` in the `header files`*.

- Open the `.sln` file with `Visual Studio 2019` and manually compile the project. At this point, the following error will appear:

```
The platform name WinGDK is not a valid platform name. Valid names are (Win32,Win64,HoloLens,Mac,XboxOne,PS4,IOS,Android,HTML5,Linux,LinuxAArch64,AllDesktop,TVOS,Switch,Lumin)
```

- To resolve this, open the project file `RTypeFinal2.uproject` with an IDE or other text editor and delete all instances of `WinGDK`. Start the compilation again, and you will still encounter an issue where the project cannot compile properly. The error won't show up in the *error list* but will appear in the output log with the following message:

```
1>E:/Project_Unreal/TestRTF2Stage/Source/RTypeFinal2/Public/TimerManager.h(13) : LogCompile: Error: An explicit Category specifier is required for Blueprint accessible functions in an Engine module.
```

- Locate the corresponding *header file* and *cpp file* for `TimerManager`, and delete all non-basic content from both files. Recompile the project, and you will notice a number of intermediate files with the format `Module.RTypeFinal2.gen.xx_of_xx.cpp`. Then, you will encounter two `C2352` errors and two `C2511` errors. The `C2511` error will look like this:

```
“void UGameMatchingHelperBase::EventNetworkError(UObject *,ENetworkFailure::Type,bool)”:“UGameMatchingHelperBase” does not have an overloaded member function
```

- Similar to `TimerManager`, find the *header file* and *cpp file* for `UGameMatchingHelperBase`, and delete all non-basic content. Recompile the project again.

- This time, the compilation will take longer and may cause out-of-memory errors. If this happens, recompile until no errors unrelated to the code itself appear.
- At this point, more than 30 errors will appear. If the error location points to a class’s `.obj` file, locate the corresponding *header file* and *cpp file* for the class and remove the corresponding members based on the error message, or simply delete all non-basic content. (This step might not occur.)

The remaining errors will be shown in files like `Module.RTypeFinal2.gen.83_of_140.cpp.obj` or `Module.RTypeFinal2.1_of_2.cpp.obj` and may not be as easy to locate as before.

## Step 3.2: Fix Compilation Errors - LNK2019

Next, solve the `LNK2019` *unresolved external symbol* error. A typical error message is as follows:

```
Unresolved external symbol "__declspec(dllimport) public: __cdecl FOnlineSessionSettings::FOnlineSessionSettings(void)" (_imp??0FOnlineSessionSettings@@QEAA@XZ), function "public: static void __cdecl UGameMatching::execGetPendingInvite_OnlineSessionSearchResult(class UObject *,struct FFrame &,void * const)" (?execGetPendingInvite_OnlineSessionSearchResult@UGameMatching@@SAXPEAVUObject@@AEAUFFrame@@QEAX@Z) references this symbol
```


- In this case, `UGameMatching` is the class name, and `GetPendingInvite_OnlineSessionSearchResult` is the method name that triggered the error. Proceed by deleting all the methods with similar errors. Make use of the search feature in modern IDEs to speed up this process.

- In the current version, such errors in the `UGzFindSessionsCallbackProxy` class will transfer to another method after deletion. It is recommended to solve the issue by deleting all non-basic content in both the *header file* and *cpp file* of the class.

- After deleting this code, the following `LNK2019` error, which is not caused by the game code, will automatically disappear:

```
Unresolved external symbol "__declspec(dllimport) public: virtual __cdecl FOnlineSessionSettings::~FOnlineSessionSettings(void)" (_imp??1FOnlineSessionSettings@@UEAA@XZ), function "public: virtual __cdecl FOnlineSession::~FOnlineSession(void)" (??1FOnlineSession@@UEAA@XZ) references this symbol
```


## Step 3.3: Fix Compilation Errors - LNK2005

All `LNK2005` and `LNK1169` errors are actually caused by the same file. The file is `Source\RTypeFinal2\Private\RTypeFinal2Module.cpp`, which, along with `Source\RTypeFinal2\RTypeFinal2.cpp`, contains the line `IMPLEMENT_PRIMARY_GAME_MODULE(FDefaultGameModuleImpl, RTypeFinal2, RTypeFinal2);`, leading to the module being defined multiple times.

- Deleting the `IMPLEMENT_PRIMARY_GAME_MODULE(FDefaultGameModuleImpl, RTypeFinal2, RTypeFinal2);` line in `RTypeFinal2Module.cpp` will resolve these issues. After doing so, the project should compile properly.
- In future versions, there may be more similar or different compilation errors. Be prepared to adapt as necessary.

## Step 4: Fix Editor Crashes

Although the project can be compiled, opening the project file in Unreal Engine still causes a crash. The main part of the crash log is as follows:

```
Fatal error: [File:D:/Build/++UE4/Sync/Engine/Source/Runtime/CoreUObject/Private/UObject/UObjectGlobals.cpp] [Line: 3791] Default subobject SceneComponent EnemySlot already exists for E2504 /Script/RTypeFinal2.Default__E2504.
```

This error indicates that the `EnemySlot` SceneComponent is being created twice in the constructor of the AE2504 class.

- Open `E2504.cpp` and delete the following content in the constructor:

```
this->pSlot[0] = CreateDefaultSubobject<USceneComponent>(TEXT("EnemySlot"));
this->pSlot[1] = CreateDefaultSubobject<USceneComponent>(TEXT("EnemySlot"));
this->pSlot[2] = CreateDefaultSubobject<USceneComponent>(TEXT("EnemySlot"));
this->pSlot[3] = CreateDefaultSubobject<USceneComponent>(TEXT("EnemySlot"));
this->pSlot[4] = CreateDefaultSubobject<USceneComponent>(TEXT("EnemySlot"));
```

- After compiling, try launching the project again, and you'll encounter an error: `The module "FractureEditor" could not be loaded, causing the plugin "ChaosEditor" to fail. There may be a system error or the module was not properly set.`

- Open the project file `RTypeFinal2.uproject`, go to `Plugins`, find the `ChaosEditor` object, and change `Enabled` to `false`. (Using the *Chaos* version of *UE4.26* will not solve this issue.)

- After launching, you will see a new error message as follows:

```
Unhandled Exception: EXCEPTION_ACCESS_VIOLATION reading address 0x0000000000000098
UE4Editor_Engine
UE4Editor_RTypeFinal2!AH025Petal::AH025Petal() [E:\Project_Unreal\RTypeFinal2\Source\RTypeFinal2\Private\H025Petal.cpp:10]
...
```


- Locate the *header file* and *cpp file* of `H025Petal`, and delete all non-basic content. Then, compile again.

- Once compilation is complete, try launching the project again. This time, you should be able to enter the editor. Go check out the objects corresponding to these `C++` codes.

## Step 5: Replace Configuration Files

You may have noticed the *Unreal Engine* *project settings* message: `These settings are stored in DefaultGame.ini/DefaultEngine.ini and are currently writable`. Fortunately, these assets, `DefaultGame.ini` and `DefaultEngine.ini`, are not *baked*, meaning the files extracted from `.pak` can be directly read by the engine.

- First, use *FModel* to extract all the configuration files from `RTypeFinal2\Config`.
- Among the extracted configuration files, you will find several files, including `DefaultGame.ini` and `DefaultEngine.ini`. Copy them all into the `Config` folder of the project.

After doing this, when you open the project, there will be two time-consuming shader compilations during both the editor startup and after the launch. The CPU usage will be very high, so please be patient.

## Step 6: Serialize Baked Assets

- Download [UEAssetToolkitGenerator](https://github.com/LongerWarrior/UEAssetToolkitGenerator) and follow the instructions in the documentation.

If it doesn't run, check if you have installed the `.NET 6 runtime`.

Currently, attempts to serialize assets will only create empty folders without generating any assets. So, this is where things get stuck. This might be because the current version of *UEAssetToolkitGenerator* uses an outdated version of *UAssetAPI*, which cannot handle `.usmap` mapping files.

Possible solutions include updating the *UAssetAPI* referenced by *UEAssetToolkitGenerator* to a newer version. However, since the difference between the old and new versions of *UAssetAPI* is substantial, this will require modifying a lot of code.

Another option is to modify the old version of *UAssetAPI* referenced by *UEAssetToolkitGenerator* to enable it to load `.usmap` mapping files.
