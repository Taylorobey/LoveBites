label SpeakNoEvilSceneP3:
        #Choices Converge here

        #if Cameron agrees to leave
        if cameron_leave:

                "You head up the stairs with Cameron in tow."

                ash "I take it you two had a pleasant reunion. How lovely."

                "Ashina turns her attention towards Cameron." 

                ash "If you agree to live by my rules, repeat them back to me. I need to make sure you understand what I expect from you."

                "You feel Cameron shrink away from Ashina and move closer to you."

                cam "Right, uhm…I can leave, but only if I promise not to talk about anything that happened here. I won't tell anyone about you, or that you kidnapped us in this cabin. Nada, nothing."

                ash "Yes, you understand well. Act as though this never even happened."

                ash "Hm, color me impressed. I didn't think you could convince them so well, pup."

                ash "I'm satisfied. Come along with me, human. I shall escort you back to civilization."

                "The three of you move towards the cabin's front door. Cameron takes one look back at you before disappearing into the darkness outside." 

                ash "As for you, girl, I have something to show you when I return. Be ready."

                "With that, Ashina shuts the cabin door, and you are left to your own devices."

                "You're uncertain of your future here, but you can at least rest easy now knowing that Cameron is safe. You are beyond exhausted and decide to go back to your room."

                jump LettersScene

        #if Cameron agrees to be turned
        elif cameron_turning:
                #Placeholder for the Cameron becomes a Lycan path
                hide placeholder

        #if Cameron refuses to leave or be turned, and you try to help them escape
        elif cameron_help:
                #Placeholder for a negative ending where you both die, or you die fighting Ashina and Cameron escapes.
                hide placeholder

        #if Cameron refuses to leave or be turned, and you return to Ashina
        else:
                "You find yourself in front of Ashina, your stomach hollow with dread."

                ash "Hm? Where is the human?"

                you "They…didn't want to do it. I tried to convince them, but they…"

                "You drop to your knees. It's as though the stress of the past couple days has finally caught up to you. You gasp for air as your chest heaves with sobs."

                ash "There, there. You did your best. Some people simply can't be reasoned with."

                ash "I will make this quick. But, I can't promise it will be painless if they struggle."

                ash "Go to your room. It'll be easier for you that way."

                "You turn to leave, but hesitate for a moment. You can't just let it end like this…Can you?"

                ash "I know what you're thinking. But, it's much too late to try and save them, pet. They've made their choice."

                ash "Please, I'm trying to extend kindness towards you. This isn't something you will want to witness. Run along."

                "Your legs trudge forward as you make your way to your room without replying. You can't even stand to look at Ashina right now. You don't want to do this. You can't leave Cameron behind."

                "But, there's no choice. If Ashina wants them dead, Cameron's fate is sealed. There's nothing you can do. You never have control over anything you care about."

                "You stumble your way into your room. You autopilot yourself into bed. Maybe if you go to sleep now, you can convince yourself that tonight was just a bad nightmare."

                "Yes, when you wake up, Cameron will still be alive. You tell yourself, maybe they can come to an understanding with Ashina. Everything will be ok. Everything will—"

                cam "AHHHH!"

                "A blood curdling scream pierces the air. You hear something strange. It feels like Cameron's heart is beating directly into your ears."

                you "No…No!"

                "You realize in horror that your heightened senses are making you feel everything as if you were right in front of them."

                "You hear every bit of terror in their labored breathing. You smell their fresh blood rushing from their arteries. You can practically feel it as Ashina slams their limp body into the basement wall."

                ash "I'm trying to make this easy on you, human! Stay still!"

                cam "No, please! I just wanted to save her! I love h-!"

                "You hear an awful sound. The crunching of their bones, the splitting of their tendons, the twisting of their flesh. The sound of Cameron's heartbeat slows, and soon it beats for the very last time." 

                "...You should have tried harder. To convince Cameron to leave. To escape this prison together. To have a strong enough will to live to not even end up in this fucked up situation to begin with."

                "Your inability to find control over your own life has gotten your best friend killed. Even though Ashina dealt the killing blow, you can't help but feel like this is entirely your fault."

                "You don't know if you can live with yourself after this."

                # (Demo Bad End)
