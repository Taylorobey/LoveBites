# Declare audio files to use for music
define audio.intro_music            = "MUS/Introduction_Endless_Night.mp3"
define audio.capture_music          = "MUS/Capture_You_Feel_Their_Breath.mp3"
define audio.cabin_music            = "MUS/Cabin.mp3"
define audio.dream_music            = "MUS/Dream.mp3"
define audio.starry_music           = "MUS/Starry_Night.mp3"
#placeholders until music is available
define audio.eerie_outdoors_music   = "MUS/Temp_Eerie.mp3"
define audio.connection_music       = "MUS/Connection.wav"
define audio.goodbyes_music         = "MUS/Temp_Goodbyes.mp3"

# Declare audio files to use for sounds
define audio.car                    = "SFX/Car_Speeding_By.wav"
define audio.walk                   = "SFX/Walking.mp3"
define audio.fast_walk              = "SFX/Faster_Walking.mp3"
define audio.run                    = "SFX/Running.mp3"
define audio.heart                  = "SFX/Heartbeat.wav"
define audio.howl                   = "SFX/howling.mp3"
define audio.crickets               = "SFX/crickets.mp3"
define audio.barking                = "SFX/Dogs_Barking.mp3"
define audio.creak                  = "SFX/Creak.mp3"
define audio.growl                  = "SFX/Growl.wav"
define audio.fireplace              = "SFX/Fireplace.mp3"
define audio.knocking               = "SFX/Knock (Captive Room).mp3"
define audio.mournfulhowls          = "SFX/Mournful_Howls.flac"
define audio.gore                   = "SFX/Gore.mp3"
#placeholders until audio effects are available


#so that VA isn't too loud
init python:
    renpy.voice.set_volume(0.7)
