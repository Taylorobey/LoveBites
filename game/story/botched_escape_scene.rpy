label BotchedEscapeScene:
        #Image Cabin Hearth
        #SFX Fireplace

        "You're left with your own thoughts as Ashina departs upstairs. You begin to wander the cabin aimlessly."

        # Image Cabin Door Open
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
        # Music Eerie Outdoors

        you "…Nothing?"

        # SFX Walking
        # VSFX Cabin Ext.(zoom, as if walking)

        "You take a few cautious steps outside, thinking your eyes must be playing tricks on you. Where did all the dogs go? Was this another lucky break, like when Cameron snuck in?"

        # SFX Walking
        # Image Forest Edge

        "You continue on, making it to the edge of the forest. You can hear your heart pounding in your chest. Were you really able to just… walk out of here?"

        # SFX Walking (stop)
        # Image Akari Bow Drawn (close)

        "As you move into the foliage, you're stopped dead in your tracks. A silver arrow is aimed square between your eyes. The wielder of the bow is a sharp-eyed, hooded figure with hair black as night."

        # VSFX Akari (zoom to fullbody)

        aki "Don't you dare move, monster!"

        "You put your hands up in the most placating gesture you can manage."

        you "Monster…? Uh, I think this is a misunderstanding, maybe we could just-"

        # VSFX Akari (closer)

        aki "Stop. You will not fool me. I know you."

        # VSFX Akari (closer)

        aki "I will have no mercy on you. Your death shall be painful, I will make sure of it. You will suffer for every life you have stolen, and I will have my revenge. You chose the wrong night to leave your little fortress, and now, you will finally pay."

        "You can't just let it end here. Not now."

        menu:
                # Akari Approval Choice
                "Plead your case.":
                        jump PleadCase
                #Akari Disapproval/Ashina Approval Choice
                "Call out for Ashina.":
                        jump CallOut

label BotchedConverge1:
        # Choices Converge Here

        # Image Ashina Neutral

        ash "I seem to recall telling you to stay inside, did I not, pup?"

        # VSFX Ashina (closer)

        "You turn to face Ashina as she steps closer, looming over you. You reflexively swallow."

        you "You… did."

        # VSFX Ashina (further, moving to the right)

        ash "Did you really think I would let you just walk out of here? You silly, naive little thing. You must take me for a fool."

        # VSFX Ashina (moving to the left)

        ash "This was a test, and you, my dear, have failed. I can see you are not yet ready for the privilege of independence."

        # Image Ashina Hybrid Angry
        # VSFX Ashina (closer)

        ash "Tell me, do you take joy in disrespecting me? In betraying the first ounce of trust I place in you?"

        # Image Ashina Neutral (further, center)

        ash "I will not tolerate your behavior. Get back inside. Now."

        menu:
                #Akari Approval Choice
                "Resist Ashina":
                        jump ResistAshina
                #Akari Disapproval Choice
                "Go willingly.":
                        jump GoWillingly  
                              
label BotchedConverge2:
        #Choices Converge Here

        if ash_approval >= 3:

                # Image Ashina Thoughtful
                # VSFX Ashina (as if pacing in frustration)

                "Ashina starts pacing as you look up at her from the ground, stunned. After a few moments, she stops and looks down at you with a softer expression."

                # Image Ashina Caring

                ash "Forgive me. You have been… mostly cooperative, I must admit, and you do not deserve my harshness. I understand that you would feel defensive, with how I approached you."

                #VSFX Ashina (closer)

                "She offers you a hand, and you hesitantly take it. She helps you up. You feel like a feather in her strong grasp, lifted with ease."

                #VSFX Ashina (further)
                #VSFX Zoom (as if being helped back onto your feet)

                ash "Perhaps you were feeling cooped up, and wanted to explore. I can’t blame you for that. However, you must restrain yourself."

                #VSFX Ashina (further)

                "Her grip on your hand lingers a moment longer, squeezing before pulling away."

                #VSFX Ashina Neutral

                ash "Trust takes time. You will be allowed to roam soon enough, I promise. Now… Please, return to your room."

                #VSFX Ashina (fade out)
                #VSFX Zoom (as if walking through the hearth)
                #SFX Walking

                "You feel her gaze on your back as you cross the hearth and head upstairs."

                # Image Captive Cabin Room (angled, zoomed in on ceiling)
                # VSFX Blur

                "When you find yourself lying in bed, you’re cradling your hand over your chest. You can still feel the warmth from when Ashina held it."

                # VSFX Black

        elif ash_approval >= 0

                #Image Ashina Hybrid Angry
                #VSFX Ashina (closer)

                "Ashina raises a hand as if she might hit you, and you reflexively flinch. She stops, a clear hesitation in her eyes."

                # Image Ashina Concerned

                ash "...Go to your room."

                #VSFX Ashina (fade out)
                #VSFX Zoom (as if walking through the hearth)
                #SFX Walking

                "She looks away. You figure you shouldn’t give her time to rethink that decision, and hurry up the stairs."

                # Image Captive Cabin Room (angled, zoomed in on ceiling)
                # VSFX Blur

                "When you find yourself lying in bed, you struggle to drift off, haunted by memories and the look of concern on your captor’s face."

                # VSFX Black

        else:
                #TBA, Unfinished

                # Image Ashina Hybrid Angry
                #VSFX Ashina (pacing)

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
                           
