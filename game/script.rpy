# Declare characters used by this game.
define aki = DynamicCharacter("aki_name", color="#982313", who_outlines=[(3, "#e7d4d2", absolute(0), absolute(0))])

define ash = DynamicCharacter("ash_name", color="#1e22ae", who_outlines=[(3, "#d5d6eb", absolute(0), absolute(0))])

define cam              = Character("Cameron", color="#e7ab19", who_outlines=[(1, "#493505", absolute(0), absolute(0))])
define you              = Character("You", color="#cecece", who_outlines=[(1, "#292929", absolute(0), absolute(0))])
define neighbor         = Character("Neighbor", color="#444444", who_outlines=[(2, "#FFFFFF", absolute(0), absolute(0))])
define teacher          = Character("Teacher", color="#292929", who_outlines=[(2, "#FFFFFF", absolute(0), absolute(0))])

# Declare other variables to track for this game.
define humanity         = 0
define corruption       = 0
define aka_approval     = 0
define ash_approval     = 0
define cam_approval     = 0
define dog_approval     = 0
define rand_chance      = 0
define compare_chance   = 0

# Declare flags for story events. Default to False, then switch to True when event is triggered.
define meat_eaten       = False
define reveal_to_cam    = False
define corrupted_chance = False
define humanity_chance  = False
define cameron_leave    = False
define cameron_help     = False
define cameron_turning  = False
define cameron_turned   = False
define ash_lock         = False
define aka_lock         = False
define cam_lock         = False

# Declare functions for use in scripts
define flash = Fade(0.1, 0.0, 3.0, color="#fff")
style bigtext:
    color "#000"
    size 72
    yalign 0.5
    outlines [(5, "#b70000", 0, 0)]
    italic True
style skytext:
    yalign -0.55
    xalign 0.5

#Supplementary audio channels
#Extra SFX
init python:
    renpy.music.register_channel('soundb', "sound")
    renpy.music.register_channel('crickets', "sound")

#For automatic VO rendering
init python:
    config.auto_voice = "VA/{id}.mp3"

#Rolling credits
init python:
    credits = ('Project Lead', 'BizzyBee'), ('Artists', 'SabiSabi\nShapeshift Stitch\nrobyn'),  ('Programmers', 'Taylorobey\ndot\nBizzyBee\nHilarionDev'), ('GUI', 'Chiara'), ('Writing', 'starsapphire\nBizzyBee'), ('Music', 'Annish\nBizzyBee'), ('Voice Acting', 'MariaCorcobadoVA as The Narrator\nsamgrace as Ashina\nLauren Pak as Akari\nTwigs24 as Cameron'), ('UI Sound', 'Annish'), ('Supplementary Music and SFX', 'Freesound.org\nPublic Domain')
    credits_s = "{size=150}Credits\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n8.3.0" #Don't forget to set this to your Ren'py version

#for Random Numbers that change with each animation
init python:
    import random

# The game starts here, but immediately jumps to the first scene.
# Each scene is its own file for organizational purposes
label start:
    #this is needed for zooms to work properly
    camera:
        perspective True

    #name defines
    $ aki_name = "???"
    $ ash_name = "???"

    #temporary jump for testing
    #jump FailedRescueScene
    jump IntroductoryCutscene
    
    # This ends the game.
    return
