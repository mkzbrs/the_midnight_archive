

label start:

    menu:
        "Choose scene to test"

        "Introduction":
            jump introduction

        "midnight":
            jump midnight

label introduction:

    scene library_noon at bg_default with fade

    play music "chillmusic/escapism.mp3" volume 0.5

    "The clock on the wall ticks softly."

    "2:41 PM."
    
    play sound "audio/page_turn_sound_effect.mp3" volume 0.3
    "You flip another page."

    "The words blur for a moment… then settle."
    play sound "audio/bird_sound_effect.mp3" fadein 0.3 volume 0.2

    "You've been here longer than you planned."

    "But it's quiet tonight."
    
    "Unusually quiet."
    stop sound fadeout 0.2

    "No footsteps between shelves."

    "No distant chatter."

    "Even the librarian hasn't made their rounds."

    "..."

    "You should leave."

    "..."
    
    play sound "audio/page_turn_sound_effect.mp3" volume 0.3
    "Just one more page."

    scene library_after_noon at bg_default with dissolve
    "Time passes."

    "The clock reads 6:58 PM."

    "You dont remember the last few pages."

    "Your eyes sting."

    "The lines of text begin to overlap… slipping out of focus."
    $ renpy.music.set_volume(0.2, delay=2.0)

    show black:
        alpha 0.0
        linear 0.5 alpha 0.5
        pause 0.2
        linear 0.5 alpha 0.0

    "You blink."

    show black:
        alpha 0.0
        linear 0.5 alpha 0.7
        pause 0.2
        linear 0.5 alpha 0.0

    "Once."

    show black:
        alpha 0.0
        linear 0.5 alpha 0.8
        pause 0.2
        linear 0.5 alpha 0.2

    "Twice."
    stop music fadeout 2.0

    "The silence feels… deeper now."

    "Like the building itself is holding its breath."

    "You rest your head on your arm."

    "Just for a second."

    scene black with fade

    play sound "audio/breathing_sound_effect.mp3" volume 0.2 fadein 0.1


    "..."

    "Darkness."

    jump midnight
    

label midnight:

    "...."
    
    play sound "audio/metal_sound_effect.mp3" fadein 0.2

    "A sound."
    "Kinda like.."
    "Metal shifting..?"
    "You open your eyes."

    scene library_night at bg_default with fade

    play sound "audio/cricket_sound_effect.mp3" volume 0.9 fadein 0.3

    "A pale light stretches across the floor."
    "Through the window."
    "Moonlight."
    "Your eyes sting."
    "Just a habit, you glance at your watch."
    "00:00, midnight."
    "..."
    '"What a perfect coincidence"..you think.'
    "You should probably get going."
    
    stop sound fadeout 0.2

    scene black with fade
    
    play sound "audio/getting_up_sound_effect.mp3" volume 0.4
    "You start packing your stuffs."

    "Standing up, you sling your bag over your shoulder."

    play sound "audio/foot_step_sound_effect.mp3" volume 0.5
    pause 3.0
    stop sound fadeout 1.5

    "It's time to go."
    
    jump grand_staircase



default staircase_loop = 0

label grand_staircase:

    "...."

    if staircase_loop == 0:
        "You continue walking deeper into the library, searching for an exit."
        "The silence is oppressive, broken only by the sound of your footsteps."

        "Rows upon rows of books stretch into the dark."
        "For a moment, you can't tell if you're passing new ones… or the same ones again."

        "....."
        "You fasten your pace."
        "Trying to not get lost in your own thoughts."
        
        "It's been a minute, maybe two."
        "And then-you see it."
        "The Grand Staircase of the library."
        "It rises at the heart of the library, carved with intricate detail,"
        "its steps spiraling upward into shadow."
        "You've passed it countless times before."

        "But tonight... it feels different."

        "Moonlight spill through the glass dome above,"
        "laying fractured patterns of light and shadow across the steps."

        "..."
        "For a moment, you stop."
        '"Forget it. I need to leave."'
    elif staircase_loop == 4:
        jump window
        
    "The exit should be at the right of the staircase."



    menu:
        "Where to go?"

        "Go to the right":
            jump go_right
        
        "Go to the left" if staircase_loop >= 2:
            jump go_left
        
        "Go up the staircase" if staircase_loop >= 2:
            jump go_up


    
    
