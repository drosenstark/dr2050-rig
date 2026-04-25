# Pure Data Notes

Local notes for this patch folder.

These patches are intended to run inside a plugin host / DAW context rather than plain standalone Pure Data. In practice that means loading them in something like Ableton Live via the plugin environment so they can receive host transport and tempo information.

If the patch is not running inside a host that provides transport, or if the host is not actually playing, tempo-synced behavior may fall back to defaults and `playhead` may not report useful BPM data.

## `playhead` outlet mapping in this build

The installed `playhead` object here does not output tagged messages like `tempo 120` from outlet 0.
It exposes separate outlets, and the useful ones observed in `debug-host-tempo.pd` are:

- outlet `0`: playing state (`0`/`1`)
- outlet `2`: position-style tuple such as `0 8 24`
- outlet `5`: tempo in BPM, e.g. `120`
- outlet `6`: `24`
- outlet `7`: time signature, e.g. `4 4`

## Tempo-synced delay patches

For this environment, do not use:

```pd
[playhead]
|
[route tempo]
```

Use outlet `5` from `playhead` directly.

Quarter-note milliseconds:

```pd
[playhead]
(outlet 5)
|
[expr 60000 / $f1]
```

Eighth-note milliseconds:

```pd
[playhead]
(outlet 5)
|
[expr 30000 / $f1]
```

## Parameters

Parameters are name-based in this setup.

- Use the same parameter name in both places: the GUI automation setup and the patch object.
- Use parameter names that begin with a letter.
- Refer to the parameter in the patch by name.

Example:

- In the GUI / automation panel, create a parameter named `one` by typing `param one`
- In the patch, refer to it as:

```pd
[param one]
```

In that example, the parameter name is `one` everywhere:

- outside the patch, in the host / automation UI: `one`
- inside the patch, in the object text: `param one`

## Known-good patches

- `transpose-1-beat-later.pd`
  - uses `playhead` outlet `5`
  - quarter-note delay
- `transpose-1-bar-eighth-chromatic.pd`
  - uses `playhead` outlet `5`
  - dry note plus 7 chromatic delayed copies at eighth-note spacing
- `debug-host-tempo.pd`
  - probes `playhead` outlets to verify host transport/tempo behavior
