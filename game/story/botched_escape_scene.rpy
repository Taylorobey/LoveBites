label BotchedEscapeScene:
        $ save_name = "The Great Outdoors"
        window auto hide

        #Image Cabin Hearth
        camera:
                subpixel True
                linear 10.00 xpos 3000

        window auto show
        play sound walk loop

        "You're left with your own thoughts as Ashina departs upstairs. You begin to wander the cabin aimlessly."

        stop sound
        # SFX Crickets
        play crickets crickets fadein 0.5 loop
        # Image Cabin Door Open
        #hide flame
        show bg door open:
                pos (0.5,0.0)
        camera:
                xpos 0
        with dissolve
        #SFX Fireplace (fade out)
        stop soundb fadeout 2.0

        "You realize the front door is open."

        window auto hide

        menu:
                # Narrative Choice
                "Try to escape.":
                        pause 0.3
                        "Ashina should be asleep by now. This is your chance to escape and bring back help for Cameron."

                #Narrative Choice
                "Get some fresh air.":
                        pause 0.3
                        "It would be nice to get some fresh air. You've been stuck inside for a couple days now, and you can’t help feeling a bit claustrophobic."

        #choices converge here

        "You lean out of the open door as quietly as possible to find…"

        # Image Cabin Exterior Leaving POV No Dogs
        scene bg cabin ext no dogs with dissolve

        # Music Eerie Outdoors
        play music eerie_outdoors_music volume 1.5

        you "…Nothing?"

        window auto hide
        # SFX Walking
        play sound walk loop
        # VSFX Cabin Ext.(zoom, as if walking)
        show bg cabin ext no dogs:
                subpixel True 
                ypos 1.0 zoom 1.0 
                linear 1.50 ypos 1.8 zoom 2.0 
        with Pause(1.50)
        show bg cabin ext no dogs:
                ypos 1.8 zoom 2.0 
        pause 0.1
        stop sound
        window auto show

        "You take a few cautious steps outside, thinking your eyes must be playing tricks on you. Where did all the dogs go? Was this another lucky break, like when Cameron snuck in?"

        play sound walk loop
        # SFX Walking
        show bg cabin ext no dogs:
                ypos 1.8 zoom 2.0
                linear 4.0 ypos 2.5 zoom 3.0

        "You continue on, making it to the edge of the forest. You can hear your heart pounding in your chest. Were you really able to just… walk out of here?"


        # SFX Walking (stop)
        stop sound
        # Image Forest Edge
        show bg forest edge with dissolve:
                subpixel True zoom 1.05 ypos 1.0
        window auto show


        # Image Akari Bow Drawn (close)
        show aki bow drawn angry with dissolve

        "As you move into the foliage, you're stopped dead in your tracks. A silver arrow is aimed square between your eyes. The wielder of the bow is a sharp-eyed, hooded figure with hair black as night."

        ## VSFX Akari (zoom to fullbody)

        aki "Don't you dare move, monster!"

        "You put your hands up in the most placating gesture you can manage."

        you "Monster…? Uh, I think this is a misunderstanding, maybe we could just-"

        # VSFX Akari (closer)
        show aki bow drawn angry at threat_step
        with Pause(0.3)

        aki "Stop. You will not fool me. I know you."

        # VSFX Akari (closer)
        show aki bow drawn angry at threat_step_2
        with Pause(0.3)

        aki "I will have no mercy on you."

        show aki bow drawn angry:
                linear 0.25 ypos 1.75 zoom 1.75
        
        aki "Your death shall be painful, I will make sure of it."

        show aki bow drawn angry:
                linear 0.25 ypos 2.05 zoom 2.1
        
        aki "You will suffer for every life you have stolen, and I will have my revenge. You chose the wrong night to leave your little fortress, and now, you will finally pay."

        "You can't just let it end here. Not now."


        window auto hide

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
        pause 0.3
        window auto show


        you "No, wait, please! I never asked to be a monster!"


        window auto hide
        # VSFX Akari nod
        show aki bow drawn with dissolve
        with Pause(1.0)
        show aki bow drawn:
                subpixel True
                linear 0.3 ypos 1.45
                linear 0.25 ypos 1.4 
                linear 0.2 ypos 1.43 
        with Pause(0.80)
        show aki bow drawn:
                ypos 1.43 
        window auto show


        "The hooded woman looks surprised at your outburst. Her stance doesn't waver, but she nods slowly at you to continue."

        you "Where do I begin…? I was out late. A bunch of dogs, hundreds of them, cornered me into an alley. Then, a huge wolf-beast attacked me, dragged me here, and turned me into…"

        # VSFX Akari (further)
        show aki bow drawn at step_away_fast
        with Pause(0.3)

        aki "The smaller dogs you mentioned. Where are they now?"

        # Image Akari Bow Nocked
        show aki bow nocked side with dissolve
        # The spelling on that is a pet peeve of mine
        # VSFX Akari (move horizontally across the screen, as if looking around)

        "The woman lowers her bow, looking around suspiciously."
        show aki bow nocked side at shortpacing

        you "I don’t know, they were gone when I stepped outside. They must have run off somewhere, maybe-"


        window auto hide
        show aki bow nocked side at stop_shortpacing
        with Pause(1.0)
        show aki bow nocked with dissolve
        window auto show


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
        show aki thoughtful at shortpacing
        with Pause(4.0)
        show aki thoughtful at stop_shortpacing
        window auto show

        
        aki "Everything about this spells out a trap. I need to get out of here."

        show aki thoughtful look with dissolve

        "She turns her dark gaze back to you."
        
        #change name to show Akari after reveal
        $ aki_name = "Akari"

        aki "Name's Akari. We have a common enemy. I will let you go, for now. Help me, and I will help you in turn."

        show aki determined with dissolve

        aki "But do not forget, you are still a monster. Try anything funny with me, and I will not hesitate to kill you."

        # VSFX Akari (moves away and fades out)
        hide aki determined with dissolve
        
        "Akari backs into the foliage, disappearing in the blink of an eye. You notice how tense you feel, and allow yourself a moment to recover. A chill breeze ruffles your clothes."

        "The tranquil moment doesn't last for long. You hear the approach of powerful footsteps, and you know you're in for it now."

        jump BotchedConverge1

