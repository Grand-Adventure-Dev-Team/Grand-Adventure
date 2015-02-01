# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# For picking the color of characters, use http://hslpicker.com

# Declare characters used by this game.
define l = Character('Lazarus', color="#70f")
define m = Character('Malvin', color="#0400ff")
define g = Character('Grey', color="#808080")
define v = Character('Vlad', color="#000000")
define k = Character('Knox', color="#000000")
define t = Character('Tiren', color ="#f0b")

image bg darkroom = "darkroom.png"
image bg PFentrance = "PFentrance.png"
image bg PFbar = "Pfbar.png"
image bg malroom = "malroom.png"
image bg vial = "malvial.png"
image bg alchemyroom = "alchemyroom.png"
image bg PFtable = "Pftable.png"
image bg jobboard = "jobboard.png"
image bg mudfield = "mudfield.png"
image bg gobbrain = "gobbrain.png"
image bg longbeard = "longbeard.png"
image bg gobbattle = "gobbattle.png"
image bg troops = "troops.png"
image bg troops charge = "troopscharge.png"
image bg gobcharge = "gobcharge.png"
scene bg troopcamp = "troopcamp.png"
image bg healing = "healing.png"
image bg healded = "healed.png"

image barkeep joyful = "barkeep_joyful.png"
image barkeep neutral = "barkeep_neutral.png"
image Lazarus irritated = "laziritated.png"
image Lazarus Shocked = "lazshocked.png"
image Lazarus neutral = "lazneutral.png"
image Malvin irritated = "Malirritated.png"
image Malvin neutral = "Malneutral.png"
image Vlad neutral = "Vladneutral.png"
image goblinfire = "gobfire.png"
image gobsil = "gobsil.png"
image soldier weary = "wearysoldier.png"
image knox neutral = "Knoxneutral.png"
image maiya neutral = "maiyaneutral.png"



label start:

    "Welcome... Adventurer. Pick ye path... Be ye Assassin, Knight or Wizard?"

    menu:
        "Asassin."
            jump choiceassassin

        "Knight."
            jump choiceknight

        "Wizard"
            jump choicewizard

