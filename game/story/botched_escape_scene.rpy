label BotchedEscapeScene:
        #stop audio from previous scene
        #stop sound
        ###I don't think we should rely on this, also need the fireplace from prev scene
        ###Once you settle on a solution you are satisfied with, I can at least 
        #incorporate the part that hides the quick menu in the transforms if needed
        $ quick_menu = False
        window auto hide

        #Image Cabin Hearth
        scene bg hearth

        window auto show
        $ quick_menu = True

        "You're left with your own thoughts as Ashina departs upstairs. You begin to wander the cabin aimlessly."

        # SFX Crickets
        play crickets crickets fadein 0.5 loop
        # Image Cabin Door Open
        show bg door open with dissolve
        #SFX Fireplace (fade out)
        stop soundb fadeout 2.0

        "You realize the front door is open."

        $ quick_menu = False
        window auto hide

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
        play music eerie_outdoors_music volume 1.5

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
        window auto show
        $ quick_menu = True

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

        aki "I will have no mercy on you. Your death shall be painful, I will make sure of it. You will suffer for every life you have stolen, and I will have my revenge. You chose the wrong night to leave your little fortress, and now, you will finally pay."

        "You can't just let it end here. Not now."

        $ quick_menu = False
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
        window auto show
        $ quick_menu = True

        you "No, wait, please! I never asked to be a monster!"

        $ quick_menu = False
        window auto hide
        # VSFX Akari nod
        show aki bow drawn with dissolve
        with Pause(1.0)
        show aki bow drawn at jump_in_place
        with Pause(0.40)
        show aki bow drawn:
                ypos 1.43 
        window auto show
        $ quick_menu = True

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

        $ quick_menu = False
        window auto hide
        show aki bow nocked side at stop_shortpacing
        with Pause(1.0)
        show aki bow nocked with dissolve
        window auto show
        $ quick_menu = True

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
        $ quick_menu = False
        window auto hide
        show aki thoughtful at shortpacing
        with Pause(4.0)
        show aki thoughtful at stop_shortpacing
        window auto show
        $ quick_menu = True
        
        aki "Everything about this spells out a trap. I need to get out of here."

        show aki thoughtful look with dissolve

        "She turns her dark gaze back to you."
        
        #change name to show Akari after reveal
        $ aki.name = "Akari"

        aki "Name's Akari. We have a common enemy. I will let you go, for now. Help me, and I will help you in turn."

        show aki determined with dissolve

        aki "But do not forget, you are still a monster. Try anything funny with me, and I will not hesitate to kill you."

        # VSFX Akari (moves away and fades out)
        hide aki determined with dissolve
        
        "Akari backs into the foliage, disappearing in the blink of an eye. You notice how tense you feel, and allow yourself a moment to recover. A chill breeze ruffles your clothes."

        "The tranquil moment doesn't last for long. You hear the approach of powerful footsteps, and you know you're in for it now."

        jump BotchedConverge1

