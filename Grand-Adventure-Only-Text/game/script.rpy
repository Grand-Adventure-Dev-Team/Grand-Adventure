# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# For picking the color of characters, use http://hslpicker.com

# Declare characters used by this game.
define l = Character('Lazarus', color="#70f")
define m = Character('Malvin', color="#0400ff")
define g = Character('Grey', color="#808080")
define v = Character('Vlad', color="#000000")
define b = Character('Barkeep', color="#ffffff")

image bg darkroom = "darkroom.png"
image bg PFentrance = "PFentrance.png"
image bg PFbar = "Pfbar.png"
image bg malroom = "malroom.png"
image bg vial = "malvial.png"
image bg alchemyroom = "alchemyroom.png"
image bg PFtable = "Pftable.png"
image bg jobboard = "jobboard.png"

image barkeep joyful = "barkeep_joyful.png"
image barkeep neutral = "barkeep_neutral.png"
image Lazarus irritated = "laziritated.png"
image Lazarus Shocked = "lazshocked.png"
image Lazarus neutral = "lazneutral.png"
image Malvin irritated = "Malirritated.png"
image Malvin neutral = "Malneutral.png"
image Vlad neutral = "Vladneutral.png"

label start:

    "hrg- wha a- ah... ahhggh"


    "Ah, the sound of death."

    "A sound that I have heard many times by now. How long has it been, I wonder?"

    "Filled with Hesitation when I made my first kill, I had to get used to it fast."

    "You had no choice. You had to get used to it. You get used to living the life of an..."

    "{color=#f00}Assassin{/color}"



    "I walk into the guild, as I am so often used to doing."

    "I say guild, but really it was just a glorified cave."

    "We had to stay out of the way of others, after all, we didn't want anyone to accidentily stumble upon our little gang here."

    "A booming voice ringsout from the bar area; a voice not fit to be an assassins."

    b "Heya kid, you're back! How'd the job go?"

    "Well enough. Had to dirty my blade but that's how it usually ends up."

    "He nods as he gets back to work."


    "That right there was Vic. His real name is Vicros Felchter, but everyone calls him Vic."

    "If you couldn't tell by his stained outfit, hes a bartender."

    "With that big potbelly of his and booming voice, he seems out of place to be in an assassin’s guild like the Python’s Fang or really any assassin’s guild. He has a different talent that proves his worth."

    "Vic’s an info broker. Half the time he works here in the guild and the other half he spends at the local town’s bar: What Ales You."

    "When he’s not able to be at one of the bars, his twin brother Malvin fills in for him when he can. I don’t think I’ve ever seen Vic in anything but a bartender outfit."

    "I say twin brother, but the truth is far from it. They have the same face, and everyone calls him Mal instead of Malvin, but everything else is the opposite for him."

    "Mal’s a skinny man with a nervous air about him, like he always has an appointment to go to."

    "Honestly, he’s a pretty lousy bartender too. I don’t know why he doesn’t just stop bartending and take the blade full time, since that’s all he seems to be good at."

    "Unlike his brother, Mal takes on assassinations from time to time, his gaunt body working to his advantage."

    "I was only on one job with him before; and then I learned the truth."

    "Mal turns into a different man when he’s on the job. His nervous air disappears entirely; replaced with one that is business-like and to the point. He makes sure he gets the job done."

    "It’s Mal’s day off today, since the bar in town is going under reconstruction. Seems like a magical experiment or something went awry. I think I’ll go see him today: see what he’s up to."

    "Unfamilar voice" "Hey, I'm talking to you, buddy!"



    "My thoughts of seeing Mal are interrupted by someone I've never met before."

    "He had on a wierd looking hat. Must've thought it made him look tough or something. To me it looked absoloutly ridiculous."

    #---
    #“You’re in the wrong place. Western Bar Scenes is next door.”

    #“Look, I’m not wearing this thing because I want to. Now follow the script.”

    #“You’re no fun, Laz.”
    #---

    "Who in the hells are you? Never seen your face around here."

    "Unfamiliar person" "Pretty rude way to greet a new member after ignoring him, buddy."

    # "I'm not your buddy, pal!"

    "A new member? Great! You start first thing next week."

    "Unfamiliar really wierd person" "And now you're ordering me around like you're my new boss. Who in the the hells are {i}you?{/i}"

    "Your new boss, my names Grey!"



    "The guy you just put in his place" "O-oh... I'm so very sorry. It's just that you looked so young, I-"

    g "Oh, you should’ve seen this one new guy. Did something similar to you. He was last seen...you know what, forget I said that. I just had a bad flashback."

    "The man with the weird hat gulps. This was getting better by the minute..."

    g "So what’s your name anyway, young blood?"



    "This guy" "Uh, L-Lazarus, sir. Lazarus Redfield."

    g "Well then, Laz, I’m off to meet with Mal. Go and get acquainted with the other members. You’ll want friends in a place like this..."

    g "Also, whatever you do, try not to make enemies. One wrong move and you’re dead on the floor with a dagger in your neck."

    "I draw my thumb across my neck to emphasize my point."

    "Lazarus gulps again as he reaches for his own neck."

    g "Also, talk to Vic and look for an available job. We’ll start when you think you’re ready or when I think you’re ready. Whichever comes first."

    l "Yes, sir."



    "Now, to find Malvin."



    "It seems that Malvin is a bit busy..."

    "He didn't notice me when I walk in. An idea pops into my head..."

    "..."


    "..."


    "..."


    g "Hi Mal!"

    "Malvin" "Gah!"



    "He jumps and the vial he’s holding bounces around in his hands. He lunges for it and tries to get ahold of it. The vial settles down in his hands after a few grabs."



    m "D-d-don't do that! It almost spilled! Do you even know what could've happened if the poison got on me?!"

    g "...Maybe this wasn't such a good idea after all."

    "Its said that while Malvin was a bartender and assassin, but he was also our poison alchemist."

    g "Okay, fine. I'm sorry. So whats this about poison?"



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

    g "Well how does the poison kill the target."

    m "By burning him ali-... oh."

    "He finally gets it."

    g "You see it now?"

    m "Yes. Burning them alive would be problematic for a quiet assassination."

    "Ah, Mal, always missing the little things."

    g "You could probably sell it to the army. I'm sure that would be really popular."

    "Mals face lit up when I said that, but frowned again."

    m "No, that won't work."

    g "Why not?"

    m "The Materiels I used for this are pretty rare. I had only intended for this to be used by our guild, so I don’t have enough to make a market for it."

    g "Good point."

    m "I heard a rumor about a new recruit. Did he report to you yet?"

    g "Please don't let that be him!"



    "Vlad" "Seems you have some anger problems, new guy. Assassins with anger problems never last long. It seems that you want an early grave and a place of your own in one of the nine hells."

    "Uh-oh. This isn't good."

    g "Lazarus!"

    "I quickly rush over to try and protect Lazarus from Vlad."

    g "What the nine hells are you doing? I thought I made it pretty clear to try and not make enemies!"


    l "Hes the one looking to make enemies. No respect. Who is he, anyway?"

    g "He’s the one I was telling you about earlier. Remember, the one who took that new guy and left each body part in- wait, that was a different guy. Uhh..., ah! Vlad here was the one who ************************."


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




    "...Creepy."

    "He's obivously enjoying himself. You'd think he started those rumours himself."

    g "Okay, Laz. Let’s get you on your first job before you get yourself killed, Thanatos forbid, you make me happy. Hey, Vic! What jobs are available?"


    "Vic" "Slow week this time. Only 6 jobs avaliable. And half of them seem too tough for a guy's first mission."

    "I take a look at the job list."


    "Hm, Vics right. Looks like only 3 missions available and doable. I don’t even know what Lazarus is even capable of, let alone what jobs are suited for him. Hmmm... "

    "{i}Job, cutting off the taul of the Lemur{/i}"
    "{i}Reward: 500gp{/i}"
    "{i}Description: Take out the leader of the bandit guild Lemur’s Tail. See me for more instructions at a red barn just outside of Broken Shield{/i}"


    g "Hmm, this one seems good. Must be a small guild if they’re only offering that much. I’ve never even heard of Lemur’s Tail."



    "Vic" "Ah, Lemur’s Tail. It’s a new guild. Not that many members. Should be a pretty easy job. So you taking it, kid?"


    g "Laz, what do you think?"

    l "Sure, why not? A bandit leader’s not a bad place to begin my career."

    g "We’ll take it then. Let’s go, Laz."

    l "Yes, sir!"

    g "Okay, enough with the sir. It’s getting on my nerves."

    l "B-but you’re my boss, I have to-"

    g "This is an assassin’s guild, not the military. Where’d all that bravado from when we first met go?"

    l "But... I... *sigh*"

    "He takes a deep breath, as if adjusting something within himself."

    g "Alright, let’s go then, buddy."

    "{i} To be continued... {/i}"
