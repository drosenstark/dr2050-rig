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

## How params actually work (Ableton Live / plugdata VST3)

This is how params are supposed to work, and what actually happens.

**The intended flow:**

- `[param division]` in the patch is exposed as an automation knob in Ableton.
- Moving the knob sends a 0–1 float through the param outlet into the patch.
- The patch maps that float to a useful value (e.g. division count) and uses it.

**The problem — first load is broken:**

When Ableton loads a saved session, it restores parameter values, but the `[param]` outlet does not fire on load. This is a confirmed plugdata VST3 bug (GitHub issue #2044). The param outlet simply does not output anything at startup, even if the host has a stored value. So any logic that depends on reading param at init time will silently use whatever default you baked in.

**The workaround that works:**

Use a `[floatatom]` as the actual source of truth for the value. Wire it like this:

```pd
[loadbang]
|
[floatatom]  ← stores value in the .pd file itself, default e.g. 0.5
|
[expr ...]   ← maps 0–1 to useful values
```

- The floatatom saves its last value in the `.pd` file.
- On load, `loadbang` bangs it and it immediately outputs the saved value.
- Keep `[param]` in the patch and also wire it to the same expr, so automation works once the bug is fixed and for live tweaking.
- The floatatom is also clickable/draggable directly in the patch as a manual override.

**First load on a fresh instance (no saved state):**

The floatatom will output its hardcoded default (whatever value is in the `.pd` file). Set this to something musically sensible, e.g. `0.5` for 8th notes. After the user tweaks and saves the session, subsequent loads will use the saved value correctly.

**Summary:** first load of a fresh instance uses the baked-in default. After that, the saved value is used. Automation via `[param]` works during playback. Do not rely on `[param]` to initialize anything at startup.

## Known-good patches

- `transpose-1-beat-later.pd`
  - uses `playhead` outlet `5`
  - quarter-note delay
- `transpose-1-bar-eighth-chromatic.pd`
  - uses `playhead` outlet `5`
  - dry note plus 7 chromatic delayed copies at eighth-note spacing
- `debug-host-tempo.pd`
  - probes `playhead` outlets to verify host transport/tempo behavior
