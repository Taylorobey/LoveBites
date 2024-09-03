# Declare characters used by this game.
define aki = Character("Akari")
#can we call her aki instead
define ash = Character("Ashina")
define cam = Character("Cameron")
define you = Character("You")

# Declare other variables to track for this game.
define humanity = 0
define corruption = 0
define aka_approval = 0
define ash_approval = 0
define cam_approval = 0
define dog_approval = 0

# Declare flags for story events. Default to False, then switch to True when event is triggered.
define meat_eaten = False

# Declare functions for use in scripts
define flash = Fade(0.1, 0.0, 3.0, color="#fff")
style bigtext:
    color "#000"
    size 72
    yalign 0.5
    outlines [(5, "#b70000", 0, 0)]
    italic True

# The game starts here, but immediately jumps to the first scene.
# Each scene is its own file for organizational purposes
label start:
    jump IntroductoryCutscene
    
    # This ends the game.
    return
