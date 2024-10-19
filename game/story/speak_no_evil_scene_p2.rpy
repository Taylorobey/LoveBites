label SpeakNoEvilSceneP2:
        $ save_name = "Hear No Evil"

        window auto hide
        pause 0.5
        play music eerie_outdoors_music
        
        #Image Cabin Door Closed
        show bg door closed:
                subpixel True pos (-0.4, -0.48) zoom 1.8

        window auto show

        "You reach the basement and are hit with an earthy chill. You unlock the door with the key Ashina gave you, and step inside."

        window auto hide
        #Image Cabin Door Open
        show bg door open with dissolve:
                subpixel True pos (-0.4, -0.48) zoom 1.8

        #for some reason when i change the pos of the earlier bg's the later ones are broken too
        #i suppose this might be because all of them share the name "bg" in front
        #is this bad?

        #Image Basement Room    
        show bg basement with dissolve:
                subpixel True pos (0, 0.01) zoom 1.0

        #Image Cameron Frustrated
        show cam frustrated with dissolve:
                subpixel True pos (0.64, 0.18) zoom 0.66 yrotate 180.0

        window auto show

        "You find Cameron huddled in a corner of the room. They shift, acknowledging your presence, but don’t turn around."

        #show cam frustrated at cam_ground_shake
        #with Pause(0.55)
        #broken

        cam "I told you before, I won't eat. Not until you let me see her."

        you "Cam! It's me!"
 
        #Image Cameron Friendly
        show cam friendly with dissolve
        with Pause(0.2)
        #show cam friendly at cam_surprise_jump
        #with Pause(0.55)
        #broken

        cam "¡Dios mío!"

        #VSFX Cameron (moves closer, then fades out)
        show cam friendly at hug
        with Pause(1.2)
        hide cam friendly with dissolve

        "Cameron pulls you in for a big hug. Tears stream down their face as they squeeze you tight."

        #Image Cameron Caring
        show cam caring with dissolve

        cam "I…honestly thought I’d never see you again. You don't know how glad I am that you're here."

        #Image Cameron Nervous (further)
        show cam nervous with dissolve

        cam "How did you even get in? Does Ashina know you're here right now?"

        you "Right, about that. She let me visit you. But…there's a bit of a catch."

        #VSFX Cameron (slide side to side movement as if shifting in place)
        show cam nervous at nervous_shake

        "Cameron shifts nervously, a flicker of fear in their eyes."

        cam "Well… What is it?"

        #for testing
        #define ash_approval = 3
        #define corruption = 2
        #define humanity = 2
        #define cam_approval = 3

        if ash_approval >= -2:
                #temporary logic change for the demo to make sure other paths don't trigger

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
                with Pause(0.1)
                #VSFX Cameron (shaking, as if frustrated)
                show cam frustrated at nervous_shake
                
                cam "How do you expect me to just leave you here?!"

                you "Cameron…"

                window auto hide

                if humanity >= 3:
                        menu:
                                #if Humanity is 3, this is the only option, and it auto-succeeds
                                "{color=#ffff00}{b}It’s okay. You can go.{/b}{/color}":
                                        $ humanity_chance = True
                                        jump HumanityChoice

                elif corruption >= 3:
                        menu:
                                #if Corruption is 3, this is the only option, and it auto-succeeds
                                "{color=#1C4587}{b}I don’t want you here.{/b}{/color}":
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
                                "{color=#ffff00}{b}It’s okay. You can go.{/b}{/color}":
                                        $ rand_chance = renpy.random.randint(0,100)
                                        $ compare_chance = humanity * 33
                                        if rand_chance <= compare_chance:
                                                $ humanity_chance = True
                                        jump HumanityChoice

                                #Corruption % Choice
                                #if Corruption is 1 or 2
                                "{color=#1C4587}{b}I don’t want you here.{/b}{/color}":
                                        $ rand_chance = renpy.random.randint(0,100)
                                        $ compare_chance = corruption * 33
                                        if rand_chance <= compare_chance:
                                                $ corrupted_chance = True
                                        jump CorruptedChoice
        else:
                #Placeholder for the Cameron dies or becomes a Lycan paths
                hide placeholder

