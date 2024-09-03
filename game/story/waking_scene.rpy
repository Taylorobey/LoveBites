label WakingScene:

        #VSFX blur
        #i put this before scene so it wouldn't be unblurred whilst the scene was being dissolved in
        camera:
                subpixel True blur 20.0 

        # image captive cabin room (angled, zoomed in on ceiling)
        scene bg room ceiling with dissolve

        #music cabin

        #SFX crickets
        play sound crickets loop
        
        "The cool evening breeze is the first thing you sense, then the chirping of crickets outside."

        #VSFX unblur (fade in-out as if waking up)
        #not sure if this is the right amount of blur since my placeholder is pretty low-res
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

        "Your eyes are welcomed by the interior of a log cabin. It almost feels like a peaceful evening at camp, that is if it weren't for…"

        #SFX bed creak
        #i don't know what a bed creak sounds like help

        #VFX red flash (on the edges)

        show pain:
                subpixel True
                alpha 0.0
                linear 0.5 alpha 1.0 
                linear 1.0 alpha 0.5
                linear 2.0 alpha 0.0

        "A stinging sensation fills your body as you attempt to sit up. Your fingers touch the tender wound on your shoulder, the bite from that…thing, yesterday. You hesitate to call it a wolf."

        #image captive cabin room (full view)
        scene bg room mc with dissolve

        "You take a glance at your immediate surroundings. The room is mostly bare. Some fake-looking flowers decorate the minimal furnishings."
        
        menu:
                "You regret what you wished for.":
                        $ humanity += 1
                        "Flirting with disaster finally caught up with you. What the hell were you thinking? You vow that if you ever escape this place, you're going to have a serious think about your life choices."
                "At least you won't have to go to work tomorrow.":
                        $ corruption += 1
                        "It’s a dark, bitter thought, but you can’t help it. There’s a reason you were outside that night, and now you’ve gotten what you wanted, right?"
        "You’re shaken from your thoughts by the sound of a door opening. A tall, muscular woman with tan skin enters the room."

        #VSFX ashina slides in from the right
        #image ashina neutral
        show ash neutral with MoveTransition(1.0, enter=offscreenright)
        ash "I see you're finally awake. Tell me, how was your slumber?"
        you "Who... who are you? Did you bring me here?"

        #VSFX ashina steps closer
        window auto hide
        show ash neutral:
                subpixel True xzoom 1.0 
                ypos 1.0 zoom 1.0 
                linear 1.00 ypos 2.0 zoom 2.0
        with Pause(1.00)
        window auto show

        ash "That's not what I asked you."
        
        #VSFX ashina steps back
        window auto hide
        show ash neutral:
                linear 1.00 ypos 1.0 zoom 1.0
        with Pause(1.00)
        window auto show

        ash "I'll ask again, how was your slumber?"
        you "Oh, well... Fine, I guess, all things considered."

        #image ashina friendly
        ash "Good, good."
        ash "Now, sit up properly. I've prepared a meal for you."

        #SFX stomach growl
        "Your stomach grumbles at the mere mention of food. You don't know what you're doing here, much less who this woman is, but you need something in your stomach {i}now{/i}."
        "You sit up. The woman reaches into the hallway, then sets a plate on the side table next to the bed."
        ash "Here. Eat to your heart's content."
        
        #music unsettling
        stop sound

        "On the plate is a pile of raw meat. Blood pools at the bottom of the chunks, and the stench of death reeks in the air."
        you "You can't be serious…There's no way I can eat that!"
        ash "Are you really so sure? Doesn't your hunger just feel..."

        #VSFX ashina close up
        window auto hide
        show ash neutral:
                subpixel True 
                ypos 1.0 zoom 1.0 
                linear 1.00 xpos 0.45 ypos 3.8 zoom 4.0 
        with Pause(1.0)
        window auto show

        ash "Unbearable?"
        "You take another look at the plate. You hate to admit it, but your stomach betrays you. You don't just {i}want{/i} to eat it..."

        #vsfx red flash on edges like a blooming pain
        #vsfx centered text, dim surroundings
        #text "YOU NEED TO EAT THE RAW MEAT."
        window auto hide
        image hungertext = Text("YOU {b}NEED{/b} TO EAT THE {b}{outlinecolor=#000}{color=#b70000}RAW MEAT.{/b}{/color}{/outlinecolor}", style="bigtext")
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
        
        ash "Ah, so you finally understand the gravity of the situation."
        ash "You must eat this meal, or the beast will take you."
        you "The beast? What does that mean?"
        you "Did you do something to me?"
        ash "Do not question me, simply do as I tell you. Eat."

        menu:
                "Eat Ashina's meal.":
                        $ corruption += 1
                        $ meat_eaten = True
                        "The meat is… surprisingly palatable. It has a deep, tender richness. You barely restrain yourself from stuffing your face ravenously. The clawing hunger soon subsides."
                        "You realize the woman has been watching you."
                        #image ashina friendly
                        ash "Good girl. Now, get some rest."
                "Abstain from eating.":
                        $ humanity += 1
                        "You turn away from the plate on the side table. Ashina sighs."
                        ash "You will need to eat eventually, girl, but I suppose I can allow you some time to adjust. Now, get some rest."
        
        hide ash with moveoutright
        #VSFX blur
        camera:
                linear 1.0 blur 20.0
        "Seemingly satisfied with the interaction, Ashina exits the room. You notice that despite a full day’s rest, you’re struggling to keep your eyes open."
        #VSFX return to normal
        camera:
                linear 1.0 blur 0.0
        "You force your eyes to focus. On the far wall, there is an open window. A possible escape route?"

        menu:
                "Examine the open window.":
                        #sfx walking
                        play sound walk
                        #slow zoom into window
                        window auto hide
                        show bg room mc:
                                subpixel True 
                                zoom 1.0 xpan 0.0 ypan 0.0 
                                linear 1.00 zoom 4.0 xpan 3.0 ypan -125.0 
                        with Pause(1.0)
                        window auto show
                        stop sound
                        "You approach the window, and a low rumbling shakes the floor."
                        #sfx dogs barking
                        play sound walk
                        play sound barking
                        #closer to window
                        window auto hide
                        show bg room mc:
                                subpixel True 
                                linear 1.00 zoom 5.0 xpan 3.0 ypan -135.0 
                        with Pause(1.0)
                        window auto show
                        "You inch ever closer, and you hear dogs begin to growl and bark wildly."
                        #image window no dogs
                        "You finally reach the window and take a peek outside..."
                        stop sound fadeout 1.0
                        #image window with dogs
                        "Countless dogs stare from the abyss into your eyes. However, unlike the commotion before, they are completely silent. Their gaze is unwavering and they stand unnaturally still."
                        "A strange sensation rises within you. You feel... a connection. No, a web of connections. Recognition. You are a {b}sheep{/b} to be herded. A {b}pup{/b} to be corrected."
                        if meat_eaten == True:
                                "You push away the sensation, quickly shut the window, and decide you'll deal with {i}that{/i} later."
                        else:
                                menu:
                                        "Go to bed.":
                                                "You push away the sensation, quickly shut the window, and decide you'll deal with {i}that{/i} later."
                                        "Toss the meat to the dogs.":
                                                $ dog_approval += 1
                                                "You walk back to the bedside table and retrieve the plate of raw meat, before heaving the plate to toss the meat out the window."
                                                "The dogs rush towards the meat, tail wagging. You don’t know why, but you smile."
                "Head to bed.":
                        #there wasn't anything written for this choice
                        pass
        return