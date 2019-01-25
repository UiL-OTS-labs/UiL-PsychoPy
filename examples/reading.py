""" A short demonstration of running a reading experiment """


import os
import sys
uildir = os.path.dirname(os.path.dirname(sys.argv[0]) + "/..")
print (sys.path)
sys.path = sys.path[0:1] + [uildir] + sys.path[1:]
print (sys.path)

import stimuli.textstim


if __name__ == "__main__":
    text_stim = stimuli.textstim.TextStimulus()
    a = 1

