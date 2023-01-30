# The script of the game goes in this file.
default blink_timer_a = renpy.random.randint(2, 4)
default blink_timer_b = renpy.random.randint(3, 6)
default blink_timer_c = renpy.random.randint(3, 3)

##regular taps, medium intervals
#define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg']
##light taps, smaller intervals
#define sounds = ['audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']
#both taps
define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg', 'audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']

init python:
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

    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v

        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    #Generate seperate audio channel from voice for beeps.
    #renpy.music.register_channel(name='beeps', mixer='voice')

    #Character callback that generates the sound.
    #def rv(event, **kwargs):
    #    if event == "show": #When the text is shown
    #        build_sentence(_last_say_what, "eileen")
    #        renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
    #    elif event == "slow_done" or event == "end": #When the text is finished displaying or you open a menu.
    #        renpy.sound.stop(channel="beeps")

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("RIBERTO", 
            who_bold = False, 
            what_prefix = '"', 
            what_suffix = '"',
            callback = type_sound, 
            ctc = "ctc_anchored", 
            ctc_position = "fixed")

#callback = rv,

define w = Character("???", what_prefix = '"', what_suffix = '"', callback = type_sound, ctc = "ctc_anchored", ctc_position = "fixed")
#define b = Character("BAT", who_bold = False, color = '#35608b', what_prefix = '"', what_suffix = '"')
#define s = Character("SPIDER", who_bold = False, color = '#35634d', what_prefix = '"', what_suffix = '"')

# The game starts here.

label start:

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

    scene background

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    show mur at Position(xpos = 96, xanchor = 0, ypos = 19, yanchor = 0)    
    show ara at Position(xpos = 267, xanchor = 0, ypos = 5, yanchor = 0)

    # These display lines of dialogue.

    w "..."
    w "Hmm..."
    w "..."
    w "...eh?"
    show ridle with dissolve
    w "Hey!"
    w "You there!"
    w "Are you okay?"
    w "What are you doing here?"
    w "..."
    w "You don't look from around here. So squishy..."
    w "..."
    w "..."
    w "..."
    w "Not much for words, aye?"
    w "It's okay."
    w "You're not the first one to get lost in here, and surely not the last."
    w "But do not fret, I'll get you outta here."
    w "I'm #~@!?. Ye can just call me {color=#e35460}RIBERTO{/color}."
    r "I'll... uh... I'll just call you chum. Fits you pretty well."
    hide ridle
    show rflushed
    r "Aye, nice to meet you, chum!"
    hide rflushed
    show ridle
    r "Now let's get going, shall we?"
    r "There is one thing you need to know first, though."
    r "This dungeon we're trapped in... It's 'magical', y'see."
    r "Actually, the only one stuck in here is you!"
    r "I'm this dungeon's Lord."
    hide ridle
    show rflushed
    r "Self-proclaimed, must confess. Left living here for all eternity. "
    r "Well, 'undying', rather."
    r "At least these dusty old bones have kept this house of mine nice and clean all these years!"
    hide rflushed
    show ridle
    r "Anyway, this dungeon... doesn't have an exit."
    r "Nor an entrance."
    r "Not until its user desires to. This vault is ever-changing."
    r "And I may be a cool, humerous and a bit of a bonehead, but I'm not its user."
    r "That's you, chum!"
    r "The reason why you're here with me may be something you been struggling with. Emotions, life and the like."
    r "You humans are complex beings, yet so powerful."
    r "Or maybe it was purely by chance. The whim of fate."
    r "Anyhow, to catalyze your feelings into an opening I'll need you to tell me about them."

    r "...\\ \n \% "

    # This ends the game.
    return
