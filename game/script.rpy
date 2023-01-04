# The script of the game goes in this file.
default blink_timerb = renpy.random.randint(2, 4)
default blink_timers = renpy.random.randint(2, 4)

init python:
    def blinkb(trans, st, at):
        global blink_timerb

        if st >= blink_timerb:
            blink_timerb = renpy.random.randint(4, 8)
            return None
        else:
            return 0

    def blinks(trans, st, at):
        global blink_timers

        if st >= blink_timers:
            blink_timers = renpy.random.randint(6, 9)
            return None
        else:
            return 0

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("RIBERTO")
define b = Character("BAT")
define s = Character("SPIDER")

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

    scene background

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show riberto flushed
    show mur at Position(xpos = 96, xanchor = 0, ypos = 19, yanchor = 0)    
    show ara at Position(xpos = 267, xanchor = 0, ypos = 5, yanchor = 0)

    # These display lines of dialogue.

    r "..."
    r "Hello!"
    r "Aye, nice to meet you, chum!"
    r "...\\ \n \" \" working? "
    b "\"soy un murcielago\""
    s "\"soy una araña\""
    r "\"paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf\""
    r "\"paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf\""
    r "\"paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf\""
    r "\"paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf\""
    r "\"paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf\""
    r "\"paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf\""
    r "\"paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf\""
    r "\"paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf\""
    r "\"paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf\""
    r "\"paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf\""
    r "\"paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf\""
    r "\"paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf\""
    r "\"paoiipfodpfoiewjapofijslñdkjfoawiee fjlakksdjfñoaiwefñjla aksjdfñlkajsdfñlajeofjñaslkdf\""

    # This ends the game.

    return
