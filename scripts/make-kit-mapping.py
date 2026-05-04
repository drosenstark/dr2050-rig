#!/usr/bin/env python3
"""
Drum kit grid generator.

Builds N chromatic 4x4 drum kits where each kit's root is 16 semitones above
the previous one — meaning the kits chain seamlessly with no gaps or overlaps
(16 pads per kit, each pad one semitone, so the next root sits exactly where
the previous kit leaves off).

Layout: pad 0 is bottom-left, pads increase rightward then upward, so pad 15
is top-right. Kits are printed in a 2x2 arrangement: kits 3,4 on top row and
kits 1,2 on bottom row.

Usage:
    python3 drum_kit_grids.py                  # default: root C1
    python3 drum_kit_grids.py --root G0        # start from G0
    python3 drum_kit_grids.py --root C1 -n 4   # 4 kits
"""

import argparse

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# MIDI convention used here: C0 = MIDI 12, so C-1 = MIDI 0, C4 = MIDI 60.
# (This is the "scientific" convention. Some DAWs call MIDI 60 "C3" instead;
# adjust MIDI_C0 to 0 if you want C-1=MIDI 12 style, or to 24 for the C2=MIDI
# 60 convention. The note *intervals* are the same either way.)
MIDI_C0 = 12


def name_to_midi(name: str) -> int:
    """Parse a note name like 'C1', 'G#3', or 'Eb2' into a MIDI number."""
    name = name.strip()
    if len(name) < 2:
        raise ValueError(f"Bad note name: {name!r}")

    # Handle accidental
    if name[1] in ('#', 'b'):
        note_str = name[:2]
        octave = int(name[2:])
    else:
        note_str = name[0]
        octave = int(name[1:])

    # Normalize flats to sharps
    flat_to_sharp = {'Db': 'C#', 'Eb': 'D#', 'Gb': 'F#', 'Ab': 'G#', 'Bb': 'A#'}
    note_str = flat_to_sharp.get(note_str, note_str)

    if note_str not in NOTE_NAMES:
        raise ValueError(f"Unknown note: {note_str!r}")

    return MIDI_C0 + octave * 12 + NOTE_NAMES.index(note_str)


def midi_to_name(midi: int) -> str:
    """Convert a MIDI number back to a note name like 'C1' or 'G#3'."""
    octave = (midi - MIDI_C0) // 12
    note = NOTE_NAMES[(midi - MIDI_C0) % 12]
    return f"{note}{octave}"


def make_grid(root_midi: int) -> list[list[str]]:
    """Build a 4x4 grid of note names. Returns rows top-to-bottom for printing."""
    pads = [midi_to_name(root_midi + i) for i in range(16)]
    # pads[0..3] = bottom row, pads[12..15] = top row
    return [pads[12:16], pads[8:12], pads[4:8], pads[0:4]]


def format_grid(rows: list[list[str]], label: str) -> list[str]:
    """Render one grid as a list of lines."""
    lines = [f"  {label}"]
    lines.append("  ┌─────┬─────┬─────┬─────┐")
    for i, row in enumerate(rows):
        cells = '│'.join(f' {n:>3} ' for n in row)
        lines.append(f"  │{cells}│")
        if i < len(rows) - 1:
            lines.append("  ├─────┼─────┼─────┼─────┤")
    lines.append("  └─────┴─────┴─────┴─────┘")
    return lines


def side_by_side(left: list[str], right: list[str], gap: str = "      ") -> str:
    """Print two grids next to each other."""
    return '\n'.join(f"{l}{gap}{r}" for l, r in zip(left, right))


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--root', default='C1',
                        help="Root note of kit 1 (e.g. C1, G0, G#3). Default: C1")
    parser.add_argument('-n', '--num-kits', type=int, default=4,
                        help="Number of kits to generate. Default: 4")
    args = parser.parse_args()

    start_midi = name_to_midi(args.root)
    root_midis = [start_midi + 16 * i for i in range(args.num_kits)]
    roots = [midi_to_name(m) for m in root_midis]

    print(f"Roots: {' → '.join(roots)}")
    print(f"Total range: {midi_to_name(root_midis[0])} to "
          f"{midi_to_name(root_midis[-1] + 15)} "
          f"({args.num_kits * 16} pads, fully chromatic)")
    print()

    # Build all grids
    grids = {}
    for i, root_midi in enumerate(root_midis, start=1):
        label = f"KIT {i} (root {midi_to_name(root_midi)})"
        # pad label to consistent width
        label = label.ljust(24)
        grids[i] = format_grid(make_grid(root_midi), label)

    # Print in 2x2 layout: kits 3,4 on top, kits 1,2 on bottom.
    # If num_kits != 4, fall back to printing pairs in order.
    if args.num_kits == 4:
        print(side_by_side(grids[3], grids[4]))
        print()
        print(side_by_side(grids[1], grids[2]))
    else:
        kit_ids = list(range(1, args.num_kits + 1))
        for i in range(0, len(kit_ids), 2):
            pair = kit_ids[i:i+2]
            if len(pair) == 2:
                print(side_by_side(grids[pair[0]], grids[pair[1]]))
            else:
                print('\n'.join(grids[pair[0]]))
            print()


if __name__ == '__main__':
    main()