label ResistAshina:
        $ aka_approval += 1
        you "This isn’t about you! I wasn't doing anything wrong!"

        you "You think you can just turn me into some monster, ruin my life and act like I'm supposed to be grateful towards you? No! I've had enough!"

        "You turn away from Ashina and intend to put some space between you."

        #VSFX Ashina (fade out)
        #SFX Walking

        ash "You will not walk away from me!"

        #SFX Walking
        #Image Cabin Exterior POV Approaching
        #VSFX Zoom (as if being dragged to the door)

        "Ashina grabs your wrist and drags you struggling across the yard. As she does so, you notice a pair of dark eyes watching from the treeline."

        #Image Cabin Door Open
        #Image Hearth
        #Image Ashina Hybrid Angry
        #Music Cabin

        "Ashina tosses you into the cabin, slams the front door shut, and snarls at you."

        ash "I've given you a chance at a new life! And this is the thanks I get?!"

        jump BotchedConverge2

label GoWillingly:
        $ aka_approval -= 1
        "You avert your eyes from Ashina’s intense gaze, and walk back to the cabin. You hear Ashina’s footsteps behind you. Once inside, she approaches you with a fierce expression."

        # Image Ashina Concerned
        # VSFX as if  falling backwards onto the ground and looking up at Ashina

        "You stumble backwards, and your foot catches the edge of a chair, causing you to topple over. Ashina regards you hesitantly."

        ash "I told you to stay inside. Why couldn’t you just listen to me?"

        jump BotchedConverge2

label PleadCase:
        $ aka_approval += 1

        you "No, wait, please! I never asked to be a monster!"

        # VSFX Akari (further)

        "The hooded woman looks surprised at your outburst. Her stance doesn't waver, but she nods slowly at you to continue."

        you "Where do I begin…? I was out late. A bunch of dogs, hundreds of them, cornered me into an alley. Then, a huge wolf-beast attacked me, dragged me here, and turned me into…"

        # VSFX Akari (further)

        aki "The smaller dogs you mentioned. Where are they now?"

        # Image Akari Bow Nocked
        # The spelling on that is a pet peeve of mine
        # VSFX Akari (move horizontally across the screen, as if looking around)

        "The woman lowers her bow, looking around suspiciously."

        you "I don’t know, they were gone when I stepped outside. They must have run off somewhere, maybe-"

        #Image Akari Thoughtful

        aki "The large one, the wolf-beast. That is their master, is it not?"

        you "Yes. She goes by Ashina. She's been holding me captive."

        you "My friend tried to rescue me, but now they’re trapped here too. She said she wouldn’t do anything to them so long as I behave, but…"

        # Image Akari Angry

        aki "I see. So that lycanthrope is going around toying with the lives of innocent humans yet again. What a disgusting creature."

        # Image Akari Neutral

        "The woman turns her bow and arrow away from you, continuing to scan the surroundings."

        # VSFX Akari (move horizontally across the screen, as if looking around, other direction)

        aki "Everything about this spells out a trap. I need to get out of here."

        # VSFX Akari (move back to center)

        "She turns her dark gaze back to you."

        aki "Name's Akari. We have a common enemy. I will let you go, for now. Help me, and I will help you in turn."

        #change name to show Akari after reveal
        $ aki = Character("Akari")

        # VSFX Akari (closer)

        aki "But do not forget, you are still a monster. Try anything funny with me, and I will not hesitate to kill you."

        # VSFX Akari (moves away and fades out)

        "Akari backs into the foliage, disappearing in the blink of an eye. You notice how tense you feel, and allow yourself a moment to recover. A chill breeze ruffles your clothes."

        "The tranquil moment doesn't last for long. You hear the approach of powerful footsteps, and you know you're in for it now."

        jump BotchedConverge1

label CallOut:
        $ ash_approval += 1
        $ aka_approval -= 1

        # VSFX Akari (as if jumping slightly in place)

        "You desperately call out for Ashina and the hooded woman jumps slightly. She looks at you with a confused expression and lowers her bow."

        # Image Akari Bow Nocked

        aki "Who are you yelling for? You should be the only one here."

        # VSFX Akari (move slightly back and forth horizontally, a small look around)

        "The woman looks around, but there’s no sign of Ashina yet. The stranger’s dark gaze briefly returns to you."

        # Image Akari Thoughtful

        aki "You do look… different than I expected. Name’s Akari. How about you tell me-"

        #change name to show Akari after reveal
        $ aki = Character("Akari")

        #Image Akari Bow Nocked
        #SFX Growl
        #VSFX Akari (moves away and fades out)

        "There’s a sudden burst of movement and a fierce growling quickly approaching from behind you. Akari’s eyes go wide, and she quickly backs into the foliage, disappearing in the blink of an eye."

        #Image Wolf Ashina Snarling
        #Image Wolf Ashina Docile

        "The same beastly wolf that attacked you in the alley lunges forward at the treeline, then stops short, giving up the chase."

        # VSFX Ashina (fading in and out between images like a pokemon evolution until settling into the latter image)
        # Image Ashina Neutral

        "You watch as, before your eyes, the wolf begins to change. You hear the sharp cracking of bone and the mushy contorting of flesh. You want to look away, but you can’t. Soon enough, Ashina stands before you."

        jump BotchedConverge1