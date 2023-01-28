# The script of the game goes in this file.
default blink_timer_a = renpy.random.randint(2, 4)
default blink_timer_b = renpy.random.randint(3, 6)

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

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("RIBERTO", who_bold = False, what_prefix = '"', what_suffix = '"')
define b = Character("BAT", who_bold = False, color = '#35608b', what_prefix = '"', what_suffix = '"')
define s = Character("SPIDER", who_bold = False, color = '#35634d', what_prefix = '"', what_suffix = '"')

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

    "..."
    "..."
    "..."
    show rflushed with dissolve
    r "Hello!"
    r "Aye, nice to meet you, chum!"
    r "...\\ \n \% "
    b "soy un murcielago"
    s "soy una araña"
    r "paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf"
    r "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean turpis tellus, placerat eu dictum quis, 
    mattis sed lorem. Proin imperdiet neque vitae rutrum consectetur. Phasellus molestie risus sed tellus consequat, 
    elementum ullamcorper ex commodo. Vivamus ac facilisis odio."
    r "paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf"
    r "paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf"
    r "paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf"
    r "paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf"
    r "paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf"
    r "paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf"
    r "paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf"
    r "paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf"
    r "paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf"
    r "paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf"

    # This ends the game.

    return
