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

# --- AURA GLOW VARIANT (Scene 06-07) ---
image Aura_uniform_glow = Transform("images/scene6/Aura_uniform_glow.png", zoom=1.5, yoffset=300)

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

    alice "Just one more chapter… then I'll head back to the dorm."

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

    alice "Midnight?! You've got to be kidding me."
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
    alice "I've been walking straight this whole time."

    play sound "audio/scene1/foot_step.mp3" volume 1.0

    scene hallway_3 at fullscreen_cover with dissolve

    alice "No… no way. This feels like déjà vu."

    scene library_hallway at fullscreen_cover with dissolve

    alice "I swear I passed this staircase already."

    stop sound fadeout 0.5

    alice "I'm tired…"

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

    alice "I can't keep doing this… none of this makes sense anymore."

    play sound "audio/scene2/reading.mp3"

    alice "…That sound again."

    "{i}A faint golden glow flickers between the dusty bookshelves.{/i}"

    alice_speak "Hello…? Is someone there?"

    stop sound fadeout 0.5

    show Aura_neutral with dissolve

    $ cinematic = True

    aura "So… you really can see me."
    alice "She doesn't look like a normal student."
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

    aura "A fracture created when a person's mind reaches its limit."
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

    alice_speak "Why can't you do it yourself?"

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
    alice "But if she's telling the truth… then this may be the only way out."

    hide Aura_smile
    show Aura_relieved at right
    aura "Will you help me?"

    pause 2.0

    hide Alice_neutral
    show Alice_smile at left
    alice_speak "…Alright."
    alice_speak "I'll do it."

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

    alice "…I'm back in the library."

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
    return


# =============================================================================
# SCENE 06: THE RESET
# LOCATION: The Archive Veranda / Main Archives Entrance
# TIME: Midnight (00:00)
# =============================================================================

label scene_06:

    # --- SFX: Space fold transition from previous scene ---
    play sound "audio/scene6/sfx_space_fold.mp3"

    scene bg_archive_veranda at fullscreen_cover with dissolve

    play music "audio/scene6/bgm_cozy_tea.mp3" volume 0.5 fadein 1.5

    alice "The harsh, fluorescent lights of the Science Wing vanish, replaced by the scent of fresh night air and jasmine."
    alice "I'm standing on a secluded wooden veranda attached to an older, gothic section of the library."

    # --- Aura appears seated with tea set ---
    show Aura_uniform_glow at right with dissolve

    play sound "audio/scene6/sfx_tea_pour.mp3" volume 0.7

    aura "Three major stabilizing fragments have been secured."
    aura "The constellations are grounded, and the rivalry of the Alchemists is mended."
    aura "This requires gratitude."

    "{i}A soft blue steam curls from a porcelain teacup on the bench beside Aura.{/i}"

    aura "Please, drink. This tea is brewed from the 'Echo of Comfort'."
    aura "It will help clarify your memory for what is to come."

    # --- Tea interaction prompt ---
    "{b}SYSTEM:{/b} Click on the teacup to drink."

    $ cinematic = True

    # Simple imagebutton for the teacup
    show screen tea_interaction_screen

    $ tea_result = ui.interact()

    hide screen tea_interaction_screen

    play sound "audio/scene6/sfx_teacup_click.mp3" volume 0.8

    $ cinematic = False

    alice_speak "Thank you, Aura. It feels real."
    alice_speak "For a moment, I almost forget I'm trapped in a loop."

    aura "That is the danger of this space. The respite is temporary."
    aura "Even now, the memory of the past is fighting to reset."
    aura "You must maintain your critical thinking."

    aura "The 'Timeline Puzzle' in the Main Archives isn't just a lock for you to pick."
    aura "It is the literal spine of my world and yours, tangled together in a knot."
    aura "If you cannot arrange the events correctly, the loop won't just reset your night—"
    aura "—it will begin to erase your history, piece by piece."

    # --- Transition to Main Archives Door ---
    stop music fadeout 1.5

    play sound "audio/scene6/sfx_door_thrum.mp3" volume 0.6 loop

    scene bg_main_archives_door at fullscreen_cover with dissolve

    play music "audio/scene6/bgm_heavy_tension.mp3" volume 0.6 fadein 1.5

    alice_speak "Aura… usually you just whisper in my head through the bookmark."
    alice_speak "Why are you walking beside me now?"

    aura "The Main Archives are the foundation of the Temporal Blindspot."
    aura "The 'static' of the Great Forgetting is loudest there."
    aura "A tether would be shredded by the distortion."

    aura "We are here. The 'Chronos Scale' lies beyond these doors."
    aura "Steel your mind, Alice."
    aura "The 'Great Forgetting' will try to lie to you one last time."
    aura "Stay focused. Trust your observations, not your eyes."
    aura "Shall we finish this?"

    stop sound fadeout 0.3

    play sound "audio/scene6/sfx_iron_doors.mp3" volume 1.0

    # --- Screen shake for doors slamming open ---
    $ renpy.pause(0.2)
    with hpunch

    scene bg_main_archives_door at fullscreen_cover with dissolve

    jump scene_07


