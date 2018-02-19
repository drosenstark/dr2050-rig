# Dan Rosenstark's Live Improvisation

## Overview

This is my rig for live improvisation. While my focus is mainly on drums and percussion, the rig relies heavily on Maschine. Therefore, you could focus on melodic instruments of many types with ease.

A single Maschine plugin inside Ableton Live produces all the sounds. I limit myself to 8 groups in Maschine to avoid paging, each of which comes to a separate output. Using MIDI Designer, I'm able to EQ those groups, send them to a delay return. From there, the sound is passed through a Master FX section and then out to the audience (1/2 on the audio interface).

In addition to the audience mix, there is a Cue Mix which goes to the cue ouput (3/4 on the audio interface). Any group may be easily sent to the Cue Mix **instead** of the audience mix. I've found group cueing inside Maschine to be too hard to reach, and I'm also avoiding Maschine's click. Instead I've a 1-bar (4/4) recording of Maschine's click, which goes out to the Cue Output and is always volume adjustable in MIDI Designer.

I've also got a MIDI clip in Live which powers a visual metronome on the MIDI Designer display, which is a nice little hack. It's awesome for orienting where the "one" is without having to crank the click volume.

Putting Maschine inside Ableton is a trade-off: I've given up transport and tempo controls, firstly. I've also chosen to ignore the Aux sends in Maschine, and the Master section (and meters on the Jam or Studio) are not being used. In exchange, I get a more flexible routing and sends wherever I want them. I also get to use Ableton's Simple Delay, Ping-Pong Delay and Grain Delay (the former two do pitch bending awesomely), and the 3-band Ableton EQ. I also put limiters wherever I see fit. I also suspect that Maschine performs better inside Ableton, but I haven't bothered to try to prove this yet.

Here's the current MIDI Designer screen, now consolidated to one (double) page.

![DR2050 Rig in MIDI Designer Pro 2](https://www.dropbox.com/s/4pfkxi8fs192it4/2018-02-18%2018.34.37.png?raw=1)

## Dependencies

### Software

* **Maschine 2**: Maschine 2 is the heart of this rig and the sole sound source.
* **[MIDI Designer Pro 2](http://midiDR.com)**: Did I mention that I'm the software author of [MIDI Designer](http://mididesigner.com)? The whole point of this rig is to make music, and I've done many iterations of the rig without. Currently, I cannot do with it, but you could conceivably recreate this rig using a hardware MIDI controller, Lemur, or something else.
* **Ableton Live**: While I'm using Ableton Live 9 Suite, I'm quite sure that I don't use any features that aren't in the Standard Edition. Here's [the editions matrix](https://www.ableton.com/en/live/compare-editions)
* **Sugar Bytes Turnado**: I'm kind of in love with Turnado for stutters. Though I use the performance effects in Maschine quite a bit -- particularly the stutter -- I'm shoving the entire mix through Turnado and also provide a Wet knob which makes it very expressive and fun.
* **Native Instruments Guitar Rig 5**: I'm currently **only** using the Studio Reverb from this, so you could probably substitute it out with something else without an issue.

### Hardware

* **Macbook Pro**: I run the fastest, latest MBP with 16GB of RAM and an SSD. I think you could get away with 8GB or RAM and a much older I7 (my 2013 was fun), but the SSD is essential. I've got a lot of stuff on an external SSD right now, which I'm not sure is a great choice.
* **[Focusrite Scarlett 4 Pre](https://global.focusrite.com/thunderbolt-audio-interfaces/clarett-4pre)**: You need two stereo outs to play this rig. Otherwise you don't get a cue mix. You could use this rig quite well using the built-in audio interface on the Maschine MK3, too, since it's got two stereo outs (though you have to set it up using the Maschine hardware to send the audience mix to the cue as well). My feeling is that the Thunderbolt interface is much lower latency, but I'm unable to prove that hunch.
* **iPad Pro 2017 10.5"**: I use an iPad exclusively to run MIDI Designer Pro 2. While this will run on any iPad 2 or greater, I really recommend an iPad Air 2 or greater. My current iPad is definitely overkill.

### Connections

I use the built-in MIDI connection between OS X High Sierra and iOS 11, although you could use [musicIO MIDI just as well](http://musicioapp.com/ios). **Note**: I also am one of the software authors of musicIO, too.

## Notes about the MIDI Designer Layout

I don't think I'm using **any** of the features of the Extra Features Pack, so if somebody reminds me, I'll delete the photos that make this layout uneditable without the EFP. On the other hand, if you are reading this and send me a message, I could just send you a code for the EFP unlock.

## Notes about the Maschine Setup

**Do not load a kit into Slot H**

I'm using a lot of kits that are either in Maschine Expansions or come from somewhere else. You can and should load a new kit into any slot **except slot H!**. Slot H is for longer playing loops and one-shots (particularly spoken word type of things), and it's got some cool Macro controls hooked up.


## Notes on the Live Set's Recording Tracks

You may have noticed the other tracks on the Recording section: Nikki and Visitor. These are for my wife, Nikki, when she sings, and for a visitor. You should definitely use zero-latency routing to get these to the audience and the cue mixes **before** they go through the their A/D pass and come in to Ableton Live, however!
