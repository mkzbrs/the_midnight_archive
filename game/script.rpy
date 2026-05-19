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

# --- SCENE 2 SETTINGS ---
define alice_speak = Character("Alice")
define aura = Character("Aura", color="#d4af37")
image white = Solid("#ffffff")

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

    play sound "audio/scene1/page_turn.mp3"

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

    scene library_clock at fullscreen_cover

    call screen find_clock_screen
    
    play sound "audio/scene1/clock_bell.mp3" volume 0.5

    "{i}The digital clock on the wall blinks: 00:00.{/i}"

    alice "Midnight?! You’ve got to be kidding me."
    alice "The gates are probably locked already."

    play sound "audio/scene1/getting_up.mp3"

    alice "Okay… calm down. Just head to the main entrance."

    play sound "audio/scene1/foot_step.mp3"

    scene grand_staircase at fullscreen_cover with dissolve

    alice "The grand staircase should lead straight outside."

    play sound "audio/scene1/foot_step.mp3" volume 0.7

    scene library_hallway at fullscreen_cover with dissolve

    alice "Right side corridor… that should be the exit."

    scene library_hallway1 at fullscreen_cover with dissolve

    scene library_hallway2 at fullscreen_cover with dissolve

    scene library_hallway1 at fullscreen_cover with dissolve

    alice "…Wait."
    alice "Why does this hallway look the same?"
    alice "I’ve been walking straight this whole time."

    play sound "audio/scene1/foot_step.mp3" loop volume 1.0

    alice "No… no way. This feels like déjà vu."

    scene library_hallway2 at fullscreen_cover with dissolve

    alice "I swear I passed this staircase already."

    stop sound fadeout 0.5

    alice "I’m tired…"

    show library_hallway2 at lower_camera

    alice "Maybe I should rest for a second and think."

    pause 2.0

    play sound "audio/scene1/reading_book.mp3" volume 0.4

    alice "…What was that?"

    play sound "audio/scene1/reading.mp3" volume 0.8

    alice "Someone else is here."
    alice "But… the library was empty."

    show library_hallway at slow_zoom

    alice "Hello…?"

    scene black

    jump scene_02

# --- SCENE 2 STARTS HERE ---
label scene_02:

    # SYSTEM: [Display bookshelves.jpeg]
    scene bookshelves at fullscreen_cover with fade

    # SYSTEM: [Play foot_step.mp3 softly]
    play sound "audio/scene2/foot_step.mp3" volume 0.5
    
    # SYSTEM: [Play bgm_mysterious_melody]
    play music "audio/scene2/bgm_mysterious_melody.mp3" volume 0.6 fadein 2.0

    # SYSTEM: [Display SPRITE Alice_scared.png]
    show Alice_scared at left with dissolve

    alice "I can’t keep doing this… none of this makes sense anymore."

    # SYSTEM: [Play page_turn.mp3]
    play sound "audio/scene2/page_turn.mp3"

    alice "…That sound again."

    # SYSTEM: [A faint golden glow appears between the bookshelves]
    "{i}A faint golden glow flickers between the dusty bookshelves.{/i}"

    alice_speak "Hello…? Is someone there?"

    # SYSTEM: [Display SPRITE Aura_neutral.png]
    show Aura_neutral at right with dissolve

    aura "So… you really can see me."

    # SYSTEM: [Display SPRITE Alice_surprised.png]
    hide Alice_scared
    show Alice_surprised at left

    alice "She doesn’t look like a normal student."
    alice "Her uniform feels old… almost ceremonial. Like she came from another era entirely."

    # SYSTEM: [Sprite Aura_neutral.png slowly walks past Alice]
    show Aura_neutral at center with ease

    aura "Follow me."

    # SYSTEM: [Play door_open.mp3]
    play sound "audio/scene2/door_open.mp3"

    # SYSTEM: [Transition dissolve to ethereal.jpeg]
    scene ethereal at fullscreen_cover with dissolve

    # We have to re-show the characters because changing the 'scene' clears the screen
    show Aura_thinking at right
    show Alice_curious at left

    alice_speak "…Where am I?"

    aura "This place is called the Ethereal."
    aura "A space hidden between memory and reality."
    
    show Aura_neutral at right
    aura "You are trapped inside a Temporal Blindspot."

    alice_speak "Temporal… what?"

    aura "A fracture created when a person’s mind reaches its limit."
    aura "Time loops. Spaces repeat. Memories become unstable."
    aura "That is why the hallways kept bringing you back."

    hide Alice_curious
    show Alice_scared at left
    alice_speak "Then all of that was real…?"

    aura "Real enough."

    # SYSTEM: [Display echo.png floating faintly in the background]
    # 'truecenter' puts the image exactly in the middle of the screen
    show echo at truecenter with dissolve

    show Aura_thinking at right
    aura "Scattered across this campus are fragments known as Echoes."
    aura "They are pieces of lost memories connected to something called the Lost Record."

    hide Alice_scared
    show Alice_curious at left
    alice_speak "And the puzzles?"

    show Aura_neutral at right
    aura "The Echoes are sealed behind them."
    aura "Solve the puzzles, recover the Echoes, and the Lost Record can finally be unraveled."

    alice_speak "Why can’t you do it yourself?"

    # Assuming Adam draws an Aura_sad.png, since neutral doesn't fit the emotion here
    show Aura_sad at right
    aura "Because I no longer belong to your reality."
    aura "I can guide you… but only you can interact with what remains inside the campus."

    # SYSTEM: [Display archivist_bookmark.png]
    hide echo with dissolve
    show archivist_bookmark at truecenter with dissolve

    show Aura_smile at right
    aura "Take this."
    aura "The Archivist Bookmark."
    aura "As long as you carry it, I will be able to communicate with you from the Ethereal."

    hide Alice_curious
    show Alice_neutral at left
    alice_speak "This is insane…"
    alice "But if she’s telling the truth… then this may be the only way out."

    show Aura_relieved at right
    aura "Will you help me?"

    # SYSTEM: [Pause for 2 seconds]
    pause 2.0

    # Assuming Adam draws an Alice_smile.png!
    hide Alice_neutral
    show Alice_smile at left
    alice_speak "…Alright."
    alice_speak "I’ll do it."

    # SYSTEM: [Play sfx_magical_glow]
    play sound "audio/scene2/sfx_magical_glow.mp3"

    # SYSTEM: [Screen flashes brightly]
    scene white with Fade(0.1, 0.0, 0.5)

    # SYSTEM: [Fast transition dissolve back to bookshelves.jpeg]
    scene bookshelves at fullscreen_cover
    show Alice_surprised at left
    
    alice_speak "Wait—"

    # SYSTEM: [Play door_close.mp3]
    play sound "audio/scene2/door_close.mp3"

    hide Alice_surprised
    show Alice_neutral at left
    alice "…I’m back in the library."

    # SYSTEM: [Display objective text: “Solve puzzles and gather Echoes.”]
    "{b}OBJECTIVE:{/b} Solve puzzles and gather Echoes."

    # SYSTEM: [Fade out BGM slowly]
    stop music fadeout 3.0

    # SYSTEM: [The game begins]
    jump map_screen