# =============================================================================
# SCENE 07: THE ESCAPE
# LOCATION: Main Archives - The Chronos Scale
# TIME: Midnight (00:00)
# =============================================================================

# --- Teacup interactive screen (used in Scene 06) ---
screen tea_interaction_screen():
    imagebutton:
        xalign 0.3
        yalign 0.65
        idle Transform("images/scene6/teacup.png", zoom=0.4)
        hover Transform("images/scene6/teacup_glow.png", zoom=0.42)
        action Return(True)

label scene_07:

    # --- Setup puzzle weight variables ---
    $ weights_bank = [
        {"year": 1950, "value": 4.0,  "label": "1950  (4 u)"},
        {"year": 1975, "value": 1.0,  "label": "1975  (1 u)"},
        {"year": 2000, "value": 2.0,  "label": "2000  (2 u)"},
        {"year": 2025, "value": 1.0,  "label": "2025  (1 u)"},
        {"year": 2030, "value": 0.5,  "label": "2030  (0.5 u)"},
    ]
    $ scale_left  = []
    $ scale_right = []

    scene bg_main_archives_interior at fullscreen_cover with dissolve

    play sound "audio/scene7/sfx_heavy_air_hum.mp3" volume 0.5 loop

    show Aura_uniform_glow at right with dissolve

    alice "The air here feels like it is made of lead."
    alice "In the center of the room stands a towering, ancient brass contraption…"
    alice "…the Chronos Scale."

    aura "This is the 'Weight of History,' Alice."
    aura "Every event in the Lost Record has a specific temporal mass."
    aura "To unlock the gear and mend the spine of time, the scales must be perfectly balanced."
    aura "But the 'Great Forgetting' has begun to corrupt the data."
    aura "You cannot trust what is written; you must trust how they behave."

    # --- Phase 1: Puzzle testing and inference ---
    "{b}SYSTEM:{/b} Test the weights on the scale to discover their true values."

    play sound "audio/scene7/sfx_scale_slam.mp3" volume 0.8

    alice "Wait… According to the labels, 2030 should be heavy—"
    alice "—but the 1950 weight slams the platter down instantly!"
    alice "The past carries significantly more mass here. The labels are lies."

    alice "Let me calculate the true values based on the dial reaction…"
    alice "1975 is the Standard Unit — Value: 1."
    alice "That means 2030 is 0.5 units, 2000 is 2 units, 2025 is 1 unit,"
    alice "and 1950 is a staggering 4 units."

    # --- Phase 2: Final Balance Interaction ---
    "{b}SYSTEM:{/b} Place the weights to balance the Chronos Scale. Left must equal Right."

    $ cinematic = True

    # Evaluate totals and needle text dynamically inside screen via expressions
    python:
        def get_left_total():
            return sum(w["value"] for w in scale_left)
        def get_right_total():
            return sum(w["value"] for w in scale_right)
        def get_needle_text():
            l = get_left_total()
            r = get_right_total()
            if l == 0 and r == 0:
                return "— empty —"
            diff = l - r
            if diff == 0:
                return "✦ 0.0 — BALANCED"
            elif diff > 0:
                return f"Left heavy  +{abs(diff):.1f}"
            else:
                return f"Right heavy  +{abs(diff):.1f}"

    $ left_total  = get_left_total()
    $ right_total = get_right_total()
    $ needle_text = get_needle_text()

    show screen chronos_scale_screen

    $ puzzle_result = ui.interact()

    hide screen chronos_scale_screen

    $ cinematic = False

    # --- Chains groan and needle locks ---
    play sound "audio/scene7/sfx_chains_groan.mp3" volume 0.8
    pause 1.2
    play sound "audio/scene7/sfx_chime_final.mp3" volume 0.9
    pause 0.6
    play sound "audio/scene7/sfx_gear_unlock.mp3" volume 1.0

    hide Aura_uniform_glow
    show Aura_smile at right with dissolve

    aura "You've done it, Alice."
    aura "You looked past the lies of the 'Forgetting' and found the balance."
    aura "The spine of time is mended."

    # --- Blinding flash transition ---
    stop sound fadeout 0.5

    play sound "audio/scene7/sfx_blinding_flash.mp3" volume 1.0

    scene white with Fade(0.05, 0.0, 1.2)

    stop music fadeout 1.0

    # --- Dissolve back to Ethereal desk, then amber library desk ---
    scene bg_library_desk_waking at fullscreen_cover with fade

    hide Aura_smile

    show Aura_smile at right with dissolve

    play music "audio/scene7/bgm_solitude.mp3" volume 0.5 fadein 2.0

    play sound "audio/scene7/sfx_clock_tick_normal.mp3" volume 0.3 loop

    aura "The contract is fulfilled, Alice."
    aura "You have stabilized the echoes and mended the path back to your world."
    aura "When you wake, my face may fade into an imperfect memory—"
    aura "—but the balance you found tonight is yours to keep."
    aura "Go now. Your future is waiting."

    # --- Aura gives a final knowing nod, light folds inward ---
    "{i}Aura gives a final knowing nod and a bright smile as the light folds inward around her.{/i}"

    hide Aura_smile with dissolve

    # --- Alice wakes ---
    alice "My neck is stiff… my arm is numb."
    alice "The clock on the wall ticks softly: 00:01 AM."
    alice "The loop is gone. The oppressive silence has lifted."

    "{i}The desk comes into focus — Alice's notes are no longer a jumble. They are arranged in a perfect, logical sequence.{/i}"

    alice "Did I just fall asleep?"
    alice "But look at my notes… they're arranged in a perfect, logical sequence."
    alice "And in the margin of my notebook, there's a hand-drawn sketch of a perfectly aligned constellation."

    alice "I know someone was there…"
    alice "I think I said thank you."
    alice "But the face and name slip through my fingers like sand."

    # --- Alice walks toward the exit ---
    play sound "audio/scene7/sfx_footsteps_outgoing.mp3" volume 0.7 loop

    alice "I feel a sudden, quiet magnetic tug to stay in the shadows for one more minute…"
    alice "…as if I might hear the clink of a teacup or see a flicker of cerulean steam."
    alice "But I need to move forward."
    alice "I don't know why, but the midnight air feels so much lighter now."
    alice "I'm not as tired as I used to be."

    stop sound fadeout 1.5
    stop music fadeout 2.5

    # --- End credits ---
    scene black with fade

    play music "audio/scene7/bgm_end_credits.mp3" volume 0.7 fadein 2.0

    # Trigger your credits screen or next label here
    jump end_credits

label end_credits:
    # Replace with your actual credits screen call when ready
    scene black
    "[ END CREDITS ROLL ]"
    return
