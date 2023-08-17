# The script of the game goes in this file.
default blink_timer_a = renpy.random.randint(1, 4)
default blink_timer_b = renpy.random.randint(3, 6)
default blink_timer_c = renpy.random.randint(3, 4)

##regular taps, medium intervals
#define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg']
##light taps, smaller intervals
#define sounds = ['audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']
#both taps
#define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg', 'audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']

define sound = ['audio/dot.wav']
define sounds = ['audio/xylophone/x1.ogg', 'audio/xylophone/x2.ogg', 'audio/xylophone/x3.ogg', 'audio/xylophone/x4.ogg', 'audio/xylophone/x5.ogg', 'audio/xylophone/x6.ogg', 'audio/xylophone/x7.ogg', 'audio/xylophone/x8.ogg', 'audio/xylophone/x9.ogg', 'audio/xylophone/x10.ogg']

init python:
    renpy.music.register_channel("ambient", "music")

    #region
            #Generate seperate audio channel from voice for beeps.
        #renpy.music.register_channel(name='beeps', mixer='voice')

        #Character callback that generates the sound.
        #def rv(event, **kwargs):
        #    if event == "show": #When the text is shown
        #        build_sentence(_last_say_what, "eileen")
        #        renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        #    elif event == "slow_done" or event == "end": #When the text is finished displaying or you open a menu.
        #        renpy.sound.stop(channel="beeps")
    #endregion

    #region callback
    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None
  
    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None
  
    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)
  
    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d = Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))
  
    # This callback maintains the speaking variable.
    def speaker_callback(name, event, interact=True, **kwargs):
        global speaking
       
        if event == "show":
            if name == "riberto":
                renpy.sound.play(renpy.random.choice(sounds), fadein=0.001)
                for i in range(50):
                    renpy.sound.queue(renpy.random.choice(sounds), fadein=0.01)
            else:
                renpy.sound.play(renpy.random.choice(sound), fadein=0.001)
                for i in range(50):
                    renpy.sound.queue(renpy.random.choice(sound), fadein=0.01)
            speaking = name
        elif event == "slow_done":
            speaking = None
            renpy.sound.stop(fadeout=0.01)
        elif event == "end":
            speaking = None
            renpy.sound.stop(fadeout=0.01)
  
    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)
    #endregion

    #region truly random blinking
    def blinkb(trans, st, at):
        global blink_timer_a

        if st >= blink_timer_a:
            blink_timer_a = renpy.random.randint(4, 8)
            return None
        else:
            return 0

    def blinks(trans, st, at):
        global blink_timer_b

        if st >= blink_timer_b:
            blink_timer_b = renpy.random.randint(6, 9)
            return None
        else:
            return 0

    def blinkr(trans, st, at):
        global blink_timer_c

        if st >= blink_timer_c:
            blink_timer_b = renpy.random.randint(2, 8)
            return None
        else:
            return 0
    #endregion

    def clamp(num, min_value, max_value):
        return max(min(num, max_value), min_value)

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("RIBERTO", 
            who_bold = False, 
            what_prefix = '"', 
            what_suffix = '"',
            callback = speaker("riberto"), 
            ctc = "ctc_anchored", 
            ctc_position = "fixed")

define w = Character("???", what_prefix = '"', what_suffix = '"', callback = speaker("riberto"), ctc = "ctc_anchored", ctc_position = "fixed")
define y = Character("???", what_prefix = '"', what_suffix = '"', callback = speaker("none"), ctc = "ctc_anchored", ctc_position = "fixed")
#define b = Character("BAT", who_bold = False, color = '#35608b', what_prefix = '"', what_suffix = '"')
#define s = Character("SPIDER", who_bold = False, color = '#35634d', what_prefix = '"', what_suffix = '"')

#######################
# The game starts here.
#######################

