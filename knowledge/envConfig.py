import sys
import os
import subprocess
from sound import beep
from jarvisIO import play_sound, to_voice

parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)


def find(question):
    if question == "active le mode triple écran":

        os.system("xrandr --output DVI-D-0 --primary --mode 1920x1080 --pos 1920x0 --output HDMI-0 --mode 1920x1080 --pos 3840x0 --output DVI-D-1 --mode 1920x1080 --pos 0x0")

    if question == "désactive le mode triple écran":
        os.system("xrandr --output DVI-D-0 --primary --mode 1920x1080 --pos 0x0 --output HDMI-0 --mode 1920x1080 --pos 1920x0 --output DVI-D-1 --off")


