# Using Delegates as Function Parameters
When creating Dummies for blueprints, you may notice some function parameters with the type `DelegateProperty`, like the example below. However, in blueprints, it seems there is no option for the *delegate* type for parameters.

```json
{
"Type": "Function",
"Name": "Start",
"Outer": "PlayerLoader_C",
"Class": "UScriptClass'Function'",
"ChildProperties": [
    {
    "Type": "BoolProperty",
    "Name": "LoadOnly",
    "Flags": "RF_Public",
    "ElementSize": 1,
    "PropertyFlags": "BlueprintVisible | BlueprintReadOnly | Parm",
    "FieldSize": 1,
    "ByteOffset": 0,
    "ByteMask": 1,
    "FieldMask": 255,
    "BoolSize": 1,
    "bIsNativeBool": true
    },
    {
    "Type": "DelegateProperty",
    "Name": "イベント",
    "Flags": "RF_Public",
    "ElementSize": 20,
    "PropertyFlags": "ConstParm | BlueprintVisible | BlueprintReadOnly | Parm | OutParm | ReferenceParm",
    "SignatureFunction": {
        "ObjectName": "Function'PlayerLoader_C:FinsihDispatcher__DelegateSignature'",
        "ObjectPath": "RTypeFinal2/Content/Player/PlayerLoader.0"
    }
    }
],
"FunctionFlags": "FUNC_Public | FUNC_HasOutParms | FUNC_BlueprintCallable | FUNC_BlueprintEvent"
},
```

The solution to this problem is quite simple. In the function, simply create a node with a *delegate parameter*, and drag the *delegate-type pin* to the *input node* to add a new pin.

![DelegateProperty](../image/DelegateProperty.png)

You will notice that the name of the input parameter created this way is `イベント`, which is the word for "event" in the language currently used by Unreal Engine. Therefore, delegate-type parameters in the game are typically named `イベント`, which is likely how these parameters are created.