label assassin:

    scene bg darkroom

    "hrg- wha a- ah... ahhggh"

    play music "After a Kill.ogg" loop

    "Ah, the sound of death."

    "A sound that I have heard many times by now. How long has it been, I wonder?"

    "Filled with hesitation when I made my first kill, I had to get used to it fast."

    "You had no choice. You had to get used to it. You get used to living the life of an..."

    "{color=#f00}Assassin{/color}"

    scene bg darkroom
    with dissolve

    pause 1

    scene bg PFentrance
    play music "Buisness as Usual.ogg" loop

    "I walk into the guild, as I am so often used to doing."

    "I say guild, but really it was just a glorified cave."

    "We had to stay out of the way of others, after all, we didn't want anyone to accidentily stumble upon our little gang here."

    "A booming voice ringsout from the bar area; a voice not fit to be an assassins."


    with Dissolve(1)

    scene bg PFbar
    show barkeep joyful

    "Barkeep" "Heya kid, you're back! How'd the job go?"

    "You" "Well enough. Had to dirty my blade but that's how it usually ends up."

    "He nods as he gets back to work."

    show barkeep neutral

    "That right there was Vic. His real name is Vicros Felchter, but everyone calls him Vic."

    "If you couldn't tell by his stained outfit, hes a bartender."

    "With that big potbelly of his and booming voice, he seems out of place to be in an assassin’s guild like the Python’s Fang or really any assassin’s guild. He has a different talent that proves his worth."

    "Vic’s an info broker. Half the time he works here in the guild and the other half he spends at the local town’s bar: What Ales You."

    "When he’s not able to be at one of the bars, his twin brother Malvin fills in for him when he can. I don’t think I’ve ever seen Vic in anything but a bartender outfit."

    "I say twin brother, but the truth is far from it. They have the same face, and everyone calls him Mal instead of Malvin, but everything else is the opposite for him."

    "Mal’s a skinny man with a nervous air about him, like he always has an appointment to go to."

    "Honestly, he’s a pretty lousy bartender too. I don’t know why he doesn’t just stop bartending and take the blade full time, since that’s all he seems to be good at. Unlike his brother, Mal takes on assassinations from time to time, his gaunt body working to his advantage."

    "I was only on one job with him before; and then I learned the truth."

    "Mal turns into a different man when he’s on the job. His nervous air disappears entirely; replaced with one that is business-like and to the point. He gets the job done and makes sure he gets the job done."

    "It’s Mal’s day off today, since the bar in town is going under reconstruction. Seems like a magical experiment or something went awry. I think I’ll go see him today: see what he’s up to."

    "Unfamilar voice" "Hey, I'm talking to you, buddy!"

    show lazarus irritated

    "My thoughts of seeing Mal are interrupted by someone I've never met before."

    "He had on a wierd looking hat. Must've thought it made him look tough or something. To me it looked absoloutly ridiculous."

    #---
    #“You’re in the wrong place. Western Bar Scenes is next door.”

    #“Look, I’m not wearing this thing because I want to. Now follow the script.”

    #“You’re no fun, Laz.”
    #---

    "You" "Who in the hells are you? Never seen your face around here."

    "Unfamiliar person" "Pretty rude way to greet a new member after ignoring him, buddy."

    # "I'm not your buddy, pal!"

    "You" "A new member? Great! You start first thing next week."

    "Unfamiliar really wierd person" "And now you're ordering me around like you're my new boss. Who in the hells are {i}you?{/i}"

    "You" "Your new boss, my names Grey!"

    show lazarsus shocked

    "The guy you just put in his place" "O-oh... I'm so very sorry. It's just that you looked so young, I-"

    g "Oh, you should’ve seen this one new guy. Did something similar to you. He was last seen...you know what, forget I said that. I just had a bad flashback."

    "The man with the weird hat gulps. This was getting better by the minute..."

    g "So what’s your name anyway, young blood?"

    show lazarus neutral

    "Lazarus" "Uh, L-Lazarus, sir. Lazarus Redfield."

    g "Well then, Laz, I’m off to meet with Mal. Go and get acquainted with the other members. You’ll want friends in a place like this..."

    g "Also, whatever you do, try not to make enemies. One wrong move and you’re dead on the floor with a dagger in your neck."

    "I draw my thumb across my neck to emphasize my point."

    "Lazarus gulps again as he reaches for his own neck."

    g "Also, talk to Vic and look for an available job. We’ll start when you think you’re ready or when I think you’re ready. Whichever comes first."

    l "Yes, sir."

    with dissolve(1)

    scene PFentrance

    "Now, to find Malvin."

    scene bg malroom

    "It seems that Malvin is a bit busy..."

    "He didn't notice me when I walk in. An idea pops into my head..."

    "..."


    "..."


    "..."


    g "Hi Mal!"

    "Malvin" "Gah!"

    scene bg vial

    "He jumps and the vial he’s holding bounces around in his hands. He lunges for it and tries to get ahold of it. The vial settles down in his hands after a few grabs."

    scene bg alchemyroom
    show Malvin Irritated

    m "D-d-don't do that! It almost spilled! Do you even know what could've happened if the poison got on me?!"

    g "...Maybe this wasn't such a good idea after all."

    "Its said that while Malvin was a bartender and assassin, but he was also our poison alchemist."

    g "Okay, fine. I'm sorry. So whats this about poison?"

    show Malvin Neutral

    m "Uhhh, this? It’s a new venom I’m developing. However, this version isn’t that potent, so I’m trying to combine it with this special mix of snake venom."

    "He points to the bowl and then the vial."

    g "So what does it do? Anything special or just kill people faster?"

    m "If my theory is right, then this will be revolutionary in assassinations."

    g "So is this your normal revolutionary or will it actually make a difference?"

    m "H-hey, I worked hard on this!"

    g "Don't be so touchy all the time. Tell me what it does, for Thanatos's sake."

    m "Oh, fine. It’s a very volatile substance, and when applied a significant pressure change: it’ll dissipate and bedaub the quarry."

    g "Okay, you know that my vocabulary isn’t that big. In Common, please."

    m "You throw it and it covers the target in the poison."

    g "Oh... wait, what?"

    m "You didn't even get that dumbed down explaination?!"

    g "Not that, just the idea in general."

    m "What do you mean?"

    g "Well, how does the poison kill the target?"

    m "By burning them ali-... oh."

    "He finally gets it."

    g "You see it now?"

    m "Yes. Burning them alive would be problematic for a quiet assassination."

    "Ah, Mal, always missing the little things."

    g "You could probably sell it to the army. I'm sure that would be really popular."

    "Mals face lit up when I said that, but frowned again."

    m "No, that won't work."

    g "Why not?"

    m "The materiels I used for this are pretty rare. I had only intended for this to be used by our guild, so I don’t have enough to make a market for it."

    g "Good point."

    m "I heard a rumor about a new recruit. Did he report to you yet?"

    play sound "table_crash.ogg"
    play music "Trouble.ogg"

    g "Please don't let that be him."

    scene bg PFtable
    show Lazarus irritated at right
    show Vlad neutral at left

    "Man with the Skeleton Mask" "Seems you have some anger problems, new guy. Assassins with anger problems never last long. It seems that you want an early grave and a place of your own in one of the nine hells."

    "Uh-oh. This isn't good."

    g "Lazarus!"

    "I quickly rush over to try and protect Lazarus from Vlad."

    g "What the nine hells are you doing? I thought I made it pretty clear to try and not make enemies!"

    show lazarus neutral

    l "Hes the one looking to make enemies. No respect. Who is he, anyway?"

    g "He’s the one I was telling you about earlier. Remember, the one who took that new guy and left each body part in- wait, that was a different guy. Uhh..., ah! Vlad here was the one who ************************."

    show lazarus shocked

    #l "He did what?"

    #g "He ************************"

    #l "What does * mean?"

    #g "Woah. Haven’t heard that much vulgar language since my days with Lion’s Paw. Uhh, let’s just say you don’t want to know..."

    "Lazarus looks at Vlad with a new sense of fear."

    "Vlad. The Grim Reaper of Python’s Fang."

    "There are many rumors about him. No one knows the truth, not even the rest of the guild."

    "His weapon of choice is obviously the scythe."

    "Some say he’s a vampire, and that his scythe sucks out his victim’s blood, then he drinks it privately straight from the blade."

    "Others say that he’s an undead, which is why he hides behind his cloak and skeleton mask. He joined an assassin’s guild in the hopes of finding and killing the one who slew him."

    "Other rumors even claim that Vlad is Death himself, ruler of the Nine Hells."

    "Offshoots of this theory say that he’s one of Death’s agents sent to this plane. This one makes the most sense to me, since his assassin skills seem otherworldly."

    v "Gray, this one is yours, correct? Do you mind if I take him to my domain?"

    g "Yes, actually. I’ve been on recruit duty for months now. I want this one to survive long enough for me to get a break."

    v "Very well. I’ll see him soon enough, so it doesn’t matter. I can wait."


    show Lazarus Neutral
    play music "Buisness as usual.ogg" loop

    "...Creepy."

    "He's obivously enjoying himself. You'd think he started those rumours himself."

    g "Okay, Laz. Let’s get you on your first job before you get yourself killed, Thanatos forbid, you make me happy. Hey, Vic! What jobs are available?"

    scene bg PFbar
    show barkeep neutral

    "Vic" "Slow week this time. Only 6 jobs avaliable. Ahnd half of them seem too tough for a guy's first mission."

    "I take a look at the job list."

    scene bg jobboard

    "Hm, Vics right. Looks like only 3 missions available and doable. I don’t even know what Lazarus is even capable of, let alone what jobs are suited for him. Hmmm... "

    "{i}Job, cutting off the tail of the Lemur{/i}"
    "{i}Reward: 500gp{/i}"
    "{i}Description: Take out the leader of the bandit guild Lemur’s Tail. See me for more instructions at a red barn just outside of Broken Shield{/i}"

    "Hmm, this one seems good. Must be a small guild if they’re only offering that much. I’ve never even heard of Lemur’s Tail."

    scene bg PFbar
    show barkeep neutral

    "Vic" "Ah, Lemur’s Tail. It’s a new guild. Not that many members. Should be a pretty easy job. So you taking it, kid?"

    show Lazarus neutral

    g "Laz, what do you think?"

    l "Sure, why not? A bandit leader’s not a bad place to begin my career."

    g "We’ll take it then. Let’s go, Laz."

    l "Yes, sir!"

    g "Okay, enough with the sir. It’s getting on my nerves."

    l "B-but you’re my boss, I have to-"

    g "This is an assassin’s guild, not the military. Where’d all that bravado from when we first met go?"

    l "But... I... *sigh*"

    "He takes a deep breath, as if adjusting something within himself."

    l "Alright, let’s go then, buddy."

    "{i} To be continued... {/i}"

    jump let_the_games_begin

