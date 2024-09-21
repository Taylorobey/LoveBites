# Declare characters used by this game.
define aki              = Character("???", color = "#871c1c")
#can we call her aki instead
#should probably do the same as ashina and set name to ???, but with red color
define ash              = Character("???", color="#1C4587")
#yes, that's the same shade of blue as everything else.
#changed name to "???" and i think we'll just $ it to ashina when mc learns her name
define cam              = Character("Cameron", color="#d3c71e")
define you              = Character("You", color="#a3a3a3")
define neighbor         = Character("Neighbor", color="#411c87")
define teacher          = Character("Teacher", color="#411c87")

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

## Define transforms for use in scripts
# pacing
# blur

## Define some positions/zooms that are commonly used
# Torso left/center/right
# Bust left/center/right
# Lower Right
# Close to Player left/center/right

#Supplementary audio channels
#Extra SFX
init python:
    renpy.music.register_channel('soundb', "sound")

# The game starts here, but immediately jumps to the first scene.
# Each scene is its own file for organizational purposes
label start:
    #temporary jump for testing
    jump WakingScene

    #jump IntroductoryCutscene
    
    # This ends the game.
    return
