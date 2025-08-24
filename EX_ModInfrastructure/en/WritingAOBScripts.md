# Writing AOB Scripts

After the `2.0.4` update in August 2025, *UE4SS* encountered issues locating AOB signatures for key functions. This required writing custom AOB scripts to fix the problem.

A proper AOB script can reliably locate the target function across different environments and can be shared with other users to ensure *UE4SS* works correctly.

## Principle and Purpose of AOB

AOB (Array of Bytes) works by scanning process memory for a continuous byte sequence to locate specific functions or data addresses. When UE4SS starts, it automatically binds to several key functions via AOB, including:

- GUObjectArray  
- GMalloc  
- FName_ToString  
- FName_Constructor  
- FText_Constructor  
- **StaticConstructObject**

If UE4SS fails to find these or detects multiple matches, it will not function properly. For example:

- Error when no address is found:

```
[PS] Failed to find GNatives: expected at least one value`
```

- Error when multiple addresses are found (older versions did not display addresses):

```
[PS] Failed to find StaticConstructObject_Internal: found 2 unique values [7FF6CF1A8AF0, 7FF6D10A4DC0]
``` 

Below the error message, you will often see a prompt like:

```
[PS] You can supply your own AOB in 'UE4SS_Signatures/StaticConstructObject.lua'
```


Note: The AOB doesn’t always need to point to the function entry. With indirect addressing or offset calculation, it can still locate the correct address. In theory, a long enough sequence can uniquely identify the function start, but game updates may break it, requiring rework.

For the format and more details about AOB scripts, see the [UE4SS official documentation](https://docs.ue4ss.com/guides/fixing-compatibility-problems.html).

This tutorial uses `StaticConstructObject` as an example, showing how to *directly address* a function that has *multiple matches*.

## Preparation

Make sure your *UE4SS* version is experimental `v3.0.1` or above (official `v3.0.1` and earlier versions will not display addresses).

If you want to write a general AOB script, prepare a disassembler/debugger such as *X64dbg* or *IDA Pro*.

## Finding the Correct Address via Hardcoding

Save the following as `StaticConstructObject.lua` (or the corresponding function name) in:  
`\RTypeFinal2\Binaries\Win64\UE4SS_Signatures`

```lua
function Register()
    return "00" -- The "00" here does not need to be modified... unless issues occur
end

function OnMatchFound(matchAddress)
    return 0x7FF6D10A4DC0 -- Replace this with the address you want to test
end
```

Replace the address in the comment with the one you want to test. If UE4SS outputs:

```
AOB scans could not be completed because of the following reasons:
Was unable to find AOB for 'StaticConstructObject' via Lua script
```

it means the sequence did not match. You can try changing the `Register()` return value to a fixed and unique memory sequence. Returning only wildcards in `Register()` will also fail.

If the output looks like:

```
StaticConstructObject_Internal address: 0x7ff6d10a4dc0 <- Lua Script
```

then the sequence was found, and the hardcoded address was successfully marked as the function entry. If the game crashes, the address is wrong—try another. If it works, you’ve found the right one—note down the address and its index among matches.

Note: Since memory allocation can change at startup, this method may be unstable. It is only suitable for quick verification.

## Extracting an AOB Sequence

Use X64dbg or IDA Pro to debug `RTypeFinal2.exe` and jump to the previously confirmed address. Check if the disassembly looks like a function entry. If not, it might be due to memory allocation differences. In that case, remove the temporary hardcoded script and instead check the addresses from the multi-match error.

Copy about 32 bytes downward from that address in hex format. Replace variable values (addresses, offsets) with wildcards `??`. Then modify the script like this:

```lua
function Register()
    return "48 89 5C 24 10 48 89 6C 24 18 48 89 74 24 20 57 41 56 41 57 48 81 EC ?? ?? ?? ?? 48 8B 05 ?? ?? ?? ?? 48 33 C4" -- Replace with your extracted hex sequence
end

function OnMatchFound(matchAddress)
    return matchAddress -- Replace hardcoded address with matchAddress
end
```

If, like me, you’re not very familiar with assembly, you can share the hex and disassembly with an AI assistant to determine which parts should be wildcards.

Start the game. If it doesn’t crash and UE4SS outputs something like:

```
StaticConstructObject_Internal address: 0x7ff6d10a4dc0 <- Lua Script
```

then you’ve succeeded.

- If it says the address wasn’t found → check if all variable addresses were replaced with ??.

- If it says multiple addresses were found → the AOB sequence is too short or not unique enough. Extract more bytes or try using an indirect reference.

It’s recommended to test again across restarts or different devices to confirm that the AOB sequence is stable under varying memory allocations. Once confirmed, you can share the AOB script with the community to help other users.