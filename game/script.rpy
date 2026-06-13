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

transform pulsing:
    align (0.5, 0.5)
    ease 1.0 zoom 1.05
    ease 1.0 zoom 0.95
    repeat

# --- INTERACTIVE SCREENS ---
screen find_clock_screen():
    imagebutton:
        xalign 0.47  
        yalign 0.25
        
        idle Transform("scene1/clock.png", zoom=0.57)
        
        hover Transform("scene1/clock_glow.png", zoom=0.25) 

        action Return()

screen find_lamp_screen():
    imagebutton:
        xalign 0.217  
        yalign 0.716
        
        idle Transform("images/interface/puzzle1/ancient_oil_lamp.png", zoom=0.36)
        hover Transform("images/interface/puzzle1/ancient_oil_lamp_glow.png", zoom=0.36) 

        action Return()

screen find_typewriter_cassette_screen():
    default typewriter_found = False
    default cassette_found = False

    if not typewriter_found:
        imagebutton:
            xalign 0.71
            yalign 0.62
            idle Transform("images/interface/puzzle1/typewriter.png", zoom=0.469)
            hover Transform("images/interface/puzzle1/typewriter_glow.png", zoom=0.469)
            action [SetScreenVariable("typewriter_found", True), If(cassette_found, Return())]

    if not cassette_found:
        imagebutton:
            xalign 0.538
            yalign 0.65
            idle Transform("images/interface/puzzle1/cassette_player.png", zoom=0.4)
            hover Transform("images/interface/puzzle1/cassette_player_glow.png", zoom=0.4)
            action [SetScreenVariable("cassette_found", True), If(typewriter_found, Return())]

screen find_astronomy_page_screen():
    imagebutton:
        xalign 0.5
        yalign 0.8
        idle Transform("images/scene4/astronomy_page.png", zoom=0.2)
        hover Transform("images/scene4/astronomy_page_glow.png", zoom=0.2)
        action Return()

screen constellation_selection():
    imagebutton:
        xalign 0.2
        yalign 0.3
        idle Transform("images/scene4/libra.png", zoom=0.5)
        hover Transform("images/scene4/libra_glow.png", zoom=0.5)
        action Return("libra")
    
    imagebutton:
        xalign 0.8
        yalign 0.2
        idle Transform("images/scene4/draco.png", zoom=0.5)
        hover Transform("images/scene4/draco_glow.png", zoom=0.5)
        action Return("draco")

    imagebutton:
        xalign 0.3
        yalign 0.7
        idle Transform("images/scene4/aries.png", zoom=0.5)
        hover Transform("images/scene4/aries_glow.png", zoom=0.5)
        action Return("aries")

    imagebutton:
        xalign 0.7
        yalign 0.8
        idle Transform("images/scene4/leo.png", zoom=0.5)
        hover Transform("images/scene4/leo_glow.png", zoom=0.5)
        action Return("leo")

# --- SCENE 2 SETTINGS ---
define alice_speak = Character("Alice")
define aura = Character("Aura", color="#ffffff")
image white = Solid("#ffffff")


# --- PUZZLE 1 SETTINGS ---
define PUZZLE1_ITEMS = ["ancient_oil_lamp", "typewriter", "cassette_player"]
define PUZZLE1_CORRECT = ["ancient_oil_lamp", "typewriter", "cassette_player"]

default selected_item = None
default slot_1 = None
default slot_2 = None
default slot_3 = None

# --- SCENE 1 & 2 INTEGRATED ---
label start:
    show border onlayer UI
    show screen hud #For fast travel, relocate this to be after the ethereal.

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

    $ cinematic = True

    pause 2.0

    scene library_clock at fullscreen_cover with dissolve

    call screen find_clock_screen
    
    play sound "audio/scene1/clock_bell.mp3" volume 0.5

    $ cinematic = False

    "{i}The clock on the wall rang: 00:00.{/i}"

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

    stop music fadeout 0.5

    play sound "audio/scene2/door_open.mp3"

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
    
    play music "audio/scene2/bgm_mysterious_melody.mp3" volume 0.6 fadein 1.5

    alice_speak "Wait—"

    hide Alice_surprised

    show Alice_neutral at left

    $ cinematic = False

    alice "…I’m back in the library."

    show bookshelves at enblur
    show Alice_neutral at left, enblur
    call chater_intro("Puzzle I", "THE STABILIZATION TRIAL")
    play sound "audio/scene2/quest_accept.mp3"
    show bookshelves at deblur
    show Alice_neutral at left, deblur

    stop music fadeout 3.0
    jump scene_03

