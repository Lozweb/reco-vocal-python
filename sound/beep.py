from enum import Enum
import os

dir = os.path.dirname(__file__)


class SoundFile(Enum):
    beep11 = os.path.join(dir, "computerbeep_11.mp3")
    beep34 = os.path.join(dir, "computerbeep_34.mp3")
    workbeep = os.path.join(dir, "computer_work_beep.mp3")
    alert13 = os.path.join(dir, "alert13.mp3")
