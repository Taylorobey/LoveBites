## Define transforms for use in scripts
# pacing
# blur

## Define some positions/zooms that are commonly used

# short step toward player
transform step_close_short:
    linear 0.25 ypos 1.45 zoom 1.4

# step closer to player
transform step_close:
    linear 0.50 ypos 2.0 zoom 2.0
transform step_close_center_fast:
    linear 0.50 xpos 0.5 ypos 2.0 zoom 2.0

# very close to player
transform step_closer:
    linear 1.00 ypos 3.8 zoom 4.0
transform step_closer_center:
    linear 1.00 xpos 0.45 ypos 3.8 zoom 4.0

# stepping closer threateningly
transform threat_step:
    linear 0.25 ypos 1.15 zoom 1.15
transform threat_step_2:
    linear 0.25 ypos 1.45 zoom 1.4

# step away slightly
transform step_away_half:
    linear 0.50 ypos 1.5 zoom 1.66

# step back away
transform step_away:
    linear 1.00 ypos 1.0 zoom 1.0
transform step_away_fast:
    linear 0.4 ypos 1.0 zoom 1.0

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
    zoom 3.4 xpos 0.10 ypos -0.30

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

transform shortpacing:
    subpixel True
    xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 1.0 xpos 0.3 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)      
    linear 0.0 xpos 0.3 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    pause(0.25)
    linear 1.5 xpos 0.7 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.0 xpos 0.7 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    pause(0.25)
    linear 1.0 xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    repeat

transform shortpacingreverse:
    subpixel True
    xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 1.0 xpos 0.7 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)      
    linear 0.0 xpos 0.7 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    pause(0.25)
    linear 1.5 xpos 0.3 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.0 xpos 0.3 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    pause(0.25)
    linear 1.0 xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    repeat

transform stop_shortpacing:
    linear 0.6 xpos 0.5
    linear 0.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

transform annoyed_pace:
    subpixel True 
    parallel:
            xpos 0.5 
            linear 0.30 xpos 0.66
            linear 0.57 xpos 0.66
            linear 0.20 xpos 0.34
            linear 0.35 xpos 0.34

    parallel:
            yrotate 0.0 
            linear 0.30 yrotate 0.0 
            linear 0.10 yrotate 0.0 
            linear 0.17 yrotate 180.0
            linear 0.60 yrotate 180.0 
            linear 0.15 yrotate 0.0 
            linear 0.10 yrotate 0.0
    
#transforms for shaking
transform nervous_shake:
    subpixel True 
    xpos 0.5 
    linear 0.15 xpos 0.49 
    linear 0.15 xpos 0.51 
    linear 0.15 xpos 0.49 
    linear 0.15 xpos 0.5 
    pause(0.70)

transform normal_shake:
    subpixel True 
    xpos 0.34 
    linear 0.15 xpos 0.36 
    linear 0.20 xpos 0.32 
    linear 0.15 xpos 0.34 

#transform for jumping in place
transform jump_in_place:
    subpixel True 
    linear 0.15 ypos 1.45 
    linear 0.10 ypos 1.4 
    linear 0.05 ypos 1.43 
    