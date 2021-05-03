label b1c3:

scene bg black with slow_dissolve
play ambience "ambience/birds.ogg" fadein 3.0 fadeout 0.3
"Gentle patting on my shoulder stirs me from my sleep and I can hear a muffled voice break through the veil."
r "\"[mc]...\""
m "\"Huh? What?\""
scene bg broom_day_in with slow_dissolve
"I open my eyes sleepily, blinking to adjust my vision."

if Romance == True:
    play music "music/mood.ogg"
    show ran squat smile with dis
    "The grey wolf squats in front of me with a gentle smile."
    show ran squat shock with dis
    "Without thinking I throw myself into his arms, tipping him over."
    show ran sit laugh at jumping with dis
    play sound "sfx/fall.ogg"
    "He lands on his butt with an amused ‘oof’, embracing me tightly."
    show ran sit smile with dis
    "I can sense that my reaction surprised him, but the swoosh of his tail assures me I did it in a good way."
    "I rub my head against his neck fluff, just taking in his scent."
    "I didn’t think it was possible to miss someone so much."
    "Suddenly, I remember the other wolf keeping watch over me, pulling away from Ranok in order to avoid making a scene."
    show ran squat smile with dis
    "As the wolf readjusts himself, I notice that we’re in fact alone."
else:

    play music "music/mood.ogg"
    show ran squat smile with dis
    "The grey wolf squats in front of me with a gentle smile, I almost want to throw myself into his arms, but manage to reign in that impulse."
    "I'm still conflicted about my feelings and he did keep giving me mixed signals."
    "It's better to tone down a notch and take things slow, although I am extremely happy to see him and my expression betrays it."
    show ran squat talk with dis
    r "\"Hey there sleepy head.\""
    show ran squat smile with dis
    "He croons, clearly pleased to see me smile."
    "I tilt slightly to the side, to look past him."

m "\"Where’s the guard?\""
show ran squat talk with dis
r "\"He’s gone now.\""
show ran squat smile with dis
"The wolf smiles at me."
show ran squat worry t with dis
r "\"Hope you were treated ok.\""
show ran squat worry with dis
m "\"He might as well been part of the furniture, didn’t budge or make a sound.\""
show ran squat worry t with dis
r "\"Why are you on the floor? You should've used the bed.\""
show ran squat worry with dis
"Ranok raises one brow, nodding towards it."
show ran squat smile with dis
m "\"Honestly… I was afraid to startle the guy, he was super tense.\""
show ran squat talk with dis
r "\"Hah! For someone so {i}tiny{/i} you are incredibly ballsy when dealing with wolves.\""

if mc == "Caelan":
    show ran squat smile with dis
    m "\"I'm {i}caelan{/i}, alright...\""
    "I laugh off his tease."
    "The nickname really grew on me."
else:

    show ran squat smile with dis
    "And again with that {i}caelan{/i} stuff... he's been calling me tiny a lot."
    "I guess he really likes that nickname."

m "\"Since I see you instead of an executioner, I take it we’re good?\""
show ran squat talk with dis
r "\"Yes.\""
show ran squat smile with dis
"He nods with clear relief."
show ran squat talk with dis
r "\"Everything’s fine… you’re released into my custody.\""
show ran squat shock with dis
m "\"What does that mean?\""
show ran squat worry t with dis
r "\"That…\""
show ran squat worry with dis
"He cuts off, slightly troubled. "
"He’s clearly looking for the right words."
show ran squat worry t with dis
r "\"…that I’m responsible for you.\""
show ran squat shock with dis
m "\"So, pretty much what we wanted, no?\""
show ran squat smile with dis
"I enquire, as the pause made me slightly worried."
show ran squat talk with dis
r "\"Yes, pretty much.\""
show ran squat smile with dis
"He chuckles, extending a paw to help me up."
scene bg broom_day with dis
show ran c smile with dis
"As I stand up my eyes are immediately hit by a harsh beam of light."
m "\"Damn, it’s morning already?\""
"I squint."
show ran c talk with dis
r "\"Yeah…\""
show ran c smile with dis
m "\"You talked throughout the day {i}and{/i} night?\""
show ran c awkward hard with dis
r "\"It was a hard sell…\""
"He admits with a bit of embarrassment."
show ran c awkward with dis
r "\"I told you my people are rather… set in their ways.\""
r "\"Also, Verissa is questioned a lot due to her age. Many of the elders don’t trust her ability to speak with the Spirits.\""
show ran c talk r paw with dis
r "\"And then you have the elders. They like to talk…\""
show ran c shocked with dis
m "\"So that's why it's called the 'Howl'.\""
show ran c laugh with dis
"I propose cheekily and he suppresses an idle laughter."
show ran c talk with dis
r "\"I swear, my father was getting pretty fed up halfway through the meeting.\""
show ran c smile with dis
m "\"No wonder… if it started at noon, you pretty much spent eighteen hours arguing.\""
show ran c worried rt with dis
r "\"Yeah… and it got pretty heated. My father’s position...\""
show ran c worried r with dis
"He pauses, as if not sure whether he should elaborate or not, forcing me to pry."
m "\"Hmmm?\""
show ran c resigned with dis
"The wolf sighs, reaching up towards his shoulder pad."
show ran c neutral rt paw with dis
r "\"It’s a long story… and for another time. Just know there are things the elders like to bring up against him.\""
show ran c neutral r with dis
"I watch uncomfortably, as he struggles to undo a latch beneath the metal plate."
show ran c shocked with dis
m "\"You need help with that? Looks rather fiddly.\""
show ran c embarrassed with dis
"I ask needlessly, as I find my hands already reaching out towards his paws."
show ran c embarrassed blush with dis
r "\"You don't have to-\""
show ran c embarrassed e with dis
"He pauses, as my small fingers already sunk beneath the plate."
"With a click, the piece of armour is detached, and the wolf places it carefully down on the ground."
show ran c awkward with dis
r "\"Thank you.\""
show ran c smile with dis
"I watch as he removes his cloak along with leather straps which secured the shoulder pad in place and held the blade on his back."
show ran h smile with dis
"He rests his massive longsword against the wall, next to the chest."
"Only now I have a good look at that thing; it's nearly as tall as the candelabra."
"It must weigh a freaking ton, which explains his massive arms."
"I bet he could easily split me in half."
"My eyes wander around the room, as a blush creeps onto my face, especially as he undoes his belt allowing it to clang to the floor with a loud thud."
m "\"Do you want me to put it all away? The chest perhaps?\""
show ran p smile with dis
"Another flop draws my gaze back to him, as he dropped his padded armour carelessly onto the heap."
show ran p talk with dis
r "\"Aren't you settling into your role…\""
show ran p smile with dis
"He laughs teasingly."
show ran p talk with dis
r "\"Let's just leave it here. I'll have to put it back on soon enough.\""
r "\"I only have few hours to rest.\""
show ran p smile with dis
"The wolf walks towards the bed and sits down, reclining back onto his elbows."
scene ran_splayed_e with slow_dissolve
"I follow and take the spot next to him."
"It's a beautiful morning and although the wolf's expression invites me to admire the light spectacle outside, my eyes wander to the sunrays gently kissing his sculped body."
"It almost seems that the light redefines his musculature, making it even more pronounced than before."
"I shake my head slightly, trying to regain my train of thought."
"'What is {i}wrong{/i} with me?'"
scene ran_splayed_smile_en with dis
m "\"So… we're dealing with a distrusted shaman and a questioned leader.\""
"I think out loud, reflecting on our conversation as it did not exactly put me at ease."
m "\"Seems like this whole place is pretty unstable.\""
scene ran_splayed_laugh with dis
r "\"You have no idea.\""
scene ran_splayed_smile_en with dis
"Ranok laughs, smiling at me with amusement."
scene ran_splayed_neutral with dis
m "\"That’s not a good thing.\""
"If anything, it sounds like my situation isn’t exactly sorted and it’s clear Ranok realises that."
"He sighs and nods in defeat."
scene ran_splayed_talk with dis
r "\"I know.\""
scene ran_splayed_smile with dis
r "\"But one thing at a time, friend.\""
scene ran_splayed_smile_en with dis
"He pats my shoulder reassuringly."

if Romance == True:
    scene ran_splayed with dis
    "‘Friend’… I’m both glad and distraught to hear him call me that."
    "I treasure his friendship and am glad our previous mishap didn’t hamper it, but…"
    "...is it really all he wants me to be?"
    "I sigh... not even sure where my thoughts are taking me."
else:

    scene ran_splayed with dis
    "‘Friend’… I suppose that’s where the things are after the previous day fiasco."
    "It's where they should be, and I’m glad for it."
    "No point needlessly complicating things."

scene ran_splayed_e with dis
"We sit like this for a moment in silence, I can clearly see he doesn’t know what else to say while I’m deep in my thoughts."
"I desperately try to escape my infatuation… there are more important things at hand."
"If Verissa’s and Chief’s positions are indeed insecure, I might prove to be their undoing."
"For whatever reason, I feel like I have unwittingly become a pawn in a game I won’t even get to play; but I'm getting ahead of myself."
"With the chief's apparent fury and now the entire tribe's attention on me, I just need to focus on surviving until the next day."
"I slump a little, realising that this whole mess unfolded the way it did due to my own carelessness."
scene ran_splayed_brow with dis
m "\"I'm sorry I allowed myself to be seen like that…\""
scene ran_splayed_smile with dis
r "\"Heh, I did ask you to stay out of sight. \""
scene ran_splayed_smile_en with dis
"He nods with a slight smile."
m "\"You did… and I fucked up. It's just… there was so much going on-\""
scene ran_splayed_smile with dis
r "\"Relax… it wasn't all your fault.\""
scene ran_splayed_unhappy with dis
r "\"That little shit should've stayed away. He always sneaks around my house, but I thought he learned his lesson after last time I caught him outside my windows.\""
"I could hear a stifled growl brewing deep inside his throat, which makes me wonder about the pup."
"Ranok doesn't seem to like him very much."
scene ran_splayed_neutral with dis
m "\"Who is he?\""
scene ran_splayed_talk with dis
r "\"He's my younger brother. Well, half-brother anyway.\""
scene ran_splayed_neutral with dis
"The wolf rolls his eyes in annoyance."
scene ran_splayed_talk with dis
r "\"Ever since I moved out from the villa he snoops around.\""
scene ran_splayed_brow with dis
m "\"He probably just misses you.\""
scene ran_splayed_unhappy with dis
"I propose, as I find it rather harsh towards the child even if he did put our lives in danger."
"Ranok simply closes his eyes and releases an exasperated sigh."
r "\"That's neither here nor there, I'm not his damned Den-Mother.\""
"I assume that's some sort of a village nanny."
"I can see he's clearly annoyed, so I allow him a moment to calm down before I continue my questioning."
scene ran_splayed_brow with dis
m "\"What's his name?\""
scene ran_splayed_talk with dis
r "\"He doesn't have one. He hasn't earned it yet.\""
scene ran_splayed_neutral with dis
m "\"Well, you have to call him something.\""
"I chuckle."
scene ran_splayed_talk with dis
r "\"Yeah… a pup-call of sorts. It's like a nickname, usually derived from the pup's behaviour or physique.\""
r "\"His is Howl. As you can guess he wouldn't shut up when he was born. Although if you ask me, he should've been called Snitch.\""
scene ran_splayed_neutral with dis
m "\"Don't be like that. He's just a kid.\""
"I smile awkwardly."
scene ran_splayed_unhappy with dis
r "\"A very nosy and annoying one, that's for sure.\""
"Seeing him so grumpy and serious almost demands a tease."
m "\"As if you were a well-behaved pup...\""
"I laugh him off."
m "\"…with your tendency to seek out trouble, I'd say it runs in the family.\""
scene ran_splayed_brow with dis
m "\"I wonder what's your pup-name...\""
"I chuckle and I can see his eyes widen in shock."
"But only for a moment as he quickly narrows his eyes grumbling."
scene ran_splayed_unhappy with dis
r "\"Well, you can continue to wonder.\""
m "\"Come on, are you seriously not going to tell me?\""
r "\"It's a grave insult to use a pup-call towards an adult wolf.\""
"He states in a serious tone."
r "\"Once we stake a claim to our Name Tree, our pup-name is meant to be forgotten.\""
m "\"Seriously, your people need to learn to relax a bit. All this posturing is a little over the top.\""
"I laugh him off, but his expression doesn't soften, and I think I found another sore spot."
r "\"It's not posturing, if you pup-name a wolf, he is honour bound to challenge you to a duel to prove his mantle.\""
m "\"You people duel over misnaming?\""
r "\"It's not a trifle. It's deadly serious.\""
"He scolds me."
m "\"Yeah… so far with your people everything is.\""
r "\"By using a pup-name you're basically questioning a wolf's worth. The only way to restore honour is through combat. Often to the death.\""
m "\"Yeah… why am I surprised? If you kill over a Name Tree, why would misnaming be any different?\""
"The wolf issues a long huff, giving me a mixture of a hurt and patronising gaze."
scene ran_splayed_sigh with dis
r "\"Look, [mc]. I understand you're a human… and I don't know anything about your culture, but I'm sure I'd find half of your practices objectionable to say the least.\""
scene ran_splayed_sad with dis
"He states defiantly, causing me to blink."
r "\"We have lots to learn from each-other, I can see that. But for any learning to take place there has to be a willingness to listen and to understand one-another."
r "\"I want to learn from you, but so far all you do is mock our customs and give me flak over things I don't control.\""
"He finishes chastising me and I slightly sink into my shoulders."
"Although harsh, his words ring true; I've been overly cynical if not outright critical of his way of life."
scene ran_splayed_brow with dis
m "\"Yeah… you're right, I'm sorry.\""
"I admit in defeat."
scene ran_splayed_neutral with dis
m "\"All of this is just extremely confusing to me… but none of it is meant as an insult.\""
m "\"I guess it's just my defence mechanism…\""
m "\"I don't understand what's going on and I don't remember anything beyond what's happening here and now...\""
m "\"So... instead of panicking I try to pick apart everything that's new.\""
"He listens carefully to my explanation, his expression shifting a little."
m "\"I'm {i}really{/i} sorry… I'm just trying to fill up this utter void in my head, so I tend to overthink everything you tell me.\""
scene ran_splayed_unhappy with dis
r "\"You seem quite functional for someone who claims to have an empty mind.\""
"He mutters, almost as if he began questioning my memory loss."
m "\"It's all just an act, in reality I'm in the same boat as you are. I don't know any more about the human culture than you do.\""
"He narrows his eyes, but this time more worried than annoyed."
m "\"I don't remember how humans do things, but somehow I feel that even if you were to tell me… it would still be just as alien as the rest of this is.\""
scene ran_splayed_brow with dis
r "\"What are you saying? You weren't living among your kin?\""
"In truth, I want to tell him I feel as if I'm from another world entirely, but this would just be admitting lunacy."
"I sigh in resignation."
m "\"Yeah, I guess so.\""
scene ran_splayed_talk with dis
r "\"Hmmm. So, I suppose you lived somewhere among the Tigerii then... which would explain your superiority complex.\""
scene ran_splayed_neutral with dis
"I give him an annoyed look."
m "\"Your guess is as good as mine.\""
"I can see his eyes drill into me as if expecting me to elaborate."
m "\"I don't know what to tell you, Ranok… I've got nothing.\""
"I shrug and he scoffs in amusement."
scene ran_splayed_talk with dis
r "\"Well… not exactly.\""
scene ran_splayed_smile with dis
r "\"You still have your compass.\""
scene ran_splayed_smile_en with dis
"He bumps into me with his shoulder forcing a reluctant laugh out of me."
m "\"If you say so…\""
scene ran_splayed with dis
"I shrug defeated and the wolf looks towards the window."
"It's clear that my memory loss bothers him almost as much as it bothers me."
"It does kinda put a hole in his plan... can't take me home if there is no home to speak of."
"Eventually, after a moment of silence he looks back at me with his usual determination."
scene ran_splayed_smile with dis
r "\"Heh. There's always tomorrow. We'll get your memories, {i}Caelan{/i}.\""
"He grins, ruffling my hair and I smile back at him for a moment before I pause."
scene ran_splayed_brow with dis
m "\"Hold on...\""
"Suddenly it hits me… all this time he's been using my characteristic as a nickname."
scene ran_splayed_smile_en with dis
"I can see his grin widen at my realisation."
m "\"You dick! You pup-named me!\""
scene ran_splayed_laugh with dis
r "\"Took you a while.\""
scene ran_splayed_smile_en with dis
"He winks cheekily and I snicker."
m "\"All this talk about how insulting this is while you've been pup-calling me all along!\""
m "\"You're such a hypocrite!\""
scene ran_splayed_smile with dis
r "\"As the kettle said to the pot.\""
scene ran_splayed_smile_en with dis
"He snorts and I decide to teasingly punch his shoulder, although putting some actual force behind it."
scene ran_splayed_laugh with dis
"My knuckles buckle as if I hit a stone wall and I immediately have to cradle my hand in slight discomfort causing him to laugh."
r "\"Also not really a hypocrite, if you {i}are{/i} as helpless as a pup…\""
scene ran_splayed_smile_en with dis
"He laughs off my pathetic attempt at roughhousing and in turn punches me right in the chest."
"Just like I did, he placed a little bit of force behind his tease and I winced in pain, rubbing my now aching breast."
scene ran_splayed_smile with dis
r "\"See? A total pup!\""
scene ran_splayed_smile_en with dis
"He snorts, while I kept rubbing the sore spot with feigned annoyance when I notice his eyes dart to my side with a worried expression."
scene ran_splayed_sad with dis
"It's almost as if he forgot himself and is now worried that he might have overdone the punch."
"Such a good wolf…"
r "\"How’s your wound?\""
"The wolf asks, his voice lined with concern."
r "\"I was worried sick, couldn’t think straight about anything else.\""
m "\"Honestly… I think it’s fine.\""
"I look down at the bloodied bandage."
"Although it looks bad, the blood has dried off and the wound beneath doesn’t even hurt anymore."
scene ran_splayed_brow with dis
m "\"I’m glad no one took a look at it, because Vul might have been too careful.\""

if Knife == True:
    scene ran_splayed_talk with dis
    r "\"Yeah... well...\""
    scene ran_splayed_neutral with dis
    "I can see his ear pull back, as he slumps in discomfort."
    "He's still beating himself up over the issue."
    m "\"Hey, we talked about this, right?\""
    "I force myself into his line of sight, meeting his defeated gaze with a gentle smile."
    scene ran_splayed_smile with dis
    r "\"Right…\""
    scene ran_splayed_smile_en with dis
    m "\"Either way... I never been stabbed before, but this thing feels too good for a ‘grave wound’.\""
    m "\"I kinda forget it’s even there most the time.\""
    scene ran_splayed_sigh with dis
    r "\"I, for one am glad. I would like to put this whole mess behind us.\""
