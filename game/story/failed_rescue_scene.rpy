label FailedRescueScene:
        pause(0.5)
        #otherwise the tint stays if you click too fast or use skip function
        camera:
                linear 1.0 matrixcolor TintMatrix("#fff")
        
        #SFX Creak
        play soundb creak volume 0.5 noloop
        call WakeUpSequence1
        call WakeUpSequence2

        window auto show
        "You stir groggily, your sleep disturbed by a loud creaking noise." 
        #window auto hide

        # Image Captive Cabin Room (full view) 
        scene bg room mc with dissolve

        # VSFX Slow Pan or Back And Forth Pan (as if looking around the room, whichever looks more natural, before settling on the window)
        #camera:
                #subpixel True 
                #parallel:
                        #pos (0, 0) 
                        #linear 0.77 pos (-9, -153) 
                        #linear 0.33 pos (-9, -153) 
                        #linear 1.43 pos (-594, -195) 
                        #linear 0.32 pos (-594, -195) 
                        #linear 0.48 pos (0, 0) 
                #parallel:
                        #zoom 1.0 
                        #linear 0.78 zoom 1.25 
                        #linear 0.34 zoom 1.25 
                        #linear 1.41 zoom 1.31 
                        #linear 0.32 zoom 1.31 
                        #linear 0.48 zoom 1.0 
        #with Pause(3.43)
        #camera:
                #pos (0, 0) zoom 1.0 
        #window auto show

        "Your eyes search the room for the noise and you notice a struggling figure wedged into the window. Somehow, even without getting a clear view, you know who it is."

        you "Cameron?!"

        "You quickly realize you should be quiet if you don’t want to draw any unwanted attention, so you lower your voice to a hushed tone."

        you "What are you {i}doing{/i} here?"

        cam "What does it look like? I’m here to break you out! That is, if I could squeeze through this pinche window!"

        # SFX Walking
        play soundb walk noloop
        # VSFX Zoom (as if walking towards the window)
        # made the pov closer to the camera
        window auto hide
        show bg room mc at walk_to_window
        with Pause(1.0)
        window auto show
        
        stop soundb
        #moved this up, felt it was weird to still have walking noises when the camera stopped
        "With a nervous glance towards the door, you slide out of bed and approach your struggling friend."

        window auto hide
        # Image Cameron Neutral
        # VSFX Cameron (close, from upper torso to head, similar to the view you would get pulling them out of the window)
        show cam neutral at start_bust 
        with dissolve

        # SFX Creak
        play soundb creak volume 0.25 noloop

        window auto show

        "You take their arms and give a firm tug. Your strength surprises you as you’re able to lift them into the cabin with ease."

        window auto hide
        # VSFX Fade out Cameron
        hide cam neutral with dissolve
        
        # VSFX Zoom (as if moving away from the window)
        show bg room mc at back_to_bg
        pause(1.1)

        # Image Cameron Friendly
        show cam friendly with dissolve
        window auto show
        cam "Phew! I thought I might be stuck there forever. Hey, have you been working out?"

        you "How did you find this place? No, scratch that…how did you even know I was here?"

        show cam friendly at pacing

        cam "I was making a run to the corner store, you know, the one on the edge of town, for my papi. Anyways, on my way out, I saw this huge lobo dragging you out into the woods."
        # VSFX Cameron (Slowly moving across the screen, as if pacing)     

        cam "I didn’t even think, I just started following, but I couldn’t get close because there were a bunch of dogs around, and they didn’t look friendly. I followed you all the way to this cabin." 

        cam "Then…"

        window auto hide
        show cam friendly at stop_pacing
        with Pause(1.5)
        # Image Cameron Nervous
        show cam nervous with dissolve
        window auto show

        "Cameron pauses, their eyes nervously averting to the side."

        # VSFX Cameron (a brief shake of the sprite side to side, as if shivering/nervous)
        show cam nervous at nervous_shake

        cam "This is going to sound crazy, but I saw the wolf turn into a {i}woman{/i}. Then she took you inside. And honestly… I ran. I thought it had to be some crazy dream."

        window auto hide
        show cam nervous
        with Pause(0.5)

        show cam friendly with dissolve
        with Pause(0.5)
        # VSFX Cameron (Slowly moving across the screen, as if pacing)
        show cam friendly at pacing
        window auto show

        cam "I thought about going to the police, but no way they’d believe me. I went to work and tried to forget about it, but I couldn’t. So, here I am."

        show cam friendly at stop_pacing

        "There’s a long pause before you respond, not really sure how to take in all of that information."

        window auto hide
        pause(2)
        window auto show

        you "…How did you manage to get past the guard dogs?"

        window auto hide
        # Image Cameron Neutral
        show cam nervous with dissolve
        with Pause(0.5)
        # VSFX Cameron (slight up and down motion, as if shrugging)
        # looked a bit like jumping so i messed with it a little
        show cam nervous:
                subpixel True 
                ypos 1.0 
                linear 0.3 ypos 0.97
                linear 0.3 ypos 1.0 
        with Pause(0.6)
        window auto show

        cam "They left in a big pack all of a sudden. Don’t know where they ran off to, but figured this was my only chance to get you out of here."

        you "That was really risky, Cam."

        # Image Cameron Friendly
        show cam friendly with dissolve

        cam "I know, believe me. My heart was pounding the whole way here!"

        # VSFX Cameron (Slowly moving across the screen, as if pacing)
        show cam friendly at pacing
        cam "I’m probably the last person you thought would rescue you. I mean, when we found that wasp nest when we were kids, I ran screaming all the way home, just leaving you there."
        
        window auto hide
        show cam friendly at stop_pacing
        pause(2)

        # VSFX Cameron (slight up and down motion, as if shrugging)
        show cam friendly:
                subpixel True 
                ypos 1.0 
                linear 0.3 ypos 0.97
                linear 0.3 ypos 1.0 
        with Pause(0.6)
        window auto show

        cam "But, I dunno, I couldn’t leave without trying. So, come on, let’s go home and I’ll make you a nice, hot bowl of pozole. "

        "A shiver goes down your spine, and your breathing sounds... different. You get a {b}{color=#1C4587}strange feeling{/b}{/color}, like you're both here and standing outside of the room, but decide to refocus on Cam's words. This place is making you paranoid."
        camera:
                linear 1.0 matrixcolor TintMatrix("#fff")
        menu:
                "Agree to go with Cameron.":
                        jump GoWithCam
                "Urge Cameron to leave.":
                        jump UrgeCamLeave


