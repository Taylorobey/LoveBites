label WakingScene:
        $ save_name = "Careful What You Wish For"

        window auto hide

        scene bg color black with dissolve
        with Pause(0.5)

        call WakeUpSequence1 from _call_WakeUpSequence1_3
        
        window auto show

        "The cool evening breeze is the first thing you sense, then the chirping of crickets outside."

        window auto hide

        call WakeUpSequence2 from _call_WakeUpSequence2_3

        window auto show

        "Your eyes are welcomed by the interior of a log cabin. It almost feels like a peaceful evening at camp, that is if it weren't for…"

        window auto hide

        #VFX red flash (on the edges)
        call PainFlash from _call_PainFlash
        play soundb heart
        with Pause(0.7)
        stop soundb fadeout 0.5

        window auto show

        "A stinging sensation fills your body as you attempt to sit up. Your fingers touch the tender wound on your shoulder, the bite from that…thing, yesterday. You hesitate to call it a wolf."

        window auto hide
        
        #image captive cabin room (full view)
        scene bg room mc with dissolve
        stop sound fadeout 1.0

        window auto show

        "You take a glance at your immediate surroundings. The room is mostly bare. Some fake-looking flowers decorate the minimal furnishings."

        window auto hide


        menu:
                "You regret what you wished for.":
                        $ humanity += 1
                        pause 0.3

                        "Flirting with disaster finally caught up with you. What the hell were you thinking? You vow that if you ever escape this place, you're going to have a serious think about your life choices."
                "At least you won't have to go to work tomorrow.":
                        $ corruption += 1
                        pause 0.3

                        "It’s a dark, bitter thought, but you can’t help it. There’s a reason you were outside that night, and now you’ve gotten what you wanted, right?"
        "You’re shaken from your thoughts by the sound of a door opening. A tall, muscular woman with tan skin enters the room."


        window auto hide
        #VSFX ashina slides in from the right
        #image ashina neutral
        show ash neutral with MoveTransition(1.3, enter=offscreenright)

        window auto show

        ash "I see you're finally awake. Tell me, how was your slumber?"
        you "Who... who are you? Did you bring me here?"

        window auto hide


        #VSFX ashina steps closer
        show ash annoyed with dissolve
        with Pause(0.2)
        show ash annoyed at step_close
        with Pause(1.00)

        window auto show

        ash "That's not what I asked you."
        
        #VSFX ashina steps back
        window auto hide
        show ash annoyed at step_away
        with Pause(1.00)
        window auto show


        ash "I'll ask again, how was your slumber?"
        you "Oh, well... Fine, I guess, all things considered."

        #image ashina friendly
        show ash friendly with dissolve
        ash "Good, good."

        show ash friendly:
                subpixel True 
                ypos 1.0 
                linear 0.3 ypos 1.02
                linear 0.3 ypos 1.0 
        with Pause(0.6)

        ash "Now, sit up properly. I've prepared a meal for you."


        window auto hide
        #SFX stomach growl
        play sound growl
        with Pause(1.5)
        stop sound fadeout 1.0
        window auto show

        
        "Your stomach grumbles at the mere mention of food. You don't know what you're doing here, much less who this woman is, but you need something in your stomach {i}now{/i}."


        window auto hide
        show ash friendly:
                linear 1 xpos 1.2
        with Pause(1)
        hide ash friendly
        window auto show


        "You sit up. The woman reaches into the hallway, then sets a plate on the side table next to the bed."


        window auto hide
        stop music fadeout 1.0
        show ash sadistic:
                subpixel True pos (0.97, 1) zoom 1.88
                linear 0.5 xpos 0.53 
        with Pause(0.6)
        show ash sadistic:
                pos (0.53, 1) 
        window auto show


        ash "Here. Eat to your heart's content."

        scene bg meat plate with dissolve
        hide ash sadistic
        play music eerie_outdoors_music volume 1.5 fadein 0.5
        stop sound
        window auto show

        "On the plate is a pile of raw meat. Blood pools at the bottom of the chunks, and the stench of death reeks in the air."

        scene bg room mc with dissolve
        show ash sadistic with dissolve:
                pos (0.53, 1)  zoom 1.88

        you "You can't be serious… There's no way I can eat that!"

        show ash neutral with dissolve

        ash "Are you really so sure? Doesn't your hunger just feel..."

        #VSFX ashina close up
        window auto hide
        show ash neutral at step_closer_center
        with Pause(1.0)
        window auto show


        ash "Unbearable?"

        scene bg meat plate with dissolve
        hide ash neutral
        "You take another look at the plate. You hate to admit it, but your stomach betrays you. You don't just {i}want{/i} to eat it..."

        #vsfx red flash on edges like a blooming pain
        #vsfx centered text, dim surroundings
        #text "YOU NEED TO EAT THE RAW MEAT."

        window auto hide
        play sound heart loop
        image hungertext = Text("YOU {b}NEED{/b} TO EAT THE {b}{outlinecolor=#000}{color=#b70000}RAW MEAT.{/b}{/color}{/outlinecolor}", style="bigtext", font="CabinSketch-Bold.ttf")
        show hungertext
        show pain:
                subpixel True
                alpha 0.0
                linear 1.0 alpha 1.0 
                linear 1.0 alpha 0.5
                linear 1.0 alpha 1.0 
                linear 1.0 alpha 0.5
                linear 1.0 alpha 1.0
        pause(5.0)
        hide hungertext
        hide pain with dissolve

        #image ashina neutral
        stop sound fadeout 0.5
        stop music fadeout 1.0

        scene bg mc room with dissolve
        show ash sad with dissolve
        window auto show


        ash "Ah, so you finally understand the gravity of the situation."

        show ash neutral with dissolve

        ash "You must eat this meal, or the beast will take you."

        you "The beast? What does that mean?"

        you "Did you do something to me?"

        show ash annoyed with dissolve

        ash "Do not question me, simply do as I tell you. Eat."

        hide ash annoyed with dissolve
        scene bg meat plate with dissolve

        
        menu:
                #corruption choice
                "Eat the meal.":
                        $ corruption += 1
                        $ ash_approval += 1
                        $ meat_eaten = True
                        pause 0.3
                        "The meat is… surprisingly palatable. It has a deep, tender richness. You barely restrain yourself from stuffing your face ravenously. The clawing hunger soon subsides."
                        "You realize the woman has been watching you."

                        scene bg room mc with dissolve
                        #image ashina friendly
                        show ash friendly with dissolve
                        ash "Good girl. Now, get some rest."

                #humanity choice
                "Abstain from eating.":
                        $ humanity += 1
                        pause 0.3
                        "You turn away from the plate on the side table. The woman sighs."

                        scene bg room mc with dissolve
                        show ash neutral with dissolve
                        
                        ash "You will need to eat eventually, girl, but I suppose I can allow you some time to adjust. Now, get some rest."
        

        window auto hide
        ## slow this down?
        hide ash with easeoutright
        
        #VSFX blur
        camera:
                linear 1.0 blur 20.0
        window auto show


        "Seemingly satisfied with the interaction, your captor exits the room. You notice that despite a full day’s rest, you’re struggling to keep your eyes open."
        

        window auto hide
        #VSFX return to normal
        camera:
                linear 1.0 blur 0.0
        window auto show


        "You force your eyes to focus. On the far wall, there is a window. A possible escape route?"

        window auto hide

        menu:
                "Examine the window.":
                        jump ExamineWindow
                "Head to bed.":
                        jump HeadtoBed

