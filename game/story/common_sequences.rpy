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
        show ash hybrid arms down with dissolve
        with Pause(0.4)
        show ash thoughtful:
                xoffset 40
        with dissolve
        with Pause(0.4)
        show ash neutral:
                xoffset 0
        with dissolve
        window auto show
        return

label AshinaScaryShift:
        show ash thoughtful_reverse:
                xoffset 40
        with dissolve
        with Pause(0.05)
        show ash hybrid arms down:
                xoffset -305
        with dissolve
        with Pause(0.05)
        show ash angry hybrid:
                xoffset -305
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

label AshinaScaryShiftReverse:
        show ash thoughtful:
                xoffset 40
        with dissolve
        with Pause(0.15)
        show ash hybrid arms down:
                xoffset 0
        with dissolve
        with Pause(0.05)
        show ash angry hybrid:
                xoffset 0
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

label Shake:
        camera:
                subpixel True 
                linear 0.1 xpos 15
                linear 0.1 xpos -15
                linear 0.1 xpos 15
                linear 0.1 xpos -15
                linear 0.1 xpos 0
        with dissolve
        return

label Jump:
        camera:
                subpixel True 
                linear 0.1 ypos 15
                linear 0.1 ypos -15
                linear 0.1 ypos 0
        with dissolve
        return

label PainShake:
        window auto hide
        camera:
                subpixel True 
                linear 0.1 xpos 15
                linear 0.1 xpos -15
                linear 0.1 xpos 15
                linear 0.1 xpos -15
                linear 0.1 xpos 0
        
        show pain onlayer screens:
                subpixel True
                alpha 0.0
                linear 0.5 alpha 1.0 
                linear 1.0 alpha 0.5
                linear 2.0 alpha 0.0
        


label PainFlash:
    window auto hide
    show pain:
                subpixel True
                alpha 0.0
                linear 0.5 alpha 1.0 
                linear 1.0 alpha 0.5
                linear 2.0 alpha 0.0
    return

label GoToHearth:
        window auto hide
        # SFX Walking
        play sound walk loop
        # Image Cabin Door Open
        show bg door open with dissolve:
                subpixel True
                zoom 1.0
                linear 2.00 zoom 2.0 yalign(0.5)
        with Pause(1.5)
        show bg door open:
                zoom 2.0 yalign(0.5)
        # Image Cabin Hall
        stop crickets fadeout 1.0
        show bg hallway with dissolve:
                subpixel True 
                zoom 0.53
                linear 2.00 zoom 1.0 xalign(0.8) yalign(0.3)
        with Pause(1.5)
        show bg hallway:
                zoom 1.0 xalign(0.8) yalign(0.3)
        stop music fadeout 4.0
        play soundb fireplace volume 0.3 loop fadein 2.0
        # Image Downstairs
        show bg downstairs with dissolve:
                subpixel True
                zoom 1.0 xalign(0.5) yalign(0.01)
                linear 2.00 zoom 2.0 xalign(0.5) yalign(0.01)
        with Pause(1.5)
        show bg downstairs:
                zoom 2.0 xalign(0.5) yalign(0.01)
        return

label GoDownstairs:
        window auto hide
        play sound walk loop
        show bg downstairs with dissolve:
                subpixel True
                zoom 1.0 xalign(0.5) yalign(0.01)
                linear 2.00 zoom 2.0 xalign(0.5) yalign(0.01)
        with Pause(1.5)
        show bg downstairs:
                zoom 2.0 xalign(0.5) yalign(0.01)
        stop sound fadeout 1.0
        return

label GoUpstairs:
        window auto hide
        play sound walk loop
        show bg upstairs with dissolve:
                subpixel True
                zoom 1.0 xalign(0.5) yalign(0.01)
                linear 2.00 zoom 2.0 xalign(0.5) yalign(0.01)
        with Pause(1.5)
        show bg upstairs:
                zoom 2.0 xalign(0.5) yalign(0.01)
        stop sound fadeout 1.0
        return

label GoOutsideDogs:
        window auto hide
        play sound walking loop
        show bg door open with dissolve:
            subpixel True
            zoom 1.0 pos(0.5,0)
            linear 2.00 zoom 2.0 yalign(0.5)
        with Pause(1.5)
        stop soundb fadeout 1.0
        show bg door open:
            zoom 2.0 yalign(0.5)
        play crickets crickets fadein 0.5
        scene bg cabin ext dogs with dissolve
        pause 1.0
        stop sound
        return

label GoOutsideNoDogs:
        window auto hide
        stop soundb fadeout 2.0
        play sound walking loop
        show bg door open with dissolve:
            subpixel True
            zoom 1.0 pos(0.5,0)
            linear 2.00 zoom 2.0 yalign(0.5)
        with Pause(1.5)
        stop soundb fadeout 1.0
        show bg door open:
            zoom 2.0 yalign(0.5)
        play crickets crickets fadein 0.5
        scene bg cabin ext no dogs with dissolve
        pause 1.0
        stop sound
        return