else:

    r "\"Are you complaining that he didn’t stab you hard enough?\""
    "He laughs nervously."
    m "\"Well… I never been stabbed before, but this thing feels too good for a ‘grave wound’.\""
    m "\"I kinda forget it’s even there most the time.\""
    scene ran_splayed_sigh with dis
    r "\"I, for one am glad. I would like to put this whole mess behind us.\""

scene ran_splayed_neutral with dis
"I nod in agreement and we both gaze idly at the window."
scene ran_splayed_e with dis
"He leans back, tensing out his exposed belly and I have to fight the urge to just pet it."
"I don’t understand my bizarre attraction to him, it feels very sudden."
"He's charming, alright... but it's not typical of me to get lost in a guy like this..."
"Or is it?"
"After all, I did lose all my memory... but I'd like to think I wasn't this easy to wrap around a finger..."
"Still... something about this wolf is different."
"He's quirky, a bit forward and too full of himself... but at the same time extremely vulnerable."
"I think he let himself be boxed up his entire life and our little mishap proved it best."
"I can feel a blush slowly creeping onto my face, as I’m reminded what I actually wanted to talk about."
"He's not alone; even if we're just friends, I want him to know I understand what he's going through."
m "\"Ranok…\""
scene ran_splayed_smile_en with dis
r "\"Hmm?\""
"He looks at me with a soft smile."

if Romance == True:
    m "\"I-\""
    m "\"I wanted to tell you something, but I don’t know how.\""
    scene ran_splayed_smile with dis
    r "\"You seem to have pretty good grasp of our language.\""
    scene ran_splayed_smile_en with dis
    "He smirks."
    m "\"It’s not that…\""
    "I struggle, this is much harder to do than I thought."
    "He just looks at me with a smirk, raising one brow in a teasing expression."
    "Damn, he knows how to disarm me."
    scene ran_splayed_brow with dis
    m "\"It’s about yesterday morning.\""
    "I finally spill it out, looking away at the window."
    scene ran_splayed_talk with dis
    r "\"Oh.\""
    r "\"I would rather not talk about that.\""
    scene ran_splayed_neutral with dis
    "His voice takes on a more serious tone."
    "I swallow heavily, not wanting to leave the matter unresolved."
    scene ran_splayed_brow with dis
    m "\"I just want you to know… that I don’t-\""
    m "\"Oh fu-\""
    "I sigh."
    m "\"I don't mind it, ok?\""
    scene ran_splayed_sad with dis
    m "\"And if you do, I hope you won’t start calling me…\""
    m "\"...defective.\""
    "I cringe, really unsettled by the term."
    scene ran_splayed_unhappy with dis
    r "\"I would {i}never{/i}!\""
    scene ran_splayed_sad with dis
    m "\"Good. Because I don’t think it’s right. I don’t think anyone should feel wrong, or broken just because… they-\""
    m "\"…like guys.\""
    "I finish, not even looking at him."
    "I can’t believe I just said it, but… I am glad I did; it had to be said."
    scene ran_splayed_shocked with dis
    "I hear the wolf readjust himself, as he turns to face me with an expression full of disbelief."
    r "\"Wait a moment... You-\""
    r "\"You like males?\""
    "Fuck."
    m "\"…\""
    "It is hard to force myself to face him, but I have to look into his eyes, otherwise what was the point in bringing all of this up?"
    "To my surprise his expression is kind and a little bit expectant, I could almost see a light lit up above his head."
    m "\"I hope we can still be friends.\""
    scene ran_splayed_unhappy with dis
    r "\"Of course, we can!\""
    "He scoffs at me, as if it was never a question and I’m glad to hear it."
    scene ran_splayed_sad with dis
    r "\"But-\""
    "Uh-oh."
    scene ran_splayed_talk with dis
    r "\"I’m not like you.\""
    scene ran_splayed_neutral with dis
    "He grimaces with embarrassment."
    scene ran_splayed_smile with dis
    r "\"I really do like females.\""
    scene ran_splayed_smile_en with dis
    m "\"Oh…\""
    "I freeze, looking at the window."
    "In truth I just want to jump out of it."
    m "\"I-\""
    scene ran_splayed_smile with dis
    r "\"Besides, you’re rather small and… wrong species, no?\""
    scene ran_splayed_smile_en with dis
    "He cuts me off with a chuckle, almost as if trying to save me embarrassment."
    "I laugh nervously."
    m "\"Heh, yeah…\""
    scene ran_splayed_smile with dis
    r "\"Don’t worry about it, it doesn’t change anything between us.\""
    scene ran_splayed_e with dis
    "Of course, it does!"
    "I just made a fool out of myself…"
    "…fuck!"
    "I guess I've seen too many stories, to think this would work out the way I thought it would."
    "But I guess it's for the best... I really don't feel I'm in control of my emotions and I'm shifting from one extreme to another..."
    "I’m so dumb... why would I even think of romance in my current situation?"
    scene ran_splayed_sad with dis
    r "\"You ok? You've gone pretty quiet.\""
    scene ran_splayed_smile with dis
    r "\"I hope you’re not taking my rejection too hard.\""
    scene ran_splayed_smile_en with dis
    "He winks at me in a clear jest."
    m "\"Rejection? You should be so lucky! Who said I'm interested?\""
    scene ran_splayed_laugh with dis
    "I punch his arm teasingly, nervous laughter escaping my lips."
    scene ran_splayed_e with dis
    r "\"Whatever you say, {i}tiny{/i}...\""
else:

    "I want to prod him about what happened yesterday morning, but quickly realise it’s better left alone."
    "I mean, I’m not entirely sure what’s even going on in my own head to unpack whatever's going on inside of his noggin."
    "It's pretty clear he's conflicted about his own feelings and considering what we've just went through, I guess it's best to leave it alone for a while."
    "At least until we both get a chance to reflect on everything."
    scene ran_splayed_brow with dis
    m "\"Never mind.\""
    "I shake my head with an awkward smile."
    scene ran_splayed_sad with dis
    r "\"O-ok?\""
    "He looks to me unconvinced of my sincerity, but I know it's the right decision."
    "My emotions are running wild and most of my knee-jerk reactions are putting me on a spot."
    "I guess I’m projecting my dependency onto the wolf and the last thing I need is misconstruing his quirkiness as a romance opportunity."
    scene ran_splayed_smile with dis
    r "\"Are you really not going to tell me?\""
    scene ran_splayed_smile_en with dis
    "He teases, making this whole thing that much more awkward."
    m "It was nothing… just a wild thought."
    "I wave my hand at him."
    scene ran_splayed_smile with dis
    r "\"Heh, you sure know how to pique an interest with your word choices...\""
    scene ran_splayed_smile_en with dis
    m "\"Huh?\""
    scene ran_splayed_smile with dis
    r "\"As a wolf, I do like wild thoughts.\""
    scene ran_splayed_smile_en with dis
    "He croons seductively, bumping my shoulder and I chuckle."
    m "\"My compass tells me to leave it for another time.\""
    scene ran_splayed with dis
    r "\"Ah, then say no more. Another day it is!\""

scene bg broom_day with dis
"He chuckles and plops down on the bed."
stop music fadeout 9.0
r "\"Now, I don’t know about you, but I really need to get some sleep.\""
"He makes an exaggerated yawn, his tongue coiling up inside his maw like a snake."
r "\"Would you close the shutters?\""
m "\"Sure.\""
"I walk towards the window, allowing the wolf to splay himself out when I suddenly stop in my tracks."
m "\"Wait- you have fucking shutters and you’re only mentioning them now?!\""
r "\"Yeah... why?\""
m "\"This whole mess could’ve been avoided if they were closed to begin with!\""
r "\"Maybe… but aside from looking suspicious to others, being locked in a dark room would freak you out even more than this whole thing already did.\""
"He shrugs through another protracted yawn."
"I chuckle, looking at his open jaw; his tongue dangling out in such a goofy fashion."
"He finally closes his muzzle with a loud smack."
r "\"You were on the verge of heart-attack anyway.\""
scene bg window_day with dis
"I shake my head with a sigh, deciding to simply drop the issue."
"Carefully, I relocate the clutter onto the floor."
play sound "sfx/window_creak.ogg"
"Once the ledge is cleared, I open up the window and for the first time lean out of it freely."
scene bg outdoor_d with dis
"The fresh air feels wonderful on my skin and this little taste of the outside world only makes me want more."
"The forest is alive and buzzing with activity."
"I can hear the gentle rustle of leaves accompanied by the chirping of birds."
"There’s even a pair of squirrels chasing each-other across the canopy, jumping from one branch to another."
"Maybe we get to go out sometime later…"
"I would really love that."
"A hike through these woods seems a dream come true; this place looks like it’s from a fairy-tale."
"But for the time being, I’ll just follow Ranok’s lead."
"I’ve put us in danger one time too many on a silly whim."
play sound "sfx/window_creak_c.ogg"
scene bg broom_day_shut with dis
"I decide to simply grab the shutters and close them, allowing the dark to claim the bedroom."
"Since I’m no longer a secret, I leave the window open, allowing much needed forest air to flow freely into the otherwise dank room."
r "\"Sorry I left you without any provisions… you must be-\""
"He interrupts issuing another prolonged yawn."
r "\"-starved. Brought you some food, it’s in the kitchen.\""
"The wolf mutters and I smile, seeing he’s pretty much half asleep already."
m "\"Don't you worry about me... you just rest.\""
play sound "sfx/door open.ogg"
scene bg kitchen_day with dis
"I go to the kitchen, to find a linen bundle on the table."
"I sit down, slowly unwrapping it to reveal thick slices of roasted ham and some forest fruits."
"The ham smells wonderfully, causing my mouth to water with its smoky aroma."
"But it's the berries that pique my attention; they're glistening with morning dew and look extremely ripe."
"I select one large blackberry and eat it."
"It immediately bursts with sweet tang at the slightest touch of my tongue, bringing a smile to my face."
"They're freshly picked and carefully selected which must've taken some time considering the season."
"Why is he trying so hard if he's into girls?"
"I sigh, shaking my head."
"I'm reading into things again, while I should focus on more important matters."
"I'm curious how exactly the meeting went."
"Ranok’s description doesn’t fill me with confidence."
"I can understand Verissa being questioned a lot, after all, I myself kinda felt she was too young to be a shaman…"
"…and I don’t even know what shamans do."
"But the chief?"
"He seems like one tough guy… why would he be questioned."
"It almost sounded as if the elders had a hook on him, which in and of itself sounds rather scary."
"I might not have a full picture to truly understand a power dynamic in this tribe, but it seems the elders have a large sway."
"At this point I’m not sure if it’s my place to wonder such things, or if it’s my prerogative to know the details due to the situation we’re all in."
"I simply pick up a piece of ham and bite in."
"It's luscious and the oaky aroma just makes me feel warm inside."
"This food, although very simple really hits the spot."
"I don't know why, but I have a feeling I was used to much different type of meals… a bit more complex, true… but devoid of this pure joy."
"I regard the parcel again, seeing that the selection is rather odd."
"I flash my brows as I decide to give it a try."
"I eat another berry, while chewing a slice of ham and to my surprise the combination works."
"The sweet and savoury blend in an unexpectedly delicious way."
"That wolf sure knows how to please me…"
"I look back towards the bedroom and an involuntary smile creeps on my face, as I admire Ranok's musculature."
"Even lazily splayed out on the bed he looks extremely attractive; wish I was this photogenic."
"Wait… photo-what?"
"Ugh... another of those weird, fucking words I somehow understand but have no context for."
"If this continues much longer, I'm going to go insane..."
"There goes my appetite."
"I just sit there, looking at the window with slight worry."
"I might be finding my bearing among these wolves… but I'm as much in the weeds with regards to who I am as I was the day I woke up."
"I'm just starved for answers and I'm sure this is the reason why I push for additional information whenever I can."
"I need to keep an eye on this… I don’t feel like pressing Ranok for unnecessary details."
"Especially if he doesn’t feel like divulging just yet."
"So far trusting him worked just fine."
"Realising I won't be able to eat anymore, I simply walk to the cupboard and wash off my hands."
"I guess I should rest a bit as well, my body is aching all over from sleeping rough."
scene bg broom_day_shut with dis
"As I return to the bed, I can see that Ranok is already fast asleep, snoring slightly as his massive chest expands and falls down in a slow rhythm."
scene sleeping with slow_dissolve
play music "music/mood.ogg" fadein 3.0
"His muzzle is burrowed into the pillows and slightly opened, allowing his saliva to dribble out."
"I smile, knowing all too well how this wolf drools in his sleep."
"I’m glad it’s the pillows that will now soak up all that spit."
m "\"You’re so cute for someone so big…\""
"I mutter, fighting the urge to just rub his belly, but he is too darn adorable not to."
"My hand reaches towards his breast and I hesitate for a moment."
"That’s when a lazy stretch tenses up his body as the wolf readjusts himself slightly and I cannot help myself anymore."
"I let my hand sink into the lush coat of his chest, ruffling it gently."
"My fingers slide beneath the Moonstone, for the first time feeling its surface."
"It's polished and heavier than I expected."
"I move it slightly out of the way so I can rub his breasts."
scene sleeping_smile with dis
r "\"Mmmmmm…\""
"His expression adjust into a soft smile; he’s clearly enjoying this even through sleep."
"I move my hand gently towards the abdomen, trying not to stir him from his slumber."
"I ruffle his coat around the navel, drawing another idle stretch from the wolf."
"I chuckle quietly; he's so fluffy I'm gonna die…"
"My fingers brush across his entire belly, his coat soft and inviting."
"But even now I can clearly feel defined muscles beneath all that fur… he really didn’t have an idle moment in his life."
"I press slightly harder, as to give his abs a slight workout."
"He groans softly and I instantly blush noticing his crotch tense up…"
"I’m no longer sure which one of us gets more out of this little stimulation..."
"I allow myself few more moments, but as I notice my own excitement I decide to stop."
stop music fadeout 6.0
"I exhale heavily, trying to release the pent-up tension."
"This got slightly awkward…"
scene bg broom_day_shut with slow_dissolve
"I rub my hands uncomfortably, trying to figure out what to do."
"For a moment I consider returning to the floor, but then I remember his own words."
"Ranok wouldn’t be happy if he found me like that again…"
"I look back at him, still sleeping in perfect bliss."
"He looks so peaceful that I decide to simply lay beside him, although keeping appropriate distance."

if Romance == True:
    "He made it clear he’s not interested, so I will respect our personal spaces."
    "Last thing I want is another awkward accident."
else:
    "Last thing I want is another awkward accident."

"I know his tendency to roll over, so I simply take one spare blanket and furl it up to create some sort of divide between us."
"I lay there for a moment, feeling most of my body ache."
"Sleeping on the floor was not good for me, so the soft bed accompanied by his rhythmic breathing quickly puts me to sleep."
scene bg black with slow_dissolve
"But we don’t get to sleep long, as Ranok gets up after just a few hours."
scene bg broom_day_shut with slow_dissolve
show ran p stretch with dis
"I have to admire his self-discipline as getting out of the bed is almost like an uphill battle for me."
show ran p confused pt with dis
r "\"What’s this all about?\""
show ran p confused with dis
"Ranok points to my makeshift barricade, as he rubs his eyes."
m "\"Ummm…\""
m "\"I thought it would… prevent… you know.\""
"I wince uncomfortably."
show ran p embarrassed with dis
r "\"Oh…\""
"The wolf mutters sleepily."
show ran p shocked at jumping with dis
r "\"OH!\""
"He almost shouts out in sudden realisation."
show ran p awkward with dis
r "\"I can return to sleeping in the kitchen if you'd like.\""
show ran p embarrassed with dis
"He proposes nonchallantly and this time I'm the one shouting out in panic."
show ran p shocked with dis
m "\"NO! No!\""
m "\"That is the LAST thing I want you to do!\""
show ran p confused pt with dis
r "\"Well… this makes things a bit weird though.\""
show ran p embarrassed with dis
"He gazes reluctantly at the rolled-up blanket."

if Romance == True:
    m "\"After what you said... I just didn't want to-…\""
    "I try to explain myself, but he cuts me off."
else:
    m "\"Sorry... I just didn't want you to get flustered again.\""

