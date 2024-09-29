label CreditsScene:
    $ credits_speed = 25 #scrolling speed in seconds
    #scene bg color black #replace this with a fancy background
    #with dissolve
    #pause(0.5)
    #show theend:
        #yanchor 0.5 ypos 0.5
        #xanchor 0.5 xpos 0.5
    #with dissolve
    #with Pause(2.0)
    #hide theend with dissolve
    play music main_menu volume 0.6 fadein 1.0
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide thanks with dissolve
    show cred at Move((0.5, 3.9), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    pause(credits_speed)
    stop music fadeout 2.0
    pause (2.3)
    return