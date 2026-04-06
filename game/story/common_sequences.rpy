# functions to call for common parts of scenes

label AsleepSequence:
        window auto hide

        scene bg color black
        play music cabin_music fadein 0.5 loop volume 0.3
        play crickets crickets fadein 0.5 loop volume 0.5

        show overlay room ceiling:
                subpixel True
                additive 0.0
                matrixcolor BrightnessMatrix(-1.0)
                blur 10.0
        
        pause 2.0

        show overlay room ceiling with dissolve:
                subpixel True
                parallel:
                        linear 0.25 matrixcolor BrightnessMatrix(0.25)
                        linear 0.5 matrixcolor BrightnessMatrix(-0.4)
                        linear 0.5 matrixcolor BrightnessMatrix(-1.0)
                        linear 0.5 matrixcolor BrightnessMatrix(-0.3)
                parallel:
                        linear 1.25 additive 0.75
                        linear 0.5 additive 0.5

        pause 1.75

        show overlay room ceiling:
                subpixel True
                blur 10.0
                additive 0.5
                matrixcolor BrightnessMatrix(-0.3)

        pause 0.1
        
        window auto show
        return

label WakeUpSequence:
        window auto hide
        scene bg color black
        show overlay room ceiling:
                subpixel True
                blur 10.0
                additive 0.5
                matrixcolor BrightnessMatrix(-0.3)
        with dissolve

        show overlay room ceiling:
                subpixel True
                parallel:
                        linear 1.0 matrixcolor BrightnessMatrix(-1.0)
                        linear 1.0 matrixcolor BrightnessMatrix(0.0)
                        linear 0.5 matrixcolor BrightnessMatrix(-1.0)
                        linear 1.0 matrixcolor BrightnessMatrix(0.0) blur 0.0
                parallel:
                        linear 1.75 additive 1.0
                        linear 1.75 additive 0.0
        
        pause 3.5

        show bg room ceiling:
                subpixel True
                blur 0.0        
                matrixcolor BrightnessMatrix(0.0)
                additive 0.0

        pause 0.1

        window auto show
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

label FastShake:
        camera:
                subpixel True 
                linear 0.05 xpos 15
                linear 0.05 xpos -15
                linear 0.05 xpos 15
                linear 0.05 xpos -15
                linear 0.05 xpos 0
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
        return
        


label PainFlash:
        window auto hide
        show pain:
                subpixel True
                alpha 0.0
                linear 0.5 alpha 1.0 
                linear 1.0 alpha 0.5
                linear 2.0 alpha 0.0

        play soundb heart
        with Pause(0.7)
        stop soundb fadeout 0.5

        window auto show
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

label corruption_animation:
        show corruption_flame:
                pos(0.85,0.00) zoom 0.5 alpha 0.9
        with Dissolve(0.15)
        show corruption_light:
                pos(0.85,0.00) zoom 0.5 alpha 0.9
        with Dissolve(0.15)
        show corruption_paw:
                pos(0.85,0.00) zoom 0.5 alpha 1.0
        with Dissolve(0.3)
        pause 0.2
        show corruption_light:
                pos(0.85,0.00) zoom 0.5 alpha 0.9
                linear 1.0 alpha 0.0
        pause 0.4
        show corruption_flame:
                pos(0.85,0.00) zoom 0.5 alpha 0.9
                linear 1.0 alpha 0.0
        pause 0.2
        show corruption_paw:
                pos(0.85,0.00) zoom 0.5 alpha 1.0
                linear 0.25 alpha 0.4
                linear 0.2 alpha 1.0
        pause 0.5
        hide corruption_flame
        hide corruption_light
        hide corruption_paw with Dissolve(0.75)
        pause 0.5
        return

label humanity_animation:
        show humanity_flame:
                pos(0.85,0.00) zoom 0.5 alpha 0.8
        with Dissolve(0.15)
        show humanity_light:
                pos(0.85,0.00) zoom 0.5 alpha 0.8
        with Dissolve(0.15)
        show humanity_hand:
                pos(0.85,0.00) zoom 0.5 alpha 0.7
        with Dissolve(0.3)
        pause 0.2
        show humanity_light:
                pos(0.85,0.00) zoom 0.5 alpha 0.8
                linear 1.0 alpha 0.0
        pause 0.4
        show humanity_flame:
                pos(0.85,0.00) zoom 0.5 alpha 0.8
                linear 1.0 alpha 0.0
        pause 0.2
        show humanity_hand:
                pos(0.85,0.00) zoom 0.5 alpha 0.7
                linear 0.25 alpha 0.3
                linear 0.2 alpha 0.7
        pause 0.5
        hide humanity_flame
        hide humanity_light
        hide humanity_hand with Dissolve(0.75)
        pause 0.5
        return