show ran p awkward with dis
r "\"Don’t worry about it. It was a one-time fluke.\""
"He laughs."
show ran p talk r with dis
r "\"I simply never went to sleep like that before… you know, effectively snuggled up to someone.\""
show ran p awkward with dis
r "\"It was just to keep you warm, remember?\""
show ran p wink with dis
"The wolf winks and gets up."
show ran p talk with dis
r "\"It'll never happen again.\""
m "\"Yeah…\""
hide ran p talk with dis
"I mumble, looking as he approaches the window and opens the shutters."
scene bg broom_day with dis
"He stretches out as the light floods the room again."
"I watch as he goes into a whole routine of exercises; touching his toes and arching himself backwards."
"It's quite embarrassing to just sit here, but it would be even more so to join him and make a fool out of myself."
"I'm stiff like a plank, especially after sleeping rough."
show ran p talk with dis
r "\"I have to run some errands today… my father is in a rather sour mood, as you can imagine.\""
show ran p think with dis
r "\"I need you to stay out of sight while I’m gone. Although you’re allowed to stay in the village, you’re still kinda controversial.\""
show ran p neutral with dis
m "\"Yeah, I figured.\""
show ran p smile with dis
"There goes our hike in the woods…"
show ran p talk e with dis
r "\"Don’t worry, it’s not permanent. Not if I can help it.\""
show ran p talk p with dis
r "\"At the moment you’re freaking everyone out a little bit, but it should pass with time.\""
show ran p smile with dis
"I'm not happy about being cooped up in this house any longer, but I don’t exactly have a choice in the matter either."
show ran p talk with dis
r "\"I’m working with Verissa on a plan to smooth things over. Once that’s done, you'll be introduced to the tribe proper.\""
show ran p smile with dis
m "\"And that means?\""
show ran p awkward with dis
r "\"Let’s worry about it when we get there.\""
show ran p smile with dis
"He snorts, rubbing his nose."
"That's another non-answer, as usual; I should start getting used to those by now."
hide ran p smile with dis
scene bg kitchen_day with dis
"He walks away into the kitchen, and I decide to follow."
scene waterbowl with dis
"We take turns with the water bowl and during my wash up I realise my teeth feel rather coarse and my breath is not what I’d like it to be."
m "\"Do you guys clean your teeth at all? Perhaps with a brush or some paste…\""
r "\"I swear, that theory about you being a lost human noble begins to check out on near regular basis.\""
"The male laughs, approaching me with a teasing smirk."
"He presents me with a little birch twig, it’s flesh young and juicy."
r "\"Grind the end with your teeth and then use the bristles to clean.\""
"He demonstrates, gnawing on an imaginary twig."
"I shrug, no longer questioning this renaissance fair I’m living through. "
"In truth, it’s actually all quite interesting."
"The twig has a rather pleasant, fresh flavour, almost citrusy in fact and to my surprise, is quite effective in what it’s supposed to do."
scene bg kitchen_day with dis
show ran p smile with dis
"Once I’m done, I rinse my mouth and look at Ranok who approaches me with a smile."
"He randomly puffs into my face, his breath smelling incredibly fresh and pepperminty."
"That’s when he hands me a small bushel of fresh peppermint."
show ran p wink with dis
r "\"Chew on it and you’ll be set.\""
"He winks."
hide ran p wink with dis
"I take a few leaves and put them into my mouth."
m "\"Hmmm.\""
"I flash my brow in amusement; it’s not that bad."
"Seeing that there isn’t anything into which I could spit out the mushed leaves, I simply swallow them."
"I mean... it's just peppermint."
"Ranok scrambles around the house frantically, collecting different bits and pieces of his gear."
scene bg broom_day with dis
show ran c embarrassed e with dis
"I join the wolf in the bedroom, resting against the doorframe and watching as he hastily combs his neck fur."
"It's hard to stifle a chuckle, both at his sorry attempts at taming his fluff and the fact he's using the very same 'weapon' I tried to fend of Vulgor."
show ran c shocked with dis
m "\"You need any help with that?\""
show ran c awkward with dis
r "\"Would you, really?\""
show ran c embarrassed blush with dis
"He sounds almost pleading."
show ran c shocked blush with dis
m "\"Sure, why not?\""
show ran c smile with dis
"I approach the wolf, who passes me the comb with slight embarrassment in his eyes."
show ran c awkward with dis
r "\"I'm in a bit of a hurry, so this will be great help.\""
show ran c smile e with dis
m "\"Don't worry about it.\""
"I snicker, sinking the comb into his lush neck."
"At first, I'm worried there will be some tangles to struggle with."
"I wouldn't want to pull to hard, as to not cause pain, however his fur is well kempt."
m "\"You think you'll take long?\""
"I ask while running the comb from the back of his head to the base of his shoulders."
"The sounds of his fur againts the comb is almost as satisfying as the brushing itself."
show ran c awkward with dis
r "\"I hope not, but you never know… father wants me to deal with a few things.\""
show ran c smile e with dis
"The idea of staying here alone is just as novel as it is slightly distressing… for some reason I almost feel vulnerable when he's not around."
m "\"What things?\""
show ran c neutral rt with dis
r "\"I'd rather not discuss that now…\""
show ran c neutral e with dis
"He sounds troubled and although it does pique my curiosity I decide not to pry."
"Ranok's made good on coming forward with information at the right time before."
"I don't have a reason to distrust him."
show ran c smile e with dis
"He groans softly, closing his eyes as I continue to groom him."
"Truth be told, brushing him feels rather nice and I can see he's enjoying it as well, as his tail begins to swish energetically."
show ran c awkward with dis
r "\"Right, that'll have to do.\""
show ran c smile with dis
"He smiles, running a paw through his fluff."
show ran c talk with dis
r "\"Thanks.\""
show ran c smile with dis
m "\"No problem.\""
"I shrug; honestly I don't think I did much at all as his fur was tidy to begin with."
show ran c talk with dis
r "\"I'll try to come back as soon as I'm able.\""
show ran c talk paw with dis
r "\"Verissa should check on you later today, to change your dressing.\""
show ran c neutral with dis
m "\"Before you go... I would need to… use the facilities.\""
show ran c confused with dis
"The wolf blinks."
show ran c confused paw with dis
r "\"The facilities? What are you talking about?\""
show ran c confused with dis
"Oh, no… he's making me spell it out for him."
"I really hate that I have to announce my toilet breaks; it's really awkward."
m "\"Ummm… I need to water the bushes...\""
show ran c shocked with dis
r "\"Oh!\""
"He finally exclaims in understanding, quickly looking at the kitchen door."
show ran c talk r paw with dis
r "\"Hrm… just use one of the buckets in the other room.\""
show ran c neutral with dis
"Now I'm the one who blinks."
m "\"You can't be serious… are you telling me you're doing your business in a bucket?\""
show ran c shocked with dis
r "\"What? No!\""
show ran c embarrassed with dis
m "\"Then what made you suggest me doing it?\""
r "\"Well, I assumed you just needed to pee, but if it's the number two, then I-\""
show ran c shocked with dis
m "\"No! It's not number two!\""
show ran c confused with dis
"I interrupt him, completely mortified about this entire conversation."
m "\" I- ugh… I just won't be peeing into a bucket.\""
show ran c talk e with dis
r "\"Lah-di-dah, my lord.\""
show ran c smile with dis
"He gets up, genuflecting in a mocking fashion."
show ran c talk paw with dis
r "\"If your highness wants to do his business outside, you have to go through the window.\""
show ran c smile with dis
"He nods towards the ledge and I sigh in mild annoyance."
m "\"Oh, you've gotta be kidding me.\""
show ran c smirk paw with dis
r "\"Well, I'm meant to keep you out of sight, which is part of the whole deal here. Using the front door isn't an option.\""
show ran c smile with dis
"He snickers, bumping my shoulder teasingly."
m "\"Ugh, fine… but I don't think you'll fit through…\""
show ran c wink with dis
r "\"Good thing you are {i}tiny{/i}, then.\""
show ran c smile with dis
"I give him an annoyed stare, grumbling under my breath."
m "\"I will find out your pup-name, if it's the last thing I do.\""
show ran c laugh with dis
r "\"Sure, you will.\""
"He laughs, walking towards the kitchen."
show ran c talk e with dis
r "\"I'll meet you on the other side.\""
scene bg window_day with dis
"I shake my head and approach the sill, slowly pulling myself onto the ledge."
"Once I'm up, I look around for any sign of the wolf."
"It takes him a while to walk around the house, but once he arrives he extends his paw, helping me down from the ledge all the while smiling as I clumsily clamber over."
scene bg outdoor_d with dis
show ran c smile with dis
m "\"This is ridiculous…\""
show ran c neutral r with dis
"The wolf gives two quick glances in both directions, ensuring no one's around his house."
show ran c talk r paw with dis
r "\"Right… if it's just a leak, you can simply go here.\""
show ran c smile with dis
"He points to the side and I look around in confusion."
m "\"What?\""
scene bg cottage side day with dis
show ran c talk paw with dis
r "\"Here, against the wall.\""
show ran c smile with dis
m "\"I'm not pissing on your house!\""
"I huff defiantly at the suggestion."
show ran c smirk shrug with dis
r "\"What does it matter? I don't care and the house won't mind.\""
show ran c smile with dis
"I stand still, not even acknowledging it."
show ran c laugh with dis
r "\"D'aww, are you a shy pee-er? Is that it?\""
show ran c smile with dis
"He asks mockingly."
m "\"I'm {i}not{/i} a shy pee-er!\""
show ran c smirk with dis
r "\"Well then, prove it.\""
"A challenging smirk stretches across his muzzle and my mouth opens wide."
m "\"What?\""
show ran c talk e with dis
r "\"Here, I'll show you how it's done.\""
show ran c smile e with dis
"He snickers and turns to the side, slowly undoing his pants."
hide ran c smile e with dis
"I quickly throw my gaze into the distance, shielding my eyes with a hand."
m "\"NO! Don't show me ANYTHING!\""
play sound "sfx/trickle.ogg" fadeout 3.0
"The wolf only chuckles, as I hear a stream splash against the wall."
m "\"Ugh, dude!\""
"I mutter in annoyance, walking some distance away from him."
r "\"Haha… You {i}are{/i} a shy pee-er!\""
stop sound fadeout 3.0
m "\"And you're a shameless one!\""
"He knows how to make me feel uncomfortable, that's for sure."
show ran c smile e with dis
"Eventually he joins me, still tidying up his pants."
show ran c smile with dis
"Once he's done, I can see his arm swoop to embrace me, but I manage to evade his grasp at the very last moment."
show ran c shocked with dis
m "\"Nope! You're not touching me with those paws until you wash them!\""
show ran c laugh with dis
r "\"I didn't piss on them!\""
"Ranok scoffs at the suggestion."
show ran c smile with dis
m "\"I'm serious…\""
"He laughs, shaking his head and giving me an amused shrug."
show ran c wink with dis
r "\"As you wish, my lord.\""
show ran c smile with dis
m "\"Just take me to the toilet, please!\""
"I almost sound pleadingly, really getting more and more uncomfortable about this whole situation."
show ran c worried rt paw with dis
r "\"The outhouse is a little bit further behind…\""
show ran c sad with dis
"He says with a worried tone."
show ran c sad t with dis
r "\"I'd rather no one see you… you sure you can't just muster the courage to go here?\""
show ran c shocked with dis
m "\"Is this the only privy in the entire village, or are you expecting people to be queuing up to yours in particular?\""
show ran c smirk with dis
r "\"Haha… fine, fine. Cut the snark.\""
show ran c smile with dis
"The wolf shakes his head and waves at me to follow."
scene bg outdoor_d with dis
show ran c smile with dis
"We walk few paces through the bushes, until I can see a small shed nestled between the trees."
show ran c talk r paw with dis
r "\"Right… here it is.\""
show ran c smile with dis
m "\"Yep…\""
"I nod, pretty much having my worst suspicions confirmed."
"I look around, almost as if hoping that another toilet, more suited to my needs materialise out of the blue, but I quickly realise there's no other way around it."
show ran c confused with dis
m "\"Ok, now if you won't mind…\""
"I sigh, shooing him away with my hands."
show ran c think with dis
r "\"Hmmm. I don't know about this. I'd rather stay close-\""
show ran c shocked with dis
m "\"Ranok! I'm not planning an escape and I doubt anyone is going to ambush me while I'm in the loo; I just want to have some privacy…\""
"I mutter in resignation and the wolf gives me an awkward smile."
show ran c awkward with dis
r "\"Fine, fine. You're right.\""
r "\"Sorry.\""
hide ran c awkward with dis
"He backs down slowly, and I take a deep breath."
"This is going to be the least favourite part of this entire misadventure."
scene bg black with slow_dissolve

scene bg window_day with slow_dissolve
"I try to pull myself back onto the ledge, but before I even know it, Ranok aids me in my struggle."
"My eyes widen as his massive paw cups my butt, allowing the wolf to push me upwards."
"Did he just feel me up?"
"I dart my gaze back towards him, only to catch a glimpse of his cheeky expression as he rushes off into the distance."
r "\"Stay put!\""
"His mocking command reaches me, and I shake my head in amusement."
"Scampering through windows feels so odd, but also kind of fun."
"There's something inherently childish about it, as if I'm a naughty kid having a forbidden sleepover at a friend's house."
scene bg broom_day with dis
"Once I jump over the ledge, I almost trip over the clutter that previously occupied it."
"I have half a mind to just return all of this to the sill, but considering how musty this house is, I'd rather be able to leave the window open for a while."
"For the time being, I simply move it all to the cupboard; I'm just a guest, I shouldn't rearrange things."
"When I place the leather-bound book down, I decide to have a quick peek inside."
"I flip the hard cover, curiously looking over the first page, wondering if I will recognise the lettering."
"To my surprise it looks like a regular book, with regular writing."
"'Brief history of Fhreyfall.'"
"Ugh… a history book."
"Considering my circumstances, it's the last thing I need..."
"It would be like reading Chronicles of Narnia."
"I laugh at my own joke, putting the book away… only to have my heart sink immediately at the realisation I have no idea why it was so funny."
"What's Narnia anyway?"
scene bg black with dis
ow "\"Forever lost...\""
scene bg broom_day with dis
"Oh no, not this again…"
"I quickly shake my head, not wanting to deal with another invasive torrent of thoughts."
"With Ranok gone I don't have my safety net and I cannot let this day drag on."
"I need to keep myself busy."
"I glance around to find something to do and the first thing that comes to my mind is tidying up the place."
"It’s clear Ranok doesn’t spend much time in his house, but that’s no excuse to live with so much dust… that’s not healthy."
scene bg kitchen_day with dis
"I remember seeing a broom earlier near the fireplace, so I walk into the kitchen to find it."
"I also open all the windows, leaving the doors to the bedroom ajar so that the fresh air could run through the house while I commence my cleaning."
"I grab the broom and immediately get to work of brushing all the dirt from the floor and gather up all the cobwebs dotting the walls and corners."
"Over time I begin to collect a small heap which I only grow by brushing more and more dust from all the different nooks and crannies."
"As I don't see a shovel anywhere, I decide to use one of the dirty linens still bundled up in the bedroom."
"I lay it out flat in the middle of the floor and simply brush the mound of dust onto it, I then bring the corners together, effectively creating a sack."
"Once that is done, I simply walk over to the window and chuck the dirt outside, flapping the linen over the ledge to dust it off."
"I rest myself against the wall, rubbing my forehead and releasing an exhausted sigh."
"This was a bit of a workout."
"But just as I try to rest, the nagging sensation in my stomach returns."
"Nope, not today dark thoughts!"
"I won't let you overwhelm me even if I'll have to clean this house inch by inch."
"Holding the dirty cloth in my hand gives me an idea."
"I rush over towards the water bowl and decide to use the remaining contents to wash the floors."
"I simply dip the cloth and then rub it over the wooden panels."
"Slowly, but surely each plank regains its shine and polish."
"I almost thought this was naked wood but turns out it was only dull because of all the dirt and grime."
"The draft makes cleaning that much easier and pleasant, with cool breeze gently kissing my skin."
"I stop now and then to nibble on what remained from my breakfast."
scene bg broom_day with dis
"I don't know how long I spent on my knees, cleaning the floors… might have been two or three hours, but eventually I end up in the bedroom, finishing the last panel."
"I stretch out, feeling the pain in the back and my hands, but also sense of pride at the fruit of my labour."
"I use whatever water was left inside to clean up the surfaces, dusting off everything with a damp cloth."
"I could see some stray wolves passing by the windows from time to time, taking a curious gander inside."
"I guess they just want to sneak a peek at the human and I can’t blame them."
"Had the roles been reversed, and I learned one of my friends had a werewolf inside their house, I would’ve done the same."
"As the afternoon turns into an evening, I admire my handy work."
scene bg kitchen_day with dis
"The cottage looks quite homely now."
play sound "sfx/knock.ogg"
"And just as on cue, I hear knocking at the door."
"For a moment, I wonder whether I should actually answer, that's when the familiar cold voice reaches me."
v "\"Piglet?\""
"I sigh through a smile, quickly opening the doors."
play sound "sfx/door open.ogg"
show vul talk p with dis
v "\"Got some food for ya.\""
show vul neutral with dis
"The black male stands in the doorway, holding in his paw a loaf of bread and string of sausages."
"Thank goodness, all this work was making me quite hungry."
"Not to mention, I just lost my only source of occupation that allowed me to steady my emotions."
show vul intrigued with dis
m "\"Will you stay with me for a while?\""
"The black male regards me with a risen brow, clearly surprised by the suggestion."
m "\"Don't worry, it's not an immoral proposition.\""
"I jest."
m "\"I'd like some company. Now that everyone knows I’m here… it should be fine, right?\""

if Vulgor >= 2:
    show vul talk with dis
    v "\"Desperation doesn't suit you, Piglet.\""
    show vul neutral e with dis
    "He scoffs, walking past me and entering the cabin."
    play sound "sfx/door close.ogg"
    "I hastily close the door, as the wolf approaches the table and inspects one of the tankards."
    show vul sigh with dis
    v "\"Might as well grab a beer if I'm to pup-sit you.\""
    show vul intrigued with dis
    "He teases, looking at me expectantly."
else:

    show vul neutral e with dis
    v "\"Hmmm…\""
    show vul neutral l with dis
    "He ponders, looking at the opened windows."
    show vul intrigued with dis
    m "\"It’s not night yet.\""
    "I add teasingly."
    show vul unamused with dis
    m "\"Surely no one will suspect us of getting up to no good.\""
    play sound "sfx/door close.ogg"
    "The black wolf snorts and closes the door behind him."
    show vul sigh with dis
    v "\"Very well. But I'll have some ale while I'm here.\""

show vul neutral with dis
m "\"Sure, if there is any.\""
"I shrug, looking around the kitchen."
"Vulgor points towards a barrel standing in the corner of the room."
"Guess Ranok's home is pretty well stocked up."
show vul talk pu with dis
v "\"He always stashes the good stuff.\""

if Vulgor >= 2:
    show vul neutral with dis
    "Vulgor passes me the mug, shoving it into my chest."
    "I guess he expect me to fetch the beer for him."
    "I just shrug and decide to play along."
else:

    show vul neutral with dis
    "I nod and fetch one of the tankards that rested on the table."

"As I approach the barrel I notice it doesn't have a tap, but I can see the lid has a handle on it."
show vul smile with dis
"I lift it up and submerge the mug in the dark liquid."
show vul smile l with dis
"As I bring it back to Vul, he has already seated himself comfortably at the table, his gaze clearly darting around the house in mild amusement."
show vul talk sup with dis
v "\"I see Ranok has found himself a little den-wife.\""
show vul smile with dis
m "\"W-what?!\""
"I blurt out, blush appearing on my face almost instantly."
m "\"It was extremely dirty in here!\""
show vul amused with dis
v "\"Mhmmmm…\""
show vul smile with dis
"He croons teasingly, taking a gulp of ale and sliding the bread and sausages across the table towards me."
m "\"Seriously!\""
m "\"I don't want to get allergies… it's enough that there's fur everywhere, I can do without dust!\""
show vul talk with dis
v "\"What's 'allergies'?\""
show vul intrigued x with dis
"He asks indifferently, catching me off guard."
m "\"It's… it's..\""
"Fuck… how do I explain it?"
m "\"It's when your body reacts badly to certain things… like getting a rash or a stuffy nose.\""
"I propose, grabbing a knife and cutting off a thick slice of bread."
"The wolf gives me a sceptical look, as I enjoy the wonderful aroma of a freshly baked loaf."
show vul talk s with dis
v "\"Dust makes you ill?\""
show vul intrigued x with dis
"He scoffs, taking another sip."
m "\"Well, it can.\""
m "\"Fur as well, but so far, I'm fine.\""
"To be fair I can't recall if I ever was allergic to fur or dust but I'm not going to admit I cleaned the entire house because I'm slowly losing my damned mind."
m "\"I was simply tidying up, because the last thing I need is getting allergies.\""
m "\"Especially since it's spring, there's plenty of pollen in the air.\""
"Vulgor puts the mug down and drills his gaze into me."
show vul eyeroll with dis
v "\"Flowers make you ill as well? Fuck me, might as well just roll over and die.\""
show vul intrigued x with dis
"I curl my lips, staring at the ceiling."
m "\"You're not a human, you wouldn't understand.\""
"Do beast men even have allergies?"
"I toy with the piece of bread, squishing the slice between my fingers."
"It's still warm and sprightly."
show vul talk ang with dis
v "\"I doubt anyone in Avalan would understand your nonsense.\""
show vul neutral with dis
"On that we can agree…"
"I swear, there is nothing more satisfying than a smell of fresh bread."
"It completely distracts me from Vulgor's jabs, inviting to take bite and I finally succumb."
show vul intrigued with dis
"I gasp, feeling the crust crunch between my teeth."
"The taste of the rustic grain immediately summoned emotions tied to some long-lost memory…"
"…a more wholesome time, time of happiness and joy."
"I'm in heaven."
show vul unamused with dis
v "\"Doesn't take much to please you, huh?\""
"The wolf comments on my obvious satisfaction with a slightly troubled expression."
m "\"You have no idea how much I wanted some fresh bread, it's almost as if you read my mind.\""
show vul eyeroll with dis
v "\"Actually, it was Ranok's idea.\""
show vul neutral with dis
"He looks at the window."
m "\"Oh?\""
show vul talk with dis
v "\"Ever since he found you, he was learning about humans...\""
show vul talk pl with dis
v "\"Your history, customs... staples of your diet.\""
show vul neutral with dis
"I discretely dart my gaze around the house, locating different books stashed in corners."
"Now that Vulgor mentioned it, Ranok doesn’t strike me as a scholarly type."
"He was doing his research while I was still unconscious… it makes me feel almost humbled."
show vul talk e with dis
v "\"We don't care much for bread, it's prey chow, so there's hardly any around that hasn't gone stale.\""
show vul talk pu with dis
v "\"But now that you're no longer a secret, he asked for one to be made fresh for you.\""
show vul neutral with dis
"I blink, taking in what he just said."
"Ranok went to all this trouble for me?"
"Huh…"
"That's extremely considerate and sweet of him."
show vul intrigued with dis