# --- SCENE 3 STARTS HERE ---
label scene_03:

    scene bookshelves at fullscreen_cover with fade
    play sound "audio/scene3/sfx_clock_tick_normal.mp3" loop
    play music "audio/scene3/bgm_eerie_ambient.mp3" volume 0.5 fadein 2.0

    alice "Ugh... my head. Did I... fall asleep? Was it all just a dream?"
    alice "Maybe it's best if I just leave."
    "{i}Alice starts walking, then pauses.{/i}"
    alice "Wait, there's something in my pocket."

    play sound "audio/scene3/sfx_bookmark_pulse.mp3"
    $ cinematic = True
    show archivist_bookmark at truecenter with dissolve

    alice "It's the Archivist."

    play sound "audio/scene3/sfx_aura_voice_echo.mp3"
    show Aura_neutral at right with dissolve
    aura "I told you, it is not a dream."

    alice_speak "Aura? It... it's real?"

    aura "Yes, it is reality. Focus, Alice. What do you need to do next?"

    alice_speak "I don't know, tell me what to do."
    hide Aura_neutral with dissolve
    $ cinematic = True
    show Aura_smile at right with dissolve

    aura "Look to the relics of the past to stabilize the present. Walk through time, not away from..."

    hide archivist_bookmark with dissolve
    hide Aura_smile with dissolve
    $ cinematic = False
    "{i}Alice fumbles and drops the Archivist on the floor. Aura's voice cuts out abruptly.{/i}"

    alice_speak "Aura? Where did you go?"

    "{i}Alice grabs the Archivist from the floor.{/i}"
    $ cinematic = True
    show archivist_bookmark at truecenter with dissolve
    show Aura_neutral at right with dissolve

    play sound "audio/scene3/sfx_aura_voice_echo.mp3"
    aura "I told you that you can only see and interact with me while holding the Archivist. Do not drop it again. Now, proceed to the specialized hallway section."
    aura "Follow the path, Alice. Do not lose your focus, or the reality will fracture again. Keep your grip firm on the Archivist."

    alice_speak "I understand. I'm moving toward the hallway now."

    hide archivist_bookmark with dissolve
    hide Aura_neutral with dissolve
    $ cinematic = False
    scene library2_puzzle1 at fullscreen_cover with dissolve

    alice_speak "Hey, what is that on the table?"

    show Aura_neutral at right with dissolve
    aura "Pick those 3 items up and let's see what's the quest you need to do."

    "{b}SYSTEM:{/b} Find and click on the oil lamp."
    call screen find_lamp_screen

    alice_speak "3? This is only one, let's find another 2."

    scene library1_puzzle2 at fullscreen_cover with dissolve
    "{b}SYSTEM:{/b} Find and click on the remaining 2 items."
    call screen find_typewriter_cassette_screen

    alice_speak "There they are."

    alice "An ancient oil lamp, a mechanical typewriter, and a plastic cassette player..."
    alice_speak "What do I need to do with this?"

    aura "Swap those three items in chronological order."

    hide Aura_neutral with dissolve

    jump puzzle_1

#----- Puzzle 1 label -----
label puzzle_1:

    $ selected_item = None
    $ slot_1 = None
    $ slot_2 = None
    $ slot_3 = None

    call screen arrange_interface_screen()

    if _return == True:
        play sound "audio/scene3/sfx_echo_stabilize.mp3"
        alice_speak "You are right, we need to arrange it in this evolution timeline. I am a brilliant girl!"
        $ cinematic = True
        show echo at truecenter with dissolve
        aura "Well reasoned, Alice. You have stabilized the first fragment. Now, proceed to the next area."

        hide echo with dissolve
        $ cinematic = False
        play sound "audio/scene3/sfx_wall_dissolve.mp3"

        scene black with dissolve
        "{i}The back wall dissolves to reveal a real, physical path leading deeper into the school.{/i}"
        
        jump scene_04
    else:
        play sound "audio/scene3/sfx_reality_ripple.mp3"
        with hpunch
        alice "Hurm... that's wrong I think. Technology? Evolution? What is the true order?"
        aura "I don't know, what's your idea?"
        jump puzzle_1

