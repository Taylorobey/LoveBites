label SpeakNoEvilSceneP2:
        #Image Cabin Door Closed
        show bg door closed

        "You reach the basement and are hit with an earthy chill. You unlock the door with the key Ashina gave you, and step inside."

        #Image Cabin Door Open
        show bg door open with dissolve
        #SFX Walking
        play sound walk
        #Image Basement Room
        show bg basement with dissolve

        "You find Cameron huddled in a corner of the room. They shift, acknowledging your presence, but don’t turn around."

        #Image Cameron Frustrated (alt. Thoughtful) (far away, in the corner of the room)
        show cam frustrated with dissolve

        cam "I told you before, I won't eat. Not until you let me see her."

        you "Cam! It's me!"

        #Image Cameron Friendly
        show cam friendly with dissolve

        cam "¡Dios mío!"

        #SFX Faster Walking
        play sound fast_walk
        #VSFX Cameron (moves closer, then fades out)

        "Cameron pulls you in for a big hug. Tears stream down their face as they squeeze you tight."

        #Image Cameron Caring
        show cam caring with dissolve

        cam "I…honestly thought I’d never see you again. You don't know how glad I am that you're here."

        #Image Cameron Nervous (further)
        show cam nervous with dissolve

        cam "How did you even get in? Does Ashina know you're here right now?"

        you "Right, about that. She let me visit you. But…there's a bit of a catch."

        #VSFX Cameron (slide side to side movement as if shifting in place)

        "Cameron shifts nervously, a flicker of fear in their eyes."

        cam "Well… What is it?"

        if ash_approval >= 3:

                you "She agreed to let you go, on one condition."

                #Image Cameron Neutral
                show cam neutral with dissolve

                cam "Alright, lay it on me."

                you "You can never talk about anything that happened here ever again. No spreading chisme about a werewolf lady kidnapping us. No cabin in the woods."

                #Image Cameron Nervous
                show cam nervous with dissolve

                cam "What? But, how am I going to explain to people where I've been?"

                #Image Cameron Frustrated (alt. Thoughtful)
                show cam frustrated with dissolve

                cam "Hell, what am I going to say when people start wondering about you?!"

                you "I don't know, Cam. You'll have to make something up."

                #Image Cameron Nervous
                show cam nervous with dissolve

                cam "You'll get to come with me eventually, won't you…?"

                you "I can't promise that, Cam. I’m sorry."

                #Image Cameron Frustrated
                show cam frustrated with dissolve
                #VSFX Cameron (shaking, as if frustrated)

                cam "How do you expect me to just leave you here?!"

                you "Cameron…"

                if humanity >= 3:
                        menu:
                                #if Humanity is 3, this is the only option, and it auto-succeeds
                                "It’s okay. You can go.":
                                        $ humanity_chance = True
                                        jump HumanityChoice

                elif corruption >= 3:
                        menu:
                                #if Corruption is 3, this is the only option, and it auto-succeeds
                                "I don’t want you here.":
                                        $ corrupted_chance = True
                                        jump CorruptedChoice

                elif reveal_to_cam:
                        menu:
                                #Narrative Choice
                                #if monster reveal chosen in doors scene
                                "I could die if you tell anyone.":
                                        jump DieIfTell

                                #Narrative Choice
                                "I care about Ashina.":
                                        jump CareAboutAshina
                                        
                                #Narrative Choice
                                "She’ll kill you.":
                                        jump ShellKillYou

                                #Humanity % Choice
                                #if Humanity is 1 or 2
                                "It’s okay. You can go.":
                                        $ rand_chance = renpy.random.randint(0,100)
                                        $ compare_chance = humanity * 33
                                        if rand_chance <= compare_chance:
                                                $ humanity_chance = True
                                        jump HumanityChoice

                                #Corruption % Choice
                                #if Corruption is 1 or 2
                                "I don’t want you here.":
                                        $ rand_chance = renpy.random.randint(0,100)
                                        $ compare_chance = corruption * 33
                                        if rand_chance <= compare_chance:
                                                $ corrupted_chance = True
                                        jump CorruptedChoice
                
                else:
                        menu:
                                #Narrative Choice
                                "I care about Ashina.":
                                        jump CareAboutAshina
                                        
                                #Narrative Choice
                                "She’ll kill you.":
                                        jump ShellKillYou

                                #Humanity % Choice
                                #if Humanity is 1 or 2
                                "It’s okay. You can go.":
                                        $ rand_chance = renpy.random.randint(0,100)
                                        $ compare_chance = humanity * 33
                                        if rand_chance <= compare_chance:
                                                $ humanity_chance = True
                                        jump HumanityChoice

                                #Corruption % Choice
                                #if Corruption is 1 or 2
                                "I don’t want you here.":
                                        $ rand_chance = renpy.random.randint(0,100)
                                        $ compare_chance = corruption * 33
                                        if rand_chance <= compare_chance:
                                                $ corrupted_chance = True
                                        jump CorruptedChoice
        else:
                #Placeholder for the Cameron dies or becomes a Lycan paths
                hide placeholder