if Romance == True:
    "But at this point it's hard to differentiate between just his general kind-hearted nature and something more…"
    "Am I reading into things again?"
    "Probably... I mean, he did say he's not into me."
else:

    "This is extremely confusing… he’s going out of his way far more than necessary."
    "Perhaps I should actually talk more openly with him, try to figure out what his actual feelings are."
    "There's no hurt in that, right?"

if Vulgor >= 2:
    show vul talk with dis
    v "\"Everything alright?\""
    show vul intrigued with dis
    "The black male asks idly, as he takes another thirsty gulp from his tankard."
    m "\"Yeah.\""

"I smile, biting into the bread again."
show vul unamused with dis
"As I chew, I grab the knife and cut off a piece of sausage."
"I give it a quick sniff, before stuffing it into my mouth."
"Only now I notice that the wolf has been avoiding looking at me for quite a while now."
"I almost choke, trying to swallow my food through a laugh."
show vul intrigued x with dis
m "\"Dude, you stabbed me!\""
m "\"Being an experienced butcher, I'm sure you’ve seen worst things than me eating!\""
show vul growl x with dis
v "\"Wanna bet?\""

if Vulgor >= 2:
    "He sneers teasingly, giving me a side-eye."
else:

    "He sneers, giving me a side-eye."

show vul neutral e with dis
"I just shake my head in amusement and continue with my meal."
"The sausage is nice, but a little bit too garlicy for my taste, however I'm not going to complain about free food."
"All of this is extremely wholesome and makes me feel warm inside, as if an echo of my past tried to scream through the shroud of my amnesia."
"I’ve had to enjoy a homely meal like this before."
"I just sigh, relishing this sliver of a good memory."
show vul neutral with dis
"We sit like this for a while, Vul simply finishing his ale and not saying much."
"He doesn't seem to be much of a talker, but I don’t mind."
"His company alone allows me to steel myself against any nagging feelings stalking the recesses of my mind."
"I just wish I had something to start a conversation with."
show vul sigh with dis
v "\"Despite the bandage looking rather gruesome, you seem to be doing fine.\""
show vul neutral with dis
m "\"Oh… yeah.\""
"I smile awkwardly, reminded that the dressing is pretty much red and crusty."

if Knife == True:
    show vul intrigued with dis
    m "\"I'm sorry I didn't pick you…\""
    m "\"It was clear you knew what you were doing… and I might have accidentally traumatised Ranok.\""
    "The black male looks at me with confusion."
    show vul talk p with dis
    v "\"You were the one being stabbed… and you're worried Ranok got traumatised?\""
    show vul neutral with dis
    "I wince."
    m "\"When you put it like that…\""
    show vul talk l with dis
    v "\"Ranok got thick skin, as for me…\""
    show vul smirk with dis
    v "\"I still got to stab you.\""
else:

    show vul intrigued with dis
    m "\"Well, you did a good job.\""
    "I rub my side, to put him at ease."
    m "\"It looks worse than it feels, that's for sure.\""
    show vul smile with dis
    "Vul readjusts himself, patting the hilt of his dagger."
    show vul talk sup with dis
    v "\"Since you enjoy it so much, I could do it again.\""

show vul smile ue with dis
"He gives me a satisfied grin."
"At this point it's hard to tell whether he's teasing or being serious, but I decide to just laugh it off."
show vul talk su with dis
v "\"One has to wonder if you're not into it, considering how you almost beg to get skewered.\""
show vul smile with dis
"I roll my eyes, giving him a stern look as the joke becomes slightly tortured."
show vul intrigued with dis
m "\"What are you on about?\""
show vul talk with dis
v "\"The Chief?\""
show vul neutral with dis
"He asks mockingly."
show vul talk p with dis
v "\"I've heard Ranok's father nearly cut you open like an actual pig.\""
show vul neutral e with dis
"The wolf snorts, loudly slurping the remnants of his beer while I wince uncomfortably."
m "\"Yeah.\""
"I'm not proud of my carlessness."
m "\"Had Verissa not intervened, I wouldn’t be here.\""
show vul talk with dis
v "\"You dropped the ball, Piglet. I told you to be careful.\""
show vul neutral with dis
"The male nods, giving me a patronising look."
m "\"I know…\""
m "\"I’m just grateful Verissa stuck up for me…\""
show vul talk pu with dis
v "\"She didn't do it for you… nor she had any other choice.\""
show vul neutral with dis
"He shrugs, toying with the now nearly empty tankard."
show vul talk pl with dis
v "\"Had you been killed without her making her case, all of us would face serious consequences.\""
show vul neutral with dis
m "\"I assumed as much.\""
"I sink in my shoulders, awkwardly trailing my gaze around the room."
"Somehow, I feel embarrassed as if I disappointed him."

if Vulgor >= 2:
    show vul talk e with dis
    v "\"But you have more luck than brains…\""
else:

    show vul talk e with dis
    v "\"As dumb as you are, you seem to be equally as lucky.\""

show vul neutral with dis
"He snorts, noticing my discomfort."
show vul talk with dis
v "\"The little runt went straight for his dad.\""
show vul talk pl with dis
v "\"Had it been Tano, he'd go for one of the elders and we'd all be fucked.\""
show vul intrigued with dis
m "\"Perhaps you should tell that to Ranok.\""
"I mutter, immediately recalling my conversation with the wolf."
m "\"He seems to hold a grudge against his brother.\""
show vul talk with dis
v "\"Why shouldn't he? The pup is nothing but trouble.\""
show vul neutral with dis
"The black male scoffs in annoyance."
m "\"He's still his brother.\""
show vul talk e with dis
v "\"Half-brother. And siblings don’t mean much to us.\""
show vul neutral x with dis
"He waves his paw impatiently."
show vul talk p with dis
v "\"Each of us is expected to have multiple pups, most of which with a different partner.\""
show vul talk su with dis
v "\"So, the only reason to keep track of all the blood relations is to not accidentally bugger one of them.\""
show vul smile with dis
"He lets out a loud snort, as if the idea amused him."
m "\"Yeah… Ranoks told me as much.\""
show vul neutral x with dis
"Their way of life is definitely much different to what I expected."
show vul talk e with dis
v "\"Why are you worrying about that pup anyway? He has nothing to do with you.\""
show vul neutral with dis
m "\"I just worry. I wouldn't want Ranok to take it out on him.\""
show vul sigh with dis
v "\"Psh. Two peas in a pod.\""
show vul neutral e with dis
"The black male scoffs, slushing the remnants of his drink around the cup."
m "\"What do you mean?\""
show vul talk p with dis
v "\"You and Ranok.\""
show vul neutral with dis
"He shrugs, taking the last gulp of his poison."
show vul talk with dis
v "\"Worrying about strangers who get you into trouble is exactly what started this whole mess.\""
show vul neutral with dis
m "\"Then you know I'm right; because saving me was a kind thing to do.\""
show vul talk ang with dis
v "\"Kindness is what gets people killed.\""
show vul neutral x with dis
"The black wolf nods towards the other tankard on the table."
show vul talk p with dis
v "\"Are you going to have one?\""
show vul intrigued with dis
"I look at his risen brow."
"I'm not much of an ale drinker…"

