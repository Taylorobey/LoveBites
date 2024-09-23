label BotchedEscapeScene:
        #stop audio from previous scene
        #stop sound

        #Image Cabin Hearth
        scene bg hearth

        "You're left with your own thoughts as Ashina departs upstairs. You begin to wander the cabin aimlessly."
        play crickets crickets fadein 0.5 loop
        # Image Cabin Door Open
        show bg door open with dissolve
        #SFX Fireplace (fade out)
        # SFX Crickets

        "You realize the front door is open."

        menu:
                # Narrative Choice
                "Try to escape.":
                        "Ashina should be asleep by now. This is your chance to escape and bring back help for Cameron."

                #Narrative Choice
                "Get some fresh air.":
                                "It would be nice to get some fresh air. You've been stuck inside for a couple days now, and you can’t help feeling a bit claustrophobic."

        #choices converge here

        "You lean out of the open door as quietly as possible to find…"

        # Image Cabin Exterior Leaving POV No Dogs
        show bg forest edge with dissolve:
                subpixel True xzoom 1.0 yzoom 7.82 


        # Music Eerie Outdoors
        play music eerie_outdoors_music

        you "…Nothing?"

        # SFX Walking
        play sound walk loop
        # VSFX Cabin Ext.(zoom, as if walking)

        "You take a few cautious steps outside, thinking your eyes must be playing tricks on you. Where did all the dogs go? Was this another lucky break, like when Cameron snuck in?"

        # SFX Walking
        # Image Forest Edge
        show bg forest edge with dissolve:
                subpixel True xzoom 1.0 yzoom 1.0

        "You continue on, making it to the edge of the forest. You can hear your heart pounding in your chest. Were you really able to just… walk out of here?"

        # SFX Walking (stop)
        stop sound
        # Image Akari Bow Drawn (close)
        show aki bow drawn with dissolve

        "As you move into the foliage, you're stopped dead in your tracks. A silver arrow is aimed square between your eyes. The wielder of the bow is a sharp-eyed, hooded figure with hair black as night."

        ## VSFX Akari (zoom to fullbody)

        aki "Don't you dare move, monster!"

        "You put your hands up in the most placating gesture you can manage."

        you "Monster…? Uh, I think this is a misunderstanding, maybe we could just-"

        # VSFX Akari (closer)
        show aki bow drawn:
                subpixel True 
                ypos 1.0 zoom 1.0 
                linear 0.19 ypos 1.13 zoom 1.12 
        with Pause(0.29)
        show aki bow drawn:
                ypos 1.13 zoom 1.12

        aki "Stop. You will not fool me. I know you."

        # VSFX Akari (closer)
        show aki bow drawn:
                subpixel True 
                ypos 1.13 zoom 1.12 
                linear 0.2 ypos 1.43 zoom 1.36 
        with Pause(0.3)
        show aki bow drawn:
                ypos 1.43 zoom 1.36 

        aki "I will have no mercy on you. Your death shall be painful, I will make sure of it. You will suffer for every life you have stolen, and I will have my revenge. You chose the wrong night to leave your little fortress, and now, you will finally pay."

        "You can't just let it end here. Not now."

        menu:
                # Akari Approval Choice
                "Plead your case.":
                        $ aka_approval += 1
                        jump PleadCase
                #Akari Disapproval/Ashina Approval Choice
                "Call out for Ashina.":
                        $ ash_approval += 1
                        $ aka_approval -= 1
                        jump CallOut