label go_right:

    "You head right."

    if staircase_loop == 0:
        "As someone who regularly visits the library, you know the layout well."
        "You keep on walking."
        "As you walk, you notice something odd."
        "It feels longer than it should."
    elif staircase_loop >= 1:
        "As you walk, you notice something odd again."
        '"I dont remember this corridor being this long.."'

    "....."
    "You slow down."
    "Something isn't right."
    "Then-"
    "You stop."
    "It's the Grand Staircase."
    "Again."

    $ staircase_loop += 1


    jump grand_staircase



label go_left:
    "You take the left path."

    if staircase_loop == 2:
        "The path to the left is quieter."
        "Your footsteps sound… softer here."
        "You take a few steps."
        "The shelves seem taller than before."
        "...No."
        "They weren't this tall."
        "The shelves feel… closer here."
    
    elif staircase_loop == 3:
        "You take your chance to go left again."
        "Hoping that maybe this time, it will lead you somewhere else."
        "Few steps in-"
        "You stop."
        "The silence feels wrong immediately."
    

    "For a moment, you consider turning back."
    
    "....."
    "You slow down."
    "Something isn't right."
    "Then-"
    "You stop."
    "It's the Grand Staircase."

    $ staircase_loop += 1
    
    jump grand_staircase


label go_up:
    "You decide to climb the Grand Staircase."

    if staircase_loop == 2:
        "The steps creak under your weight as you ascend."
        "The air grows colder, and the shadows deepen."
        "Shadows stretch along the walls of the staircase."
        "Reaching the second floor, you walk through the dimly lit corridor."
        "Taking a look at the side, you see averanda."
        "The moonlight casts long shadows across the floor."
        "Halfway through, you stop."
        "Something drifts in the air."
        "..."
        '"...Why does it smell like tea?"'
        "You speak to yourself."
        "It's faint."
        "But too precise to ignore."

    elif staircase_loop == 3:
        "You climb the staircase again."
        "The air feels heavier this time."
        "The shadows seem to move on their own."
        "Reaching the second floor, you walk through the dimly lit corridor again."
        "The moonlight casts long shadows across the floor again."
        "Halfway through, you stop again."
        "The smell of tea is stronger now."
        '"I know its here."'
      
    "....."
    "You slow down."
    "Something isn't right."
    "Then-"
    "You stop."
    "It's the Grand Staircase."
    
    $ staircase_loop += 1
    
    jump grand_staircase



label window:
    "You feel exhausted."
    "The library seems to stretch endlessly around you."
    "You can't tell how long you've been wandering."

    "With a slight breath left, you decide to walk on to the nearest window."
    "The moonlight is brighter here."
    "You then look out, hoping to see the school grounds outside."
    
    "For a moment, all you see is darkness."
    "Which isn't how window supposed to work."

    "A faint reflection begins to form in the window."

    "A girl stands there."

    "Messy hair."
    "Tired eyes."
    "A uniform slightly wrinkled from endless wandering."

    "..."

    "You stare at her."
    "And she stares back."

    "The moonlight behind you should've revealed the school couryard."
    "But the window reflects only the library."
    "Only you."

    alice "...Me?"

    "The girl in the glass tilts her head slightly."
    "So do you."

    "You slowly raise a hand."
    "The girl mirrors you."
    "A second too late."
    "But still.. Perfectly."

    alice "...Who..."

    "Your voice comes out dry."
    "Weaker than you expected."

    "...Who am I again...?"

    "The question slips out before you can stop it."

    "Pale skin."
    "Dark circles beneath tired eyes."
    "A name slowly surfaces in your mind."

    alice "...Alice."

    "Alice."

    "You repeat it quietly."
    "Like testing whether it still belongs to you."

    alice "...Is this really me?"

    "You press your hand against the glass."

    "It's freezing."

    alice "...How long have I been here?"

    "No answer comes."
    "Alice keeps staring at the reflection."

    "But the girl in the glass no longer feels distant."

    "She just looks... tired."

    "The exhaustion hits all at once."

    "Her legs tremble."
    "Her thoughts grow slower."
    "Even breathing feels heavier now."

    "Alice: Leaning against a bookshelf, sliding down to the floor)"
    alice "I can't... Im too tired for this."

    "Her vision blurs. The mental exhaustion that had been weighing on her all day finally takes its toll. She rests her head in her hands, the silence of the library now feeling heavy and suffocating."

    "The moonlight from the window barely reaches her now."

    "The endless shelves stand quietly around her."

    alice "Just for a little while..."

    "Her voice is barely above a whisper."

    "She pulls her knees closer to herself."
    "Her eyes slowly drift shut."

    "The library remains completely still."

    "No footsteps."
    "No turning pages."
    "Only silence."

    "And before Alice realizes it—"

    "Sleep quietly takes her."

    jump encounter
    return

