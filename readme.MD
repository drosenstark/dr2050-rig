# Dan Rosenstark's Rig for Live Improvisation

## Overview

This is my rig for live improvisation. While my focus is mainly on drums and percussion, the rig relies heavily on Maschine. Therefore, you could focus on melodic instruments of many types with ease.

A single Maschine plugin inside Ableton Live produces all the sounds. I limit myself to 4 groups in Maschine to keep sane, each of which comes to a separate output. Using MIDI Designer, I'm able to EQ those groups, send them to a delay return. From there, the sound is passed through a Master FX section and then out to the audience (1/2 on the audio interface).

In addition to the audience mix, there is a Cue Mix which goes to the cue output (3/4 on the audio interface). Any group may be easily sent to the Cue Mix **instead** of the audience mix. I've found group cueing inside Maschine to be too hard to reach, and I'm also avoiding Maschine's click. Instead I'm using Ableton Live's click, which goes out to the Cue Output and is always volume adjustable in MIDI Designer.

Ableton Link functionality in MIDI Designer provides a visual click.

Putting Maschine inside Ableton is a trade-off: I've given up transport and tempo controls, firstly. I've also chosen to ignore the Aux sends in Maschine, and the Master section (and meters on the Jam or Studio) are not being used. In exchange, I get a more flexible routing and sends wherever I want them. I also get to use Ableton's Simple Delay, Ping-Pong Delay and Grain Delay (the former two do pitch bending awesomely), and the 3-band Ableton EQ. I also put limiters wherever I see fit. I also suspect that Maschine performs better inside Ableton, but I haven't bothered to try to prove this yet.

One of the most altering goals of this rig is that I need to be able to load Maschine Groups from the Browser without losing pieces of the rig. That's why there are no macros assigned to group-level controls. I've also avoided having a Return Group (that routes back from Live and goes out to Maschine's master out). This allows me to solo any group without accidentally killing the entire mix.

Here's the current MIDI Designer screen, now consolidated to one (double) page.

![DR2050 Rig in MIDI Designer Pro X](http://dr2050.com/clips/2018-02-19-DR2050-Rig-smaller.png)

## What's in the Box

The files included are the Ableton Project and the MIDI Designer layout. The rest is in the Dependencies.

## Dependencies

### Software

* **Maschine 2**: Maschine 2 is the heart of this rig and the sole sound source. [ [Native Instruments Maschine](https://www.native-instruments.com/en/products/maschine/production-systems/maschine/) ]
* **[MIDI Designer Pro X](http://midiDR.com/app)**: Did I mention that I'm the software author of [MIDI Designer](http://mididesigner.com)? The whole point of this rig is to make music, and I've done many iterations of the rig without. Currently, I cannot do with it, but you could conceivably recreate this rig using a hardware MIDI controller, Lemur, or something else.
* **Ableton Live**: While I'm using Ableton Live 11 Standard, I'm quite sure that I don't use any features that aren't in the Standard Edition. Here's [the editions matrix](https://www.ableton.com/en/live/compare-editions).
* **Native Instruments Guitar Rig 5**: I'm currently **only** using the Studio Reverb from this, so you could probably substitute it out with something else without an issue. [ [NI Guitar Rig 5 Player](https://www.native-instruments.com/en/products/komplete/guitar/guitar-rig-5-player/) ]
* **DJM Filter by X-Fer Records**: I use this in Group H. [ [DJM Filter Free Download Page](https://splice.com/plugins/4442-djmfilter-vst-au-by-xfer-records) ]

### Hardware

* **Macbook Pro**: Now with the M1 etc... it doesn't matter. I ran this rig on an Macbook Air for a while!
* **[Focusrite Scarlett 4 Pre](https://global.focusrite.com/thunderbolt-audio-interfaces/clarett-4pre)**: You need two stereo outs to play this rig. Otherwise you don't get a cue mix. You could use this rig quite well using the built-in audio interface on the Maschine MK3, too, since it's got two stereo outs (though you have to set it up using the Maschine hardware to send the audience mix to the cue as well). My feeling is that the Thunderbolt interface is much lower latency, but I'm unable to prove that hunch.
* **iPad Pro 12.9"**: You could use an iPad that runs iPadOS 16 or better.
* **Maschine Controllers**: I'm using Maschine MK3 and a Maschine Jam (Jam on the right).

![](http://dr2050.com/automaticImages/dan-rig-2018-02-22.jpg)

### Connections

I use the built-in MIDI connection between macOS and iPad (using Audio/MIDI Setup).

## Notes about the Maschine Setup

### Record-Only Pedal with Maschine MK3

Maschine Studio has two mono inputs for Play and Record pedals. In this rig, there is no Maschine Studio and there's no need for a Play pedal. To get a Record pedal only, plug your pedal in halfway to Maschine MK3's pedal slot.

### Maschine Can't Recognize Maschine Jam

If you use the same computer with multiple Jam controllers, [you might encounter this issue](http://maschineismygirlfriend.com/post/maschine-jam-is-lighting-up-and-then-shutting-off-on-os-x).

## Links

* [MIDI Designer Pro X on the App Store](https://mididesigner.com/app)
* [The Band -- music4yourTrip -- on Soundcloud](https://soundcloud.com/music4yourtrip)
* [Superfly Music on SoundCloud](https://soundcloud.com/superflymusic)
* [Maschine is My Girlfriend](http://maschineismygirlfriend.com)
