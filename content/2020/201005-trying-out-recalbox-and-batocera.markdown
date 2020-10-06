Title: Trying out Recalbox and Batocera
Author: gozar
Date: 2020-10-05 20:31
Slug: trying-out-recalbox-and-batocera
Category: Software
Tags: recalbox,batocera,emulation,emulationstation
Status: published
...

Today I decided to play around with the new version of [Recalbox](https://www.recalbox.com/) on one of my Raspberry Pis and Batocera on an old Intel Core 2 Duo Mac mini.

## Recalbox

First up was the Raspberry Pi. Setting up Recalbox was a piece of cake. I used [balenaEtcher](https://www.balena.io/etcher/) to image a 32GB SD card and then booted up the machine. It took awhile to set up the card, but after it was done, I was ready to go. Recalbox sets up a *Share* partition on the card. When you put the SD card in to a computer, a drive shows up with that partition. Inside it is where you put the ROMs and BIOSes that Recalbox will need.

My only issue with the install was when I went to use the composite out. I want to use the Recalbox on real CRTs, so I need the composite to work. The documentation for setting this up on the Recalbox site is missing. It looks like they are redoing their documentation. Luckily, I was able to [track down the missing documention on Archive.org](https://web.archive.org/web/20190615013227/https://github.com/recalbox/recalbox-os/wiki/Connect-your-recalbox-to-a-CRT-with-composite-(EN)). Using their directions I was able to get composite out working with Recalbox on my Raspberry Pi.

I stuck the SD card into my computer and edited the file `/boot/config.txt` adding the following lines:

    sdtv_mode=2
    hdmi_ignore_hotplug=1
    audio_pwm_mode=2

I then modified `recalbox.conf` changing _global.videomode_ to default:

    global.videomode=default

After a restart I was good to go! Unfortunately, the sound is pretty staticy, but that will be a problem to fix another day.

![Recalbox on a Pi3](https://cdn.gtia.com/pics/2020/Recalbox-2020-10-05-800x.jpeg)

## Batocera

Next up was to see how the performance of an 11 year old Mac Mini would be under emulation. [Batocera](https://batocera.org/) is weird for an install. By default, it runs only from the USB flash drive. To install it on the computer, you boot Batocera, and then in the menu, you can install it on the computer. Be sure there isn't anything you want on the drive of the computer, but it wipes it out! What's weird about this install is that it re-downloads Batocera as the first step in the process, drawing the process out.

The Mac Mini was fine, although it struggled a lot more with Dreamcast games versus the RPi3. I'm still looking for a use for this old Mac Mini because the Pi is a better choice. The latency with 2600 games was noticable even for me. I don't know where or why that is. The Mac has a spinny hard drive and only 2GB of RAM, so maybe there is a bottleneck. I'll have to do some more research.