label CallOut:
        pause 0.3
        # VSFX Akari (as if jumping slightly in place)
        show aki bow drawn at jump_in_place
        with Pause(0.40)
        
        window auto show


        "You desperately call out for Ashina and the hooded woman jumps slightly. She looks at you with a confused expression and lowers her bow."

        # Image Akari Bow Nocked
        show aki bow nocked side with dissolve

        aki "Who are you yelling for? You should be the only one here."

        window auto hide
        # VSFX Akari (move slightly back and forth horizontally, a small look around)
        show aki bow nocked side at shortpacing
        pause 3.0
        show aki bow nocked side at stop_shortpacing
        window auto show

        "The woman looks around, but there’s no sign of Ashina yet. The stranger’s dark gaze briefly returns to you."
        
        # Image Akari Thoughtful
        show aki thoughtful look with dissolve

        #change name to show Akari after reveal
        $ aki_name = "Akari"


        aki "You do look… different than I expected. Name’s Akari. How about you tell me-"


        window auto hide
        #Image Akari Bow Nocked
        show aki bow nocked with dissolve
        #SFX Growl
        play soundb growl noloop
        with Pause(1.0)
        #VSFX Akari (moves away and fades out)
        hide aki bow nocked with dissolve
        window auto show


        "There’s a sudden burst of movement and a fierce growling quickly approaching from behind you. Akari’s eyes go wide, and she quickly backs into the foliage, disappearing in the blink of an eye."

        window auto hide
        #Image Wolf Ashina Snarling
        show wolf snarl with dissolve
        stop soundb fadeout 0.5
        #Image Wolf Ashina Docile
        show wolf neutral with dissolve
        window auto show

        "The same beastly wolf that attacked you in the alley lunges forward at the treeline, then stops short, giving up the chase."

        ## VSFX Ashina (fading in and out between images like a pokemon evolution until settling into the latter image)
        #made this a sequence as she will presumably have multiple times she can shift
        call AshinaShiftFromWolf

        "You watch as, before your eyes, the wolf begins to change. You hear the sharp cracking of bone and the mushy contorting of flesh. You want to look away, but you can’t. Soon enough, Ashina stands before you."

        jump BotchedConverge1

