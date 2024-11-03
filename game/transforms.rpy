## Define transforms for use in scripts

### Define some positions/zooms that are commonly used

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
    linear 1.00 pos(0,0) zoom 4.0

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
    linear 0.5 ypos 1.0 zoom 1.0
transform step_away_fast:
    linear 0.4 ypos 1.0 zoom 1.0

# walk to window in main cabin
transform walk_to_window:
    subpixel True 
    yoffset 0.0 zoom 1.0 
    linear 1.00 yoffset 1521.0 zoom 4.0
#with offset instead of pan the transform doesn't have a weird u curve down

# closer to window
transform close_to_window:
    linear 1.00 yoffset 2097.0 zoom 5.0
#since the previous transform was changed and (the old version of) this one was relative to the previous transform it wouldn't work, so i changed this one too

# coming back to normal bg view
transform back_to_bg:
    linear 1.00 zoom 1.0 yoffset 0.0
#i think this one was consequentially broken too, fixed it though

# Torso left/center/right
transform torso_close_right:
    linear 0.60 pos (0.51, -0.03) zoom 2.0 

# Bust left/center/right
transform start_bust:
    zoom 3.4 xpos 0.10 ypos -0.30

###Define some transforms for pacing characters
transform pacing:
    subpixel True
    xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 1.25 xpos 0.25 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)      
    linear 0.0 xpos 0.25 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    pause(0.25)
    linear 2.0 xpos 0.75 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.0 xpos 0.75 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    pause(0.25)
    linear 1.25 xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    repeat

transform stop_pacing:
    linear 0.75 xpos 0.5
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
    linear 0.5 xpos 0.7 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)      
    linear 0.0 xpos 0.7 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    pause(0.25)
    linear 1.0 xpos 0.3 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.0 xpos 0.3 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    pause(0.25)
    linear 0.5 xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    repeat

transform stop_shortpacing:
    linear 0.6 xpos 0.5
    linear 0.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)

#this pace is bad, causes a bug
#transform annoyed_pace:
    #subpixel True 
    #parallel:
            #xpos 0.5 
            #linear 0.30 xpos 0.66
            #linear 0.57 xpos 0.66
            #linear 0.20 xpos 0.34
            #linear 0.35 xpos 0.34

    #parallel:
            #yrotate 0.0 
            #linear 0.30 yrotate 0.0 
            #linear 0.10 yrotate 0.0 
            #linear 0.17 yrotate 180.0
            #linear 0.60 yrotate 180.0 
            #linear 0.15 yrotate 0.0 
            #linear 0.10 yrotate 0.0
    
#switched from xpos to xoffset to make these more generally useful
#note: offset of +/- 10 is (very) roughly equal to a change in position of 0.01

###Define some transforms for shaking
transform nervous_shake:
    subpixel True 
    linear 0.15 xoffset -10
    linear 0.15 xoffset +10  
    linear 0.15 xoffset -10 
    linear 0.15 xoffset +10
    linear 0.15 xoffset 0 
    pause(0.70)

transform normal_shake:
    subpixel True
    linear 0.15 xoffset 20
    linear 0.20 xoffset -20 
    linear 0.15 xoffset 20
    linear 0.15 xoffset 0

transform annoyed_shake:
    subpixel True 
    linear 0.15 xoffset 30
    linear 0.15 xoffset -30 
    linear 0.15 xoffset 30
    linear 0.15 xoffset 0

transform cam_ground_shake:
    subpixel True 
    linear 0.15 xoffset -15
    linear 0.15 xoffset +15  
    linear 0.15 xoffset -15 
    linear 0.15 xoffset 0 

###Define some transforms for jumping in place
transform jump_in_place:
    subpixel True 
    linear 0.15 yoffset 0
    linear 0.10 yoffset -50
    linear 0.05 yoffset -25
    linear 0.05 yoffset 0

transform cam_surprise_jump:
    subpixel True
    linear 0.15 yoffset 0
    linear 0.15 yoffset -30
    linear 0.15 yoffset 0


#transform for nodding motion
transform nod:
    subpixel True 
    linear 0.15 ypos 2.03 
    linear 0.15 ypos 1.97 
    linear 0.15 ypos 2.0 

#transform for cameron hugging the player
transform hug:
    linear 1.0 pos (0.25, -0.04) zoom 2.5

#transforms for speak no evil p3
transform ash_closer_to_cam:
    subpixel True 
    linear 0.60 pos (0.24, 0.0) zoom 1.3

transform ash_closer_to_you:
    subpixel True 
    linear 0.45 pos (0.3, 0.06) zoom 2.0 

transform cam_further_from_ash:
    subpixel True 
    parallel:
            xpos 0.0 
            ease_bounce 0.20 xpos -0.07 
    parallel:
            ypos 0.0 
            ease 0.20 ypos 0.03 
    parallel:
            zoom 1.5 
            ease_back 0.20 zoom 1.75 

transform ash_steps_away:
    subpixel True 
    linear 0.30 xpos 0.4

transform ash_steps_away2:
    subpixel True 
    linear 0.60 pos (0.4, 0.0) zoom 1.3

#transforms for shadows to fade in and out in dream scene
transform shadowfade:
    alpha 0.0
    linear random.uniform(1.5, 2.0) alpha 1.0
    linear random.uniform(1.5, 2.0)  alpha 0.0  
    repeat

transform corruptfade:
    parallel:
            linear 0.05 xoffset -2 yoffset 2 
            linear 0.05 xoffset 3 yoffset -3 
            linear 0.05 xoffset 2 yoffset -2
            linear 0.05 xoffset -3 yoffset 3
            linear 0.05 xoffset 0 yoffset 0
            repeat
    parallel:
            alpha 0.0
            linear random.uniform(1.3, 2.3) alpha 1.0
            linear random.uniform(1.3, 2.3)  alpha 0.0  
            repeat