label start:

    play music "audio/fire.ogg"
    #play ambient "audio/raintweak.ogg"
    play ambient "audio/rainece.ogg"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image background:
        "images/bg00.png"
        pause 0.25
        "images/bg01.png"
        pause 0.25
        "images/bg02.png"
        pause 0.25
        "images/bg03.png"
        pause 0.25
        repeat

    image ctc_anchored:
        "ctc fixed 02.png"
        yalign 0.88
        xalign 0.925
        0.5
        linear 0.5 yalign 0.87
        0.5
        linear 0.5 yalign 0.88
        repeat

    image mur:
        "bat.png"
        function blinkb
        "bat blink.png"
        0.25
        repeat

    image ara:
        "spi.png"
        function blinks
        "spi blink.png"
        0.2
        repeat

    image ridle:
        "riberto idle 01.png"
        0.05
        "riberto idle 02.png"
        0.15
        "riberto idle 03.png"
        0.05
        "riberto idle 00.png"
        function blinkr
        repeat

    image rflushed:
        "riberto flushed 01.png"
        0.15
        "riberto flushed 02.png"
        0.15
        "riberto flushed 03.png"
        0.15
        "riberto flushed 04.png"
        0.15
        "riberto flushed 05.png"
        0.15
        "riberto flushed 06.png"
        0.15
        "riberto flushed 07.png"
        0.15
        "riberto flushed 00.png"
        3.95
        repeat

    image rjaw = Composite(
        (91, 166),
        (0,0), "riberto blank.png",
        (0,0), WhileSpeaking("riberto", "rjawchoice", "riberto jaw idle.png"),
        )

    image rjawchoice:
        choice:
            "riberto jaw move 01.png"
            clamp(3/preferences.text_cps, 0.05, 5)
            "riberto jaw move 02.png"
            clamp(3/preferences.text_cps, 0.05, 5)
        choice:
            "riberto jaw move 01.png" #-
            clamp(3/preferences.text_cps, 0.05, 5) 
            "riberto jaw move 02.png"
            clamp(3/preferences.text_cps, 0.05, 5)
            "riberto jaw move 03.png"
            clamp(3/preferences.text_cps, 0.05, 5)
            "riberto jaw move 02.png"
            clamp(3/preferences.text_cps, 0.05, 5)
        repeat

    image rjawmove1:
        "riberto jaw move 01.png"
        clamp(3/preferences.text_cps, 0.05, 5)
        "riberto jaw move 02.png"
        clamp(3/preferences.text_cps, 0.05, 5)
        "riberto jaw move 01.png"
        clamp(3/preferences.text_cps, 0.05, 5)
        repeat

    image rjawmove0:
        "riberto jaw move 01.png"
        clamp(3/preferences.text_cps, 0.05, 5)
        "riberto jaw move 02.png"
        clamp(3/preferences.text_cps, 0.05, 5)
        "riberto jaw move 01.png" #-
        clamp(3/preferences.text_cps, 0.05, 5) 
        "riberto jaw move 02.png"
        clamp(3/preferences.text_cps, 0.05, 5)
        "riberto jaw move 03.png"
        clamp(3/preferences.text_cps, 0.05, 5)
        "riberto jaw move 02.png"
        clamp(3/preferences.text_cps, 0.05, 5)
        "riberto jaw move 01.png"
        clamp(3/preferences.text_cps, 0.05, 5)
        "riberto jaw move 02.png"
        clamp(3/preferences.text_cps, 0.05, 5)
        repeat

    scene background

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    show mur at Position(xpos = 96, xanchor = 0, ypos = 19, yanchor = 0)    
    show ara at Position(xpos = 267, xanchor = 0, ypos = 5, yanchor = 0)

    # These display lines of dialogue.

    y "..."
    w "Hmm..."
    y "..."
    w "...eh?"
    show ridle
    show rjaw
    with dissolve
    w "Hey!"
    w "You there!"
    w "Are you okay?"
    w "What are you doing here?"
    y "..."
    w "You don't look from around here. So squishy..."
    y "..."
    y "..."
    y "..."
    w "Not much for words, aye?"
    w "It's okay."
    w "You're not the first one to get lost in here, and surely not the last."
    w "But do not fret, I'll get you outta here."
    w "I'm #%%\\ŷ!. Ye can just call me {color=#e35460}RIBERTO{/color}."
    r "I'll... uh... I'll just call you chum. Fits you pretty well."
    hide ridle
    hide rjaw
    show rflushed
    show rjaw
    r "Aye, nice to meet you, chum!"
    hide rflushed
    hide rjaw
    show ridle
    show rjaw
    r "Now let's get going, shall we?"
    r "There is one thing you need to know first, though."
    r "This dungeon we're trapped in... It's 'magical', y'see."
    r "Actually, the only one stuck in here is you!"
    r "I'm this dungeon's lord."
    hide ridle
    hide rjaw
    show rflushed
    show rjaw
    r "Self-proclaimed, must confess. Left living here for all eternity. "
    r "Well, 'undying', rather."
    r "At least these dusty old bones have kept this house of mine nice and clean all these years!"
    hide rflushed
    hide rjaw
    show ridle
    show rjaw
    r "Anyway, this dungeon... doesn't have an exit."
    r "Nor an entrance."
    r "Not until its user desires to. This vault is ever-changing."
    r "And I may be a cool, humerous and a bit of a bonehead, but I'm not its user."
    r "That's you, chum!"
    r "The reason why you're here with me may be something you been struggling with." 
    r "Emotions, life and the like."
    r "You humans are complex beings, yet so powerful."
    r "Or maybe it was purely by chance."
    r "The whim of fate."
    r "Anyhow,"
    r "To catalyze your feelings into an opening I'll need you to tell me about them."

    r ""
    r "...\\ \n \% "

    # This ends the game.
    return