label PleadCase:
        you "No, wait, please! I never asked to be a monster!"

        # VSFX Akari nod
        show aki bow drawn:
                subpixel True 
                ypos 1.43 
                linear 0.15 ypos 1.45 
                linear 0.10 ypos 1.4 
                linear 0.05 ypos 1.43 
        with Pause(0.40)
        show aki bow drawn:
                ypos 1.43 

        "The hooded woman looks surprised at your outburst. Her stance doesn't waver, but she nods slowly at you to continue."

        you "Where do I begin…? I was out late. A bunch of dogs, hundreds of them, cornered me into an alley. Then, a huge wolf-beast attacked me, dragged me here, and turned me into…"

        # VSFX Akari (further)
        show aki bow drawn:
                subpixel True 
                ypos 1.43 zoom 1.36
                linear 0.2 ypos 1.13 zoom 1.12
        with Pause(0.3)
        show aki bow drawn:
                ypos 1.13 zoom 1.12

        aki "The smaller dogs you mentioned. Where are they now?"

        # Image Akari Bow Nocked
        show aki bow nocked with dissolve
        # The spelling on that is a pet peeve of mine
        # VSFX Akari (move horizontally across the screen, as if looking around)

        "The woman lowers her bow, looking around suspiciously."
        show aki bow nocked:
                subpixel True 
                parallel:
                        xpos 0.5 
                        linear 0.30 xpos 0.34 
                        linear 0.10 xpos 0.34 
                        linear 0.17 xpos 0.34 
                        linear 0.30 xpos 0.34 
                        linear 0.20 xpos 0.66 
                        linear 0.10 xpos 0.66 
                        linear 0.15 xpos 0.66 
                        linear 0.10 xpos 0.66 
                parallel:
                        yrotate 0.0 
                        linear 0.30 yrotate 0.0 
                        linear 0.10 yrotate 0.0 
                        linear 0.17 yrotate -180.0 
                        linear 0.30 yrotate -180.0 
                        linear 0.20 yrotate -180.0 
                        linear 0.10 yrotate -180.0 
                        linear 0.15 yrotate 0.0 
                        linear 0.10 yrotate 0.0 

        you "I don’t know, they were gone when I stepped outside. They must have run off somewhere, maybe-"

        show aki bow nocked:
                xpos 0.66 yrotate 0.0

        aki "The large one, the wolf-beast. That is their master, is it not?"

        you "Yes. She goes by Ashina. She's been holding me captive."

        you "My friend tried to rescue me, but now they’re trapped here too. She said she wouldn’t do anything to them so long as I behave, but…"

        # Image Akari Angry
        show aki angry with dissolve

        aki "I see. So that lycanthrope is going around toying with the lives of innocent humans yet again. What a disgusting creature."

        # Image Akari thoughtful
        show aki thoughtful with dissolve

        "The woman turns her bow and arrow away from you, continuing to scan the surroundings."

        # VSFX Akari (move horizontally across the screen, as if looking around, other direction)
        window auto hide
        show aki thoughtful:
                subpixel True 
                parallel:
                        xpos 0.66
                        linear 0.30 xpos 0.34 
                        linear 0.10 xpos 0.34 
                        linear 0.17 xpos 0.34 
                        linear 0.30 xpos 0.34 
                        linear 0.20 xpos 0.66 
                        linear 0.10 xpos 0.66 
                        linear 0.15 xpos 0.66 
                        linear 0.10 xpos 0.66 
                parallel:
                        yrotate 0.0 
                        linear 0.30 yrotate 0.0 
                        linear 0.10 yrotate 0.0 
                        linear 0.17 yrotate -180.0 
                        linear 0.30 yrotate -180.0 
                        linear 0.20 yrotate -180.0 
                        linear 0.10 yrotate -180.0 
                        linear 0.15 yrotate 0.0 
                        linear 0.10 yrotate 0.0 
        with Pause(2.0)
        show aki thoughtful:
                xpos 0.66 yrotate 0.0 
        window auto show
        
        aki "Everything about this spells out a trap. I need to get out of here."

        show aki neutral with dissolve
        with Pause(0.5)
        show aki neutral:
                subpixel True 
                pos (0.66, 1.13) zoom 1.12 
                linear 0.5 pos (0.5, 1.4) zoom 1.3 

        "She turns her dark gaze back to you."
        window auto hide
        with Pause(0.50)
        show aki neutral:
                pos (0.5, 1.4) zoom 1.3
        
        #change name to show Akari after reveal
        $ aki = Character("Akari", color = "#871c1c")

        aki "Name's Akari. We have a common enemy. I will let you go, for now. Help me, and I will help you in turn."

        show aki determined with dissolve

        aki "But do not forget, you are still a monster. Try anything funny with me, and I will not hesitate to kill you."

        ###no matter what you do or delete, Akari dissapears early here?!?!?
        
        "Akari backs into the foliage, disappearing in the blink of an eye. You notice how tense you feel, and allow yourself a moment to recover. A chill breeze ruffles your clothes."
        
        # VSFX Akari (moves away and fades out)
        hide aki determined with dissolve

        "The tranquil moment doesn't last for long. You hear the approach of powerful footsteps, and you know you're in for it now."

        jump BotchedConverge1