label DieIfTell:
        pause 0.3
        window auto show

        you "Ashina won't be the only one affected if you tell people about this."

        #Image Cameron Nervous
        show cam nervous with dissolve

        cam "What do you mean? This whole situation is her fault!"

        you "Do you really think people will let a monster like me live?"

        if cam_approval >= 0:
                #Music Goodbyes
                play music goodbyes_music volume 0.7 fadein 2.0
                #Image Cameron Frustrated
                show cam frustrated with dissolve
                with Pause(1.0)
                #VSFX Cameron (shake, as if shaking head no)
                show cam frustrated at nervous_shake

                cam "You're not a monster! You're my friend! You won't hurt anyone!"

                you "Not everyone is going to think like that, Cam. They don't all know me."

                you "All they'll see is a big, scary wolf monster, and then they’ll point their weapons straight at me. Is that what you want?"

                #Image Cameron Thoughtful
                show cam thoughtful with dissolve

                cam "No…I don't want that. I could never handle the guilt if I let that happen to you."

                "Cameron goes quiet, looking down in thought. Then, they sigh."

                #Image Cameron Neutral
                show cam neutral with dissolve

                cam "Okay. If it’s really what you want, I promise, I won’t tell anyone."

                jump CameronGoodbye

        else:
                #Image Cameron Thoughtful
                show cam thoughtful with dissolve

                "Cameron goes quiet, looking away in a clear show of guilt. After a moment, a few stray tears plummet down their cheeks."

                show cam nervous with dissolve
                with Pause(0.1)
                #VSFX Cameron (shake, as if upset)
                show cam nervous at nervous_shake

                cam "Then… then we have to take that chance. We can’t let her live, she’s going to hurt more people."

                "Their words feel like a punch to the gut."

                jump ChoicetoRescue

label CareAboutAshina:
        pause 0.3
        window auto show

        you "Ashina isn’t all bad, Cam. I don’t want anything to happen to her. I… I care about her. She isn’t keeping me here, I want to stay."

        #Image Cameron Nervous
        show cam nervous with dissolve

        "Cameron looks at you in disbelief."

        #VSFX Cameron (shake, as if shaking head no)
        show cam nervous at nervous_shake

        cam "You can’t be serious. You’re messing with me, right?"

        "You shake your head."

        you "No Cam, I mean it. She isn’t a threat, she’ll only hurt people if she has to, to protect herself. She’s had a hard life."

        you "And, it’s not like I was living a happy life either. I’ve been wanting to escape for a long time. This isn’t what I thought would happen, but trust me when I say it’s what I want."
        
        if cam_approval >= 0:
                stop music fadeout 1.0
                play music goodbyes_music volume 0.7 fadein 2.5
                
                #Image Cameron Thoughtful
                show cam thoughtful with dissolve

                cam "...You’re really serious, aren’t you? Ah, mierda."

                #VSFX Cameron (pacing, then slight up and down sighing motion)
                show cam thoughtful at pacing

                "Cameron paces in place, then sighs."

                show cam thoughtful at stop_pacing
                with Pause (0.2)
                #Image Cameron Neutral
                show cam neutral with dissolve

                cam "Okay. If it’s really what you want, I promise, I won’t tell anyone."

                jump CameronGoodbye

        else:
                #Image Cameron nervous
                show cam nervous with dissolve

                cam "You’ve gone mad. She… can’t you see she’s poisoned your head?"

                #Image Cameron Frustrated
                show cam frustrated with dissolve
                with Pause(0.2)
                #VSFX Cameron (shake, as if shaking head no)
                show cam frustrated with nervous_shake

                cam "No, I’m not feeding into this… delusion of yours. Wake up! She kidnapped you! She’s threatening to kill me!"

                jump ChoicetoRescue

label ShellKillYou:
        pause 0.3
        window auto show

        you "This is serious, Cam. If you don’t agree to this, if she even suspects that you aren’t one hundred percent on board, she’s going to kill you. I know you. You’re not cut out for this."

        if cam_approval >= 0:
                #Music Goodbyes
                stop music fadeout 1.0
                play music goodbyes_music volume 0.7 fadein 2.5
                #Image Cameron Scared
                show cam scared with dissolve
                with Pause(0.2)
                show cam scared at nervous_shake

                "The reality of the situation seems to finally set in for Cameron. You watch as their suppressed terror takes over, before they are able to collect themself."

                #Image Cameron Nervous
                show cam nervous with dissolve

                cam "You’re… you’re right. I just want to go home. If this is what it takes, then…"

                #Image Cameron Neutral
                show cam neutral with dissolve

                cam "Okay. I promise, I won’t tell anyone."

                jump CameronGoodbye

        else:
                #Image Cameron Frustrated
                show cam frustrated with dissolve
                with Pause(0.2)
                show cam frustrated at nervous_shake

                cam "No. I’m not leaving you here, not ever. If this is the one brave thing I do in my whole life… then so be it."

                jump ChoicetoRescue