label DieIfTell:
        you "Ashina won't be the only one affected if you tell people about this."

        #Image Cameron Nervous

        cam "What do you mean? This whole situation is her fault!"

        you "Do you really think people will let a monster like me live?"

        if Cameron Approval >= 0:
                #Music Goodbyes
                #Image Cameron Frustrated
                #VSFX Cameron (shake, as if shaking head no)

                cam "You're not a monster! You're my friend! You won't hurt anyone!"

                you "Not everyone is going to think like that, Cam. They don't all know me."

                you "All they'll see is a big, scary wolf monster, and then they’ll point their weapons straight at me. Is that what you want?"

                #Image Cameron Thoughtful

                cam "No…I don't want that. I could never handle the guilt if I let that happen to you."

                "Cameron goes quiet, looking down in thought. Then, they sigh."

                #Image Cameron Neutral

                cam "Okay. If it’s really what you want, I promise, I won’t tell anyone."

                jump CameronGoodbye

        else:
                #Image Cameron Thoughtful

                "Cameron goes quiet, looking away in a clear show of guilt. After a moment, a few stray tears plummet down their cheeks."

                #VSFX Cameron (shake, as if upset)

                cam "Then… then we have to take that chance. We can’t let her live, she’s going to hurt more people."

                "Their words feel like a punch to the gut."

                jump ChoicetoRescue

label CareAboutAshina:
        you "Ashina isn’t all bad, Cam. I don’t want anything to happen to her. I… I care about her. She isn’t keeping me here, I want to stay."

        #Image Cameron Neutral

        "Cameron looks at you in disbelief."

        #VSFX Cameron (shake, as if shaking head no)

        cam "You can’t be serious. You’re messing with me, right?"

        "You shake your head."

        you "No Cam, I mean it. She isn’t a threat, she’ll only hurt people if she has to, to protect herself. She’s had a hard life."

        you "And, it’s not like I was living a happy life either. I’ve been wanting to escape for a long time. This isn’t what I thought would happen, but trust me when I say it’s what I want."
        
        if Cameron Approval >= 0:
                #Image Cameron Thoughtful

                cam "...You’re really serious, aren’t you? Ah, mierda."

                #VSFX Cameron (pacing, then slight up and down sighing motion)

                "Cameron paces in place, then sighs."

                #Image Cameron Neutral

                cam "Okay. If it’s really what you want, I promise, I won’t tell anyone."

                jump CameronGoodbye

        else:
                #Image Cameron Thoughtful

                cam "You’ve gone mad. She… can’t you see she’s poisoned your head?"

                #Image Cameron Frustrated
                #VSFX Cameron (shake, as if shaking head no)

                cam "No, I’m not feeding into this… delusion of yours. Wake up! She kidnapped you! She’s threatening to kill me! "

                jump ChoicetoRescue

