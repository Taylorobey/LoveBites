label ConfrontationPlanningScene:

    #Image Captive Cabin Room (angled, zoomed in on ceiling)
    scene bg room ceiling with dissolve
    #VSFX Blur
    call WakeUpSequence2
    #Music Cabin
    play music cabin_music volume 0.3


    "You awake some hours before dawn, on the day of your meeting with Akari. For some minutes, you remain still, suspended in the quiet. It's not fatigue that holds you back, but a bittersweet nostalgia. It’s strangely comforting, these life-or-death stakes."

    if corruption > 2:
        "Perhaps being turned into a monster was just what you needed. Mundanity was driving you crazy, or more accurately, driving you into <blue>nothingness<blue>. The freedom to choose and act had lost its luster; It didn’t hold a candle to the crushing weight of reality."

    if humanity > 2:
        "Then again, best not to look upon the past with rose-tinted glasses. You know it’s dangerous to mistake routine for satisfaction. After all, that is in part what led you down this treacherous path. But, that’s <yellow>life<yellow>. You make mistakes. You try to learn from them. You keep moving forward."

    #Both of these could appear

    #VSFX Room (full view, getting up)
    scene bg room mc with dissolve
    pause(1.0)
    #SFX Walking
    play sound walk
    #Image Cabin Hall
    scene bg hallway with dissolve
    pause(1.0)
    #Image Stairs Down
    scene bg downstairs with dissolve
    pause(1.0)
    "Done with your musings, you rise from the bed. Downstairs, Ashina likely awaits, and you intend to speak with her before heading out. You've learned the hard way that careless departures can be costly. Now, each step is deliberate, weighed against the potential consequences."

    #Image Hearth
    stop sound fadeout 1.0
    show bg hearth with dissolve:
        subpixel True pos (1.44, 1.66) zoom 1.05
    show flame with dissolve:
        pos (0.59, 0.63) zoom 1.05
        #can't get this to match up juuust right

    #Image Ashina Neutral
    show ash neutral with dissolve:
        pos(0.11, 0.16) zoom 1.5

    #SFX Fireplace
    play sound fireplace

    "You find Ashina in the hearth, seated in one of the chairs, her gaze lost in the flickering flames. Her body subtly shifts when you approach, acknowledging your presence without looking at you."

    #if you told Ashina
    if aka_lock == True:

        ash "You’re off to your little rendezvous, yes? Good luck, and remember, I shall be nearby, should you have need of me."

        "Ashina's voice is serene, but her fingers betray her composure, tapping anxiously on the chair's arm."

        you "What about the dogs?"

        if dog_approval == 2:
            
            #Image Ashina Caring
            show ash caring with dissolve
            
            ash "I can tell they’ve grown fond of you. I doubt they will give you any trouble. If they do, simply call upon your connection to them, and you will be able to soothe them."

            "You give Ashina a skeptical look, not sure it’s as simple as she’s making it out to be."

            #Image Ashina Thoughtful
            show ash thoughtful with dissolve

            ash "Surely you’ve felt it by now. Not only your connection to them… but to me, as well. Trust me, you are capable of this. With time, you’ll be able to do much more amazing feats with our abilities."

            #Image Ashina Neutral
            show ash neutral with dissolve

            "She looks at you intensely, as if to prove her point. You feel a wave of confidence surge within you, washing away your doubt. It’s not the first time you’ve felt something like this."

            #Image Ashina Caring
            show ash caring with dissolve

            ash "Yes, I believe you understand. Go now, and know I will never be too far for you to reach."

        if dog_approval < 2:

            "Ashina doesn’t answer immediately, instead closing her eyes and taking long, deep breaths."

            #Image Ashina Thoughtful
            show ash thoughtful with dissolve

            ash "There, they shouldn’t bother you."

            you "How…?"

            #Image Ashina Neutral
            show ash neutral with dissolve

            ash "We have many abilities that you will come to understand, with time. Go now, and know I will never be too far for you to reach."

    else:
        #placeholder
        "you're not supposed to be here."
        "paths converge after here"

    #Paths converge

    #SFX Fireplace (fade out)
    stop sound fadeout 1.0
    #SFX Walking
    play sound walking
    #Music Eerie Outdoors
    play music eerie_outdoors_music
    #Image Cabin Ext. Leaving
    scene bg cabin ext dogs with dissolve
    pause(1.0)
    #Image Sky (bottom half)
    scene bg forest edge with dissolve

    "You depart the cabin and make your way to the forest’s edge. After standing there for a few minutes, you begin to wonder if Akari is even going to show up. Then, you hear her voice from somewhere within the shadows."

    aki "You made it. Good."

    "You’re not sure how Akari managed to evade your newly-keen senses, but considering her dedication, it makes sense that she would have honed her abilities. Akari leans out of her hiding spot, glancing side to side as if to make sure you’re alone."

    #Image Akari Neutral
    show aki neutral with dissolve

    aki "How did you get past the dogs? Did you figure out a way to deal with them?"

    if aka_lock:

        "You consider making something up, but decide that the best lie is the truth."

        if dog_approval == 2:

            you "They recognize me as one of their own now, I think. I don’t know how they’d react if you were with me, but I might be able to get them to stand down."

        else:

            you "I asked Ashina to call them off. She might do that for me again, but otherwise we’d probably just have to sneak past them somehow."

    else:
        #placeholder
        "you're not supposed to be here."

    #Paths converge

    #Image Akari Thoughtful
    show aki thoughtful with dissolve

    aki "I dislike going in without a guarantee… but we will have to make it work."

    #Image Akari Neutral
    show aki neutral with dissolve

    aki "Did you at least find out an angle to give us the upper hand? A weakness?"

    if aka_lock:
            
        "You let out what you hope to be a believably disappointed sigh."

        you "No, she wouldn’t tell me anything. I’m sorry."

        #Image Akari Frustrated
        show aki angry with dissolve

        aki "Seriously?"

        #VSFX Akari (as if pacing)
        show aki at pacing
        #i think she's facing the wrong way, not sure why


        "Akari paces back and forth, looking thoroughly frustrated."
        pause(1.0)
        show aki at stop_pacing
        "Akari paces back and forth, looking thoroughly frustrated.{fast} She stops abruptly, her eyes scanning you with scrutiny, her hand moving towards her bow. You get the feeling you should say something before she decides you’re dead weight."

        #Image Akari Neutral
        show aki neutral with dissolve
                    
        you "She didn’t tell me anything, but I think she’s fond of me, at least. Two against one is good odds, especially if she’s hesitating to hurt me."

        "You try to sound nonchalant, your heart beating hard in your chest. After a few more moments of staring at you, Akari relaxes, her hand moving away from her bow."

        #Image Akari Thoughtful
        show aki thoughtful with dissolve

        aki "True enough, that might be the best advantage we can get. Alright, meet me again at dusk, I need to prepare. Help me sneak in, and we will rid this world of that monster once and for all."

        "You wonder briefly why Akari is so hell-bent on killing Ashina. However, you’re lucky that the hooded woman hasn’t caught on to your little act. It’s not the time to go digging. Perhaps Ashina will have answers?"

        you "Got it."

        #VSFX Akari (fade out)
        hide aki with dissolve

        "You keep your answer short, worried anything else might betray a quiver in your voice. Akari disappears back into the foliage, and you’re once again left alone at the forest’s edge."

    else:
        #placeholder
        "you're not supposed to be here."

    #Paths converge

    #SFX Walking
    play sound walk
    #Image Cabin Etx. Returning (With Dogs)
    #Image Cabin Door Open
    scene bg door open with dissolve

    "You walk back to the cabin like you mean business, just in case Akari is still watching you."

    #Image Hearth
    stop sound fadeout 1.0
    scene bg hearth with dissolve:
        subpixel True pos (-0.07, -0.35) zoom 1.05
    show flame with dissolve:
        pos (0.59, 0.63) zoom 1.05
    #Music Eerier Outdoors (fade out)
    stop music fadeout 1.0
    #Music Cabin (fade in)
    play music cabin_music fadein 1.0
    #SFX Fireplace (fade in)

    "Once inside, you’re startled by Ashina rushing up to you. She briefly looks you over before speaking."

    #Image Ashina Neutral
    show ash neutral with dissolve:
        pos (0.35, 0.05) zoom 1.5

    ash "Well? How did it go?"

    you "I don’t think she suspects anything, and she wants me to sneak her in tonight." 

    "You pause, considering your next words carefully."

    you "Can I… ask you something?"

    "Ashina gives you an annoyed look."

    #Image Ashina Thoughtful
    show ash thoughtful with dissolve

    ash "Asking to ask a question is rather trivial. Out with it, girl."

    you "Do you know why Akari wants to kill you so badly?"

    #Image Ashina Sad
    show ash sad with dissolve

    "Her expression immediately falls."

    if ash_approval >= 4:
            
        ash "I am not proud of it, and I prefer not to speak of it. However…"

        #Image Ashina Caring
        show ash caring with dissolve

        ash "You deserve to know. I wish for you to understand me, and I would like to prevent you from repeating my mistakes."

        #Image Ashina Sad
        show ash sad with dissolve

        ash "As I have mentioned before, there is a beastly wolf within both of us. If we are not careful, extreme conditions or emotions can cause them to take over."

        #VSFX Ashina (slowly walking to the side)
        show ash sad:
            linear 4.0 xalign 1.0

        ash "It was a harsh winter, and I was young. I went without food in secret, so that there would be more left for my kin. I knew that it was foolhardy and reckless, but I thought myself strong enough to resist the wolf."

        #Image Ashina Thoughtful
        show ash thoughtful with dissolve

        ash "I wasn’t. The next thing I knew, I was hunched over the remains of a child, covered in his blood. I had consumed half of him before being able to stop myself."

        #Image Ashina Sad
        show ash sad with dissolve

        "You suck in a breath without meaning to, a sick feeling swirling within your stomach. Her eyes meet yours with a certain desperation, a tug at your heart begging you to let her in. So, you do."

        #VSFX Screen Shake (as if stumbling)
        #VSFX Blue (slowly tint)
        #Image Ashina Concerned (close up)

        "A wave of guilt and self-disgust hurls you forward. Deep, endless regret compresses your throat, causing you to cough and sputter. You barely feel Ashina catch your arms to keep you upright."

        #VSFX Blue (tint back to normal)

        "When the feeling passes, you find yourself amazed that Ashina could carry such overwhelming emotion and yet, still stand tall, still look so composed."

        #Image Ashina Caring

        ash "Now you understand."

        #Image Ashina Neutral

        ash "That little boy had a very determined sister, whom I’ve been evading ever since. She will stop at nothing to ensure my destruction, as is her right."

        you "Akari."

        "You mumble the name, and Ashina nods. She releases you, and you straighten back up."

        #Image Ashina Thoughtful (further away again)

        ash "Meet with her, and help her inside, as she asked. Then, I will face her, and give her the fight she deserves. What you do then, is up to you."

        #VSFX Ashina (fade out)

        "You’re still reeling when you realize Ashina is halfway up the stairs. You reach out, considering calling after her, but hesitate as your eyelids flutter with exhaustion. Perhaps a side effect of your strange Lycan abilities."

        #SFX Walking
        #Image Stairs Up

        "As you reach the stairs, you hear Ashina’s door close above. Left with your own churning thoughts and feelings, you make your way to bed."

        #If Ashina Approval < 4

            #Image Ashina Thoughtful (further away)

    ash "Yes…I know of Akari's motivations. It's nothing of your concern."

            #Image Ashina Neutral
            
    ash "You don't need all of the details. Just let her in, and I will take care of the rest." 

    you "But if I'm going to help her sneak in, I think I should know–"

    #VSFX Screen Shake
            #Image Ashina Angry Hybrid (closer)

    ash "I don't. Want. To talk about it! What about that don't you understand?!"
            
    "Ashina's chest heaves as she attempts to calm herself."

            #Image Ashina Sad (further again)

    ash "I apologize…I didn't mean to lash out like that. I need to be alone."

    "Ashina turns to leave, but not without a final word."

            #VSFX Ashina (further)

    ash "Tonight…Simply meet with Akari, and let her inside. I will confront her then. Join me in the fight, or don't. Just don't get in the way." 

    #VSFX Ashina (fade out)

    "You watch as Ashina climbs up the stairs. Soon, you hear her shut the door to her room."

    #SFX Walking
    #Image Stairs Up

    "Left with your own churning thoughts and feelings, you make your way to bed."

    return