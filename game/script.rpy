# --- CHARACTER DEFINITIONS ---
define alice = Character("Alice", what_italic=True)

# --- CUSTOM CAMERA EFFECTS ---
transform lower_camera:
    xysize (1920, 1080) 
    fit "cover" 
    align (0.5, 0.5)
    easein 2.0 yalign 1.0

transform slow_zoom:
    xysize (1920, 1080) 
    fit "cover" 
    align (0.5, 0.5)
    ease 3.0 zoom 1.5 align (0.5, 0.5)

transform fullscreen_cover:
    xysize (1920, 1080) 
    fit "cover" 
    align (0.5, 0.5) 

# --- INTERACTIVE SCREENS ---
screen find_clock_screen():
    imagebutton:
        xalign 0.35  
        yalign 0.65
        
        idle "scene1/clock.png"
        hover "scene1/clock_glow.png"
        
        at Transform(zoom=0.3)

        action Return()


# --- GAME START ---
label start:

    # SCENE 01: THE WAKE UP

    scene black
    pause 1.0
    
    scene library_noon at fullscreen_cover with fade

    play music "audio/scene1/bird.mp3" volume 0.3 fadein 1.0

    alice "Just one more chapter… then I’ll head back to the dorm."

    play sound "audio/scene1/page_turn.mp3"

    scene library_after_noon at fullscreen_cover with fade

    alice "The library always feels peaceful during asar. Quiet… warm… safe."

    alice "Maybe I should rest my eyes for a minute…"

    stop music fadeout 2.0
    scene black with fade
    pause 1.0

    play sound "audio/scene1/waking_up.mp3"
    pause 1.0

    scene library_night at fullscreen_cover with fade

    alice "Ugh… my neck hurts."
    alice "Wait… why is it so dark?"
    
    alice "Where is the clock?"

    "{b}SYSTEM:{/b} Find and click on the wall clock."

    call screen find_clock_screen
    
    play sound "audio/scene1/page_turn.mp3" volume 0.5

    "{i}The digital clock on the wall blinks: 00:00.{/i}"

    alice "Midnight?! You’ve got to be kidding me."
    alice "The gates are probably locked already."

    play sound "audio/scene1/getting_up.mp3"

    alice "Okay… calm down. Just head to the main entrance."

    play sound "audio/scene1/foot_step.mp3"

    scene grand_staircase at fullscreen_cover with dissolve

    alice "The grand staircase should lead straight outside."

    play sound "audio/scene1/foot_step.mp3" volume 0.7

    alice "Right side corridor… that should be the exit."

    scene library_hallway at fullscreen_cover with dissolve

    alice "…Wait."
    alice "Why does this hallway look the same?"
    alice "I’ve been walking straight this whole time."

    play sound "audio/scene1/foot_step.mp3" loop volume 1.0

    alice "No… no way. This feels like déjà vu."
    alice "I swear I passed this staircase already."

    stop sound fadeout 0.5

    alice "I’m tired…"

    show library_hallway at lower_camera

    alice "Maybe I should rest for a second and think."

    pause 2.0

#    play sound "audio/scene1/aura_voice1.mp3" volume 0.4

    alice "…What was that?"

#    play sound "audio/scene1/aura_voice2.mp3" volume 0.8

    alice "Someone else is here."
    alice "But… the library was empty."

    show library_hallway at slow_zoom

    alice "Hello…?"

    scene black

    jump scene_02

label scene_02:
    pass