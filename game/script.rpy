# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("RIBERTO")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image background:
        "images/bg00.png"
        pause 0.2
        "images/bg01.png"
        pause 0.2
        "images/bg02.png"
        pause 0.2
        "images/bg03.png"
        pause 0.2
        repeat

    scene background

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show riberto flushed

    # These display lines of dialogue.

    r "..."
    r "Hello!"
    r "Aye, nice to meet you, chum!"
    r "...\\ \n \" \" working? "

    # This ends the game.

    return