label ExamineWindow:
        pause 0.3
        
        #sfx walking
        play sound walk
        
        #slow zoom into window

        window auto hide
        show bg room mc at walk_to_window
        with Pause(1.0)
        window auto show

        stop sound
        "You approach the window, and a low rumbling shakes the floor."
        
        window auto hide

        #sfx dogs barking
        play sound walk
        play sound barking volume 0.25
        
        #closer to window
        show bg room mc at close_to_window
        with Pause(1.0)
        window auto show


        "You inch ever closer, and you hear dogs begin to growl and bark wildly."


        window auto hide
        #image window no dogs
        show bg window with dissolve:
                subpixel True yoffset 0.0 zoom 2.5 
        window auto show


        "You finally reach the window and take a peek outside..."
        stop sound fadeout 1.0
        stop music fadeout 1.0
        

        window auto hide
        #image window with dogs
        show bg window eyes with dissolve
        with Pause(3.0)
        window auto show

        
        "Countless dogs stare from the abyss into your eyes. However, unlike the commotion before, they are completely silent. Their gaze is unwavering and they stand unnaturally still."

        play music connection_music volume 0.25

        #VSFX Slight Blue Tint (slow fade in)
        camera:
                #matrixcolor TintMatrix("#1C4587")
                matrixcolor TintMatrix("#fff")
                linear 3.0 matrixcolor TintMatrix("#1C4587")

        "A strange sensation rises within you. You feel... a connection. No, a web of connections. Recognition. You are a {color=#1C4587}{b}sheep{/b}{/color} to be herded. A {color=#1C4587}{b}pup{/b}{/color} to be corrected."
        
        
        if meat_eaten == True:
                #otherwise the tint stays if you click too fast or use skip function
                camera:
                        linear 1.0 matrixcolor TintMatrix("#fff")
                pause 1.0
                
                window auto show

                "You push away the sensation, quickly shut the window, and decide you'll deal with {i}that{/i} later."

                window auto hide
        else:
                menu:
                        "Go to bed.":
                                pause 0.3
                                #otherwise the tint stays if you click too fast or use skip function
                                camera:
                                        linear 1.0 matrixcolor TintMatrix("#fff")
                                pause 1.0
                                window auto show

                                "You push away the sensation, quickly shut the window, and decide you'll deal with {i}that{/i} later."

                                window auto hide

                        "Toss the meat to the dogs.":
                                $ dog_approval += 1
                                pause 0.3
                                window auto show

                                "You walk back to the bedside table and retrieve the plate of raw meat, before heaving the plate to toss the meat out the window."
                                
                                "The dogs rush towards the meat, tails wagging. You don’t know why, but you smile."

                                window auto hide

                                #otherwise the tint stays if you click too fast or use skip function
                                camera:
                                        linear 1.0 matrixcolor TintMatrix("#fff")

                                pause 1.0

        jump HeadtoBed

label HeadtoBed:
        #pause 0.3
        #otherwise the tint stays if you click too fast or use skip function
        camera:
                linear 1.0 matrixcolor TintMatrix("#fff")

        pause 1.0
        #choices converge here

        stop music fadeout 1.0
        stop crickets fadeout 2.5

        window auto show


        "A wave of exhaustion nearly buckles your knees. You stumble back towards the bed, barely feeling the soft caress of the pillow before everything goes dark."
        

        window auto hide
        #VSFX black screen
        scene bg color black with dissolve
        with Pause(2.0)

        #Move to failed rescue scene
        jump FailedRescueScene