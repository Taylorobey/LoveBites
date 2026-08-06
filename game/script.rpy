# Declare characters used by this game.
define aki = DynamicCharacter("aki_name", color="#982313", who_outlines=[(3, "#e7d4d2", absolute(0), absolute(0))], who_kerning=10.0, size=65, yoffset=-3, who_italic=True)

define ash = DynamicCharacter("ash_name", color="#1e22ae", who_outlines=[(3, "#d5d6eb", absolute(0), absolute(0))], who_kerning=10.0, size=65, yoffset=-3, who_italic=True)

define cam              = Character("Cameron", color="#e7ab19", who_outlines=[(1, "#493505", absolute(0), absolute(0))], who_kerning=10.0, size=65, yoffset=-3, who_italic=True)
define you              = Character("You", color="#cecece", who_outlines=[(1, "#292929", absolute(0), absolute(0))], who_kerning=10.0, size=65, yoffset=-3, who_italic=True)
define neighbor         = Character("Neighbor", color="#444444", who_outlines=[(2, "#FFFFFF", absolute(0), absolute(0))], who_kerning=10.0, size=65, yoffset=-3, who_italic=True)
define teacher          = Character("Teacher", color="#292929", who_outlines=[(2, "#FFFFFF", absolute(0), absolute(0))], who_kerning=10.0, size=65, yoffset=-3, who_italic=True)

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
style redtext:
    color "#b70000"
    size 40
    italic True
style bluetext:
    color "#1651af"
    size 40
    italic True
style yellowtext:
    color "#ffff00"
    size 40
    italic True


#Supplementary audio channels
#Extra SFX
init python:
    renpy.music.register_channel('soundb', "sound")
    renpy.music.register_channel('soundc', "sound")
    renpy.music.register_channel('crickets', "sound")
    renpy.music.register_channel('indicators', "sound") #placeholder for UI humanity/corruption indicators

#For automatic VO rendering
init python:
    config.auto_voice = "VA/{id}.mp3"

#Rolling credits
init python:
    credits = ('Project Lead', 'BizzyBee'), ('Artists', 'SabiSabi\nShapeshift Stitch'),  ('Programmers', 'Taylorobey\ndot\nBizzyBee'), ('GUI', 'Chiara'), ('Writing', 'starsapphire\nBizzyBee'), ('Music', 'Annish\nBizzyBee'), ('Voice Acting', 'MariaCorcobadoVA as The Narrator\nsamgrace as Ashina\nLauren Pak as Akari\nTwigs24 as Cameron'), ('UI Sound', 'Annish'), ('Supplementary Music and SFX', 'Freesound.org\nPublic Domain')
    credits_s = "{size=150}Credits\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n8.5.3" #Don't forget to set this to your Ren'py version

#for Random Numbers that change with each animation
init python:
    import random

init python:
    # 'bottom' is behind 'master' (bg/sprites) and 'transient'
    config.layers.insert(0, 'bottom') #0 is absolute bottom
# so that wipe/slide/etc transitions don't show transparent background

# changing the speed of wipes
init:
    $ wipeleft = CropMove(0.5, "wipeleft")
    $ wiperight = CropMove(0.5, "wiperight")

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
    #jump TestScene
    jump IntroductoryCutscene

    #testing defines
    #define corruption = 3
    #define humanity = 3
    #define aka_lock = True
    #define aka_approval = 2
    #define ash_approval = 3
    #define dog_approval = 2

    #stop music fadeout 2.0
    #jump ConfrontationPlanningScene
    
    # This ends the game.
    return
