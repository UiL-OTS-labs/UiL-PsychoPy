""" A short demonstration of running a reading experiment """


import uil.stimuli.textstim as textstim
import psychopy.visual as psyvis


fragment_chinese = "這是一個英文例子。"
fragment_arabic = "هذا مثال باللغة الإنجليزية."
fragment_english = "This is a small english example."
fragment_japanese = "これは日本の例です。"

def run_experiment(textstim : textstim.TextStimulus, name=None):
    """Runs a small text stimulus experiment"""
    size = [s*2 for s in textstim.size()]
    window = psyvis.Window(
        name="UiL TextStimulus",
        size=size,
        screen=1,
        units="pix"
    )
    grating = psyvis.GratingStim(window, size=textstim.size())
    if name:
        grating.tex = name
    else:
        texture, _ = textstim.psychopy_texture()
        grating.tex = texture
    for i in range(60):
        grating.draw()
        window.flip()


if __name__ == "__main__":
    def_font = textstim.Font("Dejavu", size=18)
    # stim = textstim.TextStimulus(640, 480, def_font, fragment_english)
    # stim.draw()
    # stim.save_as_png("text-english.png")
    # run_experiment(stim)
    #
    # stim = textstim.TextStimulus(640, 480, def_font, fragment_arabic)
    # stim.draw()
    # stim.save_as_png("text-arabic.png")
    # run_experiment(stim)

    stim = textstim.TextStimulus(640, 480, def_font, fragment_chinese)
    stim.draw()
    stim.save_as_png("text-chinese.png")
    run_experiment(stim)

    stim = textstim.TextStimulus(640, 480, def_font, fragment_japanese)
    stim.draw()
    stim.save_as_png("text-japanese.png")
    run_experiment(stim)