label encounter:
    "..."

    "A dull sound pulls Alice out of her sleep."

    "Thump."

    "A book closing."

    "Slide."

    "The quiet scrape of something being moved across wood."

    "Alice slowly opens her eyes."

    "For a moment, she forgets where she is."

    "Then the endless shelves surrounding her return all at once."

    "The library."

    "..."

    "Another sound echoes nearby."
    "Soft."
    "Methodical."

    "As if someone is carefully rearranging books."

    "Alice stiffens."

    "She slowly lifts her head and peers through the narrow gap between two thick encyclopedias beside her."

    "A faint golden light glows at the far end of the aisle."

    "And within it—"

    "A girl stands quietly between the shelves."

    "She wears a school uniform unlike anything Alice has seen before."
    "The design is rigid and ornate."
    "Old-fashioned."
    "Almost ceremonial."

    "She moves with strange precision."
    "Taking books from the shelves."
    "And carefully rearranging them."

    "Alice swallows nervously."

    "Alice: (Whispering)"

    alice "Hello...?"

    "The girl stops."

    "A thick leather-bound book remains suspended in her hands."

    "For several seconds, she doesn't move."

    "Then—slowly—"

    "She turns her head toward Alice."

    "Her eyes are calm."
    "Too calm."

    "There is no surprise in them."
    "Only quiet curiosity."
    "And something ancient hidden beneath it."

    "Alice: (...Is someone there?)"

    "The girl's gaze lingers on her."

    "As if studying something she wasn't expecting to find."

    mysterious_girl "...You can see me?"

    "Alice slowly pushes herself upright."
    "Her legs tremble from exhaustion."

    "Up close, the girl doesn't resemble a student at all."

    "She feels like something preserved from another age."
    "A forgotten figure hidden between the pages of history."

    "The golden light around her flickers softly across the shelves."

    mysterious_girl "That shouldnt be possible."

    jump encounter2  


label encounter2:
    "The girl quietly closes the book in her hands."

    "The sound echoes through the aisle."

    "She steps away from the shelves, the faint golden light following her movements."

    'Mysterious Girl: (Turning slowly toward Alice)'

    mysterious_girl "You are only here because your mind was pushed beyond its limit."

    "Alice stays silent."

    "Her tired eyes remain fixed on the strange girl before her."


    mysterious_girl "This place is called a Temporal Blindspot."
    mysterious_girl"A space where memory and reality no longer behave correctly."

    "The library around them creaks softly."
    "As if responding to her words."

    mysterious_girl "The exhaustion, the endless looping halls, the distorted reflections..."
    mysterious_girl "They are all connected."

    Alice "...Loop?"

    'mysterious girl gives a small nod.'

    mysterious_girl "You have been trapped inside one."

    "A cold silence settles between the shelves."

    "Alice instinctively tightens her grip on her sleeve."

    
    alice "Then... how do I leave?"

    "For the first time, the mysterious girl pauses."

    
    mysterious_girl "There is a way."
    mysterious_girl "But not yet."

    "She slowly approaches."
    "Her ornate uniform glimmers faintly in the darkness, carrying an elegance that feels completely detached from the modern world."

    mysterious_girl "My name is Aura."

    "The name sounds unfamiliar."
    "And strangely old."

    aura "I can return you to your world."
    aura"But first, the Lost Record must be unraveled."

    "Aura glances toward the open library doors behind her."

    "Beyond them lies only darkness."
    "And shifting hallways that seem deeper than before."


    aura "There are Echoes scattered throughout this campus."
    aura "I cannot reach, some of them"

    "Her eyes meet Alice's."

    
    aura "But you can."

    "The golden light around Aura flickers softly."

    aura "If you wish to understand what is happening to you..."
    aura "Follow me."


    "Alice doubts and hesitates for a moment."
    "But her leg says otherwise, moving undeliberately."

    "After a moment, the footsteps fade into the distance."
    "and the library falls silent once more."

    jump a_palace_beyond_time


