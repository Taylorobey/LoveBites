label WhoYouAreScene:
        #stop audio from previous scene
        stop sound
        #VSFX blur
        #i put this before scene so it wouldn't be unblurred whilst the scene was being dissolved in
        camera:
                subpixel True blur 20.0 

        # image captive cabin room (angled, zoomed in on ceiling)
        scene bg room ceiling with dissolve
        #music cabin
        ### Need music for cabin

        #SFX crickets
        play sound crickets loop
        
        "When you next awake, something feels off. It only takes you a few moments to figure it out."

        #VSFX unblur (fade in-out as if waking up)
        #not sure if this is the right amount of blur since my placeholder is pretty low-res
        # Seems good to me, we will double check with Bizzy
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

        "You feel rested. No aches, no pains, a pleasant warmth radiating from within you. You can’t remember the last time you felt this good. But, there’s something else, too."

        # VSFX Red Flash (on the screen edges like a blooming pain)
        show pain:
                subpixel True
                alpha 0.0
                linear 0.5 alpha 1.0 
                linear 1.0 alpha 0.5
                linear 2.0 alpha 0.0

        "Hunger, and a buzzing energy in your skin, making you acutely aware of every movement and the sensation of the sheets around you. You know somebody is standing outside of the door to your room."

        # Image Captive Cabin Room (full view)
        scene bg room mc with dissolve

        "You sit up, and sure enough, the door opens and the woman steps in."

        # SFX Creak
        # VSFX Ashina (fade in)
        # Image Ashina Neutral

        ash "Come. It’s time we had a talk."

        # VSFX Ashina (fade out)

        "You’re not sure if you want to follow her, but it's not like you have much of a choice."

        # SFX Fade Out Crickets
        # SFX Walking
        # VSFX zooming and fading in and out of images as if walking through the cabin
        # Image Cabin Door Open
        # Image Cabin Hall
        # Image Cabin Hearth
        # SFX Fireplace

        "The woman leads you out of your room, down the stairs, and into a spacious hearth. The area is well adorned, equipped with ornate furnishings and a large fireplace to keep the place warm, and to cook with you suppose. Not that she used it."

        # VSFX Ashina (fade in)
        # Image Ashina Neutral

        "The woman stops and languidly gestures forward. You’re distracted by the muscles in her arm, the sight vivid and detailed in a way that’s unsettling. A loveseat made of furs and hides lies before you."

        ash "Well, don't just stand there. Sit."

        # VSFX Ashina (move center)

        "Suddenly feeling bold, you meet her gaze instead, your hands balling into fists."

        you "This is ridiculous. What do you want with me? I don’t even know who you are."

        # Image Ashina Friendly

        "There’s a glitter of amusement in her eyes, her lips twitching at a smirk."

        ash "Ashina. Now, best you listen, unless you’d rather I pay your friend a visit."

        # Change name to show ashina now that it's been revealed
        $ ash  = Character("Ashina", color="#1C4587")

        # VSFX Ashina (move lower and to the right corner, torso-up, as if viewing her across a table)

        "You sit. She glides toward the seat opposite you. A spread of elegantly plated slices of raw meat sits between the two of you. You could've mistaken it for a charcuterie board, if you didn’t know better."

        "The woman reaches forward and delicately plucks a slice of raw meat, before lowering it to her lips. She chews it as if it were soft as butter, her eyes burning into you with an intensity." 

        # VSFX Ashina (fade out)
        # VSFX Red Flash (on the screen edges like a blooming pain)
        # VSFX Zoom (as if looking down, at the table)

        "You avert your gaze to the raw meat on the table, and feel your mouth start to drool. Your pulse races as the bloody scent overpowers you. Your skin itches with a widespread pin-pricking sensation."

        # VSFX Screen Shake (like a shiver)

        you "What did you do to me…? I don't feel normal. Every little thing feels…"

        # VSFX Red (vision starts slowly tinting red)

        "Ashina’s voice sounds distant and muffled."

        ash "Overwhelming? Powerful? Perhaps even…Feral?"

        # VSFX Blur (as if lightheaded)

        you "Yes… And more. Make… Make it stop."

        ash "I figured as much."

        "You hear a distant sigh, and some movement. It’s hard to concentrate on anything but the-"

        ash "Take a deep breath and look at me."

        # Image Ashina Neutral (same torso-up-view as before)
        # Image Cabin Hearth (full view)
        # VSFX Effects gradually fade

        "You do so, and feel the sensations begin to subside. You feel as if you could get lost in her eyes, tumbling down into their depths, if you wanted to. You don’t. You definitely don’t."

        "Your captor stretches her arms out to her sides in a dramatic gesture."

        ash "Now, pay attention. I am going to explain how your life will be from now on, girl."

        ash "That is- What you have become, what you must do to survive, and why you can never return to your old life."

        # Image Ashina Hybrid Thoughtful

        ash "I am, and you are, lykánthrōpos, lycanthrope, or in layman's terms, werewolf. Descendants of witches, able to infect others with our so-called curse."

        ash "There are many historical accounts of our supposed origins, most claiming that our distant ancestors became as we are through acts of heinous depravity, usually related to the consumption of human flesh."

        ash "I have plenty of notes and readings on the subject that you will eventually be given access to, should you behave. Moving on."

        # Image Ashina Neutral
        # VSFX Ashina (move back to fullbody, center)

        "The woman stands, walking around you as she speaks."

        # VSFX Ashina (move from center to left)

        ash "We have heightened strength, senses, and connection with one another and canines. As the full moon approaches, we become closer to our beast, our wolf, and can change our skin with more ease."

        # Ashina (fade out)

        "Her hand runs along the back of your seat, nearly brushing your skin. It sends a shiver down your spine."

        ash "You will need to be trained to handle your beast, lest you be driven mad with hunger and rage. And trust me, pup, you do not want that to happen."

        # Image Ashina Neutral
        # VSFX Ashina (move in from the left, as if coming around from behind the MC’s seat)

        "She gives you a very serious, knowing look. Then, her features contort as you’ve seen once before."

        # Image Ashina Hybrid Angry
        # VSFX Ashina (move center)

        ash "We are carnivores. We crave raw meat like nothing else. Our emotions, like our senses, are heightened and must be kept in check."

        # VSFX Ashina (close to the screen/MC)

        "Her voice becomes more like a growl as she advances on you. You feel your breath catch in your throat."

        ash "And this is why we cannot be around people. The sight of us losing control for even a moment, or worse, the mistakes we make under the wolf’s influence, will be punished with death or torture."

        # VSFX Ashina (further)
        # Image Ashina Hybrid Thoughtful

        ash "There is ugliness in what we are, but there is beauty, too. You will know it when you feel the wind flowing through your fur, and find you are a part of something so much greater than yourself."

        # VSFX Ashina (back to fullbody center)
        # Image Ashina Neutral

        "She looks at you expectantly as she looms over you, and you realize she’s waiting for a response."

        menu: 
                # Ashina Approval Choice
                "Respond with appreciation.":
                        jump AppreciationResponse
                "Option Unavailable (Demo)":
                        return

