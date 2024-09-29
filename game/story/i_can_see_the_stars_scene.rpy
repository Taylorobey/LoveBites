label ICanSeeTheStarsScene:
    $ save_name = "I Can See The Stars"
    $ ash.name = "Ashina"

    window auto hide
    
    #Flags: Key information to defeating Ashina, or betraying Akari and preparing Ashina for the confrontation, or neither. Increased Humanity or Corruption.

    #Image Cabin Door Open
    pause 1.0
    show bg door open with dissolve:
        subpixel True xzoom 1.0 yzoom 1.0
    pause 0.5
    show ash neutral with dissolve:
        subpixel True pos(0.3,0.03) zoom 1.5 

    window auto show

    "The door to your room opens, with Ashina's stance taking up the whole frame."

    show ash thoughtful with dissolve

    ash "Are you ready as I asked, pup? You could stand to go outside for a spell, and I’d much rather you do so with supervision this time."

    window auto hide
    hide ash thoughtful with dissolve

    if ash_approval >= 0:
        window auto show
        "You aren’t about to look a gift horse… well, wolf in the mouth. Some fresh air does sound nice."

        window auto hide

        play sound walk loop
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

        # Image Downstairs
        show bg downstairs with dissolve:
            subpixel True
            zoom 1.0 xalign(0.5) yalign(0.01)
            linear 2.00 zoom 2.0 xalign(0.5) yalign(0.01)
        with Pause(1.5)
        show bg downstairs:
            zoom 2.0 xalign(0.5) yalign(0.01)

        # Image Cabin Hearth
        show bg hearth with dissolve:
            subpixel True
            zoom 0.7 pos(0.52,-0.2)
            linear 2.0 xpos -0.0 
        with Pause(2.0)
        show bg hearth:
            pos(-0.0,-0.2)
        
        show bg door open with dissolve:
            subpixel True
            zoom 1.0 pos(0.5,0)
            linear 2.00 zoom 2.0 yalign(0.5)
        with Pause(1.5)
        show bg door open:
            zoom 2.0 yalign(0.5)

        play crickets crickets volume 1.5 fadein 1.5

        show bg forest edge with dissolve:
            subpixel True 
            pos (0.5, 0.0)
            xzoom 1.0 yzoom 1.0
            zoom 1.0

        stop sound
        window auto show


        "You follow Ashina down the stairs, through the hearth, and out to the forest’s edge. The chilly air caresses your skin, and you instinctively relax."

    else:
        you "I don't want to go outside. I've been through enough already tonight, I'm so tired…"

        #Image Ashina Hybrid Angry
        show ash annoyed with dissolve

        ash "I wasn't making a request. It will only be for a brief moment, so quit your whining."

        hide ash annoyed with dissolve

        "Ashina grabs your wrist, and you can only resign yourself to being dragged along. "

        window auto hide

        play sound walk loop
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

        # Image Downstairs
        show bg downstairs with dissolve:
            subpixel True
            zoom 1.0 xalign(0.5) yalign(0.01)
            linear 2.00 zoom 2.0 xalign(0.5) yalign(0.01)
        with Pause(1.5)
        show bg downstairs:
            zoom 2.0 xalign(0.5) yalign(0.01)

        # Image Cabin Hearth
        show bg hearth with dissolve:
            subpixel True
            zoom 0.7 pos(0.52,-0.2)
            linear 2.0 xpos -0.0 
        with Pause(2.0)
        show bg hearth:
            pos(-0.0,-0.2)
        
        show bg door open with dissolve:
            subpixel True
            zoom 1.0 pos(0.5,0)
            linear 2.00 zoom 2.0 yalign(0.5)
        with Pause(1.5)
        show bg door open:
            zoom 2.0 yalign(0.5)

        play crickets crickets volume 1.5 fadein 1.5

        show bg forest edge with dissolve:
            subpixel True 
            pos (0.5, 0.0)
            xzoom 1.0 yzoom 1.0
            zoom 1.0

        stop sound
        window auto show

        "She leads you down the stairs, through the hearth, and outside. The bitter chill of the late night air stings your skin."
    
    "The dogs outside the cabin are docile for once. Some are asleep together in a cuddle pile, while others play-fight with another, letting out happy little growls and barks."
    
    #for testing
    #define dog_approval = 1

    if dog_approval > 0:
        window auto hide
        #Image Friendly Dog
        show dog with dissolve
        window auto show

        "A few of the dogs approach you happily, tails wagging. They seem friendly."
        
        window auto hide
        hide dog with dissolve

        menu:
            #Ashina/Dogs Approval Choice
            "Pet the dogs.":
                #Increases Ashina’s Approval
                #Increases Dogs’ Approval
                $ ash_approval += 1
                $ dog_approval += 1
                pause 0.3

                #Image Happy Dog
                show happy dog with dissolve

                window auto show

                "You decide to lean down and pet them. Their tongues loll out happily as they jostle one another for your affections. You catch Ashina smiling fondly in the corner of your eye."
                
                window auto hide
                #VSFX Dog (fade out)
                hide happy dog with dissolve
                #Image Ashina Caring
                #VSFX Ashina (fade out)
                

            #Neutral Choice
            "Ignore the dogs.":
                pause 0.3
                #VSFX Dog (fade out)
                hide dog with dissolve
                window auto show

                "You avert your eyes from the dogs and they soon lose interest. You catch Ashina staring cooly at you, her expression unreadable."

                window auto hide
                #Image Ashina Neutral
                #VSFX Ashina (fade out)
    
    #SFX Walking
    #Image Forest Edge (bottom half of black and white sky image)
    #"Ashina leads you further from the cabin, up to the forest’s edge."

    #Image Ashina Thoughtful
    show ash thoughtful with easeinright

    window auto show
    ash "It's a beautiful night out, isn't it?"

    #Image Ashina Caring
    show ash caring with dissolve

    ash "I've been waiting for a chance to show you the view of the stars here. I find it relaxing, and was hoping it'd help you feel the same."

    #Image Ashina Neutral
    show ash neutral with dissolve
    #VSFX Ashina (closer)

    ash "Tell me, what do you think?"

    window auto hide
    #VSFX Ashina (fade out)
    hide ash neutral with dissolve
    #VSFX Pan Up (Pan sky image up so that it’s the top half of the image, then fade in the colored version)
    #Image Sky Color
    #Music Starry Sky
    stop crickets fadeout 1.5
    camera:
        subpixel True
        pos (0, 0) 
        linear 4.5 pos (0, -1080) 
    play music starry_music volume 0.5 fadein 5.0
    show sky_color with Dissolve(4.0)
    with Pause(1.0)
    show starryeffect onlayer screens with Dissolve(4.0)
    with Pause(4.0)
    camera:
        pos (0, -1080)

    window auto show

    "You turn your gaze to the sky above. You don’t remember the last time you were far enough from the city to be able to see the stars. They twinkle brightly, stretching endlessly across the horizon."

    "You think the view is…"

    window auto hide

    menu:
        #Humanity Choice
        "Breathtaking.":
            pause 0.3
            $ humanity += 1
            you "..."

            window auto hide
            image stars 1 = Text("Looking at the brilliant ocean of stars above makes you realize something.", style = "skytext")
            show stars 1 with dissolve
            pause(10.0)
            hide stars with dissolve
            pause(0.5)

            image stars 2 = Text("All this time, you've felt trapped and hopeless.", style = "skytext")
            show stars 2 with dissolve
            pause(10.0)
            hide stars with dissolve
            pause(0.5)

            image stars 3 = Text("You've felt as though your life were meaningless.", style = "skytext")
            show stars 3 with dissolve
            pause(10.0)
            hide stars with dissolve
            pause(0.5)

            image stars 4 = Text("You’ve felt as though things would never get better, no matter what you did.", style = "skytext")
            show stars 4 with dissolve
            pause(10.0)
            hide stars with dissolve
            pause(0.5)

            image stars 5 = Text("Every day was a steady current, threatening to drag you under.", style = "skytext")
            show stars 5 with dissolve
            pause(10.0)
            hide stars with dissolve
            pause(0.5)

            image stars 6 = Text("In all your turmoil, you forgot something.", style = "skytext")
            show stars 6 with dissolve
            pause(10.0)
            hide stars with dissolve
            pause(0.5)

            image stars 7 = Text("Something everyone knows when they’re young and ends up forgetting.", style = "skytext")
            show stars 7 with dissolve
            pause(10.0)
            hide stars with dissolve
            pause(0.5)

            image stars 8 = Text("There is so much beauty to be found in the world around you.", style = "skytext")
            show stars 8 with dissolve
            pause(10.0)
            hide stars with dissolve
            pause(0.5)

            image stars 9 = Text("Even in the bleakest life, if you simply stop and look, you can find hope. Wonder. Happiness. A reason to keep on living.", style = "skytext")
            show stars 9 with dissolve
            pause(10.0)
            hide stars with dissolve
            pause(0.5)

            image stars 10 = Text("The thought brings tears to your eyes, emotions welling up within you.", style = "skytext")
            show stars 10 with dissolve
            pause(10.0)
            hide stars with dissolve
            pause(0.5) 

            image stars 11 = Text("How lucky you are, right here, right now, to be alive.", style = "skytext")
            show stars 11 with dissolve
            pause(10.0)
            hide stars with dissolve
            pause(0.5)

        #Corruption Choice
        "Depressing.":
            pause 0.3
            $ corruption += 1
            you "..."

            window auto hide
            image skies 1 = Text("Looking at the vast, dotted void above fills you with a profound emptiness.", style = "skytext")
            show skies 1 with dissolve
            pause(10.0)
            hide skies with dissolve
            pause(0.5)

            image skies 2 = Text("The view reminds you of how small you are in the grand scheme of the universe.", style = "skytext")
            show skies 2 with dissolve
            pause(10.0)
            hide skies with dissolve
            pause(0.5)

            image skies 3 = Text("How meaningless you are to those celestial bodies in the sky.", style = "skytext")
            show skies 3 with dissolve
            pause(10.0)
            hide skies with dissolve
            pause(0.5) 

            image skies 4 = Text("How you yearn to be as free, as grand, as beautiful as they are.", style = "skytext")
            show skies 4 with dissolve
            pause(10.0)
            hide skies with dissolve
            pause(0.5) 

            image skies 5 = Text("Try as you may, these things will always be out of your reach.", style = "skytext")
            show skies 5 with dissolve
            pause(10.0)
            hide skies with dissolve
            pause(0.5)

            image skies 6 = Text("Your life is insignificant.", style = "skytext")
            show skies 6 with dissolve
            pause(10.0)
            hide skies with dissolve
            pause(0.5)

            image skies 7 = Text("You are insignificant.", style = "skytext")
            show skies 7 with dissolve
            pause(10.0)
            hide skies with dissolve
            pause(0.5)

            image skies 8 = Text("But, that's a comfort in and of itself.", style = "skytext")
            show skies 8 with dissolve
            pause(10.0)
            hide skies with dissolve
            pause(0.5) 

            image skies 9 = Text("Nothing really matters, so you can do whatever you want with your life.", style = "skytext")
            show skies 9 with dissolve
            pause(10.0)
            hide skies with dissolve
            pause(0.5)

            image skies 10 = Text("Everything. Anything. Nothing at all. It's all the same in the end.", style = "skytext")
            show skies 10 with dissolve
            pause(10.0)
            hide skies with dissolve
            pause(0.5)

            image skies 11 = Text("You take in a deep breath, releasing the negative energy within you.", style = "skytext")
            show skies 11 with dissolve
            pause(10.0)
            hide skies with dissolve
            pause(0.5)

            image skies 12 = Text("How strangely comforting it is, accepting your place within the universe.", style = "skytext")
            show skies 12 with dissolve
            pause(10.0)
            hide skies with dissolve
            pause(0.5)
    
    #VSFX Pan (pan down to show the treeline)
    #Image Ashina Thoughtful (fade in)
    hide starryeffect onlayer screens with dissolve
    camera:
        subpixel True
        pos (0, -1080) 
        linear 4.5 pos (0, 0)
    show ash thoughtful
    pause(4.5)

    ash "Speechless, are you? I can't say I blame you."

    you "Ashina…"

    #Image Ashina Neutral
    show ash neutral with dissolve

    ash "What is it?"

    window auto hide

    label starsdemochoice:
        menu:
            #Ashina Route Choice
            "There is someone after you.":
                #Locks you out of Akari’s route.
                #Increases Ashina Approval
                $ ash_approval += 1
                $ aka_lock = True
                window auto show

                you "I need to tell you something. Someone is after you. The other night-"

                #Image Ashina Friendly
                show ash friendly with dissolve

                ash "What, that little miscreant in the woods? I’ve been giving her the run around for years, don’t you fret your little head about it."

                #Image Ashina Concerned
                show ash friendly with dissolve

                "Ashina waves a hand dismissively, but you catch her arm and look at her meaningfully. It gives her pause enough for you to carry on."

                you "The other night, when… I went outside against your wishes…"

                #Image Ashina Neutral
                show ash neutral with dissolve

                you "I met a huntress armed with a bow and arrow, who I now know is named Akari. She shot a note up to my window earlier tonight, asking to meet in two days’ time, and told me she intends to kill you, Ashina. Soon."

                #Image Ashina Thoughtful
                show ash thoughtful with dissolve

                ash "Hm, I'd like to see her try. She's delusional if she thinks she can take me down. I will devise a way to deal with her, don’t you worry. I have no need- hm."
                
                "Ashina pauses, as if reconsidering her words. The arrogant atmosphere around her melts away, and she visibly softens. She takes a breath before meeting your gaze."

                #Image Ashina Caring
                show ash caring with dissolve

                ash "Forgive me. I… appreciate you telling me this. I am glad I arrived that night before the huntress could do you any harm. My heart could not bear to lose yet another… of my kin."

                "You weren't prepared for Ashina to be so…caring towards you. You feel heat rise to your cheeks and instinctively look away before speaking again."

                you "What should I do about the meeting then? Akari will be expecting me."

                #Image Ashina Thoughtful
                show ash thoughtful with dissolve

                ash "Hm… Meet with her. Best she doesn’t know that anything is amiss. Learn her plan, and then we can prepare accordingly."

                #Image Ashina Neutral
                show ash neutral with dissolve

                ash "You shouldn't be in any danger if she has no reason to believe you'll betray her. However… If something happens, call out to me, and I will come to your aid."
            #Akari Route Choice
            "Option not available. (demo)":
                jump demoroute
            #Neutral/Cameron Route Choice
            "Option not available. (demo)":
                jump demoroute

    #VSFX Ashina (fade out)
    #VSFX Pan (pan back up to the sky)
    camera:
        subpixel True
        pos (0, 0) 
        linear 4.5 pos (0, -1080)
    pause(4.5)

    if ash_approval >= 3:
        "Ashina moves closer to you, her hand slowly hooking around your upper arm. There’s a pause, then her head comes to rest on your shoulder, just as cautious as her hand."

        "It’s a profound show of intimacy, and it takes you off guard. You can’t help but feel that, at this moment, Ashina seems more like a flighty fawn than the intimidating beast from the alleyway."

        "You find yourself leaning just slightly into her touch, and you feel the tension in her body begin to ease, little by little. You glance to the side, wishing you could see her expression from this angle, but quickly avert your eyes when she suddenly speaks."

        ash "If I may confess something to you, pup…"

        ash "I think I have been lonely for a long, long time."

        ash "I usually avoid the city, but I found myself wandering the streets more often than I should these past few months. The first night I saw you I thought you reckless, and began to watch over you for your own good."

        ash "I grew accustomed to our walks. Some nights later, I decided I must have you. I reasoned to myself that it was the perfect opportunity, that it was my duty to continue the Lycan bloodline, but…"

        ash "If I am honest, that is only half the truth."

        ash "I know that none of this was your choice, and I regret that my situation prevented me from being able to give you a gentler introduction into this life. I hope in time you can come to understand my position."

        ash "Regardless, I need you to know this: I did not bring you here to suffer. With time, I intend to show you all of the joy and freedom that comes with our so-called curse. Stay by my side, and I will protect you for as long as I live. I promise you that."

    ash "Let us continue our stargazing in silence. We can go back inside whenever you are ready."
    
    you "..."

    #Music Starry Sky (fade out)
    #Image Sky (fade back to no color, then scene fade to black)

    window auto hide
    with Pause(1.5)
    
    show thanks with Dissolve(2.0):
        subpixel True pos (0.16, -0.58) 

    with Pause(3.0)
    hide thanks with dissolve

    $ credits_speed = 25 #scrolling speed in seconds
    pause(0.5)
    show cred at Move((0.5, 3.1), (0.5, -1.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    pause(credits_speed)

    hide sky_color with dissolve
    hide starryeffect onlayer screens with dissolve
    show bg color black with dissolve:
        pos (0.5,-0.5)
    stop music fadeout 2.0
    stop sound fadeout 2.0
    stop soundb fadeout 2.0
    stop crickets fadeout 2.0
    with Pause(2.5)

    return

label demoroute:
    narrator "Sorry, this option isn't available in the demo."
    jump starsdemochoice







