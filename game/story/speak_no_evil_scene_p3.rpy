label SpeakNoEvilSceneP3:
        #Choices Converge here
        window auto hide
        show bg color black with Dissolve(3.0)
        define cameron_leave = True
        
        #if Cameron agrees to leave
        if cameron_leave:

                "You head up the stairs with Cameron in tow."

                scene bg hearth with dissolve:
                        subpixel True
                        zoom 0.7
                        pos(-1.0,-0.2)
                
                #Image Ashina Neutral (further from you and cameron)
                #Image Cameron Neutral (closer to you and to the side)
                show ash neutral with dissolve:
                        subpixel True pos (0.36, 0.0) xrotate 0.0 yrotate 180.0
                show cam neutral with dissolve:
                        subpixel True pos (0.0, 0.0) zoom 1.5 xrotate 0.0 yrotate 180.0

                ash "I take it you two had a pleasant reunion. How lovely."

                #VSFX Ashina (closer to Cameron)
                window auto hide
                show ash neutral:
                        subpixel True 
                        pos (0.36, 0.0) zoom 1.0 
                        linear 0.60 pos (0.24, 0.0) zoom 1.3 
                with Pause(0.70)
                show ash neutral:
                        pos (0.24, 0.0) zoom 1.3
                #Image Cameron Nervous
                show cam nervous with dissolve
                window auto show

                "Ashina turns her attention towards Cameron."

                ash "If you agree to live by my rules, speak them in your own words. I need to make sure you understand what I expect of you."

                #VSFX Cameron (move away from Ashina and closer to you)
                window auto hide
                show cam nervous:
                        subpixel True 
                        parallel:
                                xpos 0.0 
                                ease_bounce 0.20 xpos -0.07 
                        parallel:
                                ypos 0.0 
                                ease 0.20 ypos 0.03 
                        parallel:
                                zoom 1.5 
                                ease_back 0.20 zoom 1.75 
                with Pause(0.30)
                show cam nervous:
                        pos (-0.07, 0.03) zoom 1.75 
                window auto show

                "Cameron shrinks away from Ashina, moving closer to you."

                #Image Cameron Thoughtful
                show cam thoughtful with dissolve

                cam "Right, um… I can leave, but only if I promise not to talk about anything that happened here. I can't tell anyone about you, or werewolves, or the cabin. Nada, nothing."

                window auto hide
                #Image Ashina Friendly
                show ash friendly with dissolve
                with Pause(0.5)
                #VSFX Ashina (moves back to give Cameron space)
                show ash friendly:
                        subpixel True 
                        xpos 0.24 
                        linear 0.30 xpos 0.4 
                with Pause(0.40)
                show ash friendly:
                        xpos 0.4 
                window auto show

                ash "Yes, you understand well. Act as though this never even happened."

                #VSFX Ashina (closer to you, opposite side of Cameron)
                window auto hide
                show ash friendly:
                        subpixel True 
                        pos (0.4, 0.0) zoom 1.3 
                        linear 0.60 pos (0.51, -0.03) zoom 2.0 
                with Pause(0.70)
                show ash friendly:
                        pos (0.51, -0.03) zoom 2.0 
                window auto show

                ash "Hm, color me impressed. I didn't think you could convince them so well, pup."

                window auto hide
                #VSFX Ashina (further away again)
                show ash friendly:
                        subpixel True 
                        pos (0.51, -0.03) zoom 2.0 
                        linear 0.60 pos (0.4, 0.0) zoom 1.3 
                with Pause(0.70)
                show ash friendly:
                        pos (0.4, 0.0) zoom 1.3 
                with Pause(1.0)
                #Image Ashina Thoughtful
                show ash thoughtful with dissolve:
                        xpos 0.35
                window auto show

                ash "I'm satisfied. Come along with me, human. I shall escort you back to civilization."

                window auto hide
                #SFX Walking
                #Image Cabin Door Open
                #Image Ashina Neutral
                #Image Cameron Caring
                #VSFX Cameron (fade out and towards the door)
                show bg door open with Dissolve(1.0):
                        subpixel True pos (0.0, 0.0) zoom 1.0 
                with Pause(1.0)
                hide cam thoughtful with dissolve

                "The three of you approach the front door. Cameron takes one look back at you before disappearing into the darkness outside. You do your best to commit their face to memory, knowing it may be the last time you see them."

                show ash neutral with dissolve

                ash "As for you, girl, I have something to show you when I return. Be ready."

                window auto hide
                #VSFX Ashina (fade out and towards the door)
                hide ash neutral with dissolve
                with Pause(0.5)
                #Image Cabin Door Closed
                show bg door closed with Dissolve(1.5):
                        subpixel True pos (0.0, 0.0) zoom 1.0 
                window auto show

                "With that, Ashina shuts the cabin door, and you are left to your own devices."

                "You're uncertain of your future here, but you can at least rest easy now knowing that Cameron is safe."
                window auto hide

                stop music fadeout 1.5
                show bg color black with Dissolve (2.0)

                jump LettersScene

        #if Cameron agrees to be turned
        elif cameron_turning:
                #Placeholder for the Cameron becomes a Lycan path
                hide placeholder

        #if Cameron refuses to leave or be turned, and you try to help them escape
        elif cameron_help:
                #Placeholder for a negative ending where you both die, or you die fighting Ashina and Cameron escapes.
                hide placeholder

        #if Cameron refuses to leave or be turned, and you return to Ashina
        else:
                "You find yourself in front of Ashina, your stomach hollow with dread."

                #VSFX Ashina (closer)

                ash "Hm? Where is the human?"

                you "They…didn't want to do it. I tried to convince them, but they…"

                #VSFX Ashina (perspective angled as if you’re on the ground below her, or just fade her out if that looks too awkward)
                #SFX Impact

                "You drop to your knees. The stress of the past couple days finally catches up to you. You gasp for air as your chest heaves with sobs. You feel Ashina’s hand on your head, patting you."

                #Image Ashina Caring

                ash "There, there. You did your best. Some people simply can't be reasoned with."

                #Image Ashina Thoughtful

                ash "I will make this quick. But, I can't promise it will be painless if they struggle."

                #Image Ashina Neutral

                ash "Go to your room. It'll be easier for you that way."

                #VSFX Zoom/Movement (as if standing)

                "You shakily rise to your feet, but hesitate. You don’t have to just let this happen. You could…"

                ash "I know what you're thinking. But, it's much too late to try and save them, pet. They've made their choice."

                #Image Ashina Caring

                ash "Please, I'm trying to extend a kindness towards you. This isn't something you will want to witness. Go."

                #VSFX Ashina (fade out)
                #SFX Fireplace (fade out)
                #SFX Walking
                #Image Cabin Hall

                "Your legs trudge up the stairs as if weighed down by a thick mud. You can't even stand to look at Ashina right now. You don't want to do this. Everything within you screams for you to rush to your friend’s aid."

                #SFX Walking
                #Image Cabin Door Closed

                "But, there's no choice. You’d just be getting yourself killed, too, and what good would that do? They made their decision, and you can’t help but understand Ashina’s position. If only you could’ve just made them agree… but you can’t control other people."

                #SFX Walking
                #Image Cabin Door Open
                #Image Captive Cabin Room

                "You stumble into your room. You autopilot yourself into bed. Maybe if you go to sleep now, you can convince yourself that tonight was just a bad nightmare. Push this all deep down, where all the things you can’t deal with go."

                cam "AHHHH!"

                #VSFX Red (blooming at the edges of the screen)
                #SFX Heartbeat

                "A blood curdling scream pierces the air. It feels like Cameron's heart is beating directly into your ears."

                you "No…No!"

                "You realize in horror that your heightened senses have honed in on the room two floors below. No matter how hard you fight to shut them down, your intrusive thoughts sharpen their focus. The more you try, the more you think about it, and the more you feel."

                "You hear every bit of terror in their labored breathing. You smell the fresh tang of blood rushing from their arteries. As Ashina slams their limp body into the basement wall, the thud reverberates throughout your entire body."

                ash "I'm trying to make this easy on you, human! Stay still!"

                cam "No, please! I just wanted to save her! I love-!"

                #VSFX Red (full screen pulsing red)

                "You hear an awful sound. The crunching of their bones, the splitting of their tendons, the twisting of their flesh. The sound of Cameron's heartbeat suddenly silences. Your eyes tightly shut."

                #SFX Heartbeat (stop)
                #VSFX Black Screen

                "...You should have tried harder. To convince Cameron to leave. To escape this prison together. To have a strong enough will to live to not even end up in this fucked up situation to begin with. Your inability to take control of your own life has gotten your best friend killed."

                "Ashina dealt the killing blow, but you are the reason Cameron was here in the first place. You were a fool to think that flirting with danger would solve your problems for you. Leaving it all up to forces outside of yourself, taking no responsibility… just like your parents."

                "You don't know if you can live with yourself after this. Even if you do, it doesn’t feel like there’s enough left of you for it to even matter."


                # (Demo Bad End)
