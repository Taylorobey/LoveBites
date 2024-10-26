# functions to call for common parts of scenes
label WakeUpSequence1:
    #VSFX blur
    #i put this before scene so it wouldn't be unblurred whilst the scene was being dissolved in
    camera:
            subpixel True blur 20.0 

    # image captive cabin room (angled, zoomed in on ceiling)
    scene bg room ceiling with dissolve

    #music cabin
    play music cabin_music volume 0.3

    #SFX crickets
    play crickets crickets loop volume 0.5

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
    return

label AshinaShiftFromWolf:
        window auto hide
        hide wolf neutral with dissolve
        #show shifting ashina
        #show wolf neutral with dissolve:
                #subpixel True
                #pos (0.4, 0.2)
                #xzoom 1.09 yzoom 1.5
        #with Pause(0.2)
        #hide wolf neutral with dissolve
        with Pause(0.2)
        show ash angry hybrid with dissolve
        with Pause(0.4)
        show ash thoughtful with dissolve
        with Pause(0.4)
        show ash neutral with dissolve
        window auto show
        return

label AshinaScaryShift:
        show ash thoughtful with dissolve
        with Pause(0.15)
        show ash angry hybrid
        # player shakes, scared
        camera:
                subpixel True 
                linear 0.1 xpos 5 
                linear 0.1 xpos -5
                linear 0.1 xpos 5 
                linear 0.1 xpos -5
                linear 0.1 xpos 0
        with dissolve
        return

label AshinaScaryFastShift:
        show ash angry hybrid
        # player shakes, scared
        camera:
                subpixel True 
                linear 0.1 xpos 5 
                linear 0.1 xpos -5
                linear 0.1 xpos 5 
                linear 0.1 xpos -5
                linear 0.1 xpos 0
        with dissolve
        return

# common vfx that don't involve characters
# VFX red flash (on the edges)

label PainFlash:
    window auto hide
    show pain:
                subpixel True
                alpha 0.0
                linear 0.5 alpha 1.0 
                linear 1.0 alpha 0.5
                linear 2.0 alpha 0.0
    return