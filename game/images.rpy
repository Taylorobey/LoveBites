# Declare background images
image bg intersection       = "bg/intersection.png"
image bg street dog         = "bg/street_one_dog.png"
image bg street dogs        = "bg/street_two_dogs.png"
image bg street many        = "bg/street_many_dogs.png"
image bg street full        = "bg/street_full_dogs.png"
image bg alley              = "bg/alley.png"

image bg room ceiling       = "bg/cabin_ceiling.png"
image bg room mc            = "bg/captive_room.png"
image bg room mc open window:
    "bg/captive_room_open_window.png"
    subpixel True zoom 0.5
image bg door closed        = "bg/cabin_door_closed.png"
image bg door open          = "bg/cabin_door_open.png"
image bg downstairs         = "bg/downstairs.png"
image bg upstairs           = "bg/upstairs.png"
image bg wall               = "bg/cabin_wall.png"
image bg hallway            = "bg/hallway.png"
image bg hearth             = "bg/hearth.png"
image bg cabin ext no dogs  = "bg/cabin_exterior_nodogs.png"
image bg cabin ext dogs:
    "bg/eyes/yardeyes1.png" with dissolve
    1.7
    "bg/eyes/yardeyes2.png" with dissolve
    1.7
    repeat

image bg cabin approach     = "temp/mc_room.jpg"
image bg forest edge        = "bg/sky.png"
image bg sky color          = "bg/sky_color.png"
image bg basement:
    "bg/basement.png"
    subpixel True zoom 0.5
image bg window:
    "bg/window.png"
    subpixel True zoom 0.4
image bg meat plate:
    "bg/meat_plate.png"
    subpixel True zoom 0.5
image bg meat board:
    "bg/meatboard.png"
    subpixel True zoom 0.5

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

image bg ripple two:
    "bg/ripples/RPL_0201.png"
    0.1 #this part defines how long to wait before next frame
    "bg/ripples/RPL_0202.png"
    0.1
    "bg/ripples/RPL_0203.png"
    0.1
    "bg/ripples/RPL_0204.png"
    0.1
    "bg/ripples/RPL_0205.png"
    0.1
    "bg/ripples/RPL_0206.png"
    0.1
    "bg/ripples/RPL_0207.png"
    0.1
    "bg/ripples/RPL_0208.png"
    0.1
    "bg/ripples/RPL_0209.png"
    0.1
    "bg/ripples/RPL_0210.png"
    0.1
    "bg/ripples/RPL_0211.png"
    0.1
    repeat

image bg ripple three:
    "bg/ripples/RPL_0301.png"
    0.1 #this part defines how long to wait before next frame
    "bg/ripples/RPL_0302.png"
    0.1
    "bg/ripples/RPL_0303.png"
    0.1
    "bg/ripples/RPL_0304.png"
    0.1
    "bg/ripples/RPL_0305.png"
    0.1
    "bg/ripples/RPL_0306.png"
    0.1
    "bg/ripples/RPL_0307.png"
    0.1
    "bg/ripples/RPL_0308.png"
    0.1
    "bg/ripples/RPL_0309.png"
    0.1
    "bg/ripples/RPL_0310.png"
    0.1
    "bg/ripples/RPL_0311.png"
    0.1
    repeat

image bg ripple four:
    "bg/ripples/RPL_0401.png"
    0.1 #this part defines how long to wait before next frame
    "bg/ripples/RPL_0402.png"
    0.1
    "bg/ripples/RPL_0403.png"
    0.1
    "bg/ripples/RPL_0404.png"
    0.1
    "bg/ripples/RPL_0405.png"
    0.1
    "bg/ripples/RPL_0406.png"
    0.1
    "bg/ripples/RPL_0407.png"
    0.1
    "bg/ripples/RPL_0408.png"
    0.1
    "bg/ripples/RPL_0409.png"
    0.1
    "bg/ripples/RPL_0410.png"
    0.1
    "bg/ripples/RPL_0411.png"
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

image fog:
    "bg/fog/fog1.png" with Dissolve(2.0)
    2
    "bg/fog/fog2.png" with Dissolve(2.0)
    2
    "bg/fog/fog3.png" with Dissolve(2.0)
    2
    "bg/fog/fog4.png" with Dissolve(2.0)
    2
    repeat