label GoWithCam:

        #Cameron Approval Choice: 
        $ cam_approval += 1
        $ ash_approval -= 1

        "You try to ignore that, in the back of your head, you hunger more for the plate of raw meat from earlier than a bowl of soup. You’d give anything to feel normal. Your tiny, dingy apartment doesn’t sound so bad right now."

        you "Yeah, let’s get out of here."

        jump CamCaught

label UrgeCamLeave:

        #Ashina Approval Choice:
        $ ash_approval +=1

        you "Cameron… It’s not that easy. "

        # Image Cameron Nervous
        show cam nervous with dissolve

        cam "What do you mean? We can just walk out right now!"

        you "Sure, we could physically escape…"

        you "But, something’s obviously after me. What’s to stop them from dragging me back here again? "

        # Image Cameron Friendly
        show cam friendly with dissolve

        cam "I’ll watch over you. When you get out of work, I can pick you up and take you home. I’ll even stay over at your place and keep a look out."

        you "And what makes you think they won’t hurt you to get to me?"

        # Image Cameron Nervous
        show cam nervous with dissolve

        cam "…"

        you "You need to leave, Cameron. Before the dogs come back. Before she finds you."

        show cam nervous:
                subpixel True 
                ypos 1.0 
                linear 0.15 ypos 0.98 
                linear 0.15 ypos 1.02 
                linear 0.15 ypos 1.0 
        with Pause(0.55)
        show cam nervous:
                ypos 1.0 

        cam "Fine, fine, I’ll go. But I’m not just going to leave you out here."

        cam "I’ll get help, and I’ll come back. Just hang tight, okay?"

        jump CamCaught

label CamCaught:

        # Image Cabin Door Closed
        scene bg door closed with dissolve

        # Image Cameron Neutral
        show cam neutral onlayer screens with dissolve:
                xalign 0.6 zoom 1.5 

        stop music fadeout 2.0
        "Cameron’s hand reaches for the doorknob. When they open the door, your stomach drops."

        # SFX Creak
        play sound creak volume 0.5

        # Image Cabin Door Open
        show bg door open with dissolve
        #so cam doesn't disappear

        ## Ashina and Cameron should be moving together at the parts where Ashina moves towards Cameron, as if she's pulling them around with her while taunting you, also hopefully with how Ashina's pose works Cameron can be more in front of her while she's menacing them.
        # VSFX Fade In Ashina
        # Image Ashina Friendly
        # not sure why xalign is playing opposites
        show ash friendly with dissolve:
                subpixel True xalign 0.4 zoom 1.5

        show cam scared onlayer screens with dissolve

        # Music Capture
        play music capture_music volume 0.3 loop

        ash "My my, what do we have here?"

        # VSFX Crossfade Ashina Friendly into
        # Image Ashina Angry Hybrid
        show ash angry hybrid with dissolve:
                subpixel True xalign 0.4 zoom 1.5

        "The woman’s features suddenly become beastly, claws curling out from her fingernails and fur sprouting through her skin."

        # Image Cameron Scared
        # again xalign is playing opposites i don't know whyyy aaaaaa
        show cam scared onlayer screens with dissolve:
                xalign 0.6 zoom 1.5 

        "In the blink of an eye, your captor wraps her claws around Cameron’s throat. At any moment, she could pierce their skin and tear them to shreds."

        "She meets your gaze as she taunts you."

        # VSFX Ashina and Cameron (closer)
        show ash angry hybrid with moveinleft:
                xalign 0.5
        show cam scared onlayer screens with moveinleft:
                xalign 0.7

        ash "A friend of yours, I take it?"

        "Cameron, in contrast to their big talk beforehand, is now frozen with fear in your captor’s grasp."

        # VSFX Ashina and Cameron (further away)
        show ash angry hybrid with moveinleft:
                xalign 0.7
        show cam scared onlayer screens with moveinleft:
                xalign 0.9

        ash "At least this human knows their place. Had they dared to put up a fight, I would have killed them where they stood. "

        ash "Now, what to do with them…"

        you "Let them go! Please…"

        # VSFX Ashina and Cameron (closer)
        show ash angry hybrid with moveinleft:
                xalign 0.5
        show cam scared onlayer screens with moveinleft:
                xalign 0.7

        ash "You do not give the orders around here. Besides, that is something I simply cannot do." 

        # VSFX Ashina and Cameron (further away)
        show ash angry hybrid with moveinleft:
                xalign 0.7
        show cam scared onlayer screens with moveinleft:
                xalign 0.9

        ash "It’d be foolish of me to free a human that knows of this place. Much less someone so set on freeing my little pet." 

        "You feel indignant over her calling you a \"little pet\", but decide this wouldn’t be the time to object."

        ash "Perhaps, if you are a good girl, I’ll have mercy on your little friend here."

        # VSFX Ashina and Cameron (further away, as if backing out the door)
        show ash angry hybrid with dissolve:
                subpixel True xpos 0.55 ypos 45 zoom 1.1
        show cam scared onlayer screens with dissolve:
                subpixel True xpos 0.7 ypos 45 zoom 1.1

        ash "Keep them in your thoughts whenever you feel like acting up again, won’t you?"

        stop music fadeout 2.0

        # VSFX Ashina and Cameron quickly Fade Out
        hide ash angry hybrid with dissolve
        hide cam scared onlayer screens with dissolve

        # SFX Creak
        play sound creak volume 0.5

        # Image Cabin Door Closed
        scene bg door closed with dissolve

        # Music Cabin
        play music cabin_music volume 0.3 fadein 2.0

        "Before you even have a chance to protest, your captor shuts the door. Your legs shake, threatening to give out, and you stumble back towards the bed."

        # Image Captive Cabin Room
        scene bg room mc with dissolve

        "You have to be careful. Before, everything you did only affected you. Frankly, those stakes weren’t very high. You’ve felt like your life is worth very little for a while now."

        "But now, everything you do has Cameron’s very life on the line. Everything counts now, and you\’ll do anything in your power to keep them safe."

        "Somehow, another wave of exhaustion hits you. Perhaps it’s sleep debt catching up to you."

        # Image Captive Cabin Room (angled, zoomed in on ceiling)
        scene bg room ceiling with dissolve
        # VSFX Blur (as if falling asleep)
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

        "You lie down without thinking, your hands curling into fists and tears welling in your eyes. You fight to stay conscious, but it’s no use."

        stop crickets fadeout 2.5

        "…Just before you drift off, you notice your nails feel unusually sharp."

        stop music fadeout 1.5

        # Image Black Screen
        scene bg color black with dissolve
        with Pause(2.0)

        #this scene breaks the dreamscene, but dreamscene plays fine if you jump straight to it
        jump DreamScene