menu:
    "Agree":
        $ Vulgor += 1
        $ DrinkingBuddy = True
        "But I guess I can humour the wolf."
        show vul smile with dis
        m "\"Yeah, sure.\""
        show vul talk su with dis
        v "\"Then be a good servant and fill mine up as well.\""
        show vul smile with dis
        "I blink, as he pushes his mug towards me, but decide not to make much of his tease."
        "I walk over to the barrel and plunge the tankards one by one, filling them up to the brim with the dark liquid."
        "It's almost as black as coffee."
        "Oooh… coffee would be great, but something tells me that it would join the likes of salt and soap- another frivolity to tease me over."
        "I place the tankard next to the black wolf and he picks it up."
        show vul talk sup with dis
        v "\"Sláinte!\""
        show vul smile u with dis
        "He raises his mug, clearly waiting for me to clang mine into it."
        m "\"Sláinte!\""
        show vul smile with dis
        "I oblige and we spill a little bit in the process."
        "I cannot contain a timid chuckle, as I sit back and take a sip."
        "The bitterness of the brew hits me almost instantly."
        "It’s malty and rich, almost like roasted cereal."
        "There’s also a hint of floral sweetness to it that I cannot wrap my finger around."
        "I smack my lips, licking off thin foam that lingered on them."
        "It’s like no beer I ever drank, that’s for sure."
        "If I drank any that is..."
        show vul talk s with dis
        v "\"Enjoying it?\""
        show vul intrigued with dis
        m "\"I think ale is an acquired taste, no?\""
        "He rises his brow."
        m "\"Considering I never had anything like it before, only time will tell.\""
        "I can see my comment catches him by surprise and he laughs, shaking his head."
        show vul amused with dis
        v "\"Cheeky little Piglet.\""
        show vul intrigued x with dis
        "He takes a long, thirsty gulp, all the while gazing at me, almost as if expecting me to match his tempo."
        "Yeah… that’s not going to happen, buddy; but I’m willing to at least try."
        show vul neutral x with dis
        "I take another mouthful, barely even tapping into the contents of the oversized mug."
        "That’s definitely more than a pint, at least two times more."
        show vul talk p with dis
        v "\"If you’re going to sip it like a housefly, you might finish before next Full Moon.\""
        show vul neutral with dis
        "He snorts, as I swallow my drink."
        "I huff in annoyance and take another, this time much deeper gulp."
        show vul intrigued with dis
        "Forcefully chugging the ale might not be pleasant but is actually better than the lingering bitterness when I take my time with it."
        m "\"Speaking of…\""
        "I look at his moonstone, finally having a somewhat natural segue into a proper conversation with him."
        m "\"Are all wolves born during the same night Moon Brothers?\""
        show vul neutral with dis
        v "\"Hmmm?\""
        m "\"Like you and Ranok.\""
        "I shrug, taking a bite of the sausage to get rid of the aftertaste."
        "In truth, now the sausage doesn’t seem that bad, it pairs well with the ale."
        "Masks it’s bitterness, that’s for sure."
        show vul intrigued with dis
        "I look to Vulgor expectantly, as he takes his time with another gulp."
        "He eventually lets out a sigh and rubs his lips."
        show vul talk with dis
        v "\"Why do you ask?\""
        show vul neutral with dis
        m "\"Well, since you said blood relations don't mean much... I'm kinda curious, as you two make a big deal out of the Moon Brother thing.\""
        m "\"How do wolves become Moon Brothers?\""
        show vul talk pl with dis
        v "\"You have to be born in the waters of the same Moon Well during the same Phase of Aluna."
        show vul neutral l with dis
        m "\"A Moon Well?\""
        "I ask, cutting off another slice of bread."
        show vul neutral e with dis
        "I watch as the wolf walks over to the ale barrel, helping himself to a third mug."
        "It’s surprising how fast he goes through those… I’m not even halfway finished."
        show vul talk ang with dis
        v "\"There is a shallow pool at the centre of our shrine. It's lined with small stones and filled with clear spring water.\""
        show vul neutral x with dis
        "He explains, sipping off the excess that began spilling from the mug as he retrieved it from the barrel."
        "I think it’s safe to say he enjoys the ale more than my company…"
        show vul talk pl with dis
        v "\"The pool supposedly collects the moonlight, blessing the waters which then are used for different religious purposes.\""
        show vul intrigued with dis
        m "\"Like birth?\""
        "I look to him as he takes his seat."
        show vul talk l with dis
        v "\"Among others.\""
        show vul neutral with dis
        "The wolf shrugs as he wets his lips again."
        "I can see he’s nowhere near getting drunk, it's almost like drinking water to him..."
        "I just have a suspicion that once he has his fill, he’ll simply fuck off."
        "I need to pace him a little, so I cut off a piece of sausage and push it his way."
        show vul amused with dis
        v "\"Heh.\""
        show vul smile with dis
        "He smiles at my gesture and takes a bite."
        show vul talk sup with dis
        v "\"Those are for you.\""
        show vul intrigued with dis
        m "\"I know... but they pair well with the beer. And it's plenty enough for me.\""
        "I smile, taking an idle sip."
        show vul amused with dis
        v "\"Fair play.\""
        show vul smile with dis
        "He shrugs, flicking up the remaining piece of sausage and swallowing it with a loud chomp."
        show vul talk l with dis
        v "\"Anyway... when a female goes into labour, she's brought to the Well. Once a pup is born, one of the pebbles reveals itself as a Moonstone.\""
        show vul talk p with dis
        v "\"Have two females go into the labour at the same time… well… you can guess the rest.\""
        show vul intrigued with dis
        m "\"That sounds… magical.\""
        "I smile, genuinely amazed by the concept."
        "It sounds so simple and in tune with nature."
        "Their traditions, even if odd, do have a certain allure to them."
        show vul talk e with dis
        v "\"I guess so. I’m sure there is some trick involved…\""
        show vul talk lx with dis
        v "\"There’s always a trick in religion.\""
        show vul neutral x with dis
        "He scoffs in annoyance."
        show vul talk ang with dis
        v "\"I wouldn’t place much stock in the coincidence of being born at the same time as another pup. That's just sappy nonsense.\""
        show vul intrigued x with dis
        m "\"You… you don’t believe in it?\""
        show vul neutral x with dis
        "It’s almost amusing how polar opposites those two wolves are; with Ranok screaming fate at everything he sees, while Vul sniffing some sort of deceit everywhere he looks."
        show vul talk lx with dis
        v "\"I might not believe in the supernatural aspect of my bond with Ranok… but I've heard enough about the circumstances of my birth to concede a simple fact:\""
        show vul talk ang with dis
        v "\"We {i}are{/i} Moon Brothers. The rest is fluff.\""
        show vul intrigued x with dis
        m "\"Oh?\""
        show vul unamused with dis
        "I issue involuntarily, expecting a follow up, but the wolf does not respond."
        "Instead, Vul simply takes another long swig at his tankard, emptying it in one go."
        show vul intrigued with dis
        "Once he bangs it back onto the table, he looks at me with confusion."
        show vul talk with dis
        v "\"What?\""
        show vul neutral with dis
        m "\"What were the circumstances of your birth?\""
        show vul eyeroll with dis
        v "\"Ugh…\""
        "He rolls his eyes in annoyance, I guess he didn’t mean to mention it."
        show vul intrigued x with dis
        m "\"We can have another.\""
        "I propose, to which he only gives me a telling gaze."
        show vul talk p with dis
        v "\"How can you have another, if you haven't even finished your first one?\""
        show vul intrigued with dis
        "He knows I’m fishing for detail, but how can he blame me?"
        m "\"Please! You can’t leave me hanging like this…\""
        show vul talk l with dis
        v "\"Try me.\""
        show vul neutral with dis
        "He scoffs, standing up."
        "Fuck, I'm losing him!"
        show vul intrigued with dis
        m "\"Ok, I didn’t want to do this, but you kinda owe me for the choking.\""
        show vul talk su with dis
        v "\"I owe you, you say?\""
        show vul smile with dis
        "He laughs mockingly."
        show vul amused with dis
        v "\"Press your luck further, Piglet and you’ll earn another scar.\""
        show vul neutral with dis
        "I watch, as he approaches the door and I fidget with my fingers in panic."
        "At this point I don’t know if it’s about the story itself, or the fear of being left alone."
        show vul shocked with dis
        m "\"Moonshine!\""
        "I shout out as his paw lands on the door handle, almost surprised by the words that came out of my mouth."

        if Booze == True:
            m "\"We can have some moonshine!\""
            show vul neutral l with dis
            v "\"Hrmmmmm…\""
            "He croons, narrowing his eyes and looking back at me."
        else:

            "He stops in his tracks as his ear twitch."
            show vul talk l with dis
            v "\"I don't drink booze alone.\""
            show vul neutral with dis
            "The male says in a low growl, giving me an idle tail flick."
            m "\"Of course. We'll share.\""
            "He regards me with slight disbelief."
            show vul talk p with dis
            v "\"You wouldn't drink when stabbed, but you would drink now?\""

        show vul amused with dis
        v "\"That desperate, huh?\""
        show vul smile with dis
        "The black wolf snickers, approaching the cupboard and I sigh internally."
        show vul talk su with dis
        v "\"Very well.\""
        show vul neutral at fourteen with move
        "He walks towards the cupboard and retrieves the familiar clay bottle."
        "I watch as he removes the cork with his teeth, causing a loud pop."

        if Booze == True:
            show vul talk p at six with move
            v "\"Here. Earn it.\""
        else:

            show vul talk p at six with move
            v "\"Here. Prove it.\""

        show vul neutral with dis
        "He passes me the bottle and I swallow heavily feeling the boozy smell hit me once again."
        "This is not going to be pleasant, but I better put my money where my mouth is."
        show vul intrigued with dis
        "I reluctantly grab the bottle, remembering his initial tip."
        "I tilt my head back and allow a large gulp to slush straight into the back of my throat, swallowing deeply."
        show vul amused with dis
        v "\"Hmph.\""
        show vul smile with dis
        "He mutters in amusement, seeing as I manage to stomach two long swigs."
        show vul talk su with dis
        v "\"Not bad for a suckling.\""
        show vul smile with dis
        "He guzzles down nearly twice as much as I did and passes me the bottle again."
        "It takes all my willpower not to wince, as I force myself to take another gulp."
        "Once I put the bottle down on the table, I quickly stuff my mouth with a piece of sausage."
        show vul intrigued with dis
        m "\"Well then?\""
        show vul talk l with dis
        v "\"Why are you so insistent?\""
        show vul neutral xl with dis
        "He reaches for the bottle and takes another swig."
        m "\"I just want to get to know you.\""
        show vul talk ang with dis
        v "\"There’s nothing worse than a needy drinking buddy.\""
        show vul neutral x with dis
        "The bottle slides across the boards towards me."
        show vul talk p with dis
        v "\"Especially if they cannot keep up.\""
        show vul intrigued with dis
        "I narrow my brows defiantly, taking a long gulp of the booze."
        "I'm not really paying it any mind at this point; it stopped burning as it used to."
        "I bang the bottle on the table and look at him angrily."
        m "\"I can keep up, don't worry...\""
        "I look at him expectantly, to which he simply shrugs."
        show vul talk e with dis
        v "\"I didn't agree to anything, did I?\""
        show vul neutral x with dis
        m "\"Ah, come on! Not fair!\""
        show vul talk x with dis
        v "\"Life ain't fair, Piglet. Better get used to it.\""
        show vul unamused with dis
        m "\"Come on, Vul! Don't be like that!\""
        show vul growl lx with dis
        v "\"Ugh. Verissa's right. You talk too much.\""
        show vul talk ang with dis
        v "\"Especially for someone with death penalty over their head.\""
        show vul intrigued x with dis
        m "\"The tribe already knows I'm here...\""
        show vul talk lx with dis
        v "\"Yeah... would be shame if they found out you can speak as well.\""
        show vul neutral e with dis
        "He nods towars the opened windows."
        m "\"Oh, shit!\""
        show vul smile with dis
        "Vul chuckles, watching me scramble to close them one by one."
        show vul amused with dis
        v "\"Relax, Piglet. It was just a joke… no one would dare to eavesdrop on us while I'm here.\""
        show vul intrigued x with dis
        m "\"Not even Howl?\""
        "I stop my frantic efforts, looking at him with worry."
        show vul talk e with dis
        v "\"Especially not Howl.\""
        show vul talk with dis
        v "\"He ain't the bravest pup in the pack and in this tribe everyone knows to stay the fuck away from me.\""
        show vul talk ang with dis
        v "\"Maybe in time I can teach you that as well… mighty curious how for a preykin you seem to have very little survival instincts.\""
        show vul neutral x with dis
        "I roll my eyes, slightly annoyed he caused my heart to pound like a drum."
        m "\"Thanks, I really needed a good scare.\""
        "I mumble, returning to my seat."
        show vul amused with dis
        v "\"Ha. It wasn't a scare, Piglet. You are as clueless as an actual livestock.\""
        show vul talk ang with dis
        v "\"If anyone around finds out that you're ready for the knife, it's off to the chopping block.\""
        show vul neutral with dis
        "Again, I roll my eyes; this time at his apt analogy."
        show vul intrigued x with dis
        m "\"Thanks, noted. Simple 'keep the windows closed when talking with Ranok' would suffice.\""
        show vul eyeroll with dis
        v "\"You should cut the talking to minimum, really.\""
        show vul talk p with dis
        v "\"This cottage became a talking point and there will be plenty of noses sniffing about.\""
        show vul talk with dis
        v "\"Anyway, time for me to go.\""
        show vul neutral with dis
        "He stands up and takes a final gulp from the clay bottle."
        show vul talk l with dis
        v "\"Stayed here long enough as it is...\""
        show vul intrigued with dis
        m "\"Why? Afraid other wolves will think you're enjoying the company of an otherkin?\""
        "I grumble, thinking it was a jab at me."
        show vul talk ang with dis
        v "\"As if I care what others think…\""
        show vul amused with dis
        v "\"I simply can see you’ve got your hands full.\""
        show vul smile with dis
        "He looks around the clean house."
        show vul talk su with dis
        v "\"Ranok’s dirty laundry won’t clean itself.\""
        show vul smile with dis
        m "\"You dick!\""
        show vul amused with dis
        v "\"Besides... you're all out of booze.\""
        show vul smile with dis
        "He tips the bottle over and let it roll towards the edge of the table, forcing me to rush in to catch it before it crashes againts the floor."
        show vul whisper s with dis
        v "\"Nice one.\""
        show vul smile with dis
        "He winks at me in approval as he pulls on the front door."
        play sound "sfx/door open.ogg"
        show vul talk p with dis
        v "\"Verissa should be with you in a bit. Try not to get killed between now and then."
        show vul neutral e with dis
        "The black wolf nods and leaves the house."
        hide vul neutral e with dis
        play sound "sfx/door close.ogg"
    "Refuse":

        $ Booze = False
        "I wouldn’t be much of a drinking buddy anyway."
        show vul unamused with dis
        m "\"No, it's not my thing. Sorry.\""
        show vul talk e with dis
        v "\"Thought as much… you're a suckling after all.\""
        show vul talk with dis
        v "\"I'm going to help myself to another round.\""
        show vul neutral with dis
        "The wolf gets up, pushing the chair away."
        m "\"By all means.\""
        "I smile, glad he isn't actually going to bail on me."
        show vul growl with dis
        v "\"I wasn't asking for permission.\""
        show vul neutral with dis
        "He mutters in annoyance, as he approaches the barrel."
        show vul talk e with dis
        v "\"{size=-10}Let an otherkin into your house and he starts acting as if he owns the damned place.{/size}\""
        show vul neutral with dis
        "I chuckle at his comment, not really sure if it's just teasing or genuine grievance."
        "Once he filled his mug, he returned to the table and plopped down comfortably, causing the chair to moan under his sudden weight."
        show vul talk with dis
        v "\"Sláinte!\""
        show vul neutral with dis
        "He raises his mug for a moment in a clear toast and then proceeds to drink."
        "We sit like that for a moment in silence."
        "He's clearly not a talkative type and I'm struggling to find any topic for a conversation."
        "I look at his moonstone, remembering how it somehow unsettles me."
        "I wonder about the importance of the necklace."
        m "\"Are all wolves born during the same night Moon Brothers?\""
        show vul neutral with dis
        v "\"Hmmm?\""
        m "\"Like you and Ranok.\""
        "I shrug, taking a bite of the sausage."
        show vul intrigued with dis
        "I look to Vulgor expectantly, as he takes his time with another gulp."
        "He eventually lets out a sigh and rubs his lips."
        show vul talk with dis
        v "\"Why do you ask?\""
        show vul neutral with dis
        m "\"Well, since you said blood relations don't mean much... I'm kinda curious, as you two make a big deal out of the Moon Brother thing.\""
        m "\"How do wolves become Moon Brothers?\""
        show vul talk pl with dis
        v "\"You have to be born in the waters of the same Moon Well during the same Phase of Aluna."
        show vul neutral l with dis
        m "\"A Moon Well?\""
        "I ask, cutting off another slice of bread."
        show vul neutral e with dis
        "I watch as the wolf walks over to the ale barrel, helping himself to a third mug."
        "It’s surprising how fast he goes through those..."
        show vul talk ang with dis
        v "\"There is a shallow pool at the centre of our shrine. It's lined with small stones and filled with clear spring water.\""
        show vul neutral x with dis
        "He explains, sipping off the excess that began spilling from the mug as he retrieved it from the barrel."
        "I think it’s safe to say he enjoys the ale more than my company…"
        show vul talk pl with dis
        v "\"The pool supposedly collects the moonlight, blessing the waters which then are use for different religious purposes.\""
        show vul intrigued with dis
        m "\"Like birth?\""
        "I look to him as he takes his seat."
        show vul talk l with dis
        v "\"Among others.\""
        show vul neutral with dis
        "The wolf shrugs as he wets his lips again."
        "I can see he’s nowhere near getting drunk, it's almost like drinking water to him..."
        "I just have a suspicion that once he has his fill, he’ll simply fuck of."
        "I need to pace him a little, so I cut off a piece of sausage and push it his way."
        show vul amused with dis
        v "\"Heh.\""
        show vul smile with dis
        "He smiles at my gesture and takes a bite."
        show vul talk sup with dis
        v "\"Those are for you.\""
        show vul intrigued with dis
        m "\"I know... but I'm sure it pairs well with the beer. And it's plenty enough for me.\""
        "I smile idly."
        show vul amused with dis
        v "\"Fair play.\""
        show vul smile with dis
        "He shrugs, flicking up the remaining piece of sausage and swallowing it with a loud chomp."
        show vul talk l with dis
        v "\"Anyway... when a female goes into labour, she's brought to the Well. Once a pup is born, one of the pebbles reveals itself as a Moonstone.\""
        show vul talk p with dis
        v "\"Have two females go into the labour at the same time… well… you can guess the rest.\""
        show vul intrigued with dis
        m "\"That sounds… magical.\""
        "I smile, genuinely amazed by the concept."
        "It sounds so simple and in tune with nature."
        "Their traditions, even if odd, do have a certain alure to them."
        show vul talk e with dis
        v "\"I guess so. I’m sure there is some trick involved…\""
        show vul talk lx with dis
        v "\"There’s always a trick in religion.\""
        show vul neutral x with dis
        "He scoffs in annoyance."
        show vul talk ang with dis
        v "\"I wouldn’t place much stock in the coincidence of being born at the same time as another pup. That's just sappy nonsense.\""
        show vul intrigued x with dis
        m "\"You… you don’t believe in it?\""
        show vul neutral x with dis
        "It’s almost amusing how polar opposites those two wolves are; with Ranok screaming fate at everything he sees, while Vul sniffing some sort of deceit everywhere he looks."
        show vul talk lx with dis
        v "\"I might not believe in the supernatural aspect of my bond with Ranok… but I've heard enough about the circumstances of my birth to concede a simple fact:\""
        show vul talk ang with dis
        v "\"We {i}are{/i} Moon Brothers. The rest is fluff.\""
        show vul intrigued x with dis
        m "\"Oh?\""
        show vul unamused with dis
        "I issue involuntarily, expecting a follow up, but the wolf does not respond."
        "Instead, Vul simply takes another long swing at his tankard, emptying it in one go."
        show vul intrigued with dis
        "Once he bangs it back onto the table, he looks at me with confusion."
        show vul talk with dis
        v "\"What?\""
        show vul neutral with dis
        m "\"What were the circumstances of your birth?\""
        show vul eyeroll with dis
        v "\"Ugh…\""
        "He rolls his eyes in annoyance, I guess he didn’t mean to mention it."
        show vul intrigued x with dis
        m "You can have another.\""
        "I propose, to which he only gives me a telling gaze."
        show vul growl with dis
        v "\"Oh, can I? Thank you for your permission...\""
        "He knows I’m fishing for detail, but how can he blame me?"
        m "\"Please! You can’t leave me hanging like this…\""
        show vul talk l with dis
        v "\"Try me.\""
        show vul neutral with dis
        "He scoffs, standing up."
        "Fuck, I'm losing him!"
        show vul intrigued with dis
        m "\"Ok, I didn’t want to do this, but you kinda owe me for the chocking.\""
        show vul talk pu with dis
        v "\"I owe you, you say?\""
        show vul unhappy with dis
        "He scoffs mockingly."
        show vul growl with dis
        v "\"Press your luck further, Piglet and you’ll earn another scar.\""
        show vul neutral with dis
        "I watch, as he approaches the door and I fidget with my fingers in panic."
        "At this point I don’t know if it’s about the story itself, or the fear of being left alone."
        m "\"Please?\""
        show vul unamused with dis
        v "\"Yup, you've gotten needy...\""
        show vul talk e with dis
        v "\"That’s my cue.\""
        show vul neutral with dis
        "The wolf huffs, as he stands up and approaches the barrel."
        "He hastily plunges the mug, getting one last taste of the ale."
        show vul neutral e with dis
        "As he finishes, he plops the tankard on the table and issues a satisfied sigh."
        show vul talk su with dis
        v "\"I'll let you get back to your duties… if you run out of chores, you could always do his dirty laundry.\""
        show vul amused with dis
        "He laughs, approaching the door."
        show vul intrigued with dis
        m "\"Ha-ha. You're so funny.\""
        "I grumble, to which he only shrugs."
        show vul eyeroll with dis
        v "\"At least I'm more fun than you are, Piglet.\""
        play sound "sfx/door open.ogg"
        show vul talk p with dis
        v "\"Verissa should be with you in a bit. Try not to get killed between now and then."
        show vul neutral e with dis
        "The black wolf nods and leaves the house."
        hide vul neutral e with dis
        play sound "sfx/door close.ogg"

