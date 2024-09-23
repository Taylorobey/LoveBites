label WhoYouAreScene:
        #stop audio from previous scene
        stop sound

        call WakeUpSequence1

        hide bg onlayer screens with Dissolve(2.0)

        "When you next awake, something feels off. It only takes you a few moments to figure it out."

        call WakeUpSequence2

        "You feel rested. No aches, no pains, a pleasant warmth radiating from within you. You can’t remember the last time you felt this good. But, there’s something else, too."

        call PainFlash
        play soundb heart
        with Pause(0.7)
        stop soundb fadeout 0.5

        "Hunger, and a buzzing energy in your skin, making you acutely aware of every movement and the sensation of the sheets around you. You know somebody is standing outside of the door to your room."

        stop soundb fadeout 0.5

        # Image Captive Cabin Room (full view)
        scene bg room mc with dissolve

        "You sit up, and sure enough, the door opens and your captor steps in."

        # VSFX Ashina (fade in)
        # Image Ashina Neutral
        show ash neutral with MoveTransition(1.0, enter=offscreenright)

        ash "Come. It’s time we had a talk."

        # VSFX Ashina (fade out)
        hide ash neutral with easeoutright

        "You’re not sure if you want to follow her, but it's not like you have much of a choice."

        window auto hide

        # SFX Fade Out Crickets
        stop crickets fadeout 1.0

        # SFX Walking
        play sound walk
        ## VSFX zooming and fading in and out of images as if walking through the cabin

        # Image Cabin Door Open
        show bg door open with dissolve:
                subpixel True
                zoom 1.0
                linear 2.00 zoom 2.0 yalign(0.5)
        with Pause(1.5)
        show bg door open:
                zoom 2.0 yalign(0.5)

        # Image Cabin Hall
        show bg hallway with dissolve:
                subpixel True 
                zoom 0.53
                linear 2.00 zoom 1.0 xalign(0.8) yalign(0.3)
        with Pause(1.5)
        show bg hallway:
                zoom 1.0 xalign(0.8) yalign(0.3)
        
        stop music fadeout 4.0

        play soundb fireplace volume 0.3 loop fadein 2.0

        # Image Downstairs
        show bg downstairs with dissolve:
                subpixel True
                zoom 1.0
                linear 2.00 zoom 2.0 xalign(0.5) yalign(0.01)
        with Pause(1.5)
        show bg downstairs:
                zoom 2.0 xalign(0.5) yalign(0.01)

        # Image Cabin Hearth
        show bg hearth with dissolve:
                subpixel True
                zoom 0.7
                pos(0.52,-0.2)

        window auto show

        stop sound fadeout 1.0
        "The woman leads you out of your room, down the stairs, and into a spacious hearth. The area is well adorned, equipped with ornate furnishings and a large fireplace to keep the place warm, and to cook with you suppose. Not that she used it."

        # VSFX Ashina (fade in)
        # Image Ashina Neutral
        ## change transform to have her standing in front of chair once hearth bg is done
        show ash neutral at center
        with dissolve

        "The woman stops and languidly gestures forward. You’re distracted by the muscles in her arm, the sight vivid and detailed in a way that’s unsettling. A loveseat made of furs and hides lies before you."

        ash "Well, don't just stand there. Sit."

        window auto hide
        show ash neutral at center:
                subpixel True
                linear 1.0 pos(0.55,1.75) zoom 1.83
        with Pause(1.0)
        show ash neutral:
                pos(0.55,1.75) zoom 1.83
        window auto show
        "Suddenly feeling bold, you meet her gaze instead, your hands balling into fists."

        you "This is ridiculous. What do you want with me? I don’t even know who you are."

        # Image Ashina Friendly
        show ash friendly with dissolve

        "There’s a glitter of amusement in her eyes, her lips twitching at a smirk."

        ash "Ashina. Now, best you listen, unless you’d rather I pay your friend a visit."

        window auto hide

        # Change name to show ashina now that it's been revealed
        $ ash  = Character("Ashina", color="#1C4587")

        hide ash friendly with dissolve

        # VSFX Ashina (move lower and to the right corner, torso-up, as if viewing her across a table)
        show bg hearth with dissolve:
                subpixel True
                zoom 0.7
                pos(0.52,-0.2)
                linear 1.0 zoom 1.05 pos(1.44, -0.33)
        with Pause(1.0)
        show bg hearth:
                subpixel True
                zoom 1.05 pos(1.44, -0.33)

        show ash friendly with dissolve:
                pos(0.63,0.12) zoom 1.83

        window auto show
        "You sit. She glides toward the seat opposite you. A spread of elegantly plated slices of raw meat sits between the two of you. You could've mistaken it for a charcuterie board, if you didn’t know better."

        "The woman reaches forward and delicately plucks a slice of raw meat, before lowering it to her lips. She chews it as if it were soft as butter, her eyes burning into you with an intensity." 

        play music eerie_outdoors_music

        # VSFX Ashina (fade out)
        hide ash friendly with dissolve
        # VSFX Red Flash (on the screen edges like a blooming pain)
        show pain onlayer screens:
                subpixel True
                alpha 0.0
                linear 0.5 alpha 1.0 
                linear 1.0 alpha 0.5
                linear 2.0 alpha 0.0
                repeat
        play sound heart loop

        # VSFX Zoom (as if looking down, at the table)
        window auto hide
        camera:
                subpixel True 
                pos (0, 0) zoom 1.0 
                linear 3.00 pos (-900, -912) zoom 1.62 
        with Pause(3.10)
        camera:
                pos (-900, -912) zoom 1.62 
        window auto show

        "You avert your gaze to the raw meat on the table, and feel your mouth start to drool. Your pulse races as the bloody scent overpowers you. Your skin itches with a widespread pin-pricking sensation."

        ## VSFX Screen Shake (like a shiver)
        window auto hide
        camera:
                subpixel True 
                linear 0.15 xpos -1000 
                linear 0.15 xpos -900 
                linear 0.15 xpos -1000 
                linear 0.15 xpos -900
        window auto show

        you "What did you do to me…? I don't feel normal. Every little thing feels…"

        # VSFX Red (vision starts slowly tinting red)
        show bg color red onlayer screens:
                alpha 0.0
                zoom 2.5
                linear 5.0 alpha 0.8

        "Ashina’s voice sounds distant and muffled."

        ash "Overwhelming? Powerful? Perhaps even… Feral?"

        # VSFX Blur (as if lightheaded)
        #camera:
                #subpixel True 
                #linear 1.00 blur 5.0 
                #linear 1.00 blur 15.0 
        ### for some reason the bg image crops during this?

        you "Yes… And more. Make… Make it stop."

        ash "I figured as much."

        "You hear a distant sigh, and some movement. It’s hard to concentrate on anything but the-"

        ash "Take a deep breath and look at me."

        stop sound fadeout 1.0

        # Image Ashina Neutral (same torso-up-view as before)
        # Image Cabin Hearth (full view)
        window auto hide
        camera:
                subpixel True 
                linear 2.0 pos (0, 0) zoom 1.0
        with Pause(2.0)
        show ash caring with dissolve:
                pos(0.5,0.22) zoom 1.8
        window auto show

        # VSFX Effects gradually fade
        camera:
                subpixel True 
                linear 3.00 blur 0.0
        show bg color red onlayer screens:
                subpixel True
                linear 3.0 alpha 0.0
        show pain onlayer screens:
                subpixel True
                linear 4.0 alpha 0.0
        
        stop music fadeout 3.0
        camera:
                subpixel True 
                pos (0, 0) zoom 1.0
        "You do so, and feel the sensations begin to subside. You feel as if you could get lost in her eyes, tumbling down into their depths, if you wanted to. You don’t. You definitely don’t."
        #need blue on "depths"

        "Your captor stretches her arms out to her sides in a dramatic gesture."

        show ash sadistic:
                subpixel True 
                xpos 0.5 
                linear 0.25 xpos 0.45 
                linear 0.25 xpos 0.55 
                linear 0.25 xpos 0.5 
        with Pause(0.85)
        show ash sadistic:
                xpos 0.5 

        ash "Now, pay attention. I am going to explain how your life will be from now on, girl."

        show ash friendly with dissolve

        ash "That is- What you have become, what you must do to survive, and why you can never return to your old life."

        # Image Ashina Hybrid Thoughtful
        show ash thoughtful with dissolve

        ash "I am, and you are, lykánthrōpos, lycanthrope, or in layman's terms, werewolf. Descendants of witches, able to infect others with our so-called curse."

        show ash sadistic with dissolve

        ash "There are many historical accounts of our supposed origins, most claiming that our distant ancestors became as we are through acts of heinous depravity, usually related to the consumption of human flesh."

        show ash friendly with dissolve

        ash "I have plenty of notes and readings on the subject that you will eventually be given access to, should you behave. Moving on."

        # Image Ashina Neutral
        # VSFX Ashina (move back to fullbody, center)
        show ash neutral with dissolve
        with Pause(0.5)
        show ash neutral:
                linear 1.0 pos(0.42,0.03) zoom 1.8

        "The woman stands, walking around you as she speaks."

        # VSFX Ashina (move from center to left)   
        show ash neutral:
                subpixel True ypos 0.03 
                xpos 0.42 
                linear 3.0 xpos -0.36

        ash "We have heightened strength, senses, and connection with one another and canines. As the full moon approaches, we become closer to our beast, our wolf, and can change our skin with more ease."

        with Pause(3.1)
        show ash neutral:
                pos (-0.36, 0.03)

        "Her hand runs along the back of your seat, nearly brushing your skin. It sends a shiver down your spine."

        show ash neutral:
                subpixel True ypos 0.03 
                xpos 0.96 
                linear 2.55 xpos 0.42 

        ash "You will need to be trained to handle your beast, lest you be driven mad with hunger and rage. And trust me, pup, you do not want that to happen."

        # Image Ashina Neutral
        # VSFX Ashina (move in from the left, as if coming around from behind the MC’s seat)
        with Pause(2.60)
        show ash neutral:
                pos (0.42, 0.03) 

        "She gives you a very serious, knowing look. Then, her features contort as you’ve seen once before."

        # Image Ashina Hybrid Angry
        # VSFX Ashina (move center)
        show ash angry hybrid with dissolve

        ash "We are carnivores. We crave raw meat like nothing else. Our emotions, like our senses, are heightened and must be kept in check."

        # VSFX Ashina (close to the screen/MC)
        show ash angry hybrid:
                subpixel True 
                xpos 0.42 zoom 1.8 
                linear 0.30 xpos 0.16 zoom 3.36 
        with Pause(0.40)
        show ash angry hybrid:
                xpos 0.16 zoom 3.36 

        "Her voice becomes more like a growl as she advances on you. You feel your breath catch in your throat."

        show ash thoughtful with dissolve

        ash "And this is why we cannot be around people. The sight of us losing control for even a moment, or worse, the mistakes we make under the wolf’s influence, will be punished with death or torture."

        # VSFX Ashina (further)
        # Image Ashina Hybrid Thoughtful
        show ash thoughtful:
                subpixel True
                linear 0.30 xpos 0.42 zoom 1.8
 
        ash "There is ugliness in what we are, but there is beauty, too. You will know it when you feel the wind flowing through your fur, and find you are a part of something so much greater than yourself."

        with Pause(0.40)
        show ash thoughtful:
                xpos 0.42 zoom 1.8

        # Image Ashina Neutral
        show ash neutral with dissolve

        "She looks at you expectantly as she looms over you, and you realize she’s waiting for a response."
        label WHOdemochoice:
                menu: 
                        # Ashina Approval Choice
                        "Respond with appreciation.":
                                $ ash_approval += 1
                                jump AppreciationResponse
                        #Ashina Disapproval Choice
                        "Option Unavailable (Demo)":
                                # "Respond with disgust. ":
                                $ ash_approval -= 1
                                jump DisgustResponse