label CallOut:
        # VSFX Akari (as if jumping slightly in place)
        show aki bow drawn:
                subpixel True 
                ypos 1.43 
                linear 0.15 ypos 1.45 
                linear 0.10 ypos 1.4 
                linear 0.05 ypos 1.43 
        with Pause(0.40)
        show aki bow drawn:
                ypos 1.43 
        
        "You desperately call out for Ashina and the hooded woman jumps slightly. She looks at you with a confused expression and lowers her bow."

        # Image Akari Bow Nocked
        show aki bow nocked with dissolve

        aki "Who are you yelling for? You should be the only one here."

        # VSFX Akari (move slightly back and forth horizontally, a small look around)
        show aki bow nocked:
                subpixel True 
                parallel:
                        xpos 0.5 
                        linear 0.30 xpos 0.34 
                        linear 0.10 xpos 0.34 
                        linear 0.17 xpos 0.34 
                        linear 0.30 xpos 0.34 
                        linear 0.20 xpos 0.66 
                        linear 0.10 xpos 0.66 
                        linear 0.15 xpos 0.66 
                        linear 0.10 xpos 0.66 
                parallel:
                        yrotate 0.0 
                        linear 0.30 yrotate 0.0 
                        linear 0.10 yrotate 0.0 
                        linear 0.17 yrotate -180.0 
                        linear 0.30 yrotate -180.0 
                        linear 0.20 yrotate -180.0 
                        linear 0.10 yrotate -180.0 
                        linear 0.15 yrotate 0.0 
                        linear 0.10 yrotate 0.0 
        with Pause(2.0)
        show aki bow nocked:
                xpos 0.66 yrotate 0.0 

        "The woman looks around, but there’s no sign of Ashina yet. The stranger’s dark gaze briefly returns to you."

        # Image Akari Thoughtful
        show aki thoughtful with dissolve

        aki "You do look… different than I expected. Name’s Akari. How about you tell me-"

        #change name to show Akari after reveal
        $ aki = Character("Akari")

        show aki thoughtful
        #Image Akari Bow Nocked
        show aki bow nocked
        #SFX Growl
        play soundb growl
        #VSFX Akari (moves away and fades out)
        hide aki bow nocked
        "There’s a sudden burst of movement and a fierce growling quickly approaching from behind you. Akari’s eyes go wide, and she quickly backs into the foliage, disappearing in the blink of an eye."

        #Image Wolf Ashina Snarling
        show wolf snarl with dissolve
        stop soundb fadeout 0.5
        #Image Wolf Ashina Docile
        show wolf neutral with dissolve

        "The same beastly wolf that attacked you in the alley lunges forward at the treeline, then stops short, giving up the chase."

        ## VSFX Ashina (fading in and out between images like a pokemon evolution until settling into the latter image)
        # Image Ashina Neutral
        window auto hide
        hide wolf neutral with dissolve
        with Pause(0.2)
        #show shifting ashina
        show ash neutral with dissolve
        hide ash neutral with dissolve
        with Pause(0.2)
        show wolf neutral with dissolve
        hide wolf neutral with dissolve
        with Pause(0.2)
        show ash neutral with dissolve
        hide ash neutral with dissolve
        with Pause(0.2)
        show wolf neutral with dissolve
        hide wolf neutral with dissolve
        with Pause(0.2)
        show ash neutral with dissolve
        window auto show

        "You watch as, before your eyes, the wolf begins to change. You hear the sharp cracking of bone and the mushy contorting of flesh. You want to look away, but you can’t. Soon enough, Ashina stands before you."


        jump BotchedConverge1