label a_palace_beyond_time:

    "The library doors close behind them with a distant echo."
    "Aura walks ahead without hesitation."
    "Her footsteps are soft against the wooden floor."
    "Measured."
    "Certain."

    "Alice follows closely behind."

    "The deeper they move into the library, the stranger the air begins to feel."
    "The shelves seem taller here."
    "The shadows longer."

    alice "Where are we going?"
    "Her voice sounds smaller than before."

    alice "I've already checked every inch of this floor."
    "There are no other exits."

    "Aura continues walking calmly through the dim aisle."
    aura "You searched with eyes that only understand the present."
    "The golden glow surrounding her faintly illuminates the shelves beside them."

    
    aura "But inside a Temporal Blindspot..."
    aura "Paths do not always remain where they should."

    "They stop at the farthest corner of the library."

    "There are no books here."
    "No windows."
    "Only a cold stone wall buried beneath layers of darkness."

    "Alice stares at it blankly."
    alice "...This is just a dead end."

    "A nervous laugh escapes her."
    alice "We're just going to loop back to the staircase again, aren't we?"

    "Aura finally turns toward her"
    aura "Not if I choose otherwise."

    "The air suddenly grows heavy."
    "Alice instinctively steps back."
    "Aura slowly raises her hand toward the wall."

    "Soft golden light spills from her fingertips."
    "At first faint."
    "Then brighter."

    "The stone surface ripples."
    "Like disturbed water."
    "Alice freezes."
    "Lines of light begin carving themselves into the wall."

    "Elegant."
    "Ancient."
    "Unfamiliar symbols intertwining across the stone."
    "A deep hum vibrates through the floor beneath them."

    "And then—"
    "A door appears."
    "A massive wooden door emerges from the wall itself, its surface adorned with ornate patterns matching Aura's uniform."

    alice "...What..."
    "She stumbles backward slightly."
    alice "It... it wasn't there before."

    "Aura lowers her hand slowly."
    aura "It was always here, Alice."
    "Her calm eyes rest on the newly formed door."
    aura "It merely required the right key."

    "Aura places her hand against the handle."
    "For the first time since meeting her, her expression grows serious."
    aura "Beyond this door lies the truth of your situation."

    "The golden light around the doorway pulses softly."
    aura "I will explain everything there."
    "She looks back toward Alice."

    aura "What remains..."
    aura "is whether you possess the courage to remember."

    "The library falls silent once more."
    jump the_contract



