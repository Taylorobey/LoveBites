## Define transforms for use in scripts
# pacing
# blur

## Define some positions/zooms that are commonly used

# step closer to player
transform step_close:
    linear 1.00 ypos 2.0 zoom 2.0

# very close to player
transform step_closer:
    linear 1.00 ypos 3.8 zoom 4.0
transform step_closer_center:
    linear 1.00 xpos 0.45 ypos 3.8 zoom 4.0

# step back away
transform step_away:
    linear 1.00 ypos 1.0 zoom 1.0

# walk to window in main cabin
transform walk_to_window:
    subpixel True 
    zoom 1.0 xpan 0.0 ypan 0.0 
    linear 1.00 zoom 4.0 xpan 3.0 ypan -125.0

# closer to window
transform close_to_window:
    linear 1.00 zoom 5.0 xpan 3.0 ypan -135.0

# Torso left/center/right
# Bust left/center/right
# Lower Right
# Close to Player left/center/right