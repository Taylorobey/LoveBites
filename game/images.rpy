# Declare background images
image bg intersection       = "bg/intersection.png"
image bg street dog         = "bg/street_one_dog.png"
image bg street dogs        = "bg/street_two_dogs.png"
image bg street many        = "bg/street_many_dogs.png"
image bg street full        = "bg/street_full_dogs.png"
image bg alley              = "bg/alley.png"

image bg room ceiling       = "bg/cabin_ceiling.png"
image bg room mc            = "bg/captive_room.png"
image bg door closed        = "bg/cabin_door_closed.png"
image bg door open          = "bg/cabin_door_open.png"
image bg downstairs         = "bg/downstairs.png"
image bg upstairs           = "bg/upstairs.png"
image bg wall               = "bg/cabin_wall.png"
image bg hallway            = "temp/hallway.png"
image bg hearth             = "temp/hearth.png"
image bg cabin exterior     = "temp/mc_room.jpg"
image bg cabin approach     = "temp/mc_room.jpg"
image bg forest edge        = "bg/sky.png"
image bg sky color          = "bg/sky_color.png"
image bg basement           = "bg/captive_room.png"
image bg window:
    "bg/window.png"
    subpixel True zoom 0.4

image bg window eyes:
    "bg/eyes/EYES_01.png" with dissolve
    subpixel True zoom 0.4
    1.5
    "bg/eyes/EYES_02.png" with dissolve
    subpixel True zoom 0.4
    1.5
    "bg/eyes/EYES_03.png" with dissolve
    subpixel True zoom 0.4
    1.5
    repeat

image bg ripple one:
    "bg/ripples/RPL_0101.png"
    0.1 #this part defines how long to wait before next frame
    "bg/ripples/RPL_0102.png"
    0.1
    "bg/ripples/RPL_0103.png"
    0.1
    "bg/ripples/RPL_0104.png"
    0.1
    "bg/ripples/RPL_0105.png"
    0.1
    "bg/ripples/RPL_0106.png"
    0.1
    "bg/ripples/RPL_0107.png"
    0.1
    "bg/ripples/RPL_0108.png"
    0.1
    "bg/ripples/RPL_0109.png"
    0.1
    "bg/ripples/RPL_0110.png"
    0.1
    "bg/ripples/RPL_0111.png"
    0.1
    repeat

image starryeffect:
    "bg/stars/starry_1.png" with Dissolve(2.0)
    2
    "bg/stars/starry_2.png" with Dissolve(2.0)
    2
    "bg/stars/starry_3.png" with Dissolve(2.0)
    2
    repeat

# Declare color backgrounds for effect use
image bg color black        = "bg/color_black.bmp"
image bg color red          = "bg/color_red.jpg"

# Declare character images
image wolf neutral:
    "chars/ashina/ashina_wolf_sketch-no-tail.png"
    subpixel True zoom 0.1
image wolf snarl:
    "chars/ashina/ashina_wolf_snarl_sketch.png"
    subpixel True zoom 0.1
image wolf lunge            = "chars/ashina/ashina_wolf_lunge_sketch.png"

#Ashina
image ash neutral:
    "chars/ashina/ashina_neutral.png"
    subpixel True zoom 0.33 
image ash friendly:
    "chars/ashina/ashina_friendly2.png"
    subpixel True zoom 0.33 
image ash sadistic:
    "chars/ashina/ashina_friendly.png"
    subpixel True zoom 0.33  
image ash thoughtful:
    "chars/ashina/ashina_thoughtful.png"
    subpixel True zoom 0.33
image ash caring:
    "chars/ashina/ashina_caring.png"
    subpixel True zoom 0.33
image ash concerned:
    "chars/ashina/ashina_concerned.png"
    subpixel True zoom 0.33
image ash sad:
    "chars/ashina/ashina_sad.png"
    subpixel True zoom 0.33
image ash angry hybrid:
    "chars/ashina/ashina_angryhybrid.png"
    subpixel True zoom 0.37
image ash annoyed:
    "chars/ashina/ashina_annoyed.png"
    subpixel True zoom 0.33
#temps
image ash fighting:
    "chars/ashina/ashina_neutral.png"
    subpixel True zoom 0.33 
image ash hurt:
    "chars/ashina/ashina_neutral.png"
    subpixel True zoom 0.33 

#Akari
image aki neutral:
    "chars/akari/akari_neutral.png"
    subpixel True zoom 0.33 
image aki bow drawn:
    "chars/akari/akari_bow.png"
    subpixel True zoom 0.33 
image aki bow nocked:
    "chars/akari/akari_arrowready.png"
    subpixel True zoom 0.33 
image aki thoughtful:
    "chars/akari/akari_thoughtful.png"
    subpixel True zoom 0.33 
image aki angry:
    "chars/akari/akari_frustrated.png"
    subpixel True zoom 0.33 
image aki caring:
    "chars/akari/akari_caring.png"
    subpixel True zoom 0.33
image aki determined:
    "chars/akari/akari_determined.png"
    subpixel True zoom 0.33 
#temps
image aki fighting:
    "chars/akari/akari_arrowready.png"
    subpixel True zoom 0.33 
image aki dodging:
    "chars/akari/akari_bow.png"
    subpixel True zoom 0.33 
image aki hurt:
    "chars/akari/akari_neutral.png"
    subpixel True zoom 0.33 

#Cameron
image cam neutral:
    "chars/cameron/cameron_neutral.png"
    subpixel True zoom 0.33 
image cam friendly:
    "chars/cameron/cameron_friendly.png"
    subpixel True zoom 0.33 
image cam caring:
    "chars/cameron/cameron_caring.png"
    subpixel True zoom 0.33
image cam frustrated:
    "chars/cameron/cameron_frustrated.png"
    subpixel True zoom 0.33
image cam nervous:
    "chars/cameron/cameron_nervous.png"
    subpixel True zoom 0.33
image cam scared:
    "chars/cameron/cameron_scared.png"
    subpixel True zoom 0.33 
#temps
image cam thoughtful:
    "chars/cameron/cameron_neutral.png"
    subpixel True zoom 0.33

image neighbor:
    "chars/shadows/neighbor/NEI_01.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/neighbor/NEI_02.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/neighbor/NEI_03.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/neighbor/NEI_04.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/neighbor/NEI_05.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/neighbor/NEI_06.png"
    subpixel True zoom 0.6
    0.2
    repeat
image teacher:
    "chars/shadows/teacher/TEA_01.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/teacher/TEA_02.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/teacher/TEA_03.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/teacher/TEA_04.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/teacher/TEA_05.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/teacher/TEA_06.png"
    subpixel True zoom 0.6
    0.2
    repeat

image dog                   = "chars/dogs/dog.png"
image happy dog             = "chars/dogs/dog_happy.png"
# Declare other images
image logo                  = "logo_white.png"
image pain                  = "red_edges.png"