"With Vulgor gone, I'm faced again with the dreaded feeling of loneliness."
"No… not loneliness… but being alone."
"For whatever reason, I feel almost under siege when there's no one around me."
"I need to occupy myself and with the growing fear inside my chest I have to do it now."
"I quickly glance at the cupboard, remembering that Vul mentioned Ranok did some research on my kind."
"Considering my morning conversation with the grey wolf, it might be a good idea to try to find out more about my people."
"At least it'll be something to do."
scene waterbowl with dis
"I approach the cupboard and pick up the topmost volume."
"It's bound in gilded, red leather with a large golden plate donning its cover."
"The emblem is diamond-shaped and has a stylised pawprint pressed into it."
"It looks awfully expensive, that's for sure."
"'Six Tribes of Tirnan'"
"As I flip through the pages, it seems to be some sort of a chronicle."
"There are different names written into it, supported by dates and details relating to them."
"It's a long and boring roll call of people long dead, going by the way the pages aged."
"Nope, this one's of no use to me; especially without context."
"I mean, there might be some human names there, but then again… how would I know?"
"Also the pawprint on the cover tells me it's rather unlikely."
"I place the book down and pick up a blue tome which lied beneath it."
"It's much larger, even though more humbly decorated."
"'The Great Tiger Rebellion.'"
"Hmmm… another history book and this one obviously not about humans."
"I wonder why Ranok has it?"
"Surely it didn't aid him in his research."
"I'm about to put it down when I realise these wolves kept bringing tigers up an awful lot."
"Might be worth giving it a quick read."
scene bg kitchen_day with dis
"I sit myself down comfortably, browsing through the book."
"It's a hefty volume and I don't feel like reading it whole."
"Not to mention, by the looks of the sun in the sky, there's little daylight left anyway."
"I skim the pages as briefly as I can, each of them filled with dates and names that mean nothing to me and which are gone from my mind the moment I read them."
"However, on the whole it seems to be a detailed account of an ancient war spanning a century or so, which started as the title suggested by the Tigerii raising in rebellion against the 'Old Kingdom'."
"Seems that long ago Avalan used to be ruled by lions, who at least according to this book were monstrous tyrants."
"At first the Tigerii fought alone, but over the years their bravery attracted otherkin to join their struggle."
"Decade by decade their Alliance grew until at the very end, the Old Kingdom was no more and the Lion King had to abdicate."
"It's so surreal to read about other beast men… this really is a living, breathing world, with its own history and customs."
"How can I feel so… misplaced here?"
"I sigh in frustration, burrowing myself into the book."
"It's not a pleasant read and in fact most of the information is lost on me, but at least it passes the time."
scene bg kitchen_night with slow_dissolve
play ambience "ambience/forest_night.ogg" fadein 3.0
"Eventually I place the book down, utterly confused by the contents."
"None of this ring any bells, however from the looks of things the Tigers don't seem to be as bad as the wolves paint them to be."
"Even more odd is the fact wolves do not feature in this book."
"I quickly glance over the pages again, trying to find any mention of them but it's almost as if they didn't exist…"
"…before I can expand on my research, I hear a knock on the door."
play sound "sfx/knock.ogg"
"It must be Verissa."
"I close the book with a slight relief, returning it back to the cupboard."
"Not only was the read very dull, but in this dimly lit room it was outright laboursome on my eyes."
"I barely noticed how dark it got."
ve "\"[mc], you there?\""
"I approach the door without a word, remembering Vul's warning."
"I pull on the latch, releasing the lock and allow Verissa to enter."
play sound "sfx/door open.ogg"
show ver neutral with dis
"The female rushes into the room and I quickly close the door behind her."
play sound "sfx/door close.ogg"
show ver sigh with dis
ve "\"You're uncharacteristically quiet. Good.\""
show ver neutral with dis
"She nods in satisfaction."
show ver talk with dis
ve "\"But don't worry, I wasn't followed. The feast starts soon, so very few would waste their time here.\""
show ver shocked with dis
m "\"What about Tano?\""
show ver amused with dis
ve "\"My, my… it {i}can{/i} be taught.\""
show ver smile with dis
"She smiles with genuine pride on her muzzle."
show ver talk s with dis
ve "\"He's busy, I made sure of it. He won't have time to sniff about.\""
show ver neutral with dis
"I watch as she walks over to the shelf and retrieves a small plate."
"Only now do I notice she has a small sash at her waist, from which she takes a small phial and some fresh bandages."
show ver eyeroll with dis
ve "\"Why are you sitting in the dark?\""
show ver doubtful with dis
m "\"I-\""
"Do I really want to admit I have no idea how to start a fire without burning this house to the ground?"
"She's been questioning my age an awful lot, I don't want to come across as utterly clueless as well."
m "\"I prefer it this way… less conspicuous.\""
show ver doubtful t with dis
ve "\"Right…\""
show ver doubtful with dis
"I can see this wasn't exactly a convincing answer."
show ver talk l with dis
ve "\"Well, have it your way.\""
show ver neutral with dis
"She kneels down, slowly undoing my reddened dressing."
"I watch, as strip after strip is removed, revealing my blood-crusted side."
"There is a large scab covering the cut itself, but otherwise everything looks fine."
show ver talk with dis
ve "\"How do you find your current living arrangements?\""
show ver neutral with dis
"She asks absentmindedly, while inspecting my entire side."
m "\"What do you mean?\""
show ver talk x with dis
ve "\"Do you like it here with Ranok?\""
show ver neutral
m "\"Ummm, I guess…?\""
show ver sigh with dis
ve "\"It's a simple 'yes' or 'no' question, [mc].\""
show ver neutral x with dis
"The female mutters, giving me a telling look."
m "\"Yes… sorry. I'm happy here.\""
show ver neutral l with dis
ve "\"Hmmmm…\""
"Again, she sounds unconvinced."
show ver neutral with dis
m "\"Why do you ask?\""
show ver talk with dis
ve "\"I ask because the elders preferred to house you in the stockades…\""
show ver neutral with dis
m "\"The stockades?\""
show ver talk l with dis
ve "\"Our prison… and at first I was inclined to agree on the count of your-\""
show ver uncomfortable with dis
"She cuts off diplomatically, obviously trying to find a proper word."
"I decide to spare her the trouble."
show ver shocked with dis
m "\"Fuck up?\""
show ver smile et with dis
ve "\"Quite so.\""
show ver smile with dis
"She smiles softly, placing a small cloth onto the plate and pouring the content of the phial over it."
"The tincture has a slightly purple colour and immediately soaks into the material."
show ver amused with dis
ve "\"Heh, that got Ranok fired up like little ever does. He insisted you became his ward instead… a… peculiar choice, but he is the heir apparent.\""
show ver talk s with dis
ve "\"It was hard for the elders to say 'no', especially since he was ready to tear anyone to shreds over the issue; myself included.\""
show ver smile with dis
"My eyes widened in shock and she chuckles catching my surprise."
show ver smile et with dis
ve "\"Figuratively speaking of course… at least in my case.\""
m "\"Heh…\""
show ver talk with dis
ve "\"Either way, to soften that spectacle, and to make his claim on you somewhat less obvious I offered to take you under my wing instead.\""
show ver neutral with dis
"She shrugs, giving my wound a slight push and I wince in discomfort."
show ver sad t with dis
ve "\"Sharp or dull pain?\""
show ver sad with dis
m "\"Dull… but only when you press too hard.\""
ve "\"Curious…\""
show ver neutral with dis
"Her muzzle twists in a frown as she looks intently at my scar."
m "\"You wanted me to live with you?\""
show ver talk e with dis
ve "\"Well… it's more complicated than that. But yeah… should you ever want to change your accommodations; all you need to do is let me know.\""
show ver talk with dis
ve "\"It might take a while to settle, but-\""
show ver shocked with dis
m "\"No!\""
"I blurt out almost in panic, catching her attention, but she doesn't say anything."
m "\"I'm really happy here. Ranok takes good care of me.\""
show ver talk x with dis
ve "\"Indeed.\""
show ver neutral x with dis
"The female narrows her eyes ever so slightly, but enough for me to register that little shift."
m "\"Although, thank you for letting me know. I'll keep it in mind.\""
"She begins to wipe my side, cleaning it of all the dried blood and I feel slight tingling, followed by stinging."
"I wince in discomfort again, but she pays me no mind, her brows still narrowed in focus."
show ver talk with dis
ve "\"Technically you're under house arrest and as much as it doesn't sit well with me, as it doesn't sit well with Ranok; I'd rather go more subtly about it.\""
show ver talk e with dis
ve "\"I just want you to know that you have a choice… as limited as it is.\""
show ver neutral with dis
m "\"Thank you, Verissa. That means a lot.\""
"Once the entire side is cleaned, she pokes slightly at the scab."
show ver sad t with dis
ve "\"Does it hurt?\""
show ver sad with dis
"I shake my head."
show ver talk s with dis
ve "\"Good.\""
show ver neutral with dis
"She continues to wipe the scab, washing away much of the dried blood and reducing it in size until she reveals the fresh wound beneath."
"She then pours the remaining contents of the phial directly over it, causing me to seize up in pain."
show ver talk with dis
ve "\"It's ok, it's ok! Don't touch it.\""
show ver neutral with dis
"She says softly, grabbing the clean dressing and covering the cut."
show ver doubtful t with dis
ve "\"So, you guys getting along ok?\""
show ver neutral with dis
m "\"Does that surprise you?\""
show ver talk with dis
ve "\"A little bit.\""
show ver neutral with dis
m "\"Why?\""
show ver eyeroll with dis
ve "\"Call it female intuition… and personal experience; Ranok can be a little much at times.\""
show ver neutral with dis
m "\"Heh, yeah.\""
"I try to chuckle, ignoring the pain radiating through my entire left side, but I still come across as slightly unnerved."
show ver talk x with dis
ve "\"Hmmm… seems like I'm onto something. I didn't become a Shaman for nothing, you know.\""
show ver neutral x with dis
"She begins wrapping my side with clean strips of bandages, making sure that the new dressing sits nice and tight on my skin."
"I watch as she works her paws around me in silence, but eventually she forces me to speak up."
show ver talk x with dis
ve "\"Well then? You're going to tell me?\""
show ver neutral x with dis
m "\"It's nothing, really. I just struggle with reading that wolf. He's very forward… not that I mind, it just takes me by surprise half the time.\""
"She pauses her task and looks at me with slight surprise."
"Quickly however that surprise is replaced with a knowing smile and she returns to bandaging me up."
show ver amused with dis
ve "\"That's Ranok, alright. I swear, that wolf never stopped being a pup. He was playful and teasing ever since we were little.\""
show ver smile et with dis
ve "\"Not to mention he's a massive flirt.\""
"I almost choke on that remark."
show ver talk s with dis
ve "\"Sometimes I think he doesn't even realise it. It used to drive me insane, but then I understood it's just how he is… at the end of the day, he's a flatterer.\""
show ver amused p with dis
ve "\"He loves to flatter others just as much as he likes to flatter himself.\""
show ver smile with dis
m "\"Yeah… sounds about right.\""
"I nod awkwardly."
show ver talk s with dis
ve "\"Don't let that fluster you… that's what he's after. If you ignore his teasing, he'll quickly get bored and move on to other jokes.\""
ve "\"As a last resort you can just slap his ears. Moon knows, it's long overdue.\""
show ver smile with dis
"Problem is, I don't think I want him to move on to other jokes… nor I really think those are just jokes."
"Perhaps it's just his way of coping with this extremely oppressive society."
"That, or I'm again reading into things as is typical of me."
"It's nice to recognise some behavioural patterns among all this blankness."
"It's almost as if I'm meeting myself as a completely new person."
show ver talk s with dis
ve "\"There, all done.\""
show ver smile with dis
"She smiles, admiring her handiwork and patting my side."
m "\"Thank you.\""
"I look down, glad to be rid of that bloodied horror show."
show ver talk s with dis
ve "\"You're welcome. This was very fortuitous, you know...\""
show ver smile with dis
"She mutters, collecting the reddish stripes from the floor."
m "\"What was?\""
show ver talk with dis
ve "\"You started bleeding almost as if on cue. Made the whole scene so much more believable.\""
show ver smile with dis
m "\"Well, I wasn't acting. He did {i}wolf{/i}-handle me a bit…\""
show ver smile et with dis
ve "\"Haha!\""
"The female laughs at my poor joke."
show ver talk s with dis
ve "\"Yes, but still. Seems the Ancestors really look after us in our little gambit.\""
ve "\"Which is a good omen, for sure… as we need all the help we can get to see this through.\""
show ver amused p with dis
ve "\"Thus, I'll be burning those at the altar as well.\""
show ver smile with dis
"She wiggles my old, bundled bandages."
m "\"That's the key to my protection here, right?\""
show ver talk h with dis
ve "\"Sort of. They are an offering to our Ancestors. It's done when one of us is gravely wounded as a sort of intercession.\""
show ver neutral with dis
m "\"One of {i}you{/i}.\""
"I emphasise to let her know the distinction wasn't lost on me."
show ver talk h with dis
ve "\"Drastic times call for drastic measures. Either way only a shaman can do this and only a shaman can determine if the offering was accepted.\""
show ver talk l with dis
ve "\"So here we are.\""
show ver shocked with dis
m "\"Was it, though?\""
m "\"Accepted, I mean.\""
show ver uncomfortable with dis
"She looks at me a bit shocked that I would ask such a question."
"Her troubled expression leaves me feeling slightly queasy, making the answer all the more obvious."
show ver sigh with dis
ve "\"Nobody knows what the future holds, [mc]. Only time will tell…\""
show ver talk with dis
ve "\"But for now, everything turned out alright.\""
show ver neutral with dis
"I give her a slight smile, nodding softly towards my patched-up side."
show ver talk s with dis
ve "\"Well, as alright as it possibly could; all things considered.\""
show ver neutral with dis
"She chuckles, and I watch as she slowly packs up her things."
"I follow her with my gaze, as she returns the plate to the shelf feeling a void growing in my chest."
"The same nagging feeling of desperation fills my heart and I know another panic attack fast approaches."
"She's about to leave and I really don't want her to."
show ver sad with dis
"But before I manage to say anything, she gives me a worried look."
show ver sad t with dis
ve "\"What's the matter? Why is your heart racing?\""
show ver sad with dis
"Fuck… I keep forgetting about their creepy ability, however in this instance it saves me begging another person to keep me company."
m "\"I'm fine, sorry. Just slightly anxious.\""
show ver talk with dis
ve "\"Well, it's to be expected in your situation. It wasn't exactly peaceful experience for you these past few days.\""
show ver smile with dis
"She pulls up a chair and sits down at the table, looking at me with a soft smile."
show ver talk s with dis
ve "\"I can stay with you for a bit. Not long, though. I'm needed at the feast.\""
ve "\"It would be a great insult if I left the Chief hanging at the dinner table.\""
show ver neutral with dis
m "\"Is Ranok going to be there?\""
"I ask, worried he'll be held up longer than I would like."
"Last time he returned quite late."
show ver talk s with dis
ve "\"No.\""
show ver smile with dis
"She smiles, again giving me this unnerving knowing look."
show ver amused with dis
ve "\"He was pretty adamant he will come straight to his home after his patrol.\""
show ver neutral with dis
m "\"Oh. He shouldn't have.\""
show ver talk e with dis
ve "\"No… he shouldn't.\""
show ver neutral with dis
"The female agrees with a quite serious tone, however she quickly chuckles it off."
show ver talk l with dis
ve "\"But I long realised that this wolf will do as he pleases, no matter what.\""

if DrinkingBuddy == True:
    show ver neutral r with dis
    "She locks her gaze with the clay bottle at the table and gently pushes at it, letting it wobble in place for a moment."
    show ver talk s with dis
    ve "\"I see Vul took advantage of your hospitality.\""
    show ver smile with dis
    m "\"Not as much as I would like.\""
    "I laugh."
else:

    show ver talk s with dis
    "The female looks intently at the string of sausages lying on the table."
    show ver talk s with dis
    ve "\"I see Vul treated you to his own wares.\""
    show ver smile with dis
    m "\"He made those?\""
    "I ask in surprise."
    "Good thing I kept the garlic comment to myself, wouldn't want to insult him."

m "\"I thought we were bonding, he almost told me about the Moon Brother thing, when he suddenly bolted.\""

if DrinkingBuddy == True:
    show ver smile et with dis
    ve "\"If you want personal details from Vul, you need more moonshine than that.\""
    show ver smile with dis
    "She nods towards the bottle, clearly entertained by the idea of my attempt at befriending the black wolf."
else:

    show ver smile et with dis
    ve "\"If you want personal details from Vul, you need moonshine and plenty of it.\""
    show ver smile with dis
    "She chuckles, clearly entertained by the idea of my attempt at befriending the black wolf."

show ver talk s with dis
ve "\"He's not the one to open up easily. Still… him staying even for a little bit is a huge success.\""
show ver smile with dis
m "\"How so?\""
show ver talk s with dis
ve "\"Vul is more likely to pick a fight than a conversation. In fact, the only wolf he seems to tolerate is Ranok. Those two-\""
show ver smile with dis
"She sighes with genuine admiration."
show ver amused p with dis
ve "\"A bond like that is extremely rare, even among our people.\""
show ver smile with dis
"I smile, quite touched by the sentiment."
"They do seem to be true friends, not afraid to call each-other out on their bullshit."
"Something I'm sure is rare even among humans."
m "\"I envy them that.\""
show ver talk e with dis
ve "\"You and the rest of us. Those two are like two sides of the moon… and their moonstones attest to that.\""
show ver neutral with dis
m "\"Vul seemed to suggest his bond with Ranok has nothing to do with the moonstones themselves.\""
show ver smile with dis
"She smiles, scoffing softly in amusement."
show ver talk s with dis
ve "\"That's his cynical side; he's always weary of everything he cannot see or understand.\""
show ver sad t with dis
ve "\"But at the same time, I can empathise with him.\""
ve "\"After all, if people avoided you and you were told your entire life that you're damned only because of your necklace, you'd be quite resentful as well.\""
show ver sad with dis
m "\"What do you mean?\""
"I blink in confusion, causing the female to pause."
show ver neutral l with dis
"Her gaze drifts to the side as she clearly ponders whether or not she said too much."
show ver neutral e with dis
m "\"I'm sorry… I didn't mean to pry.\""
show ver talk e with dis
ve "\"No… no. I think you should know.\""
show ver neutral with dis
"She finally faces me again with a rather serious expression."
show ver talk with dis
ve "\"It should make things a little bit clearer.\""
show ver neutral with dis
"I nod expectantly."
show ver talk with dis
ve "\"Our births take place in a moonwell. It's a shallow pool of water at the centre of our shrine which collects the light of Aluna and infuses the waters with it.\""
show ver neutral with dis
m "\"I know, Vul explained as much. But why would he be considered damned?\""
show ver uncomfortable with dis
play music "music/nocturne.ogg" fadein 3.0
ve "\"The Darkmoon is a very bad omen, in fact one of the worst. No female would give birth under it if she could help it.\""
m "\"Why?\""
show ver talk ang pl with dis
ve "\"Darkmoon represents the unforgiving, ruthless side of Aluna. She's the goddess of many faces and a total eclipse is her most terrifying one.\""
show ver talk e with dis
ve "\"When Vul came into the world, he was seen as the avatar of her wroth and everyone held their breath.\""
show ver neutral e with dis
"I narrow my brows, slightly sceptical."
"It's quite easy to brush off one's behaviour to the coincidental phenomena…"
"Vul might be quick to anger, but I'm sure it's rather the result of years of being picked on, rather than the omen itself."
show ver sad t with dis
ve "\"And just as everyone held their breath, so did the pup.\""
show ver sad with dis
"I tilt my head in confusion."
show ver sad t with dis
ve "\"Vul wasn't breathing, nor moving; with eyes closed shut.\""
ve "\"He was stillborn.\""
show ver sad with dis
"My eyes widen in shock and I almost feel a void growing inside my stomach."
"I know he's alive and well, but… damn."
"I did not expect such a turn in this story."
show ver talk with dis
ve "\"When a pup is born, a moonstone appears at the bottom of the pool… but as much as he tried, the shaman couldn't find one; confirming the unthinkable.\""
show ver talk h with dis
ve "\"Vul's mother was heartbroken and refused to leave the well.\""
show ver talk e with dis
ve "\"She cursed the name of Aluna... then bargained with her... and finally she begged. All to no avail.\""
show ver neutral with dis
"The pain and suffering of the poor female must've been impossible to describe."
show ver sad t with dis
ve "\"She simply resigned herself to sitting there, in those waters; frozen in place and holding her unmoving newborn tight.\""
show ver sad with dis
"I swallow heavily, my eyes slightly glossed over."
"I cannot even begin to imagine the horror of having your child die… let alone having it die before it was even born."
show ver sad rpt with dis
ve "\"Shortly after, Ranok's mother arrived at the shrine unexpectedly. Although her pup wasn't due yet, she suddenly went into labour.\""
show ver sad r with dis
ve "\"She was brought into the same waters, resting next to Vul's mother... and just as the last slivers of darkness departed Aluna's everchanging image, another pup came into the world.\""
show ver amused with dis
ve "\"Ranok's very first yelp caused Vul to finally stir to life and open his eyes. Their first glances weren’t to their respective mothers, but to each-other instead.\""
show ver smile with dis
"A subtle smile stretches across my face."
show ver talk s with dis
ve "\"Within the same moment, the shaman picked up both stones together… one fully black and the other fully white.\""
show ver amused p with dis
ve "\"It was almost as if Vul was waiting for his brother to join him, refusing to enter this world alone.\""
show ver smile with dis
m "\"That's absolutely beautiful.\""
show ver smile e with dis
"It's hard to hide how moved I am by this story, but Verissa doesn't judge."
"In fact, she only smiles, nodding in agreement."
show ver talk s with dis
ve "\"It is… and so is their unique relationship.\""
show ver talk sp with dis
ve "\"They are the two sides of the same goddess… one full of hatred and coldness, the other loving and forgiving.\""
show ver smile with dis
"I chuckle, awkwardly rubbing my cheek to remove a stray tear; I can certainly attest to their polarity from first-hand experience."
show ver smile et with dis
ve "\"Ever since those two were at each-other's side, inseparable. Just like Mother Moon intended.\""
show ver smile tp with dis
ve "\"Nothing would get between them… it would seem not even you.\""
show ver smile with dis
"I look at her confused."
show ver shocked with dis
m "\"Why would I get between them? I would never-\""
show ver talk h with dis
ve "\"You already did.\""
show ver talk with dis
ve "\"Vul is extremely duty bound; he would do anything for his people. As an outsider you were a major threat.\""
show ver talk e with dis
ve "\"Every instinct in his body told him to kill you outright. But…\""
show ver neutral with dis
"She paused, sighing through a smile."
show ver talk l with dis
ve "\"Vul would sooner die than betray Ranok, or cause him pain… that sort of loyalty cannot be bought.\""
show ver talk h with dis
ve "\"You were the greatest test of his devotion…\""
show ver talk with dis
ve "\"And that devotion is the only reason why you're even alive.\""
stop music fadeout 6.0
show ver neutral with dis
"The female takes on a more serious tone."
show ver talk ang x with dis
ve "\"Make no mistake, [mc]. Vul tolerates you because Ranok is dead set on you.\""
show ver talk ang pl with dis
ve "\"If not for Ranok, he would've killed you without a second thought.\""
show ver neutral x with dis
"I wince uncomfortably, the feeling of utter confidence in the black male slightly weakened."
"I always knew it's Ranok whom I owed my life… I just never realised how true this sentiment really was."
show ver eyeroll with dis
ve "\"Vul might be too blind to see it, but your fate was already decided those two decades ago when as a frail pup he refused to draw his first breath.\""
show ver talk with dis
ve "\"Fate doesn't happen overnight. It's laid out from the beginning of time, until the end of the world…\""
show ver talk h with dis
ve "\"That is why it's so hard to see it at times, that is why it's near impossible to read it with any sense of certainty.\""
show ver talk l with dis
ve "\"You're basically gazing into eternity, hoping to catch a specific moment in time.\""
show ver neutral with dis
"She pauses, letting the words sink in and I'm dumbfounded."
"Everything she says is true; had Vul not forge this connection with Ranok… I would've never woken up in this cabin."
show ver talk h with dis
ve "\"This is also why I cannot always give a clear answer.\""
show ver talk with dis
ve "\"Even I have to wait until the truth reveals itself to me… and that takes time and patience.\""
show ver talk h with dis
ve "\"One just has to observe and listen.\""
show ver talk s with dis
ve "\"You're alive because seemingly unrelated events happened at different times, forming a very specific pattern.\""
show ver smile with dis
"She vocalises my own thoughts, causing me to blink in realisation."
show ver shocked with dis
m "\"That's what Ranok said...\""
m "\"'Fate is a lot of things falling into place in just the right way.'\""
"I quote the grey wolf, almost surprised at how profound his wisdom was."
show ver smile e with dis
"Verissa closes her eyes and smiles, betraying a hint of pride."
show ver smile et with dis
ve "\"Well, I'm glad to hear he's not just a goof around you.\""
show ver smile with dis
m "\"He's not as bad as you make him out to be.\""
"I mutter defiantly."
show ver smile tp with dis
ve "\"You think I don't know that?\""
show ver smile with dis
"She laughs me off."
show ver talk h with dis
ve "\"He's my friend... he has been one for a long time and will continue to be for many years to come.\""
show ver talk with dis
ve "\"I'm only harsh on him because I know he's capable of being better.\""
show ver talk h with dis
ve "\"Because that's what he always strives to be.\""
show ver smile with dis
"She explains matter-of-factly."
show ver amused p with dis
ve "\"He was born and trained to rule and he has the makings of a great chief. I just want to make sure the future he laid out for our people will come to pass.\""
show ver shocked with dis
m "\"Even if his ideas might be…\""
show ver talk s with dis
ve "\"Controversial? Radical?\""
show ver smile e with dis
"She interrupts me through a chuckle."
show ver smile tp with dis
ve "\"Dear boy… you're the walking embodiment of those. A living, breathing proof that this wolf will do anything as long as he believes it's the right thing to do.\""
show ver talk s with dis
ve "\"It's about time there was a wolf in charge with a moral compass and steel resolve to follow it.\""
show ver smile with dis
"'A moral compass…'"
"He told me to follow mine so many times, because that's the truth he strives to live by."
"He's really an amazing wolf… the fact that both Verissa and Vul place their faith in him proves it beyond doubt."
"It explains why I feel so safe around him…"
m "\"With Vul at his side and you to advise him… it seems nothing can stand in Ranok's way.\""
"I smile."
show ver smile et with dis
ve "\"Fate, [mc].\""
show ver smile e with dis
"The female nods affirmatively."
show ver amused p with dis
ve "\"Everything was arranged before any of us were even born. All we have to do is play our parts.\""
show ver talk s with dis
ve "\"And now that also includes you.\""
show ver smile with dis
"She stands up, issuing a melodic laugh."
m "\"What's so funny?\""
show ver smile et with dis
ve "\"Not in my wildest dreams would I think a {i}human{/i} be a key to the future of my people.\""
show ver talk s with dis
ve "\"I'm still trying to piece together all the parts, but so far you fit into this puzzle.\""
show ver smile with dis
"She rests her paws on her hips, looking around with slight amusement."
show ver amused with dis
ve "\"Ancestors sure do like to laugh in the face of the living. But when you're dead, the only thing you have left is a sense of humour.\""
show ver smile with dis
"The female pushes the chair back into the place and approaches the doors."
show ver talk s with dis
ve "\"I better head out, otherwise Ranok's father is going to have another fit.\""
show ver smile with dis
m "\"O-ok…\""
"I nod, standing up and approaching her."
"I pull on the handle, opening the doors for her."
play sound "sfx/door open.ogg"
show ver smile et with dis
ve "\"My, you do play your part well. You might survive us yet.\""
show ver smile with dis
"She ruffles my hair, as I blink in confusion, not really sure what she meant."
"I'm just being polite."
show ver talk s with dis
ve "\"You keep tight, Ranok should be coming back soon.\""
hide ver talk s with dis
"As the female leaves, I close the doors behind her."
play sound "sfx/door close.ogg"
"The house got incredibly dark and quiet with her departure, but I won't let that bother me."
"Despite the creeping fear inside my heart, I simply shake it off and sit down, looking at the window."
"The ominous presence deep inside my mind stirs, growing bolder with each passing moment."
"I try to distract myself; I must distract myself…"
"I cannot let it win."
"Verissa gave me a lot to think about so I focus on our conversation instead."
"She certainly managed to clear some of my doubts about Ranok."
"I can now clearly see that he's simply letting off steam whenever he can; it's the only way to avoid breaking under such immense pressure."
"I don't think I would be able to cope with so many expectations placed on my shoulders."
"It's incredibly impressive how well he manages, all things considered."
"And then there's Vul, whom I really need to be careful around."
"It would seem I've mistaken his leeway for friendliness."
"I can see he is genuinely amused by me, but it's definitely in the context of me being Ranok's 'path'."
"He's just entertaining his friend's whim."
"But I can work with that, after all the foot {i}is{/i} in the door."
"And knowing now how harsh Vul's upbringing was, growing up believing you were born bad… that must've been rough."
"A self-fulfilling prophecy."
"Him keeping distance is now so much more understandable…"
"Yes, he is quick to anger… he is violent… but if a wolf like Ranok cherishes him so much, then Vul cannot be evil."
"No, I do not see him that way, black stone be damned."
"If he means so much to Ranok, then he means as much to me."
scene bg black with dis
stop ambience fadeout 3.0
play music "music/entity.ogg" fadein 3.0
ow "\"You mean nothing.\""
scene bg kitchen_night with dis
"Suddenly the strangest of feelings overwhelms me, as if I were contracting onto myself while the walls got bigger and taller."
"The shadows seem to elongate, reaching out from within the dark corners and I immediately shift my gaze onto the table, locking my eyes with the woodwork patterns."
m "\"It's not real… it's just in my head.\""
"I breath heavily, not even realising when I start to shiver."
play sound "sfx/wall_creak.ogg"
scene bg kitchen_nightmare with slow_dissolve
"A torturous moan stretches across the back wall, as if the sudden expansion put a strain on the house."
"It feels like the room twists and contorts, with the walls closing in on me."
m "\"Get a grip, [mc]…\""
"I grab my head, pleading with myself."
play sound "sfx/wall_creak.ogg"
"I know this is just my panic attack, nothing more, but the sound continues almost as if trying to prove me wrong."
"Stumbling to my feet, I nervously look around the room."
"I feel so small and insignificant as though I shrunk and lost at least half of my height."
"I was undersized for this place before, but now it looks as if I can't even reach the table anymore."
"What is going on?!"
"My feet move back, as I retreat from the kitchen but when I feel the room begin to spin I simply run into the bedroom and slam the door shut."
scene bg broom_night with dis
play sound "sfx/door_slam.ogg"
m "\"Fuck this!\""
"I slump down, resting my crying face into my knees."
m "\"FUCK THIS SHIT!\""
"This isn't normal…"
"My tears flow like waterfalls, I'm bawling my eyes out and I realise that if I allow my wailing to continue, I will draw unnecessary attention to myself."
"I try to stabilise my breath, hearing it rattle loudly across the room."
"I remind myself what Ranok used to do and I embrace my shoulders, slowly squeezing them in the rhythm of my palpitating heart."
stop music fadeout 3.0
play ambience "ambience/forest_night.ogg" fadein 3.0
"'Breath in…'"
"I recall his caring voice."
"'…and breath out.'"
"With much struggle I manage to regain some form of self-control."
"As my breath slows down, I take in the scent of the woods outside, almost feeling as if the wolf was here with me."
scene bg black with dis
ow "\"You're all alone.\""
scene bg broom_night with dis
"I look around the empty room, feeling utterly helpless."
"I am completely at the mercy of my empty mind…"
"I don't even know what the hell is wrong with me, or why my emotions spiral out of control so violently."
"One thing is certain... I'm alone in this world."
"With each passing day it becomes clearer that I've lost everyone…"
"… my family, my friends."
"Surely I had those."
"My life, such as it was, is now gone… replaced by… whatever the fuck this is."
"My sanity cannot rely on Ranok forever, but for the time being that wolf is the key to keep whatever the hell is going on with me in check."
"I don't have a choice but to lean in."
"I try to swallow, but a lump sticks halfway down my throat."
"I notice the jug of water on the cupboard and I get up."
"I pour myself a cup and drink thirstily."

