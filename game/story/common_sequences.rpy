# functions to call for common parts of scenes
label WakeUpSequence1:
    #stop audio from previous scene
    stop sound
    #VSFX blur
    #i put this before scene so it wouldn't be unblurred whilst the scene was being dissolved in
    camera:
            subpixel True blur 20.0 

    # image captive cabin room (angled, zoomed in on ceiling)
    scene bg room ceiling with dissolve

    #music cabin
    play music cabin_music

    #SFX crickets
    play sound crickets loop

    return

label WakeUpSequence2:
    window auto hide
    camera:
            subpixel True 
            linear 1.00 blur 5.0 
            linear 1.00 blur 20.0 
            linear 1.00 blur 0.0
    with Pause(3)
    camera:
            blur 0.0 
    window auto show
    return

# common vfx that don't involve characters
# VFX red flash (on the edges)
label PainFlash:
    show pain:
                subpixel True
                alpha 0.0
                linear 0.5 alpha 1.0 
                linear 1.0 alpha 0.5
                linear 2.0 alpha 0.0
    return