# --- SCENE 4 STARTS HERE ---
label scene_04:
    scene puzzle2_library at fullscreen_cover with dissolve

    alice "This hallway just keeps going..."

    "{b}SYSTEM:{/b} Find and click on the shining object."
    call screen find_astronomy_page_screen

    play sound "audio/scene4/sfx_paper_pickup.mp3"
    show overlay_astronomy_page at truecenter with dissolve
    "{b}SYSTEM:{/b} Torn Astronomy Page obtained."

    alice "A page... it lists four constellations in a specific order: 1. Libra, 2. Draco, 3. Aries, and 4. Leo. This must be the sequence Aura mentioned."

    hide overlay_astronomy_page with dissolve
    play sound "audio/scene4/sfx_space_fold.mp3"
    scene white with Fade(0.1, 0.0, 0.5)
    scene school_courtyard at fullscreen_cover with fade

    alice_speak "Wait what? How can I teleport here?"
    alice_speak "Let me grab the Archivist and ask Aura."

    play sound "audio/scene4/sfx_bookmark_activate.mp3"
    $ cinematic = True
    show archivist_bookmark at pulsing
    
    play sound "audio/scene4/sfx_aura_voice_echo.mp3"
    show Aura_neutral at right with dissolve
    aura "The page is a focal point of this memory, Alice. It pulled you to where the connection is strongest."
    aura "Now, grip the Archivist. Focus on the sky. I will guide you through the sequence one by one. Do not rush."

    hide archivist_bookmark
    hide Aura_neutral
    with dissolve

    play music "audio/scene4/bgm_astral_ambient.mp3" volume 0.5 fadein 2.0
    scene starry_sky at fullscreen_cover with dissolve

label constellation_puzzle_loop:
    scene starry_sky at fullscreen_cover with dissolve
    $ cinematic = False
    
    # Step 1: Libra
    $ cinematic = True
    play sound "audio/scene4/sfx_aura_voice_echo.mp3"
    aura "First, the Scales of Libra. Look for two pans held in balance, forming a wide triangle against the dark. Select them."
    $ cinematic = False

    call screen constellation_selection()
    if _return != "libra":
        jump constellation_fail

    play sound "audio/scene4/sfx_blink.mp3"
    $ cinematic = True
    aura "Perfectly balanced. Proceed."
    $ cinematic = False

    # Step 2: Draco
    $ cinematic = True
    play sound "audio/scene4/sfx_aura_voice_echo.mp3"
    aura "Now, the dragon, Draco. Trace the long, winding serpent of light that curls into a wide U-shape across the expanse."
    $ cinematic = False

    call screen constellation_selection()
    if _return != "draco":
        jump constellation_fail

    play sound "audio/scene4/sfx_blink.mp3"
    $ cinematic = True
    aura "The dragon is tamed. Keep going."
    $ cinematic = False

    # Step 3: Aries
    $ cinematic = True
    play sound "audio/scene4/sfx_aura_voice_echo.mp3"
    aura "Next, the ram, Aries. Seek the gentle arch of curved horns. It is the simplest shape, like a soft, singular stroke in the sky."
    $ cinematic = False

    call screen constellation_selection()
    if _return != "aries":
        jump constellation_fail

    play sound "audio/scene4/sfx_blink.mp3"
    $ cinematic = True
    aura "The path is clear. One remains."
    $ cinematic = False

    # Step 4: Leo
    $ cinematic = True
    play sound "audio/scene4/sfx_aura_voice_echo.mp3"
    aura "Finally, the lion, Leo. Look for the majestic mane—the brightest and most crowded cluster of stars commanding the night."
    $ cinematic = False

    call screen constellation_selection()
    if _return != "leo":
        jump constellation_fail

    play sound "audio/scene4/sfx_blink.mp3"

    # Success
    $ cinematic = True
    play sound "audio/scene4/sfx_echo_collect.mp3"
    show echo at truecenter with dissolve

    play sound "audio/scene4/sfx_aura_voice_echo.mp3"
    aura "Well done, Alice. You have stabilized the second fragment. You are learning quickly."
    $ cinematic = False
    hide echo with dissolve


    "{b}SYSTEM:{/b} Destination Unlocked: Next Puzzle Area"
    
    scene black with dissolve
    jump scene_06