if DrinkingBuddy == True:
    "I'm parched and a realisation finally dawns on me… it must've been the booze."
    "This weird episode was just me tripping on whatever the hell it was we drank."
    "I slap my head in mild annoyance."
    m "\"I'm such an idiot.\""
    "I should not be drinking in my current state of mind."
    "It's literally asking for trouble."
    "I finally compose myself and take a deep breath, glad to find a reason behind all this madness."
else:

    "As I try to refill it, I notice how shaky my hands are."
    "More water splashes around the cup than ends inside of it, so I decide to put it all back onto the cupboard."
    "I regard my trembling hands, hearing my heart speed up."
    scene bg black with dis
    play music "sfx/heartbeat_fast.ogg"
    "Oh god… I need to get a grip."
    "Once more, I embrace myself tightly, trying to calm my rattled breath."
    "'Breathe in…'"
    "Memory of Ranok's voice echoes in my mind again."
    "'Breathe out…'"
    "Just think of him… think of his smell."
    stop music fadeout 3.0
    "And just like that, the aroma of actual forest, the one outside the window reaches me."
    scene bg broom_night with dis
    "I'm ok… I'm ok."

"When I look around the dark room a slight unease fills me once again."
"It's getting late, so it shouldn't be long before Ranok returns... or so I hope."
"A chill creeps down my back, sending a shiver across my entire body."
"It's gotten cold again."
"I look at the chest, remembering there was some old clothes in there."
play sound "sfx/chest_open.ogg"
"As it creeks open, I look at the contents; there's the swords, some of his old loin clothes… doubtless one of which I was gagged with; and a spare {i}cloak{/i}!"
"I pull it out and flap around to straighten the fabric."
"It's clean for the most part, just-"
"I take an idle sniff."
m "\"Phew!\""
"It's musky, very… musky."
"I drop it to the floor; that's like a whole week of extensive workouts."
"But then again…"
"I reluctantly trail the empty room… it looks so foreboding and unwelcoming."
"Being stuck on my own in this dark, old house only makes it easier to surrender myself to despair and longing."
"Despite the sweaty smell, the cloak does remind me of him… almost as if a piece of him was still here."
"And it is cold…"
"I sigh and pick up the cloth, wrapping it around my shoulders."
"It's so snug."
"It feels as if he himself embraced me… maybe a bit exhausted after a spar, a bit stinky… but still very much smelling like the forest."
"I decide to seat myself on the ledge, to look at the woods outside."
scene window_night with dis
"It's a very calm night with the bright moon high above the treetops."
"The slow rustle of the canopy is much more soothing and calming than the dark interior of the house."
"But there is no escaping the darkness stalking my mind… I feel as if I'm being watched."
"Again, my heart sinks and I burrow myself into the cloak, inhaling deeply."
"His scent calms me down slightly, but my heart is already racing."
"The ease with which I freak out is alarming, but then again… I really don't have a clue what happened in those woods."
"I huddle myself, waiting for the oblivion to claim me, but there is no such luck."
"I have to endure my tortured thoughts for what feels like an eternity, until I hear the doors to the house finally creek open."
"Ranok returned."
scene bg broom_night with dis
"I try to collect myself, to rub away any stray tears but there is no hiding my distress."
"I feel like such a wimp!"
"Ranok opens the door to the bedroom and I can see he's clearly upset."
play sound "sfx/door open.ogg"
show ran c facepalm with dis
r "\"Ugh! I’m sorry I took so long.\""
show ran c growl r paw with dis
r "\"Father put me through hell on the count of… well-\""
m "\"It’s fine…\""
show ran c shocked with dis
"I cut him off with a weak smile, no need for him to make excuses."
"I’m just glad he’s finally here."
show ran c confused with dis
r "\"Is it though?\""
show ran c neutral t with dis
r "\"Because it seems like you were crying.\""
show ran c neutral with dis
m "\"It’s just my mind wandering off…\""
m "\"…I don’t like being alone with my thoughts.\""
m "\"It takes me dark places.\""
show ran c smile e paw with dis
r "\"Speaking of…\""
hide ran c smile e paw with dis
play sound "sfx/drawer_open.ogg"
"The wolf walks towards the cupboard and opens the top drawer."
"He removes from it a bundle of tinder along with what I assume is a flint and some sort of steel loop."
play sound "sfx/tinder.ogg"
"He puts the loop onto his knuckles and strikes the flint with it, allowing sparks to fall down onto the tinder."
scene bg broom_light with dis
"Within moments he lights up the candles and the room is suddenly bathed in the warm hues."
show ran c talk e with dis
r "\"Much better…\""
show ran c smile with dis
"I can’t help but be amazed at his old-timey gadgets."
"I wouldn’t last a day without his aid or guidance; wish I was this resourceful."
show ran c talk with dis
r "\"I’m extremely tired, had a rather rough sparing session today.\""
show ran c smile with dis
"He mutters, rubbing his shoulder with pain clearly visible on his muzzle."
show ran c talk with dis
r "\"But I wouldn’t mind staying up a bit.\""

if DrinkingBuddy == True:
    show ran c smile with dis
    m "\"We could grab some ale…\""
    "I propose, remembering how Vul commented on the quality of Ranok's beverage."
    "He must enjoy it to have a barrelful of it."
    show ran c talk with dis
    r "\"Yeah, we could.\""
    show ran c smile with dis
    "The wolf smiles."
    show ran c shocked with dis
    m "\"And I could get that for ya.\""
    "I nod towards his shoulder, but he didn’t seem to understand my intention."
    r "\"Oh?\""
    m "\"I can try and massage it, while you relax.\""
    show ran c awkward with dis
    r "\"Heh… that does sound nice.\""
    show ran c smile with dis
    "He smiles again, but quickly his expression fills with embarrassment."
    show ran c awkward with dis
    r "\"I don’t want to take advantage, though.\""
    show ran c shocked with dis
    m "\"How could you, if I’m the one offering?\""
    show ran c smile with dis
    "I smirk, jumping off the ledge and rushing towards the kitchen."
else:

    show ran c shocked with dis
    m "\"I could get that for ya.\""
    "I nod towards his shoulder, but he didn’t seem to understand."
    r "\"Oh?\""
    m "\"I can try and massage it, while you relax.\""
    show ran c awkward with dis
    r "\"Heh… that does seem nice.\""
    show ran c smile with dis
    "He smiles, but quickly his expression fills with embarrassment."
    show ran c awkward with dis
    r "\"I don’t want to take advantage, though.\""
    show ran c shocked with dis
    m "\"How could you, if I’m the one offering?\""
    show ran c smile with dis
    "He smiles, looking towards the kitchen doors."
    show ran c talk paw with dis
    r "\"Well… I do have some ale in the kitchen. We could have a drink near the hearth.\""
    show ran c smile with dis
    "That sounds like a wonderful idea."
    "I smirk, jumping off the bed and rush towards the kitchen."

