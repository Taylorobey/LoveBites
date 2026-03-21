label ConfrontationScene:
    $ save_name = "High Moon"

    scene bg room ceiling with dissolve
    call WakeUpSequence2

    if aka_lock:
        # don't know weakness path
        "You jolt awake. Outside your window, the night sky is full of stars and a waning moon. It is time."

    else:
        # know weakness path
        "You jolt awake. Outside the window, the night sky is full of stars and devoid of a moon. It is time."

    "This is the section where you peep in on Ashina."

    "This is the section where you go outside to meet Akari."

    "This is the section where you and Akari enter the cabin."

    "This is where you make a choice to attack Akari, attack Ashina, or stay put."

    "This is where you make a choice to disarm Akari, protect Ashina, or watch."

    "This is where you make the corruption choice to try to kill Akari, or the humanity choice to try to distract Akari, or do nothing."

    # Jump to Akari's death scene or otherwise
    jump AkariDeathScene

    return