label constellation_fail:
    scene starry_sky at fullscreen_cover with dissolve
    play sound "audio/scene4/sfx_thunder.mp3"
    with vpunch
    $ cinematic = True
    aura "That is not the correct star, Alice! The memory is fracturing—hold the bookmark tight!"
    
    scene black with dissolve
    pause 1.0
    jump constellation_puzzle_loop

label scene_06:
    scene bg_archive_veranda at fullscreen_cover with fade

    play music "audio/scene6/bgm_solitude_calm.mp3" volume 0.5 fadein 2.0

    alice "The heaviness of the archives vanishes. The air here is cool, sweet, and smells faintly of jasmine."

    aura "Congrats, Alice. You've now completed the requirements to unlock the exit doors. Now watch this as I do the magic."

    play sound "audio/scene6/sfx_magic_sparkle.mp3"

    aura "Kachingggggg. A letter forms from those two echoes. These are the spells for you to read whenever you're ready to exit."

    alice_speak "Wait, Aura. I don't want to say goodbye to you just like that."

    show Aura_smile at right with dissolve

    aura "Sit, Alice. You have earned this silence."

    "{i}Alice sits.{/i}"
    play sound "audio/scene6/sfx_tea_pour.mp3"

    alice_speak "I... I don't know how to thank you. Or how to thank myself."

    aura "Consider it a debt paid to the library. Without you, I would have drifted in the static forever."

    alice_speak "Who are you, Aura? Truly?"

    hide Aura_smile
    show Aura_neutral at right
    with dissolve

    aura "I was an archivist here, a century ago. When the first crack appeared in the record, I tried to mend it using the Echoes. I failed, and the distortion consumed me. I became a ghost of my own duty, tethered to the bookmark you hold."

    alice_speak "You've been here for a hundred years?"

    aura "Time has little meaning in a loop. But today, it finally ends."

    "{i}Aura pushes a cup toward Alice.{/i}"

    aura "Drink. It is the last of the jasmine I harvested before the silence took the garden."

    "{i}Alice takes a sip.{/i}"
    alice_speak "It's... warm. It's the first thing that's felt real all night."

    aura "That is because you are waking up, Alice. The loop is broken."

    alice_speak "Will I see you again?"

    aura "The library has many secrets, but this specific memory will fade. Once you leave, the distortion resets to a normal night. You will go back to your studies, and I... I will finally find rest."

    show Aura_neutral at pulsing

    aura "Goodbye, Alice. Thank you for walking through the dark with me."

    play sound "audio/scene6/sfx_wind_chime.mp3"
    scene white with Fade(2.0, 0.0, 2.0)

    jump scene_07

label scene_07:
    scene bg_library_exit_door at fullscreen_cover with dissolve

    alice_speak "It's time."

    play sound "audio/scene7/sfx_magic_sparkle.mp3"
    alice_speak "Through the archives, past the tide, open the path where memories hide."

    play sound "audio/scene7/sfx_door_opening.mp3"
    scene white with Fade(0.5, 1.0, 0.5)

    scene bg_library_desk_start at fullscreen_cover with fade

    play sound "audio/scene7/sfx_clock_chime.mp3"

    alice_speak "Seven... seven o'clock? It was all just a dream?"

    "{i}Alice feels a sense of relief, gathers her belongings, and stands up quickly.{/i}"

    alice_speak "Enough studying for tonight. It's time to go home."

    scene black with fade

    return