label BotchedConverge1:
        # Choices Converge Here

        # Image Ashina Neutral
        show ash neutral with dissolve

        ash "I seem to recall telling you to stay inside, did I not, pup?"

        # VSFX Ashina (closer)
        show ash neutral:
                subpixel True
                linear 0.2 ypos 1.43 zoom 1.36 
        with Pause(0.3)
        show ash neutral:
                ypos 1.43 zoom 1.36

        "You turn to face Ashina as she steps closer, looming over you. You reflexively swallow."

        you "You… did."

        # VSFX Ashina (moving to the right)
        show ash neutral:
                subpixel True 
                parallel:
                        xpos 0.5 
                        linear 0.30 xpos 0.66
                        linear 0.10 xpos 0.66
                        linear 0.17 xpos 0.66
                        linear 0.30 xpos 0.66
                        linear 0.20 xpos 0.34
                        linear 0.10 xpos 0.34
                        linear 0.15 xpos 0.34
                        linear 0.10 xpos 0.34
                parallel:
                        yrotate 0.0 
                        linear 0.30 yrotate 0.0 
                        linear 0.10 yrotate 0.0 
                        linear 0.17 yrotate 180.0
                        linear 0.30 yrotate 180.0 
                        linear 0.20 yrotate 180.0 
                        linear 0.10 yrotate 180.0 
                        linear 0.15 yrotate 0.0 
                        linear 0.10 yrotate 0.0

        ash "Did you really think I would let you just walk out of here? You silly, naive little thing. You must take me for a fool."

        # VSFX Ashina (shake)
        show ash neutral:
                subpixel True 
                xpos 0.34 
                linear 0.15 xpos 0.36 
                linear 0.20 xpos 0.32 
                linear 0.15 xpos 0.34 

        ash "This was a test, and you, my dear, have failed. I can see you are not yet ready for the privilege of independence."
        
        show ash neutral:
                xpos 0.34
        with Pause(0.5) 
        show ash angry hybrid with dissolve
        with Pause(0.5)
        # Image Ashina Hybrid Angry
        # VSFX Ashina (closer)
        show ash angry hybrid:
                subpixel True
                linear 0.2 pos (0.5,2.0) zoom 2.0
        
        ash "Tell me, do you take joy in disrespecting me? In betraying the first ounce of trust I place in you?"
        show ash angry hybrid:
                pos (0.5,2.0) zoom 2.0
        with Pause (0.5)
        show ash neutral with dissolve

        ash "I will not tolerate your behavior. Get back inside. Now."

        menu:
                #Akari Approval Choice
                "Resist Ashina":
                        $ aka_approval += 1
                        jump ResistAshina
                #Akari Disapproval Choice
                "Go willingly.":
                        $ aka_approval -= 1
                        jump GoWillingly  
                                                     