label choiceknight

    play rain.ogg loop
    "..."
    scene bg mud field
    "They came from nowhere."

    "There weren’t supposed to be goblins on this route, but there they were. Nasty little things, goblins.""

    with dissolve(2)
    scene bg gobrain
    show gobsil
    play goblins.ogg loop

    "Goblins are a weak but stubborn race. Little green heads on a child like body, they despise the bigger races for their height and superiority."

    "Quick to breed, they rely on their sheer numbers and tenacity for the advantage. They live for the fun they have from torturing other races."

    "Fire is one of their favorite methods of destruction. Many a time a goblin fire has taken lives and ruined towns."

    show goblinfire

    "Many a time there have been campaigns to eradicate the goblin race. Every one ended in failure."

    "Legends say that one Dwarven General named Longbeard led an army of troops deep into goblin territory. It says that the fields for miles were nothing but goblins."

    "You couldn’t even see the grass."

    "It was nothing but a sea of melons. A sea of melons with teeth. A sea of melons with tenacity that would only be quelled upon death. A sea of melons that hated to be compared to melons."

    with dissolve(1)

    scene bg longbeard
    play comedytheme.ogg loop

    "As a side note, Longbeard was named that because his family was famous for long beards; his especially so. Rumors say that it was so long, that he had someone carry it for him so he wouldn’t trip on it."

    "Personally, I think he just tucked it in folds to shorten the length, considering it would be difficult to battle with such a long beard."

    with dissolve(2)

    scene bg gobsil
    play goblins.ogg loop

    "Now is not the time for jokes and fun ideas. It’s no joke that the goblins are one of the most annoying races that an adventure can come across. In small numbers, they aren’t that bad.""

    "The real trouble is when they outnumber you 10 to 1; which is what it seemed like today."

    with dissolve
    scene bg gobbattle
    play battletheme.ogg loop

    "And now, we must fight this battle in order to see tomorrow."

    "You" "Don’t falter, men! We must prevail!"

    "Sometimes the best way to encourage the troops is to get into the fray yourself. I make my way up to the front lines on foot; my horse taken out by a hail of goblin arrows.""

    scene bg gobbat

    "I swing my sword down on the first goblin I see."

    "Urgh!"

    "His skull crushed, the first goblin falls to the ground. However, another one takes it’s place; charging at me with a war cry."

    "RRRAAAAGH!!!"

    "I grunt as the goblin sword hits my shield and take a swipe of my own. My slash opens the goblin’s chest, but he still fights on."

    "After a few more exchanges, he finally falls. The next goblin steps up."

    "Argh!"

    "A hit. On the leg. I can still fight though. I bring my sword down on the goblin’s green head: splitting it open. The nasty little monster falls, and another one takes its place."

    "This continues for what feels like an eternity. Just before I reach my limit- the goblin’s seemingly endless numbers finally dwindle- we get a reprieve. I nearly fall to my knees, using just my sword to keep me up."

    scene bg gobbrain
    show soldier weary

    "Captain, should we pursue them? Their forces are in disarray. Now might be a good time to strike."

    "A soldier next to me proposes a battle plan. One of my advisors. Another soldier yells out in protest."

    "Advisor" "But we need to rest. We’re in as much of a disarray as them. An attack now would be suicide."

    "Two choices. To attack, or rest. I look out before my troops."

    image bg troops

    "They look to me expectantly; waiting for orders. I know for a fact that they’re perfectly willing to pursue them if I give the order, despite the one soldier’s compliant. But if I push them too far, they’ll break."

    "Two choices. To attack, or rest. Which choice is the best for my troops?"


    menu:
        "Attack!"
            jump attack

        "Rest."
            jump rest

