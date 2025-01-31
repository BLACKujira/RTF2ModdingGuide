# Analyzing Blueprints with kismet-analyzer

[kismet-analyzer](https://github.com/trumank/kismet-analyzer) can be used to analyze `.uasset` blueprint files and `.umap` map files, displaying the internal logic in a flowchart-like format.

## Required Skills and Resources

### Skills
- `C#` Development (if you want to generate *kismet-analyzer* yourself)

### Resources
- `.NET 8.0` build and runtime environment
- Unpacked `raw data (.uasset)` game assets
- Game's `.usmap` map file

## Preparing kismet-analyzer

You can download a pre-built *kismet-analyzer* from the [Releases](https://github.com/BLACKujira/RTF2ModdingGuide/releases) page and proceed directly to step 4. However, you will still need the *.NET 8.0 runtime* for the program to run properly.

Alternatively, you can start from step 1 to build *kismet-analyzer* yourself.

## Step 1: Clone the kismet-analyzer Repository

- First, download the [kismet-analyzer](https://github.com/trumank/kismet-analyzer) code, or use any `Git` client to pull the repository.

Many `Git` clients will not automatically pull the *UAssetAPI* project referenced by this project, so you will need to manually download or pull the *UAssetAPI* repository and place it in the corresponding folder.

## Step 2: Configure the Build Environment

- Open the `kismet-analyzer.csproj` using *Visual Studio* or another IDE and try to build the project. Most of the time, this build will fail.

If you get the error `NET SDK does not support targeting .NET 8.0. Please target .NET 6.0 or lower, or use a version of the .NET SDK that supports .NET 8.0`, please download and install the [.NET 8.0 SDK](https://dotnet.microsoft.com/en-us/download/visual-studio-sdks) and the `.NET 8.0 runtime`.

## Step 3: Build UAssetAPI and kismet-analyzer

If you try to build *kismet-analyzer* at this point, you will get an error like `Unable to copy file “D:\Extract\kismet-analyzer\UAssetAPI\UAssetAPI\bin\Debug\net8.0\UAssetAPI.dll” because it was not found.` Therefore, you need to build *UAssetAPI* first.

- Open `UAssetAPI\UAssetAPI\UAssetAPI.csproj` in your IDE and build the project.
- Then build `kismet-analyzer`.

## Step 4: Install Graphviz

- *kismet-analyzer* depends on [Graphviz](https://graphviz.org/) to generate flowcharts, so you need to install *Graphviz*.
- During installation, make sure to add it to the `PATH` system variable. Otherwise, you will need to manually add it to the `PATH` variable or modify the *kismet-analyzer* code.

## Using kismet-analyzer to Analyze Game Resources

- Open the *Command Prompt* and enter the command in the following format:

```
"(Directory where kismet-analyzer was built)\kismet-analyzer.exe" cfg "(Path to the .uasset or .umap file to analyze)" -m "(Path to the .usmap map file)" --ue-version VER_UE4_26
```

Replace `(Directory where kismet-analyzer was built)`, `(Path to the .uasset or .umap file to analyze)`, and `(Path to the .usmap map file)` with the actual paths.

Example:

```
"D:\Extract\kismet-analyzer\bin\Debug\net8.0\kismet-analyzer.exe" cfg "E:\Extract\RTypeFinal2\Content\character\Enemy\E000\ABP_E000_POW_01.uasset" -m "D:\Extract\Dumper-7\Unicode-Names-4.26.0-0+++UE4+Release-4.26-RTypeFinal2\Mappings\4.26.0-0+++UE4+Release-4.26-RTypeFinal2.usmap" --ue-version VER_UE4_26
```


If successful, it will open the browser and display the flowchart as a webpage.

---

If you encounter the following error:

```
System.ComponentModel.Win32Exception (2): An error occurred trying to start process 'dot' with working directory 'D:\Extract\kismet-analyzer\bin\Debug\net8.0'. The system cannot find the file specified.
   at System.Diagnostics.Process.StartWithCreateProcess(ProcessStartInfo startInfo)
   at System.Diagnostics.Process.Start(ProcessStartInfo startInfo)
   at KismetAnalyzer.Program.WriteDotViewer(String dot, String outputPath, String dotPath) in D:\Extract\kismet-analyzer\Program.cs:line 235
   at KismetAnalyzer.Program.Cfg(EngineVersion ueVersion, String mappings, String assetPath, String dotPath) in D:\Extract\kismet-analyzer\Program.cs:line 262
   at System.CommandLine.Handler.<>c__DisplayClass5_04.<SetHandler>b__0(InvocationContext context)
   at System.CommandLine.Invocation.AnonymousCommandHandler.Invoke(InvocationContext context)
   at System.CommandLine.Invocation.InvocationPipeline.<>c__DisplayClass4_0.<<BuildInvocationChain>b__0>d.MoveNext()
```


Please check if you have correctly added `Graphviz` to the `PATH` system variable. Otherwise, try specifying the location of `dot.exe` from `Graphviz` or modify the code around `Program.cs:line 235` in the error message to hard-code the path to `dot.exe` in the program.

## Epilogue

Since most of the game logic is implemented in C++ code, unfortunately, this method can only analyze a limited portion of the game logic.

However, the logic for the very important *game maps* is indeed in blueprints, and you can use *kismet-analyzer* to analyze it. Yes, you will need to recreate the logic of this complex blueprint in order to run custom levels. Fortunately, much of the logic involves unnecessary if branches that don't need to be recreated, and only one person needs to recreate the remaining logic, which I have already done.

In addition, user interfaces, animation blueprints, and blueprint function libraries can also be analyzed in this way, and you will obtain many useful insights.

*kismet-analyzer* primarily displays the logic of blueprints. To get detailed information about the properties, parameters, and variables of the resources themselves, you will still need to use *FModel* to convert them to JSON or use *UAssetGUI*.
