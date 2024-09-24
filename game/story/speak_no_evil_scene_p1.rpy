label SpeakNoEvilSceneP1:
    #This scene triggers if you do not have -2 Approval with Ashina
    #stop audio from previous scene
    
    camera:
        subpixel True pos (0, 0) 

    stop sound

    call WakeUpSequence1

    #SFX Knock
    play sound knocking volume 1.5

    window auto show
    "You are woken up by a loud rapping at the door."

    call WakeUpSequence2

    #Image Captive Cabin Room (full view)
    scene bg room mc with dissolve

    stop sound

    #Image Ashina Caring
    show ash caring with easeinright

    window auto show

    ash "Did you have a restful slumber?"

    window auto hide

    #Image Ashina Neutral
    show ash neutral with dissolve

    window auto show

    "Ashina stands tall above your bed. There's a kindness in her eyes, which fades away quickly when she realizes you're staring."

    show ash thoughtful with dissolve

    ash "Don't get the wrong idea, pet. I haven't forgotten about your little escapade last night."

    hide ash thoughtful with easeoutright

    "She walks back out into the hall, gesturing for you to follow. You rise from the bed, and do so."

    window auto hide
    stop crickets fadeout 2.0
    play sound walk loop
    
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
    
    stop sound
    window auto show
    ash "But, it got me thinking. Perhaps it wasn’t that you were recklessly thinking of introducing lycanthropy to the masses. Perhaps you had a more altruistic motive."
    window auto hide
    
    play sound walk loop
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

    stop sound fadeout 1.0
    #Image Ashina Neutral (closer)
    show ash neutral with dissolve

    window auto show

    "Once you read the bottom of the stairs and step into the hearth, Ashina turns and steps close to you. Her eyes burn into you with a lingering question."

    #Image Ashina Thoughtful
    show ash thoughtful with dissolve

    ash "Not that you would have gotten very far before I caught you, but you get my point."

    #Image Ashina Caring
    show ash caring with dissolve

    ash "You were trying to get help for your friend, weren't you? You must be worried about them."

    #VSFX Ashina (further)
    show ash caring with dissolve

    ash "I'm not so cruel as to keep you two apart. I'll allow you a single visit."

    #Image Ashina Neutral
    show ash neutral with dissolve

    ash "...with some stipulations."

    "After last night, you figure it’s in your best interest not to argue."

    you "I'll do anything to see them again!"

    window auto hide
    #VSFX Ashina Friendly
    show ash sadistic with dissolve
    with Pause(1.0)
    #VSFX Ashina (closer)
    show ash sadistic:
        subpixel True 
        pos (0.5, 1.0)
        linear 0.50 pos (0.5, 2.0) zoom 2.0 
    with Pause(0.60)
    show ash sadistic:
        pos (0.5, 2.0) zoom 2.0 
    window auto show

    ash "Oh? Anything? Good. Listen carefully to my words, girl."

    #for testing
    #define ash_approval = 3

    if ash_approval >= 3:
        #nodding motion
        window auto hide
        show ash friendly:
            subpixel True 
            ypos 2.0 
            linear 0.15 ypos 2.03 
            linear 0.15 ypos 1.97 
            linear 0.15 ypos 2.0 
        with Pause(0.55)
        show ash friendly:
            ypos 2.0 
        window auto show

        ash "You have been quite obedient. It seems like you have a good head on those pretty little shoulders, as you clearly grasp the reality of your situation."

        #Image Ashina Caring
        show ash caring with dissolve

        ash "I appreciate that. I am not unreasonable, and I feel you’ve earned a reward. So, let's make a deal."

        #Image Ashina Thoughtful
        show ash thoughtful with dissolve

        "She speaks with such arrogance that one could easily miss the vulnerable glint in her eyes, and the slight shift in her posture. You briefly wonder how she might look without that carefully crafted mask of hers."

        #Image Ashina Neutral
        show ash neutral with dissolve 

        ash "I'll agree to let your friend go, and they will be free to return to their normal life."

        you "Really?!"

        you "Wait a minute, if you're willing to do that…You must want something. Something big."

        #Image Ashina Friendly
        show ash friendly with dissolve

        ash "Very clever of you, pet. But, it is just one simple condition."

        #Image Ashina Thoughtful
        show ash thoughtful with dissolve

        ash "Your friend may never speak of us Lycans once they leave here. Not to the authorities. Not to their family. Not to anyone. I- we- will lose everything if that happens."

        #VSFX blue screen tint (slowly fade in)
        #SFX Fire (slowly fade in)
        #SFX Howls (slowly fade in)
        camera:
                #matrixcolor TintMatrix("#1C4587")
                matrixcolor TintMatrix("#fff")
                linear 3.0 matrixcolor TintMatrix("#1C4587")
        play sound fireplace volume 2.5 fadein 3.0 loop
        play crickets mournfulhowls volume 0.2 fadein 3.0 loop
        play music connection_music volume 0.4 fadein 1.5

        "There’s a haunted look in her eyes. A {b}{color=#1C4587}memory{/b}{/color} tugs at the edge of your consciousness. Crackling fire and {b}{color=#1C4587}mournful{/b}{/color} howls. Bottomless agony, threatening to pull you {b}{color=#1C4587}under{/b}{/color}."

        show ash sad with dissolve

        ash "They'll burn everything to the ground. The cabin. The dogs. You, over my dead body."

        #VSFX Blue (fade out)
        #SFX Fire and Howls (fade out)
        pause(0.5)
        #otherwise the tint stays if you click too fast or use skip function
        camera:
                linear 1.0 matrixcolor TintMatrix("#fff")
        stop sound fadeout 3.0
        stop crickets fadeout 3.0
        stop music fadeout 2.5

        "Just like that, the feelings fade, leaving you a bit disoriented."

        #Image Ashina Neutral
        show ash neutral with dissolve

        ash "This is my home. The land of my people. All that I have left of them… Do you understand?"

    else:
        # Placeholder for the Cameron dies or becomes a Lycan paths
        hide placeholder

    # Paths converge here - 

    you "I… I understand. I'll do my best to convince Cameron."

    you "But, if I can't…What are you going to do to them?"

    #Image Ashina Thoughtful
    show ash thoughtful with dissolve

    ash "If they refuse to cooperate, I will do what must be done."

    you "You don't mean that you'll…?"

    #Image Ashina Neutral
    show ash neutral with dissolve

    "Ashina gives you a meaningful look, and your stomach sinks. She hands you a key."

    show ash neutral:
        subpixel True 
        pos (0.5, 2.0)
        linear 0.50 pos (0.5, 1.0) zoom 1.0 
    with Pause(0.60)
    show ash neutral:
        pos (0.5, 1.0) zoom 1.0 
    window auto show

    ash "Now, go to them. Descend from the hearth, and you shall find them in the basement. I will be waiting at the top of the stairs."

    you "Wait! Isn’t there-"

    #VSFX Ashina Hybrid Angry
    show ash angry hybrid with dissolve

    ash "Go. Before I change my mind. Surely, you can convince them of something so simple."

    window auto hide
    #VSFX Ashina (fade out)
    hide ash angry hybrid with dissolve

    #SFX Walking
    play sound walk loop

    show bg downstairs with dissolve:
        subpixel True zoom 1.0 pos (0.5, 0.01) 

    with Pause(1.0)
    stop sound
    window auto show
    "She gives you a light push towards the stairs, and you can tell that the conversation is over. Your heart beats in anticipation as you descend."

    window auto hide
    play sound walk loop
    # Image Downstairs
    show bg downstairs:
        subpixel True
        zoom 1.0
        linear 2.00 zoom 2.0 xalign(0.5) yalign(0.01)

    show bg color black with Dissolve(3.0)


    window auto show

    you "That's easy for her to say… She doesn't know how stubborn Cameron can be."

    pause(0.5)
        #just in case the tint stays if you click too fast or use skip function
    camera:
        linear 1.0 matrixcolor TintMatrix("#fff")

    stop sound
    stop soundb fadeout 1.0

    jump SpeakNoEvilSceneP2