label BotchedConverge1:
        # Choices Converge Here


        show ash annoyed with dissolve

        ash "I seem to recall telling you to stay inside, did I not, pup?"

        # VSFX Ashina (closer)
        show ash annoyed at step_close_short
        with Pause(0.3)

        "You turn to face Ashina as she steps closer, looming over you. You reflexively swallow."

        you "You… did."

        window auto hide
        # VSFX Ashina (moving to the right)
        show ash annoyed at shortpacingreverse
        with Pause(2.0)
        show ash annoyed:
                linear 0.2 xpos 0.34
        window auto show

        ash "Did you really think I would let you just walk out of here? You silly, naive little thing. You must take me for a fool."

        # VSFX Ashina (shake)
        show ash annoyed at normal_shake

        ash "This was a test, and you, my dear, have failed. I can see you are not yet ready for the privilege of independence."
        

        call AshinaScaryFastShift
        pause(0.5)
        # Image Ashina Hybrid Angry
        # VSFX Ashina (closer)
        show ash angry hybrid at step_close_center_fast


        ash "Tell me, do you take joy in disrespecting me? In betraying the first ounce of trust I place in you?"
        pause (0.5)
        show ash annoyed with dissolve

        ash "I will not tolerate your behavior. Get back inside. Now."


        window auto hide

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
        pause 0.3
        window auto show

        
        you "This isn’t about you! I wasn't doing anything wrong!"

        show ash annoyed at step_away_half

        you "You think you can just turn me into some monster, ruin my life and act like I'm supposed to be grateful towards you? No! I've had enough!"

        window auto hide
        pause(0.1)
        #VSFX Ashina (fade out)
        hide ash annoyed with dissolve
        pause(0.2)
        #Image Cabin Exterior POV Approaching
        show bg cabin ext no dogs with dissolve:
                subpixel True ypos 2.5 zoom 3.0
        #SFX Walking
        play sound walk loop
        window auto show

        "You turn away from Ashina and intend to put some space between you."

        ash "You will not walk away from me!"

        stop sound
        #VSFX Zoom (as if being dragged to the door)

        "Ashina grabs your wrist and drags you struggling across the yard. As she does so, you notice a pair of dark eyes watching from the treeline."


        window auto hide
        #Image Cabin Door Open
        show bg door open with dissolve:
                subpixel True pos (0.5,1.0) zoom 1.0
        with Pause(1.0)
        #Image Hearth
        show bg hearth with dissolve:
                subpixel True xpos 0.52 ypos 1.1 zoom 0.72

        #Image Ashina Hybrid Angry
        show ash angry hybrid with dissolve

        #Fireplace
        stop music fadeout 2.0
        stop crickets fadeout 2.0
        play soundb fireplace volume 0.3 loop fadein 2.0

        play sound run
        camera:
                subpixel True 
                ypos -0.1
                ease_elastic 0.30 ypos 90 
        with Pause(0.40)
        camera:
                ypos 90
        with Pause(0.2) 
        stop sound
        window auto show

        "Ashina tosses you into the cabin, slams the front door shut, and snarls at you."

        ash "I've given you a chance at a new life! And this is the thanks I get?!"

        jump BotchedConverge2

label GoWillingly:
        pause 0.6
        hide ash annoyed with dissolve
        show bg cabin ext no dogs with dissolve:
                subpixel True ypos 2.5 zoom 3.0
        
        window auto show

        "You avert your eyes from Ashina’s intense gaze, and walk back to the cabin. You hear Ashina’s footsteps behind you."

        window auto hide
        play sound walk loop
        with Pause(1.0)
        show bg door open with dissolve:
                subpixel True pos (0.5,1.0) zoom 1.0
        with Pause(1.0)
        show bg hearth with dissolve:
                subpixel True xpos 0.52 ypos 1.1 zoom 0.72

        #Fireplace
        stop sound
        stop music fadeout 2.0
        stop crickets fadeout 2.0
        play soundb fireplace volume 0.3 loop fadein 2.0

        show ash angry hybrid with dissolve
        with Pause(0.5)
        show ash angry hybrid at step_close_short
        with Pause(0.3)

        window auto show

        "Once inside, she approaches you with a fierce expression."

        # VSFX as if  falling backwards onto the ground and looking up at Ashina

        window auto hide
        play sound run
        camera:
                subpixel True 
                ypos -0.1
                ease_elastic 0.30 ypos 90 
        with Pause(0.40)
        camera:
                ypos 90
        with Pause(0.2) 
        stop sound
        show ash concerned with dissolve
        window auto show

        "You stumble as your foot catches the edge of the walkway, causing you to topple over. Ashina regards you hesitantly."

        ash "I told you to stay inside. Why couldn’t you just listen to me?"

        #for testing
        #define ash_approval = 3

        jump BotchedConverge2

