from earsketch import *
import random

setTempo(88)

electrostring = Y13_STRING_1
drum = CIARA_ROOTED_DRUMBEAT_1
synth = DUBSTEP_BASS_WOBBLE_032

beat1 = "0-0-0-0++0-0-0-0+++++--0"
beat2 = "----0+++"
beat3 = "0+++----"

def myFunction(startMeasure):
    makeBeat(drum, 3, startMeasure, beat2)
    makeBeat(synth, 4, startMeasure, beat3)

    
for measure in range(3):
    beat3 = beat3 + beat3

for measure in range(3):
    beat2 = beat2 + beat2


fitMedia(electrostring, 1, 1, 60)
fitMedia(drum, 2, 5, 60)
setEffect(1, VOLUME, GAIN, -60, 1, 0, 5)
myFunction(1)