scene bg kitchen_night with dis
"I’m not much of an ale drinker, but I will humour the wolf; he seems to have had a rough day."
"As I fill our mugs with dark brew, Ranok builds the fire."
play sound "sfx/tinder.ogg"
"He huffs repeatedly at the tinder placed beneath the logs, slowly encouraging the flame to climb higher."
"I bring the filled tankards to the table, observing him intently."
"It would be useful to learn his method... the sooner the better."
m "\"Could you teach me how to do this?\""
scene bg kitchen_light with dis
play ambience "ambience/forest_night_and_fire.ogg"
"I ask, once the flame dances merrily inside the hearth."
show ran c talk with dis
r "\"Sure, there's not much to it.\""
show ran c smile with dis
"He nods, joining me at the table."
show ran c talk with dis
r "\"This is the fire striker.\""
show ran c smile with dis
"The wolf places a metal loop in front of me."
show ran c talk paw with dis
r "\"You make sparks by striking it at the edge of the flint.\""
show ran c smile with dis
"He then plops down a small glossy looking stone."
show ran c talk with dis
r "\"If you do that repeatedly on top of tinder, or kindling… eventually you get fire.\""
show ran c talk r paw with dis
r "\"I always have some laying around. Top drawer in the bedroom-\""
show ran c smile with dis
"He points behind me at the cupboard in the other room."
show ran c talk e with dis
r "\"-and here, underneath the hearth.\""
show ran c smile with dis
"The wolf looks down, drawing my gaze to a heap of twigs and hay hidden in the niche beneath the stove."
m "\"Thanks, I'll give it a try tomorrow.\""
show ran c smirk with dis
r "\"You better… I don't want you to wait in the dark until I come home. That's not good for you.\""
show ran c smile with dis
m "\"Yeah.\""
"I laugh awkwardly, not really keen on discussing my little freak out."
"Since he's finally here, I'd rather focus on making the most of it."
show ran c smile e with dis
"As he plops comfortably down, grabbing his mug, I stand up and walk behind him."
show ran c shocked with dis
r "\"Hmm?\""
"He follows me with his gaze, as I begin to softly knead his shoulder."
m "\"Offered you a massage, didn’t I?\""
show ran c awkward with dis
r "\"Heh… yeah.\""
show ran c smile e with dis
"He muses, closing his eyes and enjoying my rubbing."
"I’m not exactly an expert, but I simply follow cues from his body."
"I apply as much pressure and force as it takes to draw a grunt from him, letting up and changing spots when I can see he’s getting too worked up by it."
show ran c talk e with dis
r "\"Mmmmm. Feels good to be home…\""
show ran c smile e with dis
"He croons in pleasure; a soft growl reverberating in his playful words draws a slight blush from my cheeks."
"He mistakes my embarrassment for something else and quickly turns to face me with a regretful expression."
show ran c shocked with dis
r "\"I'm sorry… that was stupid of me!\""
m "\"W-what?\""
show ran c embarrassed with dis
"I blink in confusion."
r "\"All you must be thinking about is getting back home… and then I throw a comment like that.\""
"I smile at his train of thought; he's being considerate to a fault."
m "\"It's fine, really… I know what you meant.\""
show ran c sad t with dis
r "\"I will take you back, I promise.\""
show ran c sad with dis
"He insists, his gaze full of determination."
m "\"I know.\""
"I reassure him."
show ran c neutral with dis
"I have absolutely no doubts about his intentions, but I'd rather not talk about my forgotten home right now."
"I simply nod towards my hands, letting him know I want to return to the massage."
show ran c smile e with dis
"He sighs, shaking his head in amusement and rests back against the chair, allowing me access to his aching muscles."
"Well… sort of."
"I still have all his gear in my way."
show ran c shocked with dis
m "\"It would be easier if I take this off.\""
"I knock on his shoulder pad."
show ran c smirk with dis
r "\"That eager to undress me, huh?\""
show ran c smile with dis
"The wolf chuckles, causing me to gasp in annoyance, only to remind myself that teasing is just in his nature."
"I shall play along... we'll see who breaks first."
m "\"If that's what you like to think...\""
show ran c shocked with dis
"I shrug, approaching him from the front and sinking my fingers beneath the plate to feel up the latch."
show ran c embarrassed with dis
"I can see embarrassment paint across his entire muzzle… he really is all bark but no bite."
r "\"Ummmm…\""
show ran c shocked with dis
m "\"What's the matter? Human got your tongue?\""
show ran c talk g with dis
r "\"Human will get bitten if he's not careful.\""
show ran c smile with dis
"He issues a soft, playful growl as I detach the piece of armour."
show ran c shocked with dis
r "\"Huh… didn't even skip a beat.\""
"He mutters with slight surprise."
show ran c smile with dis
"It takes me a moment to realise he's talking about my heart."
"I can see a proud smile stretch across his muzzle."
show ran c talk with dis
r "\"You start to trust me.\""
show ran c smile with dis
"He says with satisfaction and I just can't help myself."
show ran c shocked with dis
m "\"That, or perhaps you're not as scary as you think you are.\""
"I chuckle, placing the metal pad onto the table."
show ran c talk g with dis
r "\"Aren't I?\""
show ran c smirk re with dis
"The wolf croons, raising from his seat and squaring up with me."
"I literally reach only to his breast and had not for his obviously gleeful tail swings, I even might have been a little intimidated."
m "\"Nope, you're just a well kempt fluffball.\""
show ran c talk e with dis
r "\"I'll take that as a compliment.\""
show ran c shocked with dis
m "\"I must've said it wrong...\""
show ran c smile with dis
"I tease, but he only shrugs, removing his leather straps and placing his massive sword against the wall next to the hearth."
show ran h smile with dis
"Once he sits himself back at the table, I get full reign over his entire back."
show ran h smile e with dis
"I smile, rubbing his tense neck muscle while he draws air through his teeth. "
"Guess that’s a sore spot, so I try to be gentler around it."
"Eventually he breaks the silence, his voice slightly deeper and strained due to my massage."
play music "music/memories.ogg" fadein 3.0
show ran h sad t with dis
r "\"Did you manage to jog your memory a little while I was gone? Remembered anything at all?\""
show ran h sad with dis
m "\"Nope…\""
"I shrug in defeat, causing him to fall silent for a moment."
show ran h sad t with dis
r "\"Shame… I was hoping there was a silver lining to your earlier distress. A bad memory perhaps.\""
show ran h sad e with dis
m "\"No such luck, I'm afraid. My distress seems to be entirely of my own making.\""
"Literally… it's all just in my own head."
show ran h neutral e with dis
"He burrows deep into his thoughts, as I continue kneading his shoulders."
"In truth, it feels almost therapeutic for me, not to mention I get to feel up all of his muscles."
"He's almost like a walking anatomy model."
show ran h neutral tp with dis
r "\"You worry about your memory, I get that…\""
show ran h talk with dis
r "\"...but I’m also glad I get to show you a bit of our life.\""
show ran h smile with dis
"He mutters, taking an idle sip of his ale."
show ran h talk p with dis
r "\"Perhaps this way, you’ll be able to see the rest of Avalan through my eyes.\""
show ran h talk e with dis
r "\"It’s quite something, I tell you that. Being able to experience it anew almost makes me envy your memory loss.\""
show ran h laugh with dis
"He laughs merrily, while I push slightly harder against his shoulder in punishment for making light of my situation."
show ran h embarrassed at jumping with dis
"As he grunts softly under my workout, I simply pretend it was unintentional."
m "\"Have you ever been outside of this forest?\""
"I ask, moving my hands down to his shoulder blades."
show ran h awkward with dis
r "\"Outside of Tirnan?\""
show ran h smile e with dis
m "\"Is that what it’s called?\""
"He nods, drawing air through his fangs in pain, as I find another bruised spot."
show ran h talk e with dis
r "\"When I was little, I snuck out of the village. I hid inside a herb sack in one of our caravans headed for Strandbard.\""
show ran h smile e with dis
"I supress a chuckle, imagining the scene; he was a troublemaker since birth."
show ran h shocked with dis
m "\"So that's where your scent comes from.\""
"I propose cheekily."
show ran h awkward with dis
r "\"My scent?\""
"He blinks in confusion and for a moment I wonder whether the comment wasn't too forward on my part."
"I quickly laugh it off though; I had to endure his teases, it's about time he tasted his own medicine."
show ran h shocked with dis
m "\"You smell like the forest.\""
show ran h shocked blush with dis
"I muse, noticing his tail gave an idle flicker before it began slowly swaying back and forth."
"He's struggling to contain a smile, clearly enjoying my observation."
m "\"Where's Strandbard?\""
show ran h smile e with dis
"I decide to spare him the lingering embarrassment of a genuine compliment by bringing our conversation back on track."
"But it's handy to know that when he pushes my buttons, I can push a few back."
show ran h talk rp with dis
r "\"It’s a Tigerii town just outside of our territory. It’s where most of our interactions with the outside world takes place.\""
show ran h talk e with dis
r "\"The name is actually derived from an old Inn around which the town grew; the Stranded Bard.\""
show ran h smile e with dis
m "\"Ah.\""
show ran h talk e with dis
r "\"I expected the place to be crawling with tigers, but to my surprise it was filled with all sorts of creatures.\""
show ran h talk p with dis
r "\"There were Lions there, Sylvan Folk of all shapes and sizes, even Lynxes and Wolves.\""
show ran h smile e with dis
"I muse, easing up on the workout and trying to imagine those various beast men."
"It all seems so fantastical."
show ran h neutral t with dis
r "\"I saw cubs playing with pups in the streets, as if they didn’t see they were different species.\""
show ran h neutral tp with dis
r "\"There was no combat training, no preparation for war of any sorts… just idle folk going about their idle lives.\""
show ran h neutral e with dis
"I almost picture a fairy tale town with happy people only doing happy things and thinking happy thoughts."
"Only thing missing is the townsfolk randomly bursting into a choreographed song."
"I know it’s just his perception as a child and perhaps the town wasn’t as idyllic, however the description does strike a chord with me."
m "\"Sounds… beautiful really.\""
show ran h think with dis
r "\"Hmmm.\""
"He pauses, looking rather concerned."
show ran h neutral ext with dis
r "\"It made me wonder why we lead such different lives. Why we shied away from the otherkin and jealously protected our woods.\""
show ran h neutral t with dis
r "\"We’re trained in combat since we’re pups, always preparing for a war.\""
show ran h neutral tp with dis
r "\"Otherkin youth play with wooden swords and chase hoops.\""
show ran h neutral ext with dis
r "\"It was very confusing.\""
show ran h neutral e with dis
"I glance at his chiselled but battered body and can see that the wolf really didn’t have an idle day in his life."
"Instead his days were filled with endless chain of spars and exercises meant to hone this physique."
"He might have a rocking bod, but it came at the cost of his childhood."
"It’s almost sad, really."
show ran h awkward with dis
r "\"When my father found out, he was furious.\""
show ran h neutral rt with dis
r "\"We don’t let pups outside our territory.\""
show ran h neutral et with dis
r "\"We don’t want them to get the wrong ideas…\""
show ran h neutral with dis
"I blink."
show ran h annoyed with dis
m "\"Wrong ideas? Like diversity and fun aren’t bad?\""
show ran h annoyed t with dis
r "\"You can scoff all you like, but yes.\""
show ran h neutral tp with dis
r "\"It makes you question everything your people stand for.\""
show ran h shocked with dis
m "\"I’ve been questioning everything since I woke up!\""
show ran h annoyed with dis
"I can’t hold in a laugh."
m "\"I find questioning things to be yet another good policy.\""
show ran h annoyed t with dis
r "\"Not when you’re too young to understand what it is that you’re questioning.\""
show ran h pouty with dis
m "\"Sheltering your kids like that doesn’t seem right.\""
m "\"Almost like you’re indoctrinating them.\""
show ran h annoyed with dis
"Ranok looks back at me and I finally splay my hands out in a ‘what’ gesture."
show ran h neutral et with dis
r "\"You don’t understand.\""
show ran h neutral e with dis
m "\"From what you’re saying you don’t understand it either!\""
"I protest through a snicker."
show ran h neutral rt with dis
r "\"I know why we don’t let the young ones out. For the tribe to be strong, their resolve needs to be strong.\""
show ran h neutral t with dis
r "\"The otherkin don’t need to worry about wars, there’s millions of them. They have plenty of soldiers even if most of their people never seen a weapon in their entire life.\""
show ran h neutral tp with dis
r "\"There’s maybe a hundred thousand of my kin left within these woods.\""
show ran h neutral et with dis
r "\"We need to keep our wits about us to hold onto what we've got left.\""
show ran h neutral e with dis
"I frown, slowly losing my hope that Ranok is that much different from the rest of his people."
"From what I’ve heard so far, they seem to be highly militarised, almost totalitarian society."
m "\"So you agree with this?\""
show ran h annoyed with dis
m "\"Pups fighting with swords, rather than playing with toys? Is that really what you want?\""
show ran h annoyed t with dis
r "\"I don’t want our people to be weak, but I also don’t want them to continue this course.\""
show ran h neutral rt with dis
r "\"Avalan changed… and we should change with it.\""
show ran h neutral tp with dis
r "\"I want to see what the tigers did with their supremacy over the continent.\""
show ran h neutral ext with dis
r "\"If indeed the Alliance of Tigeron is a fellowship of equals it’s painting itself to be.\""
show ran h sad t with dis
r "\"Or just another lie, like the Rebellion where we traded one overlord for another.\""
show ran h sad with dis
"Immidiately I remember the book I browsed through..."
"I almost want to engage with the topic, but eventually I just sigh looking at my hands still kneading his strained shoulders."
"This is all really weird, like a fairy tale…"
"Talking beasts, castles and queens."
"A little girl comes to my mind; she’s lost in a strange world and her only way home is to simply follow the lead no matter the madness."
show ran h shocked with dis
m "\"Through the looking glass…\""
"I chuckle, knowing I even had my own 'off with his head' encounter just the day before."
r "\"Huh?\""
m "\"Nothing.\""
show ran h neutral with dis
"I shake my head, looking back at him."
show ran h confused with dis
m "\"I might not know much about wolves and tigers, but the more you say, the more convinced I am that this little adventure you had as a pup did more good than harm.\""
m "\"It made you curious…\""
m "\"That longing to explore and to understand… it made you more accepting of others and I admire it.\""
show ran h smile with dis
"He stretches out with a satisfied grin."
show ran h talk e with dis
r "\"Thanks.\""
show ran h shocked with dis
m "\"I'm also glad we'll get to share this little adventure together, learning from one another.\""
show ran h laugh with dis
r "\"Damn right!\""
"Ranok cheers, raising his mug and spilling a little bit of his brew."
show ran h smile with dis
"I roll my eyes in slight annoyance; I just cleaned the floors."
show ran h talk e with dis
r "\"In all fairness I was quite nervous about you… I knew you were my path the moment I found you, but I worried.\""
show ran h smile with dis
m "\"What about?\""
show ran h awkward with dis
r "\"You know…\""
"He mutters with a troubled expression."
r "\"Would we-?\""
"He interlocks his fingers in a jigsaw gesture and I laugh."
show ran h shocked with dis
m "\"And did we?\""
show ran h smile with dis
"I smirk, causing his eyes to narrow."
show ran h talk with dis
r "\"Ok, I think you're confusing overconfidence for an attractive trait.\""
show ran h shocked with dis
m "\"As the kettle said to the pot.\""
"I quote him right back, pushing playfully on one of his muscles and the wolf widens his eyes in shock."
show ran h laugh with dis
"Our joint laughter fills the room and I return to soothing his aching back."
show ran h smile e with dis
"I must admit, it feels nice to be able to talk with someone so openly…"
"…no matter the subject, or what our respective position is on the matter, we always manage to return to a common ground."
"It's an amazing quality."
"This wolf… there is something about him that I simply adore."
show ran h talk e with dis
r "\"Damn, this feels good.\""
show ran h smile e with dis
"I bet."
"A sly smile paints across my face, as I bask in his praise."
"That is, until I see a bulge in his crotch growing larger with each workout I give to his muscles."
"He’s enjoying it {i}far{/i} too much!"
"I pull my hands away, returning hastily to the table, pretending I haven’t noticed."
show ran h smile with dis
"Last thing I want is him getting all self-conscious and giving me another speech about being 'defective'."
"I grab my mug and nervously bring it to my mouth, trying to swallow a long gulp."
show ran h talk with dis
r "\"Thanks… I needed that.\""
show ran h smile e with dis
"He mutters, still savouring the afterglow of my massage."
m "\"You’re welcome!\""
"I respond, looking away to hide my blush."

if Romance == False:
    show ran h talk e with dis
    r "\"So, how about that Wild Thought?\""
    show ran h smile e with dis
    "He asks quietly, simply reclining back into his chair."
    m "\"Sorry?\""
    show ran h talk e with dis
    r "\"Is this a better time?\""
    show ran h smile e with dis
    "He muses, lazily opening one eye."
    m "\"I- ummmm…\""
    "I struggle, unsure whether it's a good time to bring it all back up."
    "But then again, my little freak out proved to me that I really have to rely on this wolf."
    "And if we are to be friends, there has to be honesty between us."
    show ran h talk with dis
    r "\"Come on, [mc]… don't leave me hanging.\""
    show ran h talk rp with dis
    r "\"You had me wondering about it the whole day...\""
    show ran h smile with dis
    "I sigh, drawing his full attention."
    "The wolf readjusts himself slightly, looking at me with an encouraging smile."
    "Well… here goes nothing."
    m "\"I need to tell you something, but I don’t know how.\""
    show ran h talk p with dis
    r "\"You seem to have pretty good grasp of our language.\""
    show ran h smile with dis
    "He smirks."
    m "\"It’s not that…\""
    "I struggle, this is much harder to do than I thought."
    "He just looks at me with a smirk, raising one brow in a teasing expression."
    "Damn, he knows how to disarm me."
    m "\"It’s about yesterday morning.\""
    "I finally spill it out, looking away at the window."
    show ran h shocked with dis
    r "\"Oh.\""
    "It would seem I caught him off guard."
    show ran h shocked blush with dis
    r "\"What about it?\""
    m "\"I just want you to know… that I don’t-\""
    m "\"Oh fu-\""
    "I sigh."
    show ran h embarrassed with dis
    m "\"I don't mind it, ok?\""
    m "\"And if you do, I hope you won’t start calling me…\""
    m "\"…defective.\""
    "I cringe, really unsettled by the term."
    show ran h annoyed t with dis
    r "\"I would {i}never{/i}!\""
    show ran h annoyed with dis
    m "\"Good.\""
    "I sigh in relief at his actual offence."
    show ran h sad with dis
    m "\"It would really hurt if you'd ever call me that.\""
    show ran h sad t with dis
    r "\"Why would I even-?\""
    show ran h confused with dis
    "He cuts himself off, looking at me with slight confusion."
    "I cringe, slowly loosing my resolve… but since I started, I might as well finish."
    m "\"No one should feel wrong, or broken just because… they-\""
    show ran h shocked with dis
    m "\"…like guys.\""
    "I finish, not even looking at him."
    "I can’t believe I just said it, but… I am glad I did; it had to be said."
    "The wolf readjust himself, as he turns to face me with disbelief in his eyes… however there's a clear hint of kindness in his gaze."
    show ran h shocked blush with dis
    r "\"Wait a moment... You-\""
    r "\"You like males?\""
    show ran h embarrassed blush with dis
    "Fuck."
    m "\"…\""
    "It is hard to force myself to face him, but I have to look into his eyes, otherwise what was the point in bringing all of this up?"
    m "\"I hope we can still be friends.\""
    show ran h annoyed t with dis
    r "\"Of course, we can!\""
    show ran h annoyed with dis
    "He scoffs at me, as if it was never a question and I’m glad to hear it."
    show ran h sad t with dis
    r "\"You're cute and all, but-\""
    show ran h sad with dis
    "Uh-oh."
    show ran h sad t with dis
    r "\"I’m not like you.\""
    show ran h sad with dis
    "He grimaces with embarrassment."
    show ran h awkward with dis
    r "\"I really do like females.\""
    m "\"Oh…\""
    show ran h smile e with dis
    "I freeze, looking at the window."
    "In truth I just want to jump out of it."
    show ran h smile with dis
    m "\"I-\""
    show ran h talk p with dis
    r "\"Besides, you’re rather small and… wrong species, no?\""
    show ran h smile with dis
    "He cuts me off with a chuckle, almost as if trying to save me embarrassment."
    "I laugh nervously."
    m "\"Heh, yeah…\""
    show ran h talk e with dis
    r "\"Don’t worry about it, it doesn’t change anything between us.\""
    show ran h smile e with dis
    "Yeah… it doesn't."
    "I nod in agreement."
    "My childish infatuation is just that- a silly whim out of left field."
    "Especially now, when I'm not exactly in control of my own emotions."
    "But it's good to have the air cleared, at least he knows the truth about me."
    show ran h shocked with dis
    m "\"I'm sorry if I made you uncomfortable.\""
    r "\"Me?\""
    show ran h laugh with dis
    "He laughs softly."
    show ran h smirk with dis
    r "\"You're the one who has to live under the same roof with a hunk like me.\""
    r "\"Must be torture.\""
    show ran h smile with dis
    "He winks at me and I try my hardest not to blush."
    "I won't give him the satisfaction."
    m "\"Who said I'm interested?\""
    show ran h laugh at jumping with dis
    "I punch his arm teasingly, nervous laughter escaping both of our lips."
    show ran h smile e with dis
    m "\"You're not my type.\""
    show ran h talk e with dis
    r "\"Whatever you say, {i}tiny{/i}...\""
else:

    "I want to continue the conversation, but I see he's completely out of it."

show ran h smile e with dis
stop music fadeout 6.0    
"He just leans his head back and rests his eyes."
"I slurp the ale through the awkward silence, checking up on him every now and then."
"Every time he's around a complete sense of calm descends upon me to the point where I simply enjoy his presence."
"I look at the trees outside, gently rustling on the wind."
"I wonder what time it is…"
"Curious about the Tiger Rebellion he mentioned, I consider picking up the blue book again, when I notice Ranok's head slump slightly to the side."
"I think he drifted off to sleep."

if Romance == True:
    "I look at his crotch and can confirm he has been completely pacified."

"Damn, he must have been really exhausted."
"That, or my rubdown relaxed him to the point of utter bliss."
"I chuckle it off; who am I kidding?"
"My poor attempt at a massage most likely will cause him soreness in the morning."
"I also banish any thoughts of late-night reading."
"Sitting here in the dimly lit kitchen with the snug warmth of the fire, I became quite groggy myself."
"I allow us a few more moments, struggling with my drink, until I give up."
"The bitter brew is not my kind of thing."
"I poke Ranok, stirring him up from his nap."
show ran h neutral with dis
"Mentally he's already in tomorrow, so I have to help him up."
show ran h neutral e with dis
"Considering his size, it's not an easy task… he really weighs a lot."
"Once he stands up, he slumps slightly onto my shoulder and I almost stumble."
m "\"Ok there, buddy… let's go.\""
"I lead us slowly into the bedroom."
scene bg broom_light with dis
play ambience "ambience/forest_night.ogg" fadein 3.0
"When in sight of the bed, Ranok plops onto it with a heavy thud."
play sound "sfx/bed_jump.ogg"
r "\"I love you so much…\""
"He mutters quietly, clearly addressing the mattress."
"I find it rather cute."
"Within just a moment I can hear him snoring softly."
scene bg broom_night with dis
"I blow out the candles, laying myself down next to him."
"I dart my eyes between his peaceful muzzle and the soft flickers of the slowly dying fire within the hearth."
"I haven't felt this calm the entire day… the soft orange hues flooding from the kitchen just make this whole scene so idyllic."
"Only one thing would make it better-"
"And as if he read my mind, Ranok's massive paw swoops behind me and pulls me closer to his chest."
"Considering what he said, I should try and free myself from his embrace, but I'm nowhere near that strong willed."
"Instead, I succumb to my dire need for proximity."
"I sigh, smiling in mix of guilt and happiness; completely enveloped by his smell."
"I try not to fall asleep just yet, simply enjoying this intimacy."
"I could stay like this forever, just watching him sleep; his peaceful muzzle softly smiling even through his slumber."
"But it doesn’t take long for his rhythmic breathing to lull me to rest and I effortlessly drift away into a tranquil dream."
stop ambience fadeout 3.0
scene bg black with slow_dissolve

jump b1c4
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
