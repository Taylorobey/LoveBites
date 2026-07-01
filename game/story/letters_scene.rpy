label LettersScene:
    $ save_name = "A Letter"

    window auto hide
    
    scene bg color black
    with Pause(0.5)
    #Image Captive Cabin Room (angled towards ceiling)
    #Music Cabin

    "You beeline towards the bed once you enter your room. As soon as your head hits the pillow, you already start to drift off…"

    call AsleepSequence
    call WakeUpSequence
    
    #SFX Arrow Hit
    play sound creak

    "Just as you're about to fall asleep, you hear a sharp whistle. A firm snap, like the cracking of bone, proclaims the splitting of wood outside the window. You crawl out of the bed to investigate."

    #SFX Walking
    #VSFX Zoom (towards window)
    #Image Window
    #SFX Dogs Barking

    window auto hide
    scene bg room mc with dissolve
    with Pause(0.5)
    play soundb barking volume 0.3 fadein 2.0 loop
    play sound walk loop
    show bg room mc at walk_to_window
    with Pause(1.2)
    stop sound
    window auto show

    "The dogs yap and jump up at the window, alarmed by the sudden commotion."

    show bg room mc open window with dissolve
    
    "You open the window, leaning out to get a better look. To the side of the window, you discover an arrow with a piece of paper bound to its shaft."

    "Your thoughts immediately turn towards that mysterious hooded woman in the woods."

    you "Could it be…?"

    #Image Captive Cabin Room (zoomed on window)
    #VSFX Zoom (up and down backwards motion as if stepping away from the window)

    stop soundb fadeout 2.0

    "You detach the arrow from the outer cabin wall and step back, closing the window. Unfurling the parchment reveals a letter written with distinct handwriting: large, cursive letters that border between meticulous and jagged."

    #Image Letter (centered in front of the captive cabin room bg)
    #VSFX Text (on screen in more of a letter format rather than in dialogue box)
    window auto hide
    show bg room mc with dissolve
    pause 0.5

    show bg color black onlayer screens:
                alpha 0.0
                zoom 2.5
                linear 1.0 alpha 0.8
    pause 1.2

    centered "To my unlikely ally…"

    centered "Since our strange meeting, I have kept a close eye on you. From afar. I see now that you are being held prisoner by that monster. I truly pity you, knowing what cruelties that creature is capable of."

    centered "It is my sole purpose to rid this world of her evil influence. As such, I am offering you a way out. A chance at redemption."

    centered "Let us meet in two days' time at the forest’s edge. We shall then devise a plan to kill your dark mistress."

    centered "In the meantime, you must gather intel for me. Find out any weaknesses your mistress has, and how those dogs outside the cabin can be dealt with. Earn the beast's trust, so that we may exploit it."

    if aka_approval < 1:
        centered "Your behavior the night we met was less than satisfactory. I hope for your sake it was a ruse, or a moment of weakness. Make no mistake: Your captor is a murderer, and she will make one of you as well."

        centered "This is your one, and only, chance. Prove your allegiance to humanity, or share your mistress’s fate."

    if corruption > 0:
        centered "Lastly, heed this. I have seen your struggle with the beast that that vile woman placed within you. Find it warning or comfort that if you do not keep it in check, I will not hesitate to strike you down."

    centered "Good luck. I will continue to watch over you until the time comes."

    centered "Sincerely…"

    #Image Letter (disappear, leaving the captive cabin room)

    show bg color black onlayer screens:
        subpixel True
        linear 1.0 alpha 0.0

    window auto show

    you "...Akari."

    "You turn the letter in your hands. With Akari's help, you have a way to actually, finally escape this cabin once and for all… if you want to."

    "Heavy footfalls interrupt your thoughts. You quickly hide the letter and arrow under your bed."

    scene bg room mc with dissolve

    jump ICanSeeTheStarsScene

