# --- CHARACTER DEFINITIONS ---

# --- ALICE SPRITES ---
image Alice_neutral = Transform("images/scene2/Alice_neutral.png", zoom=1.5, yoffset=300)
image Alice_scared = Transform("images/scene2/Alice_scared.png", zoom=1.5, yoffset=300)
image Alice_surprised = Transform("images/scene2/Alice_surprised.png", zoom=1.5, yoffset=300)
image Alice_curious = Transform("images/scene2/Alice_curious.png", zoom=1.5, yoffset=300)
image Alice_smile = Transform("images/scene2/Alice_smile.png", zoom=1.5, yoffset=300)

# --- AURA SPRITES ---
image Aura_neutral = Transform("images/scene2/Aura_neutral.png", zoom=1.5, yoffset=300)
image Aura_thinking = Transform("images/scene2/Aura_thinking.png", zoom=1.5, yoffset=300)
image Aura_smile = Transform("images/scene2/Aura_smile.png", zoom=1.5, yoffset=300)
image Aura_relieved = Transform("images/scene2/Aura_relieved.png", zoom=1.5, yoffset=300)
image Aura_sad = Transform("images/scene2/Aura_sad.png", zoom=1.5, yoffset=300)

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

transform center_zoom:
    align (0.5, 0.5) 
    ease 1.5 zoom 2.5 alpha 0.0

# --- INTERACTIVE SCREENS ---
screen find_clock_screen():
    imagebutton:
        xalign 0.47  
        yalign 0.25
        
        idle Transform("scene1/clock.png", zoom=0.57)
        
        hover Transform("scene1/clock_glow.png", zoom=0.25) 

        action Return()

# --- SCENE 2 SETTINGS ---
define alice_speak = Character("Alice")
define aura = Character("Aura", color="#ffffff")
image white = Solid("#ffffff")