label attack

    "You" "Forward, men! This is our only chance to wipe out the goblins before they can make a second attack. Charge!"

    "The troops filed up, some reluctantly, and charged across the plain."

    scene bg troops charge

    "To charge an opponent is a risky maneuver. It leaves you defenseless in exchange for a powerful offensive."

    "To attack or defend is an important choice in any battle. If you defend, you go nowhere. If you attack, you lose more troops."

    "A very important choice. One must also know the right time when to retreat. Something these goblins have never learned. This is what makes them so dangerous."

    "Even if they appear to retreat, they’re only regrouping for another assault."

    "We reach their line; and the deafening fighting begins once more."

    jump attack2

label rest

    "Rest up, men. We’ll need our strength for the goblin’s next attack. If we attack in this state, we’ll be wiped out.""

    "The troops collapse with relieved expressions."

    jump rest2

    scene bg gobcharge

    "We’re ready for them."

    "The goblins charge across the plains, aiming straight for us. However, with our line of shields, we should hold the line."

    "A defensive wall is a risky maneuver. While it does protect your men and gives you a greater chance of surviving; you don’t gain anything from it.

    "To attack or defend is an important choice in any battle. If you defend, you go nowhere. If you attack, you lose more troops.

    "A very important choice. One must also know the right time when to retreat. Something these goblins have never learned. This is what makes them so dangerous.

    "Even if they appear to retreat, they’re only regrouping for another assault.

    "They reach our line and the deafening fighting begins once more.


 #[The path deviation ends here(only subtle differences from now on]

    scene bg troopcamp

