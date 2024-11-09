label ConfrontationPlanningScene:

    #testing defines
    #define corruption = 3
    #define humanity = 3
    #define aka_lock = False
    #define aka_approval = 2
    #define ash_approval = 3

    #Image Captive Cabin Room (angled, zoomed in on ceiling)
    scene bg room ceiling with dissolve
    #VSFX Blur
    call WakeUpSequence2
    #Music Cabin
    play music cabin_music volume 0.3


    "You awake hours before dawn, on the day of your meeting with Akari. For some minutes, you remain still, suspended in the quiet. It's not fatigue that holds you back, but a bittersweet nostalgia. It’s strangely comforting, these life-or-death stakes."

    if corruption > 2:
        "Perhaps being turned into a monster was just what you needed. Mundanity was driving you crazy, or more accurately, driving you into {color=#1C4587}{b}nothingness{/b}{/color}. The freedom to choose and act had lost its luster; It didn’t hold a candle to the crushing weight of reality."

    if humanity > 2:
        "Then again, best not to look upon the past with rose-tinted glasses. You know it’s dangerous to mistake routine for satisfaction. After all, that is in part what led you down this treacherous path. But, that’s {color=#ffff00}{b}life{/b}{/color}. You make mistakes. You try to learn from them. You keep moving forward."

    #Both of these could appear

    #VSFX Room (full view, getting up)
    scene bg room mc with dissolve
    pause(1.0)
    
    "Done with your musings, you rise from the bed. Downstairs, Ashina likely awaits, and you intend to speak with her before heading out. You've learned the hard way that careless departures can be costly. Now, each step is deliberate, weighed against the potential consequences."

    call GoToHearth

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

    "You find Ashina in the hearth, seated in one of the chairs, her gaze lost in the flickering flames. Her body subtly shifts when you approach, acknowledging your presence without looking at you."

    #if you told Ashina
    if aka_lock == True:

        "You linger for a moment, admiring the way the firelight dances over her form."

        you "Good evening. How are you feeling?"

        show ash friendly with dissolve

        "Ashina leans her head back against the chair, peering up at you. She seems relaxed, despite the situation. Like the calm before the storm. You can’t help but be comforted by her unwavering strength."

        show ash sadistic with dissolve

        ash "Just fine, pup. I’ve found the cabin a bit more lively these past few nights."

        show ash friendly with dissolve

        "She smirks in a charming fashion, and your heart flutters."

        show ash neutral with dissolve

        ash "You’re off to your little rendezvous, yes? Good luck, and remember, I shall be nearby, should you have need of me."

        "Ashina's voice is serene, but her fingers betray her composure, tapping anxiously on the chair's arm."

        you "What about the dogs?"

    else:
        "You linger for a moment, watching her, considering your words carefully."

        you "Good evening. Are you… feeling well?"

        show ash friendly with dissolve

        "Ashina leans her head back against the chair, peering up at you. Though her body language is relaxed, you can’t help but still feel a bit intimidated. The woman just has a certain air about her."

        show ash sadistic with dissolve

        ash "Just fine, pup. I’ve found the cabin a bit more lively these past few nights."

        show ash friendly with dissolve

        "She smirks in a way that you might find charming, if it weren’t for your situation. Instead, you see through the playfulness to something more sinister, a predator toying with its prey. You force a smile."

        you "Yes, well… It is a lovely home. I have to admit, though, I'm feelong a bit cooped up. It’s driving me crazy."

        show ash neutral with dissolve

        "Ashina stares at you unblinkingly, her expression unreadable. You shift nervously."

        you "I… was wondering if you might allow me a short walk outside the cabin."

        "Ashina continues to stare. With each long moment, your anxiety grows. You feel something. A presence, pushing in. You focus your thoughts on your desire for fresh air. Perhaps if you think about it, you’ll look more convincing."

        show ash thoughtful with dissolve

        "Ashina’s intense gaze finally releases you, returning to the fire."

        ash "Very well, but you must stay in sight of the cabin. Should I lose sight of you, I promise you will not enjoy the consequences."

        show ash neutral with dissolve

        "You brighten up immediately, feeling lighter on your feet. You did it. One step closer to freedom."

        you "Thank you, I really appreciate it."

        "You almost turn to leave, then remember something."

        you "Um… the dogs won’t attack me, will they?"


    #Paths converge

    if dog_approval == 2:
            
        #Image Ashina Caring
        show ash caring with dissolve
            
        ash "I can tell they’ve grown fond of you. I doubt they will give you any trouble. If they do, simply call upon your connection to them, and you will be able to soothe them."

        "You give Ashina a skeptical look, not sure it’s as simple as she’s making it out to be."

        #Image Ashina Thoughtful
        show ash thoughtful with dissolve

        ash "Surely you’ve felt it by now. Not only your {color=#1C4587}{b}connection{/b}{/color} to {i}them…{/i} but to me, as well. Trust me, you are capable of this. With time, you’ll be able to do much more amazing feats with our abilities."

        #Image Ashina Neutral
        show ash neutral with dissolve

        "She looks at you intensely, as if to prove her point. You feel a wave of {color=#1C4587}{b}confidence{/b}{/color} surge within you, washing away your doubt. It’s not the first time you’ve felt something like this."

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


    #SFX Fireplace (fade out)
    stop sound fadeout 1.0
    #SFX Walking
    play sound walking
    #Music Eerie Outdoors
    play music eerie_outdoors_music fadein 1.0
    play crickets crickets fadein 1.0 loop
    #Image Cabin Ext. Leaving
    scene bg cabin ext dogs with dissolve
    pause(1.0)
    #Image Sky (bottom half)
    show bg forest edge:
        subpixel True pos (1.37, 2.2) zoom 2.74
    show fog onlayer screens:
        alpha 0.75
    stop sound

    "You depart the cabin and make your way to the forest’s edge. After standing there for a few minutes, you begin to wonder if Akari is even going to show up. Then, you hear her voice from somewhere within the shadows."

    aki "You made it. Good."

    "You’re not sure how Akari managed to evade your newly-keen senses, but considering her dedication, it makes sense that she would have honed her abilities. Akari leans out of her hiding spot, glancing side to side as if to make sure you’re alone."

    #Image Akari Neutral
    show aki neutral:
        subpixel True pos (0, 0) zoom 2.5
    with dissolve

    aki "How did you get past the dogs?"

    if aka_lock:

        show bg forest edge:
            subpixel True ypos 2.2 zoom 2.74 
            xpos 1.37 
            linear 40 xpos -0.37

        "You begin to walk alongside the forest, buying a small amount of time to think. In your peripheral, Akari follows along, watching expectantly. You consider making something up, but then decide that the best lie is the truth."

    else:
        you "Make sure to stay in the shadows, Ashina might be watching me."

        show bg forest edge:
            subpixel True ypos 2.2 zoom 2.74 
            xpos 1.37 
            linear 40 xpos -0.37

        "Akari nods and recedes into the undergrowth, just barely staying in your line of sight. You begin to walk parallel to the forest’s edge, doing your best to appear as if taking a leisurely stroll. You keep the movement of your lips subtle enough that you hope Ashina can’t tell you’re talking from a distance."

        aki "So? The dogs?"

    #Paths converge

    if dog_approval == 2:

        you "They recognize me as one of their own now, I think. I don’t know how they’d react if you were with me, but I might be able to get them to stand down."

    else:

        you "I asked Ashina to call them off. She might do that for me again, but otherwise we’d probably just have to sneak past them somehow."

    #Image Akari Thoughtful
    show aki thoughtful with dissolve

    aki "I dislike going in without a guarantee… but we will have to make it work."

    #Image Akari Neutral
    show aki neutral with dissolve

    aki "Did you at least find out an angle to give us the upper hand? A weakness?"

    if aka_lock:
        
        show bg forest edge:
            xpos -0.37
        
        "You stop walking, then you let out what you hope to be a believably disappointed sigh."

        you "No, she wouldn’t tell me anything. I’m sorry."

        #Image Akari Frustrated
        show aki angry with dissolve

        aki "Seriously?"

        #VSFX Akari (as if pacing)
        show aki at pacing
        #i think she's facing the wrong way, not sure why
        pause(2.0)
        show aki at stop_pacing

        "Akari paces back and forth, looking thoroughly frustrated."

        "{fast}She stops abruptly, her eyes scanning you with scrutiny, her hand moving towards her bow. You get the feeling you should say something before she decides you’re dead weight."

        #Image Akari Neutral
        show aki neutral with dissolve
                    
        you "She didn’t tell me anything, but I think she’s fond of me, at least. Two against one is good odds, especially if she’s hesitating to hurt me."

        "You try to sound nonchalant, your heart beating hard in your chest. After a few more moments of staring at you, Akari relaxes, her hand moving away from her bow."

        #Image Akari Thoughtful
        show aki thoughtful with dissolve

        aki "True enough, that might be the best advantage we can get. Alright, meet me at dusk. Help me sneak in, and we will rid this world of that monster once and for all."

        "You wonder briefly why Akari is so hell-bent on killing Ashina. However, now is not the time to go digging. Perhaps Ashina will have answers."

        you "Got it."

        #VSFX Akari (fade out)
        hide aki with dissolve

        "You keep your answer short, worried anything else might betray a quiver in your voice. Akari disappears back into the foliage, and you’re once again left alone at the forest’s edge."

    else:
        "You nod just slightly, glancing for but a moment in Akari’s direction."

        you "She will be at her weakest during the new moon, as will I."

        show aki determined with dissolve

        "You almost miss how Akari’s face subtly lights up, a look of determination flashing in her eyes."

        aki "Then we will attack on the first night of the new moon, ten days from now. That night, we will meet at dusk, you will help me sneak in, and we will rid this world of that monster once and for all."

        "Seeing that determination in her eyes stirs something within you. You had a drive like that once, counting the days until you turned 18, saving every penny you could… it makes you wonder what stake Akari has in all this."

        you "Akari, forgive me for asking, but I can’t help but notice… this seems personal to you."

        show aki angry with dissolve

        "Akari stiffens, her hands ball into fists, and her jaw clenches. You can tell you’re treading on dangerous ground here, and soften your tone."

        you "I’m sorry, I don’t mean to be presumptuous, I just… I know what it’s like to be hurt by someone. To have all this anger bottled up inside, from how helpless they made you feel."

        show aki bow nocked side with dissolve

        "She looks away, silent."

        if aka_approval > 0:

            show bg forest edge:
                xpos -0.37

            "Just when you almost think the conversation is over, she halts and speaks up, her voice softer than you’ve ever heard it."

            aki "I had a twin brother… Akio."

            "You can tell this is hard for her. Pretending it’s just for the sake of looking natural, you settle down, sitting with your back against a tree and facing the cabin. You hear Akari sit behind you, nearby."

            aki "He was such a bright, cheerful boy. I complained, but he always found a way to make me smile. We were inseparable."

            "She pauses. You can imagine her bittersweet expression, searching for words. You let her take all the time that she needs."

            aki "He loved the forest, always pestering our parents to take us out to explore. It was inconvenient, as we lived near the center of the city."

            aki "It happened when we were eight years old. I was staying over with a friend. Mom and dad were busy, and he slipped away… When my parents picked me up without him, I knew something was wrong."

            aki "I overheard them seeking help from police, friends, neighbors. My gut told me he was in the forest."

            aki "Initially, my parents dismissed me, but I knew Akio was clever. When I brought it up again, my parents were desperate enough to try."

            "The tumbling words suddenly stall out, and you can hear the shake in Akari’s breath before she resumes."

            aki "We found him. Mother tried to shield my eyes, but it was too late."

            "The {color=#ff0000}{b}pain{/b}{/color} in her voice stabs your heart as if it were your own. Without thinking, you reach back. Your hand finds hers, and she flinches back. Just when you’re about to pull away, her hand suddenly pins yours in a firm, trembling grip."

            aki "His body… ruined. Torn apart by a monster. Eyes, unforgettable eyes stared out from the forest. Later, the police said it was an animal attack, but I knew."

            "You squeeze Akari’s hand, ignoring the slight pain from her iron grip. Seeming to notice, her grip loosens. A long pause hangs in the air."

            aki "... I have never told anyone that before."

            "Her voice is quietly shocked at her own confession. You let out a breath you didn’t realize you were holding, empathy weighing on your heart."

            you "I am so sorry, Akari. You shouldn’t have had to see that."

            "You turn to look at Akari. She’s looking away, her gaze distant."

            aki "Akio deserved better."

            you "So did you."

            "Her eyes flick over to you nervously before staring, realizing that you’re looking at her. A few moments pass before her hand slips away, and she rises to her feet."

            aki "Leave, before Ashina suspects."

            "You want to argue, but Akari is right. You can’t risk Ashina getting suspicious."

            you "Can we see each other again? Before the new moon?"

            "There’s a clear hesitation in Akari’s eyes. She shakes her head."

            aki "Too dangerous. Foolish."

            "She gives you a very serious look."

            aki "... do not take any risks. I am often in these woods, and if I see you out, you will regret it."

            "There’s something in her tone that makes you smile. You get the sense that some part of her wants you to disregard her words. It gives you a rare, alien confidence."

            you "See you soon then, Akari."

            "Akari gets a flustered, frustrated look about her as you turn away."

            aki "You- Stay inside! I mean it!"

            "You step away from the forest’s edge, a small smile playing on your lips. Pausing after a few paces, you take a breath and compose yourself."

        else:
            aki "Leave, before Ashina suspects."

            "You want to argue, but Akari is right. You can’t risk Ashina getting suspicious."

            you "Can we see each other again? Before the new moon?"

            aki "No. Too dangerous."

            "Akari’s response is immediate, and her tone leaves no room for disagreement."

            you "Okay. I understand."

            "You step away from the forest’s edge with a tinge of disappointment."


    #Paths converge

    #SFX Walking
    play sound walk loop
    hide fog onlayer screens with dissolve
    #Image Cabin Etx. Returning (With Dogs)
    #Image Cabin Door Open
    scene bg door open with dissolve

    "You walk back to the cabin like you mean business, just in case someone is watching you."

    #Image Hearth
    stop sound fadeout 1.0
    scene bg hearth with dissolve:
        subpixel True pos (-0.07, -0.35) zoom 1.05
    show flame with dissolve:
        pos (0.59, 0.63) zoom 1.05
    #Music Eerier Outdoors (fade out)
    stop music fadeout 1.0
    #Music Cabin (fade in)
    play music cabin_music volume 0.3 fadein 1.0
    #SFX Fireplace (fade in)
    play soundb fireplace volume 0.3 loop

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
        show ash concerned with dissolve

        "A wave of guilt and self-disgust hurls you forward. Deep, endless regret compresses your throat, causing you to cough and sputter. You barely feel Ashina catch your arms to keep you upright."

        #VSFX Blue (tint back to normal)

        "When the feeling passes, you find yourself amazed that Ashina could carry such overwhelming emotion and yet, still stand tall, still look so composed."

        #Image Ashina Caring
        show ash caring with dissolve

        ash "Now you understand."

        #Image Ashina Neutral
        show ash neutral with dissolve

        ash "That little boy had a very determined sister, whom I’ve been evading ever since. She will stop at nothing to ensure my destruction, as is her right."

        you "Akari."

        "You mumble the name, and Ashina nods. She releases you, and you straighten back up."

        #Image Ashina Thoughtful (further away again)
        show ash thoughtful with dissolve

        ash "Meet with her, and help her inside, as she asked. Then, I will face her, and give her the fight she deserves. What you do then, is up to you."

        #VSFX Ashina (fade out)
        hide ash thoughtful with dissolve

        "You’re still reeling when you realize Ashina is halfway up the stairs. You reach out, considering calling after her, but hesitate as your eyelids flutter with exhaustion. Perhaps a side effect of your strange Lycan abilities."

        #SFX Walking
        #Image Stairs Up

        "As you reach the stairs, you hear Ashina’s door close above. Left with your own churning thoughts and feelings, you make your way to bed."

    if ash_approval < 4:

        #Image Ashina Thoughtful (further away)
        show ash thoughtful with dissolve

        ash "Yes… I know of Akari's motivations. It's nothing of your concern."

        #Image Ashina Neutral
        show ash neutral with dissolve
            
        ash "You don't need all of the details. Just let her in, and I will take care of the rest." 

        you "But if I'm going to help her sneak in, I think I should know–"

        #VSFX Screen Shake
        #Image Ashina Angry Hybrid (closer)
        show ash angry hybrid with dissolve

        ash "I don't. Want. To talk about it! What about that don't you understand?!"
            
        "Ashina's chest heaves as she attempts to calm herself."

        #Image Ashina Sad (further again)
        show ash concerned with dissolve

        ash "I apologize… I didn't mean to lash out like that. I need to be alone."

        "Ashina turns to leave, but not without a final word."

        #VSFX Ashina (further)
        show ash sad with dissolve

        ash "Tonight… Simply meet with Akari, and let her inside. I will confront her then. Join me in the fight, or don't. Just don't get in the way." 

        #VSFX Ashina (fade out)
        hide ash sad with dissolve

        "You watch as Ashina climbs up the stairs. Soon, you hear her shut the door to her room."

        #SFX Walking
        #Image Stairs Up

        "Left with your own churning thoughts and feelings, you make your way to bed."

    return