label BotchedConverge2:
        #Choices Converge Here

        if ash_approval >= 3:
                
                # Image Ashina Thoughtful
                show ash annoyed with dissolve
                with Pause(0.5)

                # VSFX Ashina (as if pacing in frustration)
                show ash annoyed at shortpacingreverse

                "Ashina starts pacing as you look up at her from the ground, stunned. After a few moments, she stops and looks down at you with a softer expression."

                window auto hide
                show ash annoyed:
                        linear 0.5 xpos 0.34
                with Pause(0.5)
                # Image Ashina sad
                show ash sad with dissolve:
                        xpos 0.34
                window auto show

                ash "Forgive me. You have been… mostly cooperative, I must admit, and you do not deserve my harshness. I understand that you would feel defensive, with how I approached you."

                #VSFX Ashina (closer)
                show ash sad at step_close_center_fast
                with Pause(0.60)

                "She offers you a hand, and you hesitantly take it. She helps you up. You feel like a feather in her strong grasp, lifted with ease."

                #VSFX Zoom (as if being helped back onto your feet)
                play sound fast_walk

                window auto hide
                #VSFX Zoom/Movement (as if standing)
                camera:
                        subpixel True 
                        ypos 90 
                        ease_elastic 0.50 ypos 0 
                with Pause(0.60)
                camera:
                        ypos 0
                window auto show

                stop sound
                show ash caring with dissolve

                ash "Perhaps you were feeling cooped up, and wanted to explore. I can’t blame you for that. However, you must restrain yourself."

                #VSFX Ashina (further)

                show ash caring at threat_step_2
                with Pause(0.30)

                "Her grip on your hand lingers a moment longer, squeezing before pulling away."

                #VSFX Ashina Neutral
                show ash neutral with dissolve

                ash "Trust takes time. You will be allowed to roam soon enough, I promise. Now… Please, return to your room."

                #VSFX Ashina (fade out)
                hide ash neutral with dissolve
                #VSFX Zoom (as if walking through the hearth)
                #SFX Walking
                play sound walk loop
                show bg upstairs with dissolve:
                        subpixel True zoom 1.0 xalign(0.5) yalign(0.01)
                stop sound

                "You feel her gaze on your back as you cross the hearth and head upstairs."

                window auto hide
                play sound walk loop
                stop soundb fadeout 1.0
                show bg upstairs:
                        subpixel True
                        zoom 1.0 xalign(0.5) yalign(0.01)
                        linear 2.00 zoom 2.0 xalign(0.5) yalign(0.01)
                with Pause(2.0)
                show bg upstairs:
                        zoom 2.0 xalign(0.5) yalign(0.01)
                
                camera:
                        ypos 0
                stop sound

                # Image Captive Cabin Room (angled, zoomed in on ceiling)
                show bg room ceiling with dissolve:
                        subpixel True xpos 0.5 zoom 1.0 

                # VSFX Blur

                window auto show

                "When you find yourself lying in bed, you’re cradling your hand over your chest. You can still feel the warmth from when Ashina held it."

                window auto hide

                # VSFX Black
                show bg color black with dissolve
                
                pause 1.0

                jump SpeakNoEvilSceneP1

        elif ash_approval >= -2:

                #Image Ashina 
                show ash thoughtful with dissolve
                #VSFX Ashina (closer)

                "Ashina raises a hand as if she might hit you, and you reflexively flinch. She stops, a clear hesitation in her eyes."

                # Image Ashina Concerned
                show ash concerned with dissolve

                ash "...Go to your room."

                #VSFX Ashina (fade out)
                hide ash concerned with dissolve

                "She looks away. You figure you shouldn’t give her time to rethink that decision, and hurry up the stairs."

                stop soundb fadeout 1.0
                call GoUpstairs
                
                camera:
                        ypos 0
                
                stop sound

                # Image Captive Cabin Room (angled, zoomed in on ceiling)
                show bg room ceiling with dissolve:
                        subpixel True xpos 0.5 zoom 1.0
                
                window auto show

                "When you find yourself lying in bed, you struggle to drift off, haunted by memories and the look of concern on your captor’s face."

                window auto hide
                
                # VSFX Black
                show bg color black with dissolve
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

