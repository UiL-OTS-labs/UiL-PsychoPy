""" A short demonstration of running a reading experiment """


import uil.stimuli.textstim as textstim


fragment_chinese = "這是一個英文例子。"
fragment_arabic = "هذا مثال باللغة الإنجليزية."
fragment_english = "This is a small english example"

def run_experiment():
    """Runs a small text stimulus experiment"""


if __name__ == "__main__":
    def_font = textstim.Font("times", size=16)
    stim = textstim.TextStimulus(640, 480, def_font, fragment_english)
    stim.draw()
    stim.save_as_png("text-english.png")

    stim = textstim.TextStimulus(640, 480, def_font, fragment_arabic)
    stim.draw()
    stim.save_as_png("text-arabic.png")

    stim = textstim.TextStimulus(640, 480, def_font, fragment_chinese)
    stim.draw()
    stim.save_as_png("text-chinese.png")