label the_contract:

    "Alice hesitates only briefly before stepping through the doorway."
    "The moment she crosses the threshold—"
    "The air changes."
    "The dusty scent of old books disappears, replaced by the sharp smell of ozone and ancient stone."

    "She stops immediately."
    "Her breath catches in her throat."
    "The library is gone."

    "Above her, the ceiling has vanished entirely."
    "In its place churns an endless vortex of indigo clouds and distant stars."
    "It pulses slowly."
    "Like the heartbeat of something enormous sleeping beyond the dark."

    "Massive bookshelves drift silently through the air."
    "Weightless."
    "Ancient."
    "Like ruins submerged beneath an invisible ocean."

    "A magnificent wrought-iron chandelier hangs impossibly beneath the cosmic void, adorned with glowing blue and amber crystals."
    "Their light flickers softly across the chamber."

    "Alice slowly turns."

    "In the center of the room stands a massive desk wrapped tightly in twisting tree roots."
    "Small glowing leaves bloom from the wood."
    "Floating scrolls and luminous pages drift lazily through the air around an enormous open tome resting atop the desk."

    "Alice's voice trembling"
    alice "This..."
    alice "This can't be real."

    "Her eyes remain fixed on the endless sky overhead."

    alice "Where are we?"

    "Aura walks toward the root-covered desk."
    "Her silhouette cuts sharply against the starlight."

    aura "You have been pulled into a Temporal Blindspot."
    alice "..What?"
    aura "A fracture formed by the collapse of time and memory."
    aura "The loop you've experienced before.."
    aura "is one of it's major effects."
    "Her voice echoes softly through the chamber."

    aura "It is rare."
    aura "Only minds pushed to the edge of severe exhaustion can perceive the cracks..."
    aura "and fall into them."

    "Aura rests a hand gently against the desk."
    "The floating pages around her shift slightly."

    aura "This place is called the Ethereal."
    "The heart of the Blindspot."

    "The chandelier above flickers."

    aura "Unlike the shifting halls outside, the Ethereal exists beyond time."
    aura "Memories do not decay here."
    aura "And neither does the Lost Record."

    "Alice slowly approaches the desk, still overwhelmed by the impossible space around her."

    alice "...Lost Record?"

    "Aura turns toward her."

    "The crystal light reflects within her calm eyes."

    aura "Long before the year 2030..."
    aura "Something went wrong within this school."
    "The floating pages around the chamber begin drifting more slowly."

    aura "A fracture formed in the past."
    aura "And with it, the memories tied to this place began to decay."

    "Distant whispers echo faintly through the Ethereal."
    "Voices fading before they can fully be heard."

    aura "Events were forgotten."
    aura "Records vanished."
    aura "Entire moments in history began to deteriorate as though they had never existed at all."

    "She gently places her hand against the massive tome resting on the desk."

    aura "I am the Memory Keeper."
    aura "I preserve what remains."

    "She pauses."

    "But the memories of this school did not disappear completely."
    "A small glowing fragment materializes above Aura's hand."
    "It flickers faintly like a dying flame."

    aura "They shattered into fragments known as Echoes."
    aura "Pieces of memory and history scattered throughout the campus."

    "The fragment briefly shows distorted images."
    "A classroom."
    "Students laughing."
    "A hallway that no longer exists."

    aura "I can preserve them..."
    aura "But I cannot retrieve them myself."

    "The glowing fragment dissolves into particles of light."
    "Aura steps closer."

    aura "But you are different from me."
    aura "A candidate."

    "The floating scrolls begin circling slowly around the desk."

    aura "You can interact with the remnants of memory."
    aura "You can recover the Echoes scattered throughout the distorted campus."

    aura "So..."
    aura "Let us form a contract."

    "Alice stiffens slightly."
  
    alice "...A contract?"

    
    aura"You help me restore the Lost Record."
    aura "And in return, I will guide you through the Blindspot..."
    aura "and return you to your world once everything is complete."

    "The floating pages continue drifting endlessly around them."

    alice "And if I don't want to?"

    "For the first time, Aura's expression darkens slightly."
    aura "Then your mind will continue to fracture."

    "The chamber grows quieter."

    aura "Every failed attempt in getting echoes creates imperfect memory."
    aura "The loop resets."
    aura "And you begin again."

    "A cold silence settles between them."
    "Far above, the vortex slowly churns."

    aura "The school you knew no longer exists as it once did."
    aura "She extends her hand toward Alice."

    aura "If you help me restore the Lost Record..."
    aura "I will mend the rift and return you home."

    "The glowing pages drift endlessly around them."

    aura "So... What do you say, Alice?"

    menu :
        "Accept the contract":
            jump contract_accepted

        "Refuse the contract":
            jump gift_and_goodluck

    
label contract_refused:
    alice "...No."

    "The word leaves her mouth quietly."
    "But firmly."

    "Aura remains completely still."
    "The floating pages around the chamber slow to a stop."

    alice "I don't even know who you are."
    alice "Or if anything you're saying is real."

    "Her exhausted voice trembles slightly."
   
    alice "You expect me to trust you because you opened some magic door and talked about memories?"

    "The silence that follows feels heavy."
    "The Ethereal hums softly around them."

    "Aura lowers her gaze for a brief moment."

    aura "I see."

    "She does not sound angry."
    "Only distant."

    "Aura slowly closes the massive tome resting on the desk."
    "The sound echoes unnaturally far through the chamber."
    aura "Then the Blindspot will decide for you instead."

    "Alice takes a small step back."
    alice "...What does that mean?"

    "Aura turns toward the swirling void above them."
    aura "It means the loops will continue."
    aura "Your memories will continue to erode."
    aura "And eventually..."

    "She pauses."

    aura "you will become another wandering fragment inside this place."

    "The floating shelves around them creak softly."
    "Somewhere in the distance, indistinct whispers begin echoing through the chamber."

    alice "You're lying..."

    aura "Am I?"

    "For the first time, the calmness in Aura's eyes feels unsettling."

    aura "Tell me, Alice."
    aura "How many times have you already walked those halls?"

    "Alice opens her mouth—"
    "But no answer comes."
    "Because she doesn't know."
    "Aura gently places a hand over the closed tome."

    aura "The moment you entered the Blindspot, your time began to decay."
    aura "Whether you accept the contract or not changes only one thing."

    "She finally looks back at Alice."

    aura "Whether your suffering has meaning."

    return