# --- SCENE 1 & 2 INTEGRATED ---
label start:
    show border onlayer UI

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

    # 🛠️ FIXED: String completed properly here to clear your line 85 parsing crash!
    play sound "audio/scene1/waking_up.mp3"
    pause 1.0

    scene library_night at fullscreen_cover with fade

    alice "Ugh… my neck hurts."
    alice "Wait… why is it so dark?"
    
    alice "Where is the clock?"

    "{b}SYSTEM:{/b} Find and click on the wall clock."

    $ cinematic = True

    pause 2.0

    scene library_clock at fullscreen_cover with dissolve

    call screen find_clock_screen
    
    play sound "audio/scene1/clock_bell.mp3" volume 0.5

    $ cinematic = False

    "{i}The clock on the wall rang: 00:00.{/i}"

    # 🎵 Mysterious background melody starts here right after midnight is shown
    play music "audio/scene2/bgm_mysterious_melody.mp3" volume 0.6 fadein 2.0

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

    scene hallway_3 at fullscreen_cover with dissolve

    pause 2.0

    play sound "audio/scene1/foot_step.mp3" volume 0.7

    scene library_night at fullscreen_cover with dissolve

    alice "…Wait."
    alice "Why does this place look the same?"
    alice "I’ve been walking straight this whole time."

    play sound "audio/scene1/foot_step.mp3" volume 1.0

    scene hallway_3 at fullscreen_cover with dissolve

    alice "No… no way. This feels like déjà vu."

    scene library_hallway at fullscreen_cover with dissolve

    alice "I swear I passed this staircase already."

    stop sound fadeout 0.5

    alice "I’m tired…"

    show library_hallway at lower_camera

    alice "Maybe I should rest for a second and think."

    pause 2.0

    play sound "audio/scene1/reading_book.mp3" volume 1.0

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

    scene bookshelves at fullscreen_cover with fade

    play sound "audio/scene2/foot_step.mp3" volume 0.5

    alice "I can’t keep doing this… none of this makes sense anymore."

    play sound "audio/scene2/reading.mp3"

    alice "…That sound again."

    "{i}A faint golden glow flickers between the dusty bookshelves.{/i}"

    alice_speak "Hello…? Is someone there?"

    stop sound fadeout 0.5

    show Aura_neutral with dissolve

    $ cinematic = True

    aura "So… you really can see me."
    alice "She doesn’t look like a normal student."
    alice "Her uniform feels old… almost ceremonial. Like she came from another era entirely."

    aura "Follow me."

    show Aura_neutral at center_zoom

    # 🎵 Fade out the mysterious sound as they enter the Ethereal
    stop music fadeout 0.5

    play sound "audio/scene2/door_open.mp3"

    # Play Ethereal theme music track
    play music "audio/scene2/ethereal_bgm.mp3" volume 0.6 fadein 2.0

    scene ethereal at fullscreen_cover with dissolve

    show Aura_smile at right
    show Alice_curious at left

    alice_speak "…Where am I?"

    aura "This place is called the Ethereal."
    aura "A space hidden between memory and reality."
    
    hide Aura_smile
    show Aura_neutral at right

    aura "You are trapped inside a Temporal Blindspot."

    alice_speak "Temporal… what?"

    aura "A fracture created when a person’s mind reaches its limit."
    aura "Time loops. Spaces repeat. Memories become unstable."

    hide Aura_neutral
    show Aura_smile at right

    aura "That is why the hallways kept bringing you back."

    hide Alice_curious
    show Alice_scared at left
    alice_speak "Then all of that was real…?"

    aura "Real enough."

    show echo at truecenter with dissolve

    hide Aura_smile
    show Aura_thinking at right
    aura "Scattered across this campus are fragments known as Echoes."
    aura "They are pieces of lost memories connected to something called the Lost Record."

    hide Alice_scared
    show Alice_curious at left
    alice_speak "And the puzzles?"

    hide Aura_thinking
    show Aura_neutral at right
    aura "The Echoes are sealed behind them."
    aura "Solve the puzzles, recover the Echoes, and the Lost Record can finally be unraveled."

    alice_speak "Why can’t you do it yourself?"

    hide Aura_neutral
    show Aura_sad at right
    aura "Because I no longer belong to your reality."
    aura "I can guide you… but only you can interact with what remains inside the campus."

    hide echo with dissolve
    show archivist_bookmark at truecenter with dissolve

    hide Aura_sad
    show Aura_smile at right
    aura "Take this."
    aura "The Archivist Bookmark."
    aura "As long as you carry it, I will be able to communicate with you from the Ethereal."

    hide Alice_curious
    show Alice_neutral at left
    alice_speak "This is insane…"
    alice "But if she’s telling the truth… then this may be the only way out."

    hide Aura_smile
    show Aura_relieved at right
    aura "Will you help me?"

    pause 2.0

    hide Alice_neutral
    show Alice_smile at left
    alice_speak "…Alright."
    alice_speak "I’ll do it."

    stop music fadeout 2.0

    play sound "audio/scene2/sfx_magical_glow.mp3"

    scene white with Fade(0.1, 0.0, 0.5)

    scene bookshelves at fullscreen_cover with fade
    show Alice_surprised at left

    play sound "audio/scene2/door_close.mp3"
    
    # 🎵 Ethereal scene is done, bring back default mysterious track
    play music "audio/scene2/bgm_mysterious_melody.mp3" volume 0.6 fadein 1.5

    alice_speak "Wait—"

    hide Alice_surprised

    show Alice_neutral at left

    $ cinematic = False

    alice "…I’m back in the library."

    play sound "audio/scene2/quest_accept.mp3"
    "{b}OBJECTIVE:{/b} Solve puzzles and gather Echoes."

    show bookshelves at enblur
    show Alice_neutral at left, enblur
    call chater_intro("Puzzle I", "JUXTAPOSITION")
    show bookshelves at deblur
    show Alice_neutral at left, deblur

    stop music fadeout 3.0

# --- TARGET TRANSITION LABEL ---
# 🛠️ FIXED: Formatted the label properly so Ren'Py knows exactly where to transition at the end!
label map_screen:
    scene black with dissolve
    "The game successfully transitioned to the map screen phase!"
    return