label CallOut:
        # VSFX Akari (as if jumping slightly in place)
        show aki bow drawn at jump_in_place
        with Pause(0.40)
        
        window auto show
        $ quick_menu = True

        "You desperately call out for Ashina and the hooded woman jumps slightly. She looks at you with a confused expression and lowers her bow."

        # Image Akari Bow Nocked
        show aki bow nocked side with dissolve

        aki "Who are you yelling for? You should be the only one here."

        # VSFX Akari (move slightly back and forth horizontally, a small look around)
        show aki bow nocked side at shortpacing

        "The woman looks around, but there’s no sign of Ashina yet. The stranger’s dark gaze briefly returns to you."
        
        $ quick_menu = False
        window auto hide
        show aki bow nocked side at stop_shortpacing
        with Pause(1.0)
        # Image Akari Thoughtful
        show aki thoughtful look with dissolve

        #change name to show Akari after reveal
        $ aki.name = "Akari"
        window auto show
        $ quick_menu = True

        aki "You do look… different than I expected. Name’s Akari. How about you tell me-"

        $ quick_menu = False
        window auto hide
        #Image Akari Bow Nocked
        show aki bow nocked with dissolve
        #SFX Growl
        play soundb growl noloop
        with Pause(1.0)
        #VSFX Akari (moves away and fades out)
        hide aki bow nocked with dissolve
        window auto show
        $ quick_menu = True

        "There’s a sudden burst of movement and a fierce growling quickly approaching from behind you. Akari’s eyes go wide, and she quickly backs into the foliage, disappearing in the blink of an eye."

        #Image Wolf Ashina Snarling
        show wolf snarl with dissolve
        stop soundb fadeout 0.5
        #Image Wolf Ashina Docile
        show wolf neutral with dissolve

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

        # VSFX Ashina (moving to the right)
        show ash annoyed at annoyed_pace
        with Pause(1.0)

        ash "Did you really think I would let you just walk out of here? You silly, naive little thing. You must take me for a fool."

        # VSFX Ashina (shake)
        show ash annoyed at normal_shake:
                subpixel True 
                xpos 0.34 
                linear 0.15 xpos 0.36 
                linear 0.20 xpos 0.32 
                linear 0.15 xpos 0.34 

        ash "This was a test, and you, my dear, have failed. I can see you are not yet ready for the privilege of independence."
        
        $ quick_menu = False
        window auto hide
        show ash annoyed:
                xpos 0.34
        with Pause(0.5) 
        show ash angry hybrid with dissolve
        with Pause(0.5)
        # Image Ashina Hybrid Angry
        # VSFX Ashina (closer)
        show ash angry hybrid at step_close_center_fast
        window auto show
        $ quick_menu = True

        ash "Tell me, do you take joy in disrespecting me? In betraying the first ounce of trust I place in you?"
        pause (0.5)
        show ash annoyed with dissolve

        ash "I will not tolerate your behavior. Get back inside. Now."

        $ quick_menu = False
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
        window auto show
        $ quick_menu = True
        
        you "This isn’t about you! I wasn't doing anything wrong!"

        show ash annoyed at step_away_half

        you "You think you can just turn me into some monster, ruin my life and act like I'm supposed to be grateful towards you? No! I've had enough!"

        pause(0.1)
        #VSFX Ashina (fade out)
        hide ash annoyed with dissolve

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

        $ quick_menu = False
        window auto hide
        #Image Cabin Door Open
        show bg door open with dissolve:
                subpixel True xzoom 1.0 yzoom 1.0
        with Pause(1.0)

        #Image Hearth
        show bg hearth with dissolve:
                subpixel True xpos 0.52 zoom 0.7

        #Image Ashina Hybrid Angry
        show ash angry hybrid with dissolve

        #Fireplace
        stop music fadeout 2.0
        stop crickets fadeout 2.0
        play soundb fireplace volume 0.3 loop fadein 2.0
        window auto show
        $ quick_menu = True

        "Ashina tosses you into the cabin, slams the front door shut, and snarls at you."

        ash "I've given you a chance at a new life! And this is the thanks I get?!"

        jump BotchedConverge2

