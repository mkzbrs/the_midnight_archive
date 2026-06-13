define new_chapter = "audio/scene2/new_chapter.mp3"

label chater_intro(title, subtitle=""):


    window hide
    play sound new_chapter

    show text "{size=32}{color=#CCCCCC}" + title + "{/color}{/size}" at truecenter
    with dissolve
    $ renpy.pause (2.5, hard=True)
    hide text

    show text "{size=70}{color=#FFFFFF}" + subtitle + "{/color}{/size}" at truecenter
    with dissolve
    $ renpy.pause (2.0, hard=True)
    hide text with dissolve

    return

define config.gl2 = True
transform blurred:
    blur 10

transform enblur:
    blur 0
    linear 1 blur 10

transform deblur:
    blur 10
    linear 1 blur 0


transform flip_horizontal:
    xzoom -1.0
    xanchor 1.0

transform pulse_fadeout:
    alpha 1.0
    linear 0.4 alpha 0.3
    linear 0.4 alpha 1.0
    linear 0.4 alpha 0.3
    linear 0.4 alpha 1.0
    linear 0.4 alpha 0.3
    linear 0.4 alpha 1.0
    linear 0.4 alpha 0.3
    linear 0.4 alpha 1.0
    linear 1.5 alpha 0.0