label CameronGoodbye:
        $ cameron_leave = True

        #Image Cameron Thoughtful
        show cam nervous with dissolve
        window auto show

        "They give you a long, forlorn look, eyes tearing up."

        #Image Cameron Caring
        show cam caring with dissolve

        cam "I’m really going to miss you."

        #VSFX Cameron (fade out)
        hide cam caring with dissolve

        "You step forward and give Cameron the tightest hug you’ve ever given anyone."
        
        jump SpeakNoEvilSceneP3

label ChoicetoRescue:
        menu:
                #Narrative Choice
                "Return to Ashina.":
                        pause 0.3
                        #VSFX Cameron (fade out)
                        #SFX Walking
                        #Image Cabin Door Open
                        #Image Cabin Door Closed

                        scene bg door open with dissolve
                        with Pause(1.0)
                        show bg door closed with dissolve
                        window auto show

                        "You turn away wordlessly, defeated. Your expression falls, and everything feels fuzzy. You barely notice Cameron calling out behind you as you lock the door, and head back up the stairs."
                        
                        jump SpeakNoEvilSceneP3

                #Narrative Choice
                "Option not available. (demo)":
                        #"Help Cameron Escape."
                        #$ cameron_help = True
                        jump HelpCameronEscape

label HelpCameronEscape:
        pause 0.3
        window auto show

        narrator "Sorry, this option isn't available in the demo."
        jump ChoicetoRescue

label CorruptedChoice:
        pause 0.3
        window auto show
        
        "You give Cameron a flat, tired look."

        you "Can’t you see that you’re just causing me more trouble? I don’t want you here. Do I need to spell it out for you?"

        if corrupted_chance:
                $ cameron_leave = True
                
                #VSFX Screen (tints blue)
                #Image Cameron Scared (further)
                show cam scared with dissolve
                with Pause(0.2)
                show cam scared at nervous_shake

                "Cameron recoils, suddenly looking terrified. It takes them a few moments of panicked breathing to compose themself. They can’t look you in the eyes."

                #Image Cameron Nervous
                show cam nervous with dissolve

                cam "Okay, okay, I won’t tell anyone, I swear. I just want to go home. Please."

                "You can’t help a tinge of sadness at seeing your old friend in such a state, but you know this is for their own good. You swallow reflexively, realizing your mouth is pooling with drool, and turn away."

                #VSFX Screen (tint fades)

        else:
                #Image Cameron Neutral
                show cam neutral with dissolve

                "Cameron stares at you, unaffected by your words."

                cam "I know what you’re trying to do. My answer is no."

                #VSFX Cameron (fade out)
                hide cam neutral with dissolve

                "They walk back to the corner of the room, and sit, refusing to look at you."

                #SFX Walking
                #Image Cabin Door Open
                #Image Cabin Door Closed

                show bg door open with dissolve
                with Pause(1.0)
                show bg door closed with dissolve

                "You turn away wordlessly, defeated. Your expression falls, and everything feels fuzzy. You barely notice your hands moving to lock the door, and you head back up the stairs."
        
        jump SpeakNoEvilSceneP3

label HumanityChoice:
        pause 0.3
        window auto show

        "Your gaze softens, and you reach forward, taking Cameron’s hand."

        you "I know you, Cam. You don’t need to act tough. I promise, I’m going to be okay. It’s okay. You can go."

        if humanity_chance:
                $ cameron_leave = True

                window auto hide

                #VSFX Screen (tints yellow)
                #Music Goodbyes
                stop music fadeout 1.0
                play music goodbyes_music volume 0.7 fadein 2.5
                #Image Cameron Neutral
                
                show cam neutral with dissolve
                with Pause(0.2)
                #VSFX Cameron (zoom closer then fade out)
                show cam nervous with dissolve
                with Pause(0.2)
                hide cam nervous with dissolve
                window auto show


                "Cameron tries to keep a straight face, but breaks down into tears, pulling you into a tight hug. You hug them back, tighter than you’ve ever hugged anyone."

                cam "Okay, I won’t tell anyone. Te amo, I’m going to miss you so much."

                you "I love you too, Cam. Stay safe."

                "You hold each other for a long while, before you finally separate for the last time."

        else:
                #Image Cameron Nervous
                show cam nervous with dissolve

                "Cameron’s expression momentarily falters, before they steel themselves."

                #Image Cameron Frustrated
                show cam frustrated with dissolve
                with Pause(0.2)
                #VSFX Cameron (shake, as if shaking head no)
                show cam frustrated at nervous_shake

                cam "No, we’re not doing this. I can’t just stand here and let this happen. We’re getting out of here, right now, together."

                #VSFX Cameron (fade out)

                #"Cameron grabs your arm and heads up the stairs without giving you a chance to respond."

                # $ cameron_help = True

                jump ChoicetoRescue

        jump SpeakNoEvilSceneP3