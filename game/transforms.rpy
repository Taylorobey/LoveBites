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

# coming back to normal bg view
transform back_to_bg:
    linear 1.00 zoom 1.0 xpan 0.0 ypan 0.0

# Torso left/center/right

# Bust left/center/right
transform start_bust:
    zoom 3.2 xpos 0.12 ypos -0.17

#transform for pacing characters
transform pacing:
    subpixel True
    xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 1.75 xpos 0.14 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)      
    linear 0.0 xpos 0.14 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    pause(0.25)
    linear 2.5 xpos 0.86 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.0 xpos 0.86 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    pause(0.25)
    linear 1.75 xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    repeat

transform stop_pacing:
    linear 1.5 xpos 0.5
    linear 0.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

#transform for nervous shaking
transform nervous_shake:
    subpixel True 
    xpos 0.5 
    linear 0.15 xpos 0.49 
    linear 0.15 xpos 0.51 
    linear 0.15 xpos 0.49 
    linear 0.15 xpos 0.5 
    pause(0.70)
    