label AppreciationResponse:                        
        $ ash_approval += 1
        "You nod slowly."

        you "You know, if I’m honest… I’ve always wanted to be part of something bigger than myself. For a long time I’ve felt… lost, I guess."

        you "I thought I knew what I wanted, but everything just ended up being so… hard. Weirdly, I feel more in control now than I have in a while."

        # Image Ashina Caring

        "Ashina’s gaze softens."

        ash "The world can be cruel. No matter how clear your vision for the future, reality wears you down over time."

        # Image Ashina Thoughtful

        ash "There used to be more of us, you know. Now I fear we may be the last. I, too, once had dreams. Those dreams died with my kin."

        # Image Ashina Neutral

        ash "But there is a strength that comes with acceptance. Change what you can, and accept what you cannot, I believe the saying goes."

        ash "Still… that doesn’t mean you cannot feel angry about it. The anger pushes us forward. That is its own kind of strength."

        # VSFX Ashina (back in the bottom right torso-up-view)

        "Ashina goes quiet, staring into the embers of the fireplace. For a moment, you feel an intense sorrow that ebbs and flows into a calm. You’re not sure how long the two of you sit there in reflective silence, but eventually, she rises."

        ash "I shall retire to my room. You may move about the cabin as you wish, but do stay inside."

        # VSFX Ashina (fade out)

        "With that, she leaves, taking the calm with her."

        jump BotchedEscapeScene

label DisgustResponse:
        #Ashina Disapproval Choice
        $ ash_approval -= 1
        # "Respond with disgust.":
        # "You glare."
        # you "I didn’t ask for this. I don’t want to be a monster. You want me to play nice? Forget it."
        # you "The only reason I’m even listening to you right now is because if I don’t, you’ll hurt Cameron. We don’t need to pretend this is anything it isn’t."
        # TBA