label ShellKillYou:
        you "This is serious, Cam. If you don’t agree to this, if she even suspects that you aren’t one hundred percent on board, she’s going to kill you. I know you. You’re not cut out for this."

        if cam_approval >= 0:
                #Music Goodbyes
                #Image Cameron Scared

                "The reality of the situation seems to finally set in for Cameron. You watch as their suppressed terror takes over, before they are able to collect themself."

                #Image Cameron Nervous

                cam "You’re… you’re right. I just want to go home. If this is what it takes, then…"

                #Image Cameron Neutral

                cam "Okay. I promise, I won’t tell anyone."

                jump CameronGoodbye

        else:
                #Image Cameron Frustrated

                cam "No. I’m not leaving you here, not ever. If this is the one brave thing I do in my whole life… then so be it."

                jump ChoicetoRescue

label CameronGoodbye:
        $ cameron_leave = True
        #Image Cameron Thoughtful

        "They give you a long, forlorn look, eyes tearing up."

        #Image Cameron Caring

        cam "I’m really going to miss you."

        #VSFX Cameron (fade out)

        "You step forward and give Cameron the tightest hug you’ve ever given anyone."
        
        jump SpeakNoEvilSceneP3

label ChoicetoRescue:
        menu:
                #Narrative Choice
                "Return to Ashina.":
                        #VSFX Cameron (fade out)
                        #SFX Walking
                        #Image Cabin Door Open
                        #Image Cabin Door Closed

                        "You turn away wordlessly, defeated. Your expression falls, and everything feels fuzzy. You barely notice Cameron calling out behind you as you lock the door, and head back up the stairs."
                        
                        jump SpeakNoEvilSceneP3

                #Narrative Choice
                "Option not available. (demo)":
                        #"Help Cameron Escape."
                        $ cameron_help = True
                        jump HelpCameronEscape

label HelpCameronEscape:
        "I did say that this option wasn't available."

        "This is only a demo, after all"

        return

label CorruptedChoice:
        "You give Cameron a flat, tired look."

        you "Can’t you see that you’re just causing me more trouble? I don’t want you here. Do I need to spell it out for you?"

        if corrupted_chance:
                #VSFX Screen (tints blue)
                #Image Cameron Scared (further)

                "Cameron recoils, suddenly looking terrified. It takes them a few moments of panicked breathing to compose themself. They can’t look you in the eyes."

                #Image Cameron Nervous

                cam "Okay, okay, I won’t tell anyone, I swear. I just want to go home. Please."

                "You can’t help a tinge of sadness at seeing your old friend in such a state, but you know this is for their own good. You swallow reflexively, realizing your mouth is pooling with drool, and turn away."

                #VSFX Screen (tint fades)

        else:
                #Image Cameron Neutral

                "Cameron stares at you, unaffected by your words."

                cam "I know what you’re trying to do. My answer is no."

                #VSFX Cameron (fade out)

                "They walk back to the corner of the room, and sit, refusing to look at you."

                #SFX Walking
                #Image Cabin Door Open
                #Image Cabin Door Closed

                "You turn away wordlessly, defeated. Your expression falls, and everything feels fuzzy. You barely notice your hands moving to lock the door, and you head back up the stairs."
        
        jump SpeakNoEvilSceneP3

label HumanityChoice:
        "Your gaze softens, and you reach forward, taking Cameron’s hand."

        you "I know you, Cam. You don’t need to act tough. I promise, I’m going to be okay. It’s okay. You can go."

        if humanity_chance:
                #VSFX Screen (tints yellow)
                #Music Goodbyes
                #Image Cameron Neutral
                #VSFX Cameron (zoom closer then fade out)

                "Cameron tries to keep a straight face, but breaks down into tears, pulling you into a tight hug. You hug them back, tighter than you’ve ever hugged anyone."

                cam "Okay, I won’t tell anyone. Te amo, I’m going to miss you so much."

                you "I love you too, Cam. Stay safe."

                "You hold each other for a long while, before you finally separate for the last time."

        else:
                #Image Cameron Nervous

                "Cameron’s expression momentarily falters, before they steel themselves."

                #Image Cameron Frustrated
                #VSFX Cameron (shake, as if shaking head no)

                cam "No, we’re not doing this. I can’t just stand here and let this happen. We’re getting out of here, right now, together."

                #VSFX Cameron (fade out)

                "Cameron grabs your arm and heads up the stairs without giving you a chance to respond."

        jump SpeakNoEvilSceneP3