label AppreciationResponse:                        
        "You nod slowly."

        you "You know, if I’m honest… I’ve always wanted to be part of something bigger than myself. For a long time I’ve felt… lost, I guess."

        you "I thought I knew what I wanted, but everything just ended up being so… hard. Weirdly, I feel more in control now than I have in a while."

        # Image Ashina Caring
        show ash caring with dissolve

        "Ashina’s gaze softens."

        ash "The world can be cruel. No matter how clear your vision for the future, reality wears you down over time."

        # Image Ashina Thoughtful
        show ash thoughtful with dissolve

        ash "There used to be more of us, you know. Now I fear we may be the last. I, too, once had dreams. Those dreams died with my kin."

        # Image Ashina Neutral
        show ash neutral

        ash "But there is a strength that comes with acceptance. Change what you can, and accept what you cannot, I believe the saying goes."

        # VSFX Ashina (back in the bottom right torso-up-view)
        show ash neutral:
                linear 1.0 pos(0.5,0.22) zoom 1.8

        ash "Still… that doesn’t mean you cannot feel angry about it. The anger pushes us forward. That is its own kind of strength."

        "Ashina goes quiet, staring into the embers of the fireplace. For a moment, you feel an intense sorrow that ebbs and flows into a calm. You’re not sure how long the two of you sit there in reflective silence, but eventually, she rises."

        show ash neutral:
                subpixel True
                linear 1.0 pos(0.42,0.03) zoom 1.8

        ash "I shall retire to my room. You may move about the cabin as you wish, but do stay inside."

        # VSFX Ashina (fade out)
        hide ash neutral with easeoutright

        "With that, she leaves, taking the calm with her."

        jump BotchedEscapeScene

label DisgustResponse:
        # "You glare."
        # you "I didn’t ask for this. I don’t want to be a monster. You want me to play nice? Forget it."
        # you "The only reason I’m even listening to you right now is because if I don’t, you’ll hurt Cameron. We don’t need to pretend this is anything it isn’t."
        # TBA
        narrator "Sorry, this option isn't available in the demo."
        jump WHOdemochoice