label GoWillingly:
        pause 0.5
        hide ash annoyed with dissolve
        show bg forest edge with dissolve:
                subpixel True xzoom 1.0 yzoom 7.82
        
        window auto show
        $ quick_menu = True

        "You avert your eyes from Ashina’s intense gaze, and walk back to the cabin. You hear Ashina’s footsteps behind you."

        $ quick_menu = False
        window auto hide
        play sound walk loop
        with Pause(1.0)
        show bg door open with dissolve:
                subpixel True xzoom 1.0 yzoom 1.0
        with Pause(1.0)
        show bg hearth with dissolve:
                subpixel True xpos 0.52 zoom 0.72 

        #Fireplace
        stop sound
        stop music fadeout 2.0
        stop crickets fadeout 2.0
        play soundb fireplace volume 0.3 loop fadein 2.0

        show ash angry hybrid with dissolve
        with Pause(0.5)
        show ash angry hybrid:
                subpixel True
                linear 0.2 ypos 1.43 zoom 1.36 
        with Pause(0.3)
        show ash angry hybrid:
                ypos 1.43 zoom 1.36

        window auto show
        $ quick_menu = True
        "Once inside, she approaches you with a fierce expression."

        # VSFX as if  falling backwards onto the ground and looking up at Ashina
        $ quick_menu = False
        window auto hide
        play sound run
        camera:
                subpixel True 
                ypos 0 
                ease_elastic 0.30 ypos 90 
        with Pause(0.40)
        camera:
                ypos 90
        with Pause(0.2) 
        stop sound
        show ash concerned with dissolve
        window auto show
        $ quick_menu = True     
        # Image Ashina Concerned
        show ash concerned with dissolve

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
                $ quick_menu = False
                # VSFX Ashina (as if pacing in frustration)
                show ash annoyed at shortpacingreverse
                $ quick_menu = True

                "Ashina starts pacing as you look up at her from the ground, stunned. After a few moments, she stops and looks down at you with a softer expression."

                show ash annoyed at stop_pacing
                $ quick_menu = False
                window auto hide
                show ash annoyed:
                        pos (0.34, 1.43) yrotate 0.0
                with Pause(0.5)
                # Image Ashina sad
                show ash sad with dissolve:
                        pos (0.34, 1.43)
                window auto show
                $ quick_menu = True

                ash "Forgive me. You have been… mostly cooperative, I must admit, and you do not deserve my harshness. I understand that you would feel defensive, with how I approached you."

                #VSFX Ashina (closer)
                $ quick_menu = False
                window auto hide
                show ash sad:
                        subpixel True 
                        pos (0.34, 1.43) zoom 1.36 
                        linear 0.50 pos (0.5, 2.0) zoom 2.0 
                with Pause(0.60)
                show ash sad:
                        pos (0.5, 2.0) zoom 2.0 
                window auto show
                $ quick_menu = True

                "She offers you a hand, and you hesitantly take it. She helps you up. You feel like a feather in her strong grasp, lifted with ease."

                #VSFX Zoom (as if being helped back onto your feet)
                play sound fast_walk
                $ quick_menu = False
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
                $ quick_menu = True
                stop sound
                show ash caring with dissolve

                ash "Perhaps you were feeling cooped up, and wanted to explore. I can’t blame you for that. However, you must restrain yourself."

                #VSFX Ashina (further)
                $ quick_menu = False
                window auto hide
                show ash caring:
                        subpixel True 
                        pos (0.5, 2.0) zoom 2.0 
                        linear 0.20 pos (0.5, 1.3) zoom 1.33 
                with Pause(0.30)
                show ash caring:
                        pos (0.5, 1.3) zoom 1.33 
                window auto show
                $ quick_menu = True

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
                        subpixel True xpos 0.5 zoom 1.0

                "You feel her gaze on your back as you cross the hearth and head upstairs."

                show bg upstairs with dissolve:
                        subpixel True
                        zoom 1.0 xalign(0.5) yalign(0.01)
                        linear 2.00 zoom 2.0 xalign(0.5) yalign(0.01)
                with Pause(1.5)
                show bg upstairs:
                        zoom 2.0 xalign(0.5) yalign(0.01)

                # Image Captive Cabin Room (angled, zoomed in on ceiling)
                show bg room ceiling with dissolve:
                        subpixel True xpos 0.5 zoom 1.0 

                # VSFX Blur

                stop sound

                "When you find yourself lying in bed, you’re cradling your hand over your chest. You can still feel the warmth from when Ashina held it."
                $ quick_menu = False
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

                $ quick_menu = False
                window auto hide
                #VSFX Zoom (as if walking through the hearth)
                #SFX Walking
                play sound walk loop

                show bg upstairs with dissolve:
                        subpixel True
                        zoom 1.0 xalign(0.5) yalign(0.01)
                        linear 2.00 zoom 2.0 xalign(0.5) yalign(0.01)
                with Pause(1.5)
                show bg upstairs:
                        zoom 2.0 xalign(0.5) yalign(0.01)
                # Image Captive Cabin Room (angled, zoomed in on ceiling)
                show bg room ceiling with dissolve:
                        subpixel True xpos 0.5 zoom 1.0 
                # VSFX Blur

                stop sound
                
                camera:
                        subpixel True pos (0, 0) 


                window auto show
                $ quick_menu = True

                "When you find yourself lying in bed, you struggle to drift off, haunted by memories and the look of concern on your captor’s face."
                $ quick_menu = False
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

