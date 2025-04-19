# Resource File Prefixes

Due to Unreal Engine's characteristics, even if resources of different types are in the same directory, they cannot share the same name. As a result, developers use some prefix abbreviations to differentiate between different resource types. The corresponding relationships are as follows:

| Prefix | Resource Type                    |
|--------|-----------------------------------|
| NS     | Niagara System (Particle) |
| M      | Material                          |
| MI     | Material Instance                 |
| UMG    | Unreal Motion Graphics (UI) |
| BPL    | BluePrint Library                 |
| ABP    | Animation BluePrint               |

Of course, there are many resource files without prefixes. You can open the resource files with *FModel* and check the `Type`, `Class`, and other properties to determine the resource type.