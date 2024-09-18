label LettersScene:
    #Image Captive Cabin Room (angled towards ceiling)
    #Music Cabin
    #VSFX Blur (as if drifting asleep)

    "You beeline towards the bed once you enter your room. As soon as your head hits the pillow, you already start to drift off…"

    #VSFX Blur (to black, then as if waking up)
    #SFX Arrow Hit

    "Just as you're about to fall asleep, you hear a sharp whistle, and then the splitting of wood near your window. You crawl out of your bed to investigate."

    #SFX Walking
    #VSFX Zoom (towards window)
    #Image Window
    #SFX Dogs Barking
    #SFX Crickets

    "The dogs yap and jump up at the window as if something’s there. You open the window and lean out, looking around. To the side of the window, you discover an arrow with a piece of paper bound to its shaft."

    "Your thoughts immediately turn towards that mysterious hooded woman, with her bow and arrow."

    you "Could it be…?"

    #Image Captive Cabin Room (zoomed on window)
    #VSFX Zoom (up and down backwards motion as if stepping away from the window)
    #SFX Crickets (fade out)

    "You detach the arrow from the cabin wall, close the window, and unfurl the letter."

    #Image Letter (centered in front of the captive cabin room bg)
    #VSFX Text (on screen in more of a letter format rather than in dialogue box)

    "To my unlikely ally…"

    "Since our first meeting, I found myself intrigued by you. I have been keeping an eye on you from afar. From my understanding, you look to be a prisoner, and I know some of what that monster has subjected you to."

    "I offer you a way out and a chance at redemption. It is my sole purpose to rid this world of the evil that presides over you."

    "Let us meet in two days' time at the forest’s edge. We shall then devise a plan to kill your dark mistress."

    "In the meantime, you must gather intel for me. Find out any weaknesses your mistress has, and how those dogs outside the cabin can be dealt with. Earn the beast's trust, so that we may exploit it."

    if aka_approval > 1:
        "Your behavior the night we met was less than satisfactory. I hope for your sake it was a ruse, or a moment of weakness. Make no mistake: Your captor is a murderer, and she will make one of you as well."

        "This is your one, and only, chance. Prove your allegiance to humanity, or share your mistress’s fate."

    if corruption > 0:
        "I have seen, in your eyes, your struggle with the beast within you. Find it a warning or a comfort that if you do not keep it in check, I will not hesitate to do what must be done."

    "Good luck. I will continue to watch over you until the time comes."

    "Sincerely…"

    #Image Letter (disappear, leaving the captive cabin room)

    you "...Akari."

    "You turn the letter in your hands. With Akari's help, you have a way to actually, finally escape this cabin once and for all… if you want to."

    "Heavy footfalls interrupt your thoughts. You quickly hide the letter and arrow under your bed."

    jump ICanSeeTheStarsScene

