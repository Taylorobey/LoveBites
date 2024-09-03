label IntroductoryCutscene:

        #Image Street Intersection
        scene bg intersection
        
        #VSFX White Flash
        #SFX Car Speeding By
        play sound car
        hide placeholder with flash
        
        #VSFX Fog (ongoing)
        ### need assets for fog?
        
        #Music Introduction
        play music intro_music loop
        narrator "It’s always like this. The misleadingly calm night interrupted by reckless drivers, enjoying the lack of accountability that the dark affords them."
        narrator "You wonder what it’s like to feel that free. To never worry about how your actions affect others. To be so completely focused on the self."
        narrator "Then again, you know what kind of person that makes. You lived with them."
        
        #VSFX Shaking text
        narrator "{sc}M o n s t e r s.{/sc}"
        narrator "…"
        
        #SFX Walking (ongoing)
        play sound walk loop
        
        #VSFX Slow Zoom on Image
        ###How much zoom?
        narrator "You don’t want to think about that right now. It’s a wonder how the more exhausted your body is from work, the more active your mind gets."
        narrator "And you are exhausted. That’s the perk of working the graveyard shift- it’s the only way to get your body to pass out nearly the moment you hit the bed."
        
        #VSFX Crossfade Image
        #Image Street with one dog
        show bg street dog with dissolve
        
        #VSFX Slow Zoom on Image
        ###How much zoom?
        narrator "You’ve always had trouble sleeping, even though it’s been three years since you moved out of that house."
        narrator "You thought getting out would be the hardest part. Turns out freedom can be pretty suffocating."
        
        #VSFX Crossfade Image
        #Image Street with three dogs
        show bg street dogs with dissolve 
        
        #VSFX Slow Zoom on Image
        ###How much zoom?
        narrator "You know it’s dangerous to walk home alone before sunrise. Maybe part of you wants something to happen to you." 
        narrator "At least it would be something different, something new. Sometimes you feel as though you've been living the exact same day for these past three years. Go to work, pass out, repeat…"
        narrator "It was easier when you had something to fight against, someone to prove wrong. Now, you’re left alone with yourself, and you don’t like what you see."
        narrator "…There sure are a lot of dogs out tonight. Sure, I see the occasional stray out at night, but this is something else…"
        
        #VSFX Crossfade Image
        #Image Street with more dogs
        show bg street many with dissolve 
        
        #VSFX Medium Zoom on Image
        ###How much zoom?
        stop sound
        
        #SFX Heartbeat
        play sound heart loop
        
        #SFX Faster Walking
        play sound fast_walk loop
        narrator "No, they’re just dogs. Maybe somebody left food out and it’s attracting them."
        
        #SFX Growling
        #Music Introduction stops
        stop music
        
        #Image Black Screen
        show bg color black with dissolve
        
        #VSFX Slow Typing, use cps tag
        narrator "{cps=10}YOU FEEL THEIR BREATH ON YOUR HEELS.{/cps}"
        
        #Image Street full of dogs
        show bg street full with dissolve 
        
        #Music Capture
        play music capture_music
        
        #SFX Running
        play sound run loop
        
        #SFX Barking
        
        #VSFX Fast Zoom on Image
        ###How much zoom?
        narrator "They’re everywhere. In front of you. Behind you. Your body is suddenly alert and flooding with warmth. Your pulse is racing. You spot a side alley and turn without thinking."
        
        #Image Dead-End Alley
        scene bg alley with dissolve
        
        #Image Wolf
        show wolf neutral
        
        #SFX Running stops
        stop sound
        narrator "A large, intimidating wolf stands at the end of the alley. Although your mind is telling you to run, the sight of this ethereal creature freezes you in place."
        narrator "Your stomach lurches. You don’t have time to prepare for what comes next."
        
        #Image Wolf Lunging
        show wolf lunge with dissolve

        #VSFX Red flash
        scene bg color red with dissolve
        
        #Image Black Screen
        scene bg color black with dissolve
        #not sure why this used "show"

        
        #Music Capture stops
        stop music
        
        #Image Game Title Screen
        show logo:
                xalign 0.5
                yalign 0.5
        
        #SFX Howl
        play sound howl

        #pause before changing scenes else logo won't show
        pause(5.0)

        #move to waking scene
        jump WakingScene
        