image fire:
    "bg/fire/fire1.png" with Dissolve(0.25)
    0.25
    "bg/fire/fire2.png" with Dissolve(0.25)
    0.25
    "bg/fire/fire3.png" with Dissolve(0.25)
    0.25
    "bg/fire/fire4.png" with Dissolve(0.25)
    0.25
    repeat

image flame:
    "bg/living room flame/flame1.png" with Dissolve(0.2)
    0.2
    "bg/living room flame/flame2.png" with Dissolve(0.2)
    0.2
    "bg/living room flame/flame3.png" with Dissolve(0.2)
    0.2
    "bg/living room flame/flame4.png" with Dissolve(0.2)
    0.2
    repeat

# Declare color backgrounds for effect use
image bg color black        = "bg/color_black.jpg"
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
image aki bow drawn angry:
    "chars/akari/akari_bow_angry.png"
    subpixel True zoom 0.33 
image aki bow nocked:
    "chars/akari/akari_arrowready.png"
    subpixel True zoom 0.33 
image aki bow nocked side:
    "chars/akari/akari_arrowready_looktoside.png"
    subpixel True zoom 0.33 
image aki thoughtful:
    "chars/akari/akari_thoughtful.png"
    subpixel True zoom 0.33 
image aki thoughtful look:
    "chars/akari/akari_thoughtful_look.png"
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

#shadows
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
image shadowsb:
    "chars/shadows/B/IMG_0413.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/B/IMG_0414.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/B/IMG_0415.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/B/IMG_0416.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/B/IMG_0417.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/B/IMG_0418.png"
    subpixel True zoom 0.6
    0.2
    repeat
image shadowsc:
    "chars/shadows/C/IMG_0419.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/C/IMG_0420.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/C/IMG_0421.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/C/IMG_0422.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/C/IMG_0423.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/C/IMG_0424.png"
    subpixel True zoom 0.6
    0.2
    repeat
image shadowsd:
    "chars/shadows/D/IMG_0425.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/D/IMG_0426.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/D/IMG_0427.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/D/IMG_0428.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/D/IMG_0429.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/D/IMG_0430.png"
    subpixel True zoom 0.6
    0.2
    repeat
image shadowse:
    "chars/shadows/E/IMG_0431.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/E/IMG_0432.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/E/IMG_0433.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/E/IMG_0434.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/E/IMG_0435.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/E/IMG_0436.png"
    subpixel True zoom 0.6
    0.2
    repeat
image shadowsf:
    "chars/shadows/F/IMG_0437.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/F/IMG_0438.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/F/IMG_0439.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/F/IMG_0440.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/F/IMG_0441.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/F/IMG_0442.png"
    subpixel True zoom 0.6
    0.2
    repeat
image shadowsh:
    "chars/shadows/H/IMG_0449.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/H/IMG_0450.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/H/IMG_0451.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/H/IMG_0452.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/H/IMG_0453.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/H/IMG_0454.png"
    subpixel True zoom 0.6
    0.2
    repeat
image shadowsi:
    "chars/shadows/I/IMG_0455.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/I/IMG_0456.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/I/IMG_0457.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/I/IMG_0458.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/I/IMG_0459.png"
    subpixel True zoom 0.6
    0.2
    "chars/shadows/I/IMG_0460.png"
    subpixel True zoom 0.6
    0.2
    repeat

image dog                   = "chars/dogs/dog.png"
image happy dog             = "chars/dogs/dog_happy.png"

# Declare other images
image logo                  = "logo.png"
image pain                  = "red_edges.png"
image cred = Text(credits_s, font="FrederickatheGreat-Regular.ttf", text_align=0.5) #use this if you want to use special fonts
image theend = Text("{size=150}THE END", font="FrederickatheGreat-Regular.ttf", text_align=0.5)
image thanks = Text("Thanks for playing the demo!", font="FrederickatheGreat-Regular.ttf", size=100)
image spook logo            = "gui/Spooktober_Logo.png"
image menu no logo          = "gui/main_menu_nologo.png"
image main menu             = "gui/main_menu.png"