label gift_and_goodluck:
    "Alice lowers her gaze."
    "The swirling vortex above the Ethereal continues turning slowly."
    "Endlessly."

    "She looks at the floating shelves."
    "The glowing pages."
    "The impossible chamber existing beyond reality itself."

    "Then back at Aura."
    "The exhaustion in her body remains."
    "But now another feeling settles beside it."

    "Acceptance."
    alice "...I'll do it."

    "Her voice is quiet."
    "But certain."

    alice "If collecting these Echoes is the only way to get my life back..."
    "then we have a deal."

    "For the first time, Aura gives a faint smile."
    "It is small."
    "Almost imperceptible."
    "But genuine."

    "Aura slowly nods."
    aura "Then our paths are now connected."

    "She turns toward the massive tome resting atop the root-covered desk."
    "The ancient pages shift on their own as Aura gently reaches between them."
    "From within the book, she pulls out a slender object wrapped in soft indigo silk."

    aura "Take this."

    "She steps closer and places it into Alice's hands."
    "It is a bookmark."
    "Beautifully woven from deep indigo thread."
    "Silver runes shimmer across its surface, glowing faintly like moonlight reflected on water."

    "The moment Alice touches it—"
    "A strange warmth spreads through her palm."

    alice "...Warm?"

    "The bookmark softly hums."
    "Almost like a heartbeat."

    aura "It is a fragment of the Lost Record itself."
    aura "Fashioned into a tether."

    "Alice carefully turns it over in her hands."

    alice "It feels alive..."

    aura "In a way, it is."

    "The floating crystals above flicker gently."

    aura "This bookmark connects you to me..."
    aura "and to the Blindspot itself."

    "She slowly walks around the desk as she speaks."

    aura "If you become lost, focus your thoughts upon it."
    aura "No matter where you are within the school..."
    aura "I will hear you."

    "Alice grips the bookmark slightly tighter."


    aura "It also serves as a key."
    aura "As you stabilize memories and recover Echoes, pathways within the school will open to you."

    "The silver runes briefly glow brighter."

    aura "You will eventually learn to fold distance itself."
    aura "To return instantly to places you have restored."

    "Alice stares quietly at the glowing thread in her hand."

    "The impossible reality of everything still hasn't fully settled in."

    "But the warmth of the bookmark feels real."

    "Aura suddenly steps back."

    "Her form flickers faintly."
    "Like heat shimmering in the air."

    "Alice immediately looks up."

    alice "...Aura?"

    aura "Our contract is now sealed, Alice."
    "The Ethereal rumbles softly around them."

    aura "But remember this carefully."
    "Her voice becomes lower."
    "Sharper."

    aura "Understanding is the only thing that moves time forward."
    aura "If you stop thinking..."
    aura "you stop progressing."


    alice "Wait—then how am I supposed to—"

    "Aura raises her hand."

    aura "Sleep now, Alice."

    "The blue crystals hanging from the chandelier suddenly flare brightly."


    aura "When you awaken..."
    aura "the search will begin."

    "The light intensifies."

    aura "Seek the first Echo where history is preserved."

    "The chamber dissolves."
    "The floating shelves."
    "The vortex."
    "The roots."
    "The endless starlight."

    "Everything vanishes into blinding white."

    "....."
    "Alice blinks."
    "The cold scent of old paper returns instantly."
    "The Ethereal is gone."
    "She is sitting at her usual desk inside the school library."

    "The moonlight still shines faintly through the window."
    "The room is silent."
    "Normal."

    "Alice quickly looks around."
    "The endless cosmic chamber has disappeared completely."
    "Her breathing slows slightly."

    alice "...Was that... a dream?"

    "She glances at her watch."

    "00:00."

    "Midnight."
    "A cold chill runs down her spine."
    "Then she feels something still resting in her hand."
    "Alice slowly opens her fingers."

    "The indigo bookmark remains there."
    "Its silver runes glowing softly in the dark."

    "Alice stares at it silently."

    alice "...No."

    "She slowly stands from the desk."
    "The library doors remain closed."
    "But this time—"
    "She is no longer searching for a way out."

    "She is searching for a way to remember."

    #Testing connection with the github