label ResistAshina:
        you "This isn’t about you! I wasn't doing anything wrong!"

        show ash neutral:
                subpixel True
                linear 0.2 pos (0.5,1.55) zoom 1.66

        you "You think you can just turn me into some monster, ruin my life and act like I'm supposed to be grateful towards you? No! I've had enough!"

        show ash neutral:
                pos (0.5,1.55) zoom 1.66
        with Pause(0.1)
        #VSFX Ashina (fade out)
        hide ash neutral with dissolve

        "You turn away from Ashina and intend to put some space between you."

        #Image Cabin Exterior POV Approaching
        show bg forest edge with dissolve:
                subpixel True xzoom 1.0 yzoom 7.82
        #SFX Walking
        play sound walk loop

        ash "You will not walk away from me!"

        stop sound
        #VSFX Zoom (as if being dragged to the door)

        "Ashina grabs your wrist and drags you struggling across the yard. As she does so, you notice a pair of dark eyes watching from the treeline."

        window auto hide
        #Image Cabin Door Open
        show bg door open with dissolve:
                subpixel True xzoom 1.0 yzoom 1.0
        with Pause(1.0)

        #Image Hearth
        show bg hearth with dissolve:
                subpixel True xoffset 127.0 xzoom 1.0 zoom 0.72 

        #Image Ashina Hybrid Angry
        show ash angry hybrid with dissolve

        #Fireplace
        stop music fadeout 2.0
        stop crickets fadeout 2.0
        play soundb fireplace volume 0.3 loop fadein 2.0
        window auto show

        "Ashina tosses you into the cabin, slams the front door shut, and snarls at you."

        ash "I've given you a chance at a new life! And this is the thanks I get?!"

        jump BotchedConverge2

label GoWillingly:
        pause 0.5
        hide ash neutral with dissolve
        show bg forest edge with dissolve:
                subpixel True xzoom 1.0 yzoom 7.82
        
        "You avert your eyes from Ashina’s intense gaze, and walk back to the cabin. You hear Ashina’s footsteps behind you."

        window auto hide
        play sound walk loop
        with Pause(1.0)
        show bg door open with dissolve:
                subpixel True xzoom 1.0 yzoom 1.0
        with Pause(1.0)
        show bg hearth with dissolve:
                subpixel True xoffset 127.0 xzoom 1.0 zoom 0.72 

        #Fireplace
        stop sound
        stop music fadeout 2.0
        stop crickets fadeout 2.0
        play soundb fireplace volume 0.3 loop fadein 2.0
        window auto show

        show ash angry hybrid with dissolve

        "Once inside, she approaches you with a fierce expression."

        # Image Ashina Concerned
        show ash concerned with dissolve

        # VSFX as if  falling backwards onto the ground and looking up at Ashina

        "You stumble as your foot catches the edge of the walkway, causing you to topple over. Ashina regards you hesitantly."

        ash "I told you to stay inside. Why couldn’t you just listen to me?"

        #for testing
        #define ash_approval = 3

        jump BotchedConverge2

