label IntroductoryCutscene:
        $ save_name = "Flirting with Disaster"


        window auto hide
        
        #Image Street Intersection
        scene bg intersection
        
        show fog onlayer screens:
                alpha 0.75

        #VSFX White Flash
        #SFX Car Speeding By
        play music intro_music loop volume 0.5
        play sound car
        hide placeholder with flash
        
        #VSFX Fog (ongoing)
        ### need assets for fog?
        
        #Music Introduction

        $ renpy.pause(.2)

        window auto show


        narrator "A car speeds through the intersection and your heart nearly leaps out of your chest."

        narrator "It’s always like this. The misleadingly calm night interrupted by reckless drivers, enjoying the lack of accountability that the darkness affords them."

        narrator "You wonder what it’s like to feel that free. To never worry about how your actions affect others. To be so completely focused on the self."

        narrator "Then again, you know what kind of person that makes. You lived with them."
        
        #VSFX Shaking text

        narrator "{sc}M o n s t e r s.{/sc}"
        narrator "…"
        
        #SFX Walking (ongoing)
        play sound walk loop
        
        #VSFX Slow Zoom on Image
        show bg intersection:
                subpixel True
                offset (0.0, 0.0) zoom 1.0
                linear 20 offset (1116.0, 891.0) zoom 2.21
        #does the zoom look good? changed this to be the bg zooming and not camera so we don't have problems with getting the camera back to 1.0 whilst dissolving in the next background

        narrator "You don’t want to think about that right now. It’s a wonder how the more exhausted your body is from work, the more active your mind gets."

        narrator "And you are exhausted. That’s the perk of working the graveyard shift- it’s the only way to get your body to pass out nearly the moment you hit the bed."
                         
        #VSFX Crossfade Image
        #Image Street with one dog
        scene bg street dog with dissolve
  
        #VSFX Slow Zoom on Image
        show bg street dog:
                subpixel True 
                offset (0.0, 0.0) zoom 1.0 
                linear 25 offset (-1773.0, 1881.0) zoom 4.0
        #same thing here


        narrator "You’ve always had trouble sleeping, even though it’s been three years since you moved out of that house."

        narrator "You thought getting out would be the hardest part. Turns out freedom can be pretty suffocating."

        #VSFX Crossfade Image
        #Image Street with three dogs
        scene bg street dogs with dissolve:
                offset (0.0,0.0) zoom 1.72 
                xanchor 0 xoffset absolute(0.0) 
        
        #VSFX Slow Zoom on Image
        ###How much zoom?
        show bg street dogs:
                subpixel True 
                linear 30 xanchor 0 xoffset -1377.0 
        window auto show


        narrator "You know it’s dangerous to walk home alone before sunrise. Maybe part of you wants something to happen to you."

        narrator "At least it would be something different, something new. Sometimes you feel as though you've been living the exact same day for these past three years. Go to work, pass out, repeat…"

        #VSFX Crossfade Image
        #Image Street with more dogs
        scene bg street many with dissolve

        #VSFX Medium Zoom on Image
        show bg street many:
                subpixel True 
                offset (0, 0) zoom 1
                linear 25 offset (-1000, 1079.0) zoom 4.0

        narrator "It was easier when you had something to fight against, someone to prove wrong. Now, you’re left alone with yourself, and you don’t like what you see."

        narrator "…There sure are a lot of dogs out tonight. Sure, you see the occasional stray out at night, but this is something else…"
        
        #SFX Heartbeat
        play soundb heart loop
        
        narrator "No, they’re just dogs. Maybe somebody left food out and it’s attracting them."

        #SFX Growling
        play sound growl
        #Music Introduction stops
        stop music
        
        #Image Black Screen
        scene bg color black with dissolve
        
        #VSFX Slow Typing, use cps tag

        narrator "{cps=5}YOU FEEL THEIR BREATH ON YOUR HEELS.{/cps}"
        camera:
                offset (0,0) zoom 1.0

        stop sound fadeout .5


        window auto hide
        #Image Street full of dogs
        scene bg street full with dissolve 

        #VSFX Fast Zoom on Image
        camera:
                subpixel True 
                offset (absolute(0.0), absolute(0.0)) zoom 1.0 
                linear 10 offset (3204.0, 2124.0) zoom 4.89 

        window auto show

        
        #Music Capture
        play music capture_music volume 0.3
        
        #SFX Running
        play sound run loop
        
        #SFX Barking
        play crickets barking volume 0.5

        narrator "They’re everywhere. In front of you. Behind you. Your body is suddenly alert and flooding with warmth. Your pulse is racing. You spot a side alley and turn without thinking."


        window auto hide
        with Pause(0.5)
        camera:
                offset (3204.0, 2124.0) zoom 4.89 

        #Image Dead-End Alley
        scene bg alley with dissolve:
                subpixel True zoom 0.5 

        camera:
                offset (0,0) zoom 1.0        
        #Image Wolf
        show wolf neutral with dissolve:
                subpixel True offset (794.0, 297.0)


        #SFX Running stops
        stop sound

        window auto show


        narrator "A large, intimidating wolf stands at the end of the alley. Although your mind is telling you to run, the sight of this ethereal creature freezes you in place."

        narrator "Your stomach lurches. You don’t have time to prepare for what comes next."


        window auto hide

        stop soundb fadeout 3.0
        stop crickets fadeout 5.0

        #image wolf snarling
        show wolf snarl with dissolve:
                subpixel True offset (794.0, 297.0)
        play sound growl volume 1.5

        pause(1.5)
        stop sound fadeout .5
        #Music Capture stops
        stop music fadeout 3.0

        #Image Wolf Lunging
        show wolf lunge with Dissolve(0.1):
                subpixel True offset (-70.0, -495.0) zoom 0.75 
        $ renpy.pause(delay=0.05, hard=False)

        hide fog onlayer screens

        #VSFX Red flash
        scene bg color red with Dissolve(0.05)
        $ renpy.pause(delay=0.05, hard=False)
        #Image Black Screen
        scene bg color black with Dissolve(0.1)


        #pause slightly for dramatic effect/to let dissolve finish
        pause(1.0)
        
        #Image Game Title Screen
        show logo:
                xalign 0.5
                yalign 0.5
        
        #SFX Howl
        play sound howl volume 0.5

        #pause before changing scenes else logo won't show
        pause(5.0)

        #move to waking scene
        jump WakingScene
        