label attack2

"The plan had worked. The goblins were lying in wait. However, since we attacked immediately, they didn’t have time to set up and we slaughter the nine hells out of them."

    jump return2story

label rest2

"As it turns out, the goblins had planned an ambush. Since we didn’t attack, they got impatient and charged us, resulting in their defeat."

    jump return

label return2story

show knox neutral

    "A wounded soldier came up to me with a limp."

    "Knox" "General, I would like to talk to you."

    "It was my advisor from before."

    t "I keep telling you, Knox, don’t call me General. We know each other, so no need to use ranks. Just call me Tiren."

    k "Yes, sir, General Tiren."

    t "You should be resting like Maiya said. I’ll meet you in your tent to discuss strategy."

    k "No need, this is nothing. We can talk here."

    "Here we go again."

    t "Now listen, Knox. It’s important to get your rest. You should be able to fight as much of the time as possible. You never know when we could be attacked. Now go back to your tent. That’s an order."

    "Knox didn’t say anything. He spun on his heel and walked- err, limped, back to his tent."

    show Maiya neutral

    "Maiya" "General, I have concerns about your... condition.”

    t "What do you mean, Maiya? I’m not sick. You yourself know that much."

    "Maiya" "It’s not about your bodies health, General. It’s just that... I noticed you have a very slight limp."

    "Ever the observant one, aren’t you Maiya. I have the same problem as Knox, though he has it worse."

    t "Oh, that. I almost forgot about that; I’ve been sitting for too long. I was actually going to go see you about that. A goblin got my leg."

    "I lift my leg up and Maiya gets to work with her healing magic"

    play Wondersofmagic.ogg loop
    scene bg healing

    "I relax as the magic courses through me."

    t "Ahhh, that feels good. I always liked cleric magic."

    "Maiya says nothing as she concentrates on her work."

    scene bg healed

    "Maiya" "There. Good as new."

    scene bg troopcamp
    show maiya neutral

    "Miaya" "Is there anything else I may provide assistance for, General?”

    t "No, you’ve done more than enough. You may continue your duties."

    scene bg troopcamp

    "She nods and goes to heal more of the injured."

    "I swear she acts like an animated suit of armor. I don’t think I’ve ever seen her smile or frown. Just this medium look. It’s queer."

    "I look around the camp at the several wounded troops. Luckily there we no casualties."

    "However, from here on out, it’s only going to get harder. I can only hope to led them to victory and not death."


















































label let_the_games_begin