label BotchedConverge2:
        #Choices Converge Here

        if ash_approval >= 3:

                # Image Ashina Thoughtful
                show ash thoughtful with dissolve
                with Pause(0.5)
                # VSFX Ashina (as if pacing in frustration)
                show ash thoughtful:
                        subpixel True 
                        parallel:
                                xpos 0.5 
                                linear 0.30 xpos 0.66
                                linear 0.10 xpos 0.66
                                linear 0.17 xpos 0.66
                                linear 0.30 xpos 0.66
                                linear 0.20 xpos 0.34
                                linear 0.10 xpos 0.34
                                linear 0.15 xpos 0.34
                                linear 0.10 xpos 0.34
                        parallel:
                                yrotate 0.0 
                                linear 0.30 yrotate 0.0 
                                linear 0.10 yrotate 0.0 
                                linear 0.17 yrotate 180.0
                                linear 0.30 yrotate 180.0 
                                linear 0.20 yrotate 180.0 
                                linear 0.10 yrotate 180.0 
                                linear 0.15 yrotate 0.0 
                                linear 0.10 yrotate 0.0

                "Ashina starts pacing as you look up at her from the ground, stunned. After a few moments, she stops and looks down at you with a softer expression."
                
                show ash thoughtful:
                        xpos 0.34
                with Pause(0.5)
                # Image Ashina Caring
                show ash caring with dissolve

                ash "Forgive me. You have been… mostly cooperative, I must admit, and you do not deserve my harshness. I understand that you would feel defensive, with how I approached you."

                #VSFX Ashina (closer)

                "She offers you a hand, and you hesitantly take it. She helps you up. You feel like a feather in her strong grasp, lifted with ease."

                #VSFX Ashina (further)
                #VSFX Zoom (as if being helped back onto your feet)

                ash "Perhaps you were feeling cooped up, and wanted to explore. I can’t blame you for that. However, you must restrain yourself."

                #VSFX Ashina (further)

                "Her grip on your hand lingers a moment longer, squeezing before pulling away."

                #VSFX Ashina Neutral
                show ash neutral with dissolve

                ash "Trust takes time. You will be allowed to roam soon enough, I promise. Now… Please, return to your room."

                #VSFX Ashina (fade out)
                hide ash neutral with dissolve
                #VSFX Zoom (as if walking through the hearth)
                #SFX Walking
                play sound walk
                show bg upstairs with dissolve:
                        pos(0,0) zoom 1.0

                "You feel her gaze on your back as you cross the hearth and head upstairs."

                # Image Captive Cabin Room (angled, zoomed in on ceiling)
                show bg room ceiling with dissolve:
                        pos(0,0) zoom 1.0

                # VSFX Blur

                stop sound

                "When you find yourself lying in bed, you’re cradling your hand over your chest. You can still feel the warmth from when Ashina held it."

                # VSFX Black
                show bg color black with dissolve:
                        pos(0,0) zoom 1.0
                pause 1.0

                jump SpeakNoEvilSceneP1

        elif ash_approval >= -2:

                #Image Ashina Hybrid Angry
                show ash angry hybrid with dissolve
                #VSFX Ashina (closer)

                "Ashina raises a hand as if she might hit you, and you reflexively flinch. She stops, a clear hesitation in her eyes."

                # Image Ashina Concerned
                show ash concerned with dissolve

                ash "...Go to your room."

                #VSFX Ashina (fade out)
                hide ash concerned with dissolve

                "She looks away. You figure you shouldn’t give her time to rethink that decision, and hurry up the stairs."

                window auto hide
                #VSFX Zoom (as if walking through the hearth)
                #SFX Walking
                play sound walk loop
                show bg upstairs with dissolve:
                        pos(0,0) zoom 1.0
                with Pause(1.0)
                # Image Captive Cabin Room (angled, zoomed in on ceiling)
                show bg room ceiling with dissolve:
                        pos(0,0) zoom 1.0
                # VSFX Blur

                stop sound
                window auto show

                "When you find yourself lying in bed, you struggle to drift off, haunted by memories and the look of concern on your captor’s face."

                # VSFX Black
                show bg color black with dissolve:
                        pos(0,0) zoom 1.0
                pause 1.0

                jump SpeakNoEvilSceneP1

        else:
                #TBA, Unfinished

                # Image Ashina Hybrid Angry
                #VSFX Ashina (pacing)
                show ash angry hybrid with dissolve

                ash "You reckless, ungrateful fool. Clearly you do not understand your situation, despite me going to great lengths to explain it."

                #VSFX Ashina (fade out)
                #VSFX Zoom (as if being dragged across the room)

                "She grabs the back of your shirt, dragging you towards the staircase."

                ash "It seems I am going to need to teach you a hard lesson, girl. Perhaps then you will realize the wisdom in my words."

                # VSFX Red (at the edges of the screen)

                "You claw at her leg, her wrist, but she ignores it, dragging you painfully up the stairs. You manage to tug your shirt out of her grip, but she grabs and painfully twists your arm."

                "She forces you across the hall, and then throws you into your room. The door slams as you scramble towards it, your monstrous hands clawing at the wood. There’s a distinct sound of the door being locked."

                "You turn and make for the window, but when you’re within steps of it, the dogs outside erupt into growls and barks. Even if you climbed out, they would rip you to shreds."

                "You collapse onto the ground and sob."

                #TBA, Unfinished

                #jump FriendorFoodScene

