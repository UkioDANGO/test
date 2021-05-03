label b1c1:

stop music fadeout 3.5
scene bg black
with transition_fade
window show
play ambience "ambience/void.ogg"  fadein 6.0
play sound "sfx/heartbeat.ogg" fadein 3.0
"Complete nothingness."
"I feel as if nothing existed before this moment—no memories of anything other than this utter void."
"I don’t know how long I’ve been here; time seems to stretch into eternity."
"The rhythmic thumping that accompanies me starts to fade away."
stop sound fadeout 6
"I somehow know it’s the sound of my very own heart being silenced, as if death embraced me."
"Is this what death feels like?"
"How can I be dead if I haven’t even lived…?"
"I cannot feel anything, summon any emotion; it’s just me and this thorough nothingness."
"Finally silence envelopes me…but it is not death."
"Whatever’s happening, it does not offer me release from this empty awareness."
stop ambience fadeout 6.0
with vpunch
play music "music/entity.ogg"  fadein 3.0
"!!!"
"Suddenly I hear hundreds of whispers, one voice really, but boundless and out of time."
"It folds onto itself, forming an incoherent chatter."
"The language sounds so foreign, yet it speaks to my very core."
"Bits and pieces flood my mind like a tidal wave."
"Among the onslaught of chaos, I sift through these strange words, failing to find anything intelligible."
with vpunch
"!!!"
"Excruciating pain surges through my mind, like a blunt force to the head."
w "\"The key…\""
"I want to scream in agony, as my entire being is set aflame by those words."
"Then the black canvas pulls over my eyes."
"I can see the darkness now; cold and pitch black."
w "\"…black stone…\""
"Another surge fills my mind with painful awareness."
"I know what stones are—what earth is."
"This void is not native to me; I come from a world beyond this nothingness."
"I am trapped here!"
w "\"You and I…\""
"I suffer another torment; I feel myself materialise in the abyss, my body becoming the edge of existence."
"I'm no longer floating in nothingness."
"Instead I'm immobile, restrained, and left in the dark."
"I must break free… this isn’t right!"
"This isn’t right!"
w "\"Wake up…\""
"The whispers intensify, as if urging me on."
"Am I dreaming?"
"Is this a nightmare?"
w "\"Wake up!\""
"Their anger rises and the command is harder to ignore through the agony caused by each word."
"I want to wake up, I do!"
w "\"WAKE UP!\""

menu:
    "Open your eyes.":
        jump wake

label wake:
scene black
show bg white:
    alpha 0.0
    ease 2.0 alpha 1.0
show fade_black as mask:
    xalign 0.5 yalign 0.5 xpos 0.5 ypos 0.5 zoom 1.0 size (config.screen_width,config.screen_height) alpha 1.0
    parallel:
        pause 1.0
        ease 4.0 alpha 0.0
    parallel:
        ease 4.0 zoom 2.0

stop music fadeout 3.0
"The light rushes into my eyes, as if I'm stricken by lightning."
"I know what lightning is… I can picture it crackle across the stormy sky."
"I'm sure I've seen a storm before, with flashes so bright that for a split second everything turns white."
"Pretty much like now…"
"I’m forced to squint as my vision doesn’t adjust, everything is {i}so{/i} blurry and white; I could’ve sworn I’m staring into the sun."
"Sun…"
"I can almost recall its warmth."
"I'm certain I belong here, in this world."
"The void that held me moments ago slowly fades into my memory."
"It was just a dream, and now that I am awake, I will return to my normal life whatever it may be."
"Despite trying my hardest, I cannot remember anything concrete about my past."
"The pain in my eyes lingers and I want to shield myself from the glare, however my body is numb."
"I try to raise my hand, to bring it over my head, but it only flops in place."
"My heart speeds up at a horrid realisation:"
m "\"I cannot move…\""
"I try to speak, but it only comes out as a mumble as I struggle against my limp body."
"Am I paralysed?"
"My fingers twitch as I concentrate on them, tapping at the soft mattress beneath me."
"No, I'm just frozen… "
"I can feel that I woke up from a long, deep sleep and my body just now started thawing."
"Somehow, I manage to use my lifeless hand as pendulum, to flip myself to the left side."
"I arch my back, crawling like a snake in the bed, trying to get to the edge."
"Finally, my eyes adjust, and I can see the room."
scene bg broom_day with slow_dissolve
play ambience "ambience/birds.ogg" fadein 6.0
"Raising my head is a challenge, but eventually I manage to have a proper look around."
"I can see the door in front of me."
"There's only one window; it has a wide, cluttered ledge, and lets in the light of an early afternoon."
"There isn’t much in way of furniture— just a wooden chest next to the door, a cupboard to the left and a large wardrobe next to the window."
"I can’t help but notice how dirty everything is, with cobwebs in every corner and dust filling the air."
"Despite my memory loss, I am sure of one thing: this isn’t my room; this is NOT my home."
"Where the hell am I?"
"I struggle a bit further, still very much numb, although I can feel life returning to my limbs."
"I push myself over the edge, which I fast realize was a mistake as I fall hard to the wooden floor with a loud thud."
play sound "sfx/fall.ogg"
with vpunch
"I almost pass out at the force with which my head slams the boards, but the cold of the ground instantly seeps through my naked skin, bringing me back to my senses."
"I try to collect myself from the floor, pushing hard with both hands, but it feels as if I'm lifting a boulder."
"All I manage to do is sit up in a groggy fashion, noticing my naked upper body; at least my lower part is covered by what I think is a loincloth… which is… strange to say the least."
"There is a sound of heavy footsteps approaching from the adjacent room."
"I gaze at the doors anxiously, expecting some sort of a familiar face coming to my aid."
"Maybe I’m away with family… even though I can’t remember who my family are."
"Everything feels so strange and out of place!"
play sound "sfx/door open.ogg"
show door with dis
"The door cracks open, and my wishful thinking is snuffed out by a large wolf creature entering the room."
show vul growl at eight with dis
"He is covered in thick black fur, standing upright on his hind legs with torso chiselled like a marble statue."
"For a split second, my attention drifts to a round black stone resting on his chest, filling me with an odd sense of dread."
"However, that's quickly replaced by a more rational fear, as I shiver at the sight of the wolf's clawed paws tensing up in anticipation."
"The beast snarls, gazing at me with his wild red eyes, almost as if looking right through me and I can't help, but stare back at his massive snout filled with jagged fangs."
show vul facepalm with dis
bw "\"My fucking luck! I told him NOT to leave me alone!\""
"I don’t even register that he speaks, feeling weakness overtake me."
show vul neutral with dis
"I must be dreaming… this is a nightmare!"
"Finally, I win the inner battle, and manage to regain control of my frozen body."
"I throw myself up against the cupboard, climbing it like a cliff."
play sound "sfx/drawer_open.ogg"
"Instinctively I pull out a drawer, hastily rummaging through its contents to find anything I can use to defend myself."
"Amongst the clothes and trinkets, I grasp something with a hard handle and pull it out, holding tight in front of me with both hands."
show vul talk p with dis
bw "\"What are you doing?\""
"The wolf regards my weapon with mild contempt; it’s a wooden comb."
show vul growl with dis
"Despite how foolish I look, I still hold it out in front of me, jabbing at the air to make the beast aware I mean business."
"Before I can react, he is already on me, one paw grabbing my neck and pushing me hard against the wall."
play sound "sfx/hit.ogg"
with vpunch
"My head bounces off of it like a ball, and I nearly drop my only weapon."
"That’s when his massive paw squeezes my left wrist, the pressure he applies to my bones taking the floor from underneath me."
"My legs are noodles, and I simply hang from his hold."
show vul growl k with dis
bw "\"Let. It. Go.\""
"He reiterates through his fangs, snarling straight into my face."
"I tear up as he squeezes harder, almost to the breaking point."
"Without a choice, I let the comb go and it flops to the floor."
play sound "sfx/drop.ogg"
"The next thing I know I’m being swung onto the bed like a ragdoll, my weight meaning nothing to the beast."
with vpunch
play sound "sfx/bed_jump.ogg"
"I bounce off the bedding, scraping my shinbone on the wooden frame."
"The pain jolts to my head and I gasp, quickly grabbing my leg and pulling it close to myself."
"Fuck it hurts, it almost makes me forget about the still-throbbing wrist."
show vul growl p with dis
bw "\"Now stay there if you know what’s good for ya. I’ll be back in a moment.\""
"The wolf huffs at me in annoyance and hastily leaves the room, closing the doors behind him."
play sound "sfx/door close.ogg"
hide door
hide vul growl p
with dis
"What the fuck is going on?"
"Why can’t I wake up?"
"I lie there in bed, huddled in pain and crying, desperately trying to end this nightmare, but with no success."
"The pain lessens, and my panic slowly switches me from fight to flight mode."
"I need to escape."
"I can hear the beast rummaging in the next room, clearly looking for something."
"I look towards the window and realise that I don’t want to find out what he’s looking for."
"His current preoccupation is my best chance to get out of here!"
"I try to step off the bed as quietly as I can, tiptoeing I move closer and closer towards the only route of escape."
play sound "sfx/floor_creak.ogg"
"I freeze up as one of the boards creaks, almost as if on cue."
"My eyes trail to the doors, and I weigh my options."
scene bg window_day with dis
"Instincts overtake me and I jolt to the ledge, immediately locating the latch locking the window, but I cannot open it because of all the clutter."
play sound "sfx/racket.ogg"
"In panic I begin brushing everything off with complete abandon, racket echoing across the empty room."
"I can see the forest in front of me, freedom just within my reach."
m "\"HELP! HELP!\""
"I yell out as I hear the beast storm in, the doors flying open with a bang."
play sound "sfx/door_slam.ogg"
with vpunch
bw "\"What the fuck?\""
m "\"SOMEBODY HELP ME!\""
"Not even a second later the entire world turns, as if I were on a merry-go-round."
"My stomach moves up to my throat, and I fly across the room with the force of the spin."
scene bg broom_day
show door
with dis
play sound "sfx/bed_jump.ogg"
with vpunch
"I gasp as my back strikes the bed again."
"Despite the padding it's a very rough landing, but before I even register the world of pain my entire body is in, I see the black shadow swoop above me."
show vul growl u with dis
play sound "sfx/bed_jump.ogg"
with vpunch
"The entire bed shakes as the beast lands on top of me, his powerful paws flanking me on both sides."
"He presses his snarling muzzle into my cheek, forcing my face to one side and pressing it deeper into the bedding."
bw "\"I guess we have to do it the hard way…\""
"My eyes well up, as I feel him dribble onto my neck with each hot puff of air."
m "\"PLEASE, SOMEBODY—\""
"He cuts me off with his paw, pressing it hard to my mouth."
scene choking with slow_dissolve
"I continue my muffled shouts as I cry in horror."
"Wake up!"
"Why can’t I wake up?!"
bw "\"Shut up, or I will rip your fucking throat out!\""
"The beast growls, grabbing my neck with his other paw, the weight of his upper body now fully pressing down on me."
"He is squeezing my windpipe shut without even trying."
"I want to gouge his eyes to throw him off, but I am unable to reach his muzzle over the bulging muscles of his arms and shoulders."
"I clamp my eyes shut as my body begins to convulse, partly due to hysteria, but mainly because I am desperately trying to draw air."
"Finally, my hands go limp and fall lifelessly to the bed, ending my pathetic defence."
"I will die here."
"I don’t want to die."
play sound "sfx/heartbeat.ogg" fadein 3.0
"My muffled screams begin to fade, as the agonising pain fills my empty lungs."
bw "\"SHUT UP!\""
"He pushes harder, increasing my desperate tremors."
"My body becomes unresponsive and I lose any sense of self."
"I can hear his angered growl hush above me just as everything begins to fade."
"I slowly return to the darkness, again accompanied only by my beating heart."
stop sound fadeout 3.0
scene bg black with transition_fade
"My mind stirs with a slight discomfort stretching across my entire body; my mouth is dry and there is tension in my joints."
"I now realise my arms are twisted behind my back, arching it upwards in an uncomfortable way."
"I can feel as if something unpleasant was stuck at the back of my throat."
"Did I fall asleep like this?"
"I’m not sure what happened."
"I think I was having a bad dream—something about a werewolf and a cabin in the woods…"
"I seem to be having a lot of night terrors lately and I’m glad I can finally wake up."
scene bg broom_day with slow_dissolve
play ambience "ambience/birds.ogg" fadein 6.0
"But as I open my eyes, it’s clear that the nightmare isn’t over yet."
"It’s the same dingy, little room with a small window; black fur and fangs flashing through my mind."
"Oh no…"
"The savage attack was not a dream!"
"I try to jump up, but my hands and ankles are tied together with length of a rope, bounding me like a parcel."
"I can’t roll to either side without dislocating my shoulder; there is no breaking free from this."
"When I try to speak, I realise I’m gagged with a dirty cloth, which explains the dryness and a weird, briny aftertaste."
"I look around the room, trying to jog any memory of this place."
"Was I kidnapped?"
"Is this some sort of messed up prank?"
"I try to rationalise my situation, however the more I think about it, the more cold sweats dot my body."
"Why can’t I remember anything else than this cabin?"
"Is anyone even looking for me?"
"I can hear someone in the other room, heavy footsteps pacing impatiently back and forth."
"I gaze at the door with dread, almost certain it is the same beast that just attacked me."
"Then I hear someone else enter the cabin."
bw "\"Finally! What took you so long?\""
"The cold voice confirms my suspicion—it's that brute."
s "\"I had to avoid my father all day; he only just left. The hunt should buy us time at least until the morning.\""
s "\"How’s the human?\""
bw "\"Peachy.\""
"I frown at the comment—peachy indeed."
s "\"What do you mean? He’s awake?!\""
bw "\"See for yourself.\""
"There's a rush of padding toward the door, and I panic as a massive grey wolf enters the room."
play sound "sfx/door open.ogg"
show door
show ran c smile at four
with dis
"He's dressed in some sort of medieval armour, a green cloak falling from his shoulders."
show ran c shocked with dis
"Initially he has an excited expression, but it immediately sours at my predicament."
show ran c growl r with dis
"He throws an angry gaze towards the black male who tied me up."
show ran c growl r paw
show vul growl behind ran at right
with dis
gw "\"What the hell did you do to him?\""
bw "\"The human should’ve been tied up to begin with; he tried to escape.\""
show ran c resigned with dis
"When I see that brute I want to scream, to run away, but all I can do is wiggle and mumble."
show ran c neutral at left with move
"The grey wolf approaches me, looking down carefully over my body."
show ran c shocked with dis
gw "\"Are those {i}choke{/i} marks?!\""
show ran c growl r paw with dis
gw "\"He’s all bruised!\""
show vul eyeroll with dis
bw "\"I saved our pelts, you idiot!\""
show ran c neutral
show vul neutral
with dis
"My eyes open wide at the creatures arguing at the foot of the bed."
"Seeing one of those wolves was bad enough but seeing them both sends a chill down my spine."
"All I can do is stare, motionless."
"They are both enormous, much taller than what I consider natural, with broad shoulders making their entire posture more than intimidating…"
"And that’s without accounting for all the fangs and claws."
"I am terrified."
show ran c smile
show vul intrigued
with dis
"I avoid looking directly at them, but a shadow moves in the corner of my eye."
"The grey wolf is approaching me slowly, paw extended towards my face."
show ran c shocked
show vul growl
with dis
m "\"HELP! SOMEONE HELP ME!\""
"I try to call out, but all I accomplish are muffled whines through the gag."
show ran c sad with dis
"My crushed windpipe feels as if I've swallowed a stone—a painful lump stuck halfway down my throat thanks to that monster."
gw "\"Shhhhhh!\""
"The grey wolf tries to shush me, but I continue to yelp, despite how much it hurts."
m "\"HELP!\""
m "\"I WANT TO WAKE UP!\""
gw "\"Please, be quiet!\""
"His soft pleading almost causes me to stop, but I can hear a deep growl behind him."
show vul talk pl with dis
bw "\"Just fucking kill it, before everyone hears this!\""
show ran c shocked
show vul growl
with dis
"And just like that, the most instinctual cry comes to me, the one I always fall upon in a seemingly unending nightmare."
m "\"MOM! MOMMY!\""
"This is a bad dream; it HAS to be!"
show ran c growl r with dis
gw "\"Stop snarling! You’re making it worse!\""
show vul eyeroll with dis
"The grey wolf snaps at his companion and then gets onto the bed, his chest hovering right above me."
show vul neutral x
show ran c embarrassed
with dis
"Being exposed like this makes me shout out even more, however his massive paw gently presses down on my face."
"Although he’s trying to silence me, this wolf is going about it differently than the previous one."
"His other paw reaches behind my head, holding me securely and gently ruffling my hair."
show ran c sad with dis
gw "\"Shhhhhh…\""
"His greenish eyes plead with mine, and I find his expression and demeanour almost soothing."
show ran c neutral t with dis
gw "\"Please, calm down.\""
show ran c neutral
show vul neutral x
with dis
"I notice he begins to match his breath with mine, his massive chest expanding in the same rhythm."
"He is guiding me down from the edge of panic, and for whatever reason I follow."
"All I want is to feel safe and somehow, he manages to make me feel just that."
"Slowly I let down my fight, my muffled voice getting fainter and fainter."
show ran c smile with dis
gw "\"That’s right…\""
"He encourages me."
show ran c talk with dis
gw "\"Nothing’s going to happen to you, I {i}promise{/i}.\""
gw "\"I’m going to let go, but you have to stop screaming.\""
show ran c smile with dis
"I look at him, wide-eyed."
"He speaks slowly at me, enunciating every word in an odd fashion."
show ran c embarrassed with dis
gw "\"If anyone finds out you’re here…\""
"He gestures with a clawed finger towards his neck, making an unmistakable slit mark."
"I guess he means I would be killed."
show ran c neutral with dis
gw "\"Do you understand?\""
"I don't, but am in no position to enquire further, so I simply close my eyes and take a deep breath."
show ran c smile e with dis
gw "\"Good.\""
show ran c talk with dis
gw "\"It’s ok…\""
"His voice is oddly comforting, as if I've heard it before."
gw "\"Let me fix this...\""
show ran c smile with dis
"My mind tells me to run, however my body is powerless."
"I must trust him; there is no other choice."
"Besides, if he wanted to hurt me, he would have done so already."
"He removes the paw from my face, his furry fingers brushing the cloth fastened around it."
"I can see his claws carefully prick at the rim."
show ran c serious with dis
gw "\"I will take this off, but you must {i}promise{/i} me that you won’t scream.\""
"My eyes tear up as I watch his massive jaw open in rhythm of his words."
"I think it only now sinks in that those beasts indeed talk."
show vul talk l
show ran c neutral r
with dis
bw "\"You can’t be serious!\""
show vul unhappy with dis
"The brute protests, looking at me with a murderous gaze, but the grey wolf ignores him."
show ran c smile with dis
"He looks expectantly at me, bringing a finger to his lips to emphasize that I need to stay quiet."
show ran c talk with dis
gw "\"Ok?\""
show ran c smile with dis
"I nod, closing my eyes."
show vul neutral with dis
"As he removes the cloth, pulling the bundle out of my mouth, I gasp in relief, tears flowing down my cheeks freely."
show ran c embarrassed blush with dis
"When I try to catch my breath, the grey wolf inspects the material with which I was gagged, looking back at his companion with a disgusted expression."
show ran c growl r paw with dis
gw "\"Is this my—\""
show vul eyeroll with dis
bw "\"Had to improvise.\""
"The black wolf shrugs."
show ran c bemused
show vul neutral x
with dis
"I can’t even contemplate the implication, as my mind begins to spin out of control."
m "\"What the fuck is going on?\""
show ran c shocked
show vul intrigued
with dis
"I ask myself in a pitiful squeak."
"The grey wolf looks to his companion."
show ran c neutral rt with dis
gw "\"What language is that? Vannar or Fhreyir?\""
show ran c neutral r
show vul talk l
with dis
bw "\"How should I know? I don’t speak human.\""
show vul neutral with dis
"What are they talking about? I understand them perfectly…"
show ran c growl r paw with dis
gw "\"Great. How are we going to explain this to him after you {i}brutalised{/i} the kid?\""
show vul growl with dis
bw "\"I was being gentle.\""
m "\"Explain what?\""
show vul shocked
show ran c shocked
with dis
"I ask them without even thinking what I’m doing."
"I notice both males looking at me wide-eyed, as if they've seen a ghost."
"For the first time, the black wolf shows an expression other than scorn."
m "\"What is going on?\""
show ran c neutral r
show vul neutral l
with dis
"The wolves briefly exchange gazes, looking back at me with the same surprise in their eyes."
show ran c shocked with dis
gw "\"W-What?\""
show ran c sad
show vul growl
with dis
bw "\"It speaks…\""
show ran c mutter r
show vul neutral
with dis
gw "\"It might be just a few words.\""
"The grey wolf shakes his head, looking to me for confirmation."
show ran c sad with dis
gw "\"Right?\""
"I don’t respond; my thoughts are spinning in complete confusion, and the grey wolf simply points to my legs."
show ran c awkward with dis
gw "\"Let’s get you untied, huh?\""
show vul growl with dis
bw "\"I wouldn’t do that.\""
show vul neutral x with dis
"I ignore the brute and hastily nod to the grey wolf, desperately wanting to get out of this awkward position."
show ran c worried rt with dis
gw "\"I need him to {i}trust{/i} us… how can he do that when he’s tied up like a prisoner?\""
"He works his fingers around the knot, cursing under his breath."
show ran c bemused with dis
gw "\"Fuck, did you have to make it this tight?\""
"The other wolf only shrugs."
"I can’t see much, but I feel the stinging of bruised skin as the rope finally loosens up."
show ran c smile with dis
gw "\"There we go.\""
"My legs stretch out almost on their own accord, the tension in my knees finally letting up."
"I sigh in relief; I didn’t think it was possible to feel so good just stretching out like this."
show ran c embarrassed with dis
gw "\"Right, I need to turn you on your back.\""
"He circles the air with his finger, letting me know what he intends to do."
"I just nod."
gw "\"Please don’t do anything—\""
show vul talk x with dis
bw "\"{i}Stupid{/i}.\""
show vul neutral x
show ran c neutral
with dis
"What could I possibly do with two monsters hulking over me?"
"I allow myself to be rolled over, and I feel as the grey wolf walks onto the bed and mounts my back."
"His voice is tinged with embarrassment as I grunt under his weight."
show ran c embarrassed with dis
gw "\"Sorry, just a precaution.\""
show ran c embarrassed e with dis
"He squats on my butt, his muscular legs to either side of my torso squeezing slightly to hold me fast."
"I guess he does not trust me to stay still."
"It takes him a while to undo the knot, but when he’s finally done, I feel the blood rush to my hands."
"I try to push myself up, to force some life into my numb limbs, but I feel a giant paw pressing against my naked back with leathery pads."
show ran c embarrassed with dis
gw "\"Don’t make me regret this.\""
show ran c neutral with dis
"He whispers the words into my ear, and his cautious tone completely throws me off."
"I’m not the dangerous one here!"
"Not wanting to startle him, I stay still until he gets off me, turning back to face them only when I feel his weight disappear."
show ran c smile with dis
"His paw slides off my back, but he keeps hovering above me, his form dwarfing mine."
"I’m calm enough to finally have a proper look at him: his fur is grey, but with slight brown tint to it."
"I rub my stinging wrists, tracing the red marks where the ropes held me."
"I do that more out of contemplation rather than actual pain."
"Everything is so confusing and absurd yet feels so real."
show ran c sad with dis
gw "\"You ok?\""
"Am I?"
"I adjust myself in bed, trying to rise slightly, so that the wolf man doesn’t hover above me in such an awkward fashion."
show ran c smile with dis
"His eyes are kind and show a caring person behind the mask of a wild beast—a stark contrast to his musculature and burly build."
"Not to mention his black companion."
"I am sitting in this strange room, surrounded by talking wolves."
"If this is not a dream, then I must be insane."
show ran c worried rt
show vul unhappy e
with dis
gw "\"Seriously, you did a number on the poor kid.\""
show ran c sad with dis
"The grey wolf eyes out my neck, causing me to immediately touch it."
"I wince in pain, drawing air through my teeth."
"My throat still hurts, and clearly doesn’t want to be touched."
show ran c growl r paw
show vul unhappy l
with dis
gw "\"Gaining his trust will take a {i}fucking{/i} miracle now…\""
"He throws an angry stare to the black male who simply raises a brow."
show vul growl lx with dis
bw "\"{i}His{/i} trust? What about us?\""
bw "\"He could be dangerous.\""
show ran c annoyed r paw
show vul eyeroll
with dis
gw "\"Don’t be ridiculous, he’s {i}tiny{/i} and obviously frightened.\""
show ran c confused paw
show vul unamused u
with dis
gw "\"How dangerous could he possibly be?\""
show ran c neutral
show vul neutral
with dis
"I’m not sure I’m frightened anymore; my emotions are running riot and I have no idea what I actually feel now."
"I just sit there, unsure what to do."
show ran c smile with dis
"The grey wolf’s demeanour is quite disarming, his kind eyes and soothing voice allow me to calm the torrent in my head ever so slightly."
"Between him and the black brute, he genuinely doesn’t seem to wish me harm."
show ran c sad with dis
"I resume rubbing my wrists and the grey wolf notices that, his big paw reaching out to them."
show ran c shocked
show vul intrigued
with dis
"As he is about to touch me, I clasp his paw with both hands and bringing it close to my face so that I can have a better look."
"It is soft to the touch, the fur kempt and having a vague scent of the forest."
show ran c neutral with dis
"I turn the paw to reveal its underside, with six distinct leathery pads; they are dark brown and surprisingly supple, more akin to skin than what I initially thought."
"I trace my finger from his palm up to the dull tip of his middle claw."
"This is so surreal."
show ran c neutral e with dis
"Before I let go of his paw, I ruffle the fur around his wrist, trying to find where there might be some sort of partition in the costume."
"I find nothing, gazing at the muzzle of the wolf, dumbfounded."
"Why would I even think it’s a costume?"
show ran c smile e relax with dis
"I can’t help myself but reach out and touch his chest, despite the fur, I can clearly see defined muscles."
"I carefully brush away a round necklace; it’s stone is white, but otherwise it looks similar to the one the black wolf wears."
"I sink my fingers into the fur and am immediately met with contrasting sensations: the softness of the coat and the rock-hard pecs beneath it."
show ran c embarrassed e relax with dis
"His chest expands heavily with each breath, while I move my hand from one breast to the other, completely mesmerised."
"He is so warm…"
"I can’t believe my senses; this can’t possibly be real."
show ran c awkward with dis
gw "\"Ekhem.\""
"He clears his throat, looking as confused, as I am."
show ran c smile with dis
"My eyes and hands drift to his snout, but I stop short from touching him."
show ran c shocked with dis
"He looks at me with slight surprise, but as he notices my hesitation, he pushes his muzzle into my open palm."
show ran c smile e with dis
"His nose is wet and warm, like I’d expect a wolf’s nose to be."
show vul talk lx with dis
bw "\"What are you doing? Don’t let-\""
show vul unhappy l
show ran c neutral rt paw
with dis
gw "\"I want him to feel at ease.\""
show vul eyeroll with dis
"The grey wolf extends his paw towards his companion in a calming manner, letting him know to leave me be."
show ran c smile
show vul neutral
with dis
"I am completely lost in my own thoughts as my hand wanders the length of his muzzle, all the way to his cheeks."
"I groom his side-fluff, realising how soft and pleasant the grey fur is."
"As I caress his face, he rests his head into my hands, looking almost cute and innocent."
show ran c smile e with dis
"I hear soft thumping of his tail against the bed; he’s enjoying my attention, but I’m not really petting him."
"I’m simply trying to convince myself that he is not an illusion."
"Finally, I venture lower, to his mouth, fuelled by this exploring frenzy."
"I almost touch his lips when I hear a soft growl from the black wolf."
show vul growl u with dis
bw "\"Careful now, he used to chew on his toys.\""
show ran c eyeroll
show vul growl x
with dis
"I blink, pulling my hand back."
show ran c neutral
show vul neutral x
with dis
"What am I doing?"
"I was about to foolishly stick my fingers into a wolf’s maw!"
show ran c smile with dis
"I grimace in discomfort, but the grey male simply smiles at me."
"Any thought of harm quickly disappears from my mind, but another troubling realization takes its place."
"He’s real."
show ran c shocked
show vul intrigued
with dis
m "\"You’re…a wolf.\""
show ran c smile e with dis
"I try to keep a straight face as I say those ridiculous words."
show ran c talk with dis
gw "\"Yes. And you’re a {i}human{/i}.\""
show ran c smile with dis
"He touches my shoulder with his paw, his words still annoyingly slow and steady."
"I finally realise what it is that bothers me about it; he talks to me as if I were either stupid or a child."
"And since I'm not a child..."
"Feeling patronised, I finally snap out of the stupor and brush his paw away."
show ran c shocked
show vul unhappy
with dis
m "\"Where the hell am I?! Who are you people?!\""
show ran neutral r
show vul neutral l
with dis
"The two wolves exchange confused looks, this time both their expressions turning."
show vul talk lx
show ran worried r
with dis
bw "\"That’s more than just a few words...\""
show vul unamused u with dis
"The brute is clearly upset that I can speak, and it only fuels my frustration."
show ran c sad with dis
gw "\"Can you… {i}understand{/i} us?\""
show ran c shocked with dis
m "\"Yes, {i}of course{/i} I can! What is this place?\""
show ran c embarrassed with dis
gw "\"This is my home.\""
m "\"Why am I here? Did you kidnap me?\""
show ran c shocked with dis
gw "\"W-What? NO! I found you—\""
show ran c worried r
show vul growl p
with dis
bw "\"How did it learn our language? There’s not a hint of accent, it’s as if it was born and raised here…\""
show vul growl x
show ran c sad
with dis
"The black wolf's inquisition into my linguistic skills finally piss me off."
show ran c shocked
show vul shocked
with dis
m "\"What are you talking about?! I’m not speaking your language; you are speaking mine!\""
show ran c doubtful with dis
gw "\"You were raised speaking Wolven?\""
show vul growl p with dis
bw "\"Yeah, right… Someone shaved his ugliest pup and abandoned it in the woods.\""
show ran c shocked
show vul neutral
with dis
m "\"Speak Wolven? As in what, growling and howling?\""
show ran c bemused with dis
"I am so confused."
"I cannot hear this 'Wolven' language they insist I’m using."
show ran c sad with dis
m "\"I don’t know what you two are talking about, but this is my language… Always has been.\""
show vul growl k
show ran c worried r
with dis
bw "\"You’re either a spy or a fucking lunatic!\""
show ran c shocked
show vul shocked
with dis
m "\"I’m neither, you {i}dumb{/i} beast!\""
show vul growl u
show ran c sad
with dis
"I spit out in anger, causing the black wolf to snarl viciously, his fur bristling."
"I quickly regret doing that, as I can see the black monster tense up, ready to give me another thrashing."
show ran c growl r
show vul eyeroll
with dis
gw "\"Shut up, both of you!\""
show ran c annoyed
show vul neutral x
with dis
"The grey wolf looks back to me with slight annoyance."
show ran c neutral t with dis
gw "\"I thought you said you can understand us.\""
gw "\"So which part of being {i}killed{/i} if discovered didn’t you get?!\""
show ran c annoyed with dis
"He gives me a stern look and I cool down a bit."
"Talking back to either of them is not the best idea."
gw "\"We need to keep quiet.\""
m "\"Why? What’s going on?\""
show vul growl x with dis
bw "\"You shouldn’t be here.\""
show vul neutral x
show ran c neutral t
with dis
gw "\"I’ll explain everything, but for the time being, please {i}trust{/i} me.\""
show ran c neutral with dis
"That feels like a stretch, however I don’t seem to have any other options."
m "\"Okay, fine.\""
show ran c smile
show vul intrigued
with dis
"I concede through a sigh."
m "\"But I don’t understand anything that’s going on here.\""
show vul talk with dis
bw "\"How are you speaking our language?\""
show vul neutral with dis
m "\"This language is what I know—what I’ve always known.\""
show ran c mutter paw with dis
gw "\"We heard you speak something {i}else{/i} though… I don’t know what you said, but it wasn’t Wolven.\""
show ran c neutral with dis
m "\"W-What?\""
"No, that’s not right."
"I don’t remember speaking or thinking in any other language."
show ran c embarrassed with dis
gw "\"I really need you to help me out here…\""
"The grey wolf looks at me worried, hastily sitting down on the bed and reaching for my hand."
"I flinch, startled by the beast’s movements and proximity, managing to retreat my hand before the paw lands on it."
show ran c sad with dis
"I cradle it near my chest, making the wolf aware I’m not ok with him touching me."
"I may be a little hypocritical, considering I took full liberty in touching him, but that thought quickly disappears with another bizarre question."
show ran c neutral t with dis
gw "\"Do you speak Tigerian, perhaps?\""
m "\"{i}Tigerian?{/i}\""
"I scoff, almost mocking the grey wolf."
m "\"As in tigers?\""
show ran c bemused with dis
m "\"You’re saying there's talking tigers out there?\""
"The wolf’s eyes wander off in annoyance, as if he wants me to just make my jaded point already."
m "\"What else? Elephants? Oooh! I bet their language is what? {i}Elephantine?{/i}\""
show vul unhappy e with dis
"I finally lose it and am unable to contain a chuckle."
show vul facepalm growl p
show ran c worried r
with dis
bw "\"The human is fluent in our language and even cracks jokes. This whole mess just went from bad to worse…\""
bw "\"What are we going to do now?\""
show ran c resigned
show vul growl
with dis
gw "\"I don’t know.\""
"My thoughts begin to wander off to the world outside of this room."
"Where the hell am I?"
show ran c worried r
show vul growl lx
with dis
bw "\"That’s exactly my point! You never think these things through. Your father will—\""
show ran c worried rt with dis
gw "\"He doesn’t have to know!\""
show ran c worried r with dis
bw "\"Have you also gone mad?\""
show vul growl p with dis
bw "\"Is that thing contagious?\""
show ran c neutral rt
show vul eyeroll
with dis
gw "\"At least for now, let’s keep my father out of it.\""
gw "\"I need to find a way to present this in the least controversial way.\""
show vul talk pl
show ran c neutral r
with dis
bw "\"How do you want to do that? Roll the human in honey and cover him with fur?\""
"What are they even talking about?"
show ran c eyeroll with dis
gw "\"Obviously not!\""
show ran c pouty
show vul growl lx
with dis
bw "\"No? That’s a relief because it’s not crazier than smuggling the human here in the first place!\""
show vul eyeroll with dis
bw "\"I don’t know why I allowed you to rope me into this.\""
"I just look between the two wolves arguing, still none the wiser."
show ran c shocked
show vul intrigued
with dis
m "\"Can someone {i}please{/i} explain to me what’s going on?\""
"I find myself barking out in annoyance."
"The grey wolf looks at me surprised, and then sighs."
show ran c embarrassed with dis
gw "\"I guess this is where we introduce ourselves.\""
"He straightens up, pumping up his chest."
show ran c smile e with dis
"It’s clear he’s trying to be presentable, as if it’ll makes any difference to me."
show vul facepalm with dis
bw "\"Ugh! Don't-\""
show ran c talk with dis
gw "\"My name is Ranok.\""
"He speaks slowly, deepening his voice like some guys do when they try to impress."
show ran c talk r paw
show vul facepalm e
with dis
r "\"And this is Vulgor.\""
"He notices my reluctant gaze towards the other wolf and laughs awkwardly, the self-important image dissipating almost instantly."
show ran c awkward hard
show vul neutral
with dis
r "\"Don’t mind him. Despite his demeanour he’s a good friend.\""
"A friend?"
show ran c shocked
show vul shocked
with dis
m "\"HE ALMOST KILLED ME!\""
"I shout out, glaring at the black male with hatred in my eyes, I can still see him hovering above me, choking me until I pass out."
show ran c embarrassed with dis
"Ranok frantically shushes me, pushing his finger against his lips."
show vul talk ang with dis
v "\"If I wanted you dead, do you think you’d still be here bitching about it, little piggy?\""
show vul growl x with dis
"A soft growl follows the wolf's words, but he cuts it off as Ranok gives him a stern look."
show ran c neutral rt
show vul eyeroll
with dis
r "\"What he did was a bit… {i}harsh{/i}, but in truth he saved your life.\""
show ran c neutral
show vul neutral x
with dis
m "\"What are you talking about? He nearly choked the life out of me!\""
show ran c sad with dis
r "\"If anyone would find you here, you would be killed.\""
"His voice tries to convey the gravity of the situation, but I’m at a loss."
m "\"You keep saying that, but don’t explain why!\""
r "\"We don’t allow otherkin into our forest. Trespassing is forbidden, and punishable by death.\""
m "\"What the hell are otherkin?\""
show vul talk ang with dis
v "\"You for one, little piggy.\""
show ran c neutral rt paw
show vul neutral
with dis
r "\"It is a term for any intelligent species other than your own. You’re an otherkin to us, just as we are otherkin to you.\""
show ran c neutral with dis
"I shake my head slightly, trying to comprehend what he's saying."
m "\"Hold on. You really mean that there are more talking beasts out there?\""
show vul eyeroll with dis
v "\"Either it’s kidding, or there’s something wrong with it.\""
show ran c neutral t
show vul neutral x
with dis
r "\"You don’t remember?\""
show ran c sad with dis
"The grey wolf looks at me pleadingly, as if asking to end whatever game I'm playing."
m "\"I think I would remember living in a world inhabited by talking animals.\""
show ran c annoyed with dis
"Ranok’s brow narrows, showing he has taken offense at my comment."
r "\"We’re as much talking animals as you are a talking chimp.\""
show vul growl x with dis
v "\"I’d say it looks more like a talking piece of would-be ham.\""
"Now I'm the one offended."
show vul unhappy x with dis
m "\"Stop calling me IT! I have a name!\""
show vul shocked
show ran c smile
with dis
r "\"Well… you didn’t give it to us.\""
show vul facepalm with dis
v "\"No, don’t ask its name!\""
show ran c smile
show vul unhappy
with dis
"Ranok huffs with a cheeky smile, allowing one fang to perk out."
"He’s making a good point and I decide to ignore the black wolf’s protests."
m "\"It’s…\""
$ mc = renpy.input("Wait, what is my name?")
$ mc = mc.strip()
if mc == "":
    m "\"I... don't remember.\""
    show ran c embarrassed with dis
    r "\"Well... we have to call you something.\""
    show vul growl with dis
    v "\"No we don't!\""
    "The black wolf growls in annoyance, but Ranok completely ignores it."
    show ran c think with dis
    r "\"How about a nickname?\""
    m "\"Ummm... sure, I guess.\""
    "The wolf looks at me intensly for a moment."
    show ran c smirk with dis
    r "\"Hmmm... how about Pink?\""
    "I furrow my brow, not even entertaining the idea."
    show ran c smile e with dis
    m "\"I'm {i}not{/i} pink.\""
    show ran c smile with dis
    "Ranok looks at me with a rather challenging smile."
    r "\"Caelan then...\""
    show ran c wink with dis
    "He winks and I roll my eyes; of course he's going to call me 'tiny'."
    show ran c smile with dis
    "Wait... how do I know it means tiny?"
    show vul facepalm growl p with dis
    v "\"No, don't name it!\""
    "Seeing Vulgor's annoyance makes me snicker and it seals the deal."
    $ mc="Caelan"
"And just like that, it rolls off my tongue."
show ran c shocked with dis
m "\"[mc].\""
show ran c smile with dis
"It’s strange to hear it out loud, but it also feels right."
show vul facepalm growl p with dis
v "\"Oh, for fuck’s sake!\""
show ran c talk e
show vul eyeroll
with dis
r "\"[mc], good. We’re getting somewhere.\""
show ran c smile with dis
"The grey wolf smiles, ruffling my hair."
"I consider swatting his paw away, but his kind expression convinces me to simply ignore his forwardness."
show vul talk l with dis
v "\"What we’re getting in, is some very deep shit.\""
"I flinch seeing the black wolf look at me with his cold eyes."
show vul growl k with dis
v "\"We need to kill it.\""
show ran c shocked with dis
"I freeze, seeing that the wolf is not joking."
show ran c growl r with dis
play sound "sfx/bed_jump.ogg"
with vpunch
r "\"WHAT?!\""
"Ranok jumps up to his feet, shielding me with his body, his reaction pushing me further into paralysis."
show vul growl p with dis
v "\"We need to get rid of this freak before anyone finds out! Sheltering an otherkin is one thing, but having it speak our language is {i}deadly{/i} serious.\""
show vul growl k with dis
v "\"We need to kill it.\""
r "\"We are NOT doing that!\""
"Ranok raises his voice, causing me to wince."
"Their bodies tense up, and I can see their every muscle straining."
show vul facepalm with dis
v "\"Ranok, be reasonable. There is no way you can spin this… We can be banished!\""
show vul growl kl behind ran with dis
show ran c growl hard with dis
r "\"I DON’T care!\""
"My heart skips a beat, as I hear Ranok issue a powerful snarl."
"I cannot see his expression, but I’m sure it mirrors that of the black male, who bares his fangs in a vicious, almost feral way."
"Both wolves hold their paws close to their chest, with fingers feathered out in anticipation."
v "\"I cannot stand by while you’re making the biggest mistake of your life!\""
r "\"This is NOT a mistake; this is my destiny! Verissa—\""
with vpunch
play sound "sfx/hit.ogg"
scene fight_1 with slow_dissolve
"Without a warning, Vulgor rushes my defender and they clash few steps away from the bed, heads butting and paws interlocking."
v "\"Verissa huffs incense and eats hallucinogenic mushrooms! She’s NOT speaking with our ancestors, you {i}know{/i} that!\""
"I cannot avert my gaze from this spectacle, partially because I’m frozen, but also because my life depends on the result."
"I half expect them to thrash about biting each other, but instead they stay locked like this."
r "\"What I {i}know{/i} is that Mother Moon guided me to this human, just like Verissa said she would.\""
v "\"She said you would find your purpose! The ceremony is just a tradition…\""
v "\"You were meant to reflect on life by observing falling leaves or a sunset, not to break our sacred laws for a fucking human!\""
"I hear their strained puffs as they wrestle with each other in place."
"Despite how vicious they sound, growling and snarling, I can see they’re not really fighting, but rather trying to overpower one another."
r "\"The human… spoke my name!\""
"Ranok struggles the words through a grunt as Vulgor twists his paws back, forcing the grey wolf to one knee."
"He is losing."
v "\"Has it occurred to you that since the human {i}speaks{/i} our language, he might have simply read it?\""
"What is he even talking about, where would I have read Ranok’s name?"
"I’ve never heard it before in my life!"
r "\"Vul, you are my Moon Brother… I {i}don’t{/i} want to fight you.\""
v "\"That is exactly WHY I have to fight you!\""
v "\"You’re about to fuck up our entire lives!\""
"Vulgor’s gaze drifts towards me, his red eyes piercing right through my flesh."
"He knows he will soon have his way."
"Their laboured snarls and growls begin to send me over the edge, and I know another panic attack is fast approaching."
scene bg black with dis
"I close my eyes, huddling myself and slowly rocking back and forth like a traumatised child."
"I don’t think anymore; I just want it all to stop."
m "\"STOP IT! PLEASE!\""
"Everything goes silent, as I cry out through tears."
m "\"JUST STOP!\""
r "\"[mc]!\""
with vpunch
play sound "sfx/bed_jump.ogg"
"The mattress jumps up as the wolf’s weight lands on it."
scene bg broom_day
show door
show ran c embarrassed at left
show vul growl behind ran at right
with dis
"I open my eyes to see the grey wolf splayed out in front of me."
"Vulgor must've used my cry as a distraction to throw Ranok back."
"I glare at the brute approaching us and without even thinking I shield Ranok with my own body."
m "\"Please, don’t fight over me! I don’t understand what I’ve done wrong!\""
show ran c sad with dis
r "\"You’ve done {i}nothing{/i} wrong.\""
show ran c neutral e with dis
"I feel Ranok embrace me, as he pulls me to the side, covering me with his flank and reversing our positions."
"Now he's the one protecting me."
show ran c growl hard with dis
"Ranok eyes the black male with wild determination and his muzzle twists in a warning snarl."
show vul neutral x behind ran with dis
"Vulgor stops, folding his arms and looking down at us with mild contempt, as I stay in the grey wolf’s embrace, clinging to his fur."
"I just want to be close to someone."
"Ranok readjusts us slightly, sitting up at the edge of the bed with me still pressed into his chest, my side resting in his lap."
show vul facepalm with dis
v "\"For fuck’s sake!\""
r "\"I won’t let you harm the human.\""
show ran c growl r with dis
"He hugs me tightly, issuing another protective growl."
"There is a moment of silence while I simply fall deeper and deeper into despair."
"Why is any of this happening to me?"
show vul eyeroll with dis
v "\"Nothing is ever easy with you, is it?\""
show vul neutral x with dis
"Vulgor makes a long, drawn-out sigh, as if releasing all the tension he's built up to this moment."
show ran c neutral rt with dis
r "\"I’m not like you. I don’t solve my problems through violence and killing.\""
show ran c annoyed r
show vul growl lx
with dis
v "\"Pity. You should try it sometime.\""
"Ranok allows me another moment of warmth, but then gently pushes me away from his chest."
show ran c neutral e
show vul neutral
with dis
"I just sit there, not really present, watching as he clumsily gets back up to his feet."
"The wolves are now standing side by side, almost as if nothing really happened."
show ran c talk with dis
r "\"It’s ok, we’re done fighting…\""
"He's trying to get me to compose myself, but I'm already far gone."
show ran c embarrassed with dis
r "\"I’m sorry you had to see that.\""
r "\"It's not exactly how I envisioned our introduction.\""
"I don’t understand what’s going on."
"Why am I here, and who are those monsters?"
"Why can’t I remember anything?"
show ran c shocked with dis
"Is this really the world I was born into?"
"If so, why does it feel so alien, as if my instincts are telling me this is NOT home?"
show ran c sad with dis
r "\"Shhhh… It’s ok.\""
"The grey wolf lowers himself to get closer, and I close my eyes, huddling tightly to the wall."
scene bg black with dis
play sound "sfx/heartbeat_fast.ogg" fadein 3.0
"My head throbs with a torrent of questions that slowly overwhelms me."
"I hug my knees, pressing them into my chest."
"The adrenaline rush pumped by my palpitating heart is the only reason why I don’t break up in tears."
"Everything is just a blur, and although I can still hear them, nothing really registers."
"Not consciously, at least."
v "\"Its heart is fluttering like a startled bird in a cage. Messes with my instincts.\""
stop sound fadeout 3.0
scene bg broom_day
show door
show ran c sad at left
show vul neutral at right
with dis
"I open my eyes, looking up at them as they stare me down intensely."
"It only empowers the erratic pounding in my chest."
"I can’t breathe…"
show vul talk p with dis
v "\"Yep, there it is. Undeniable 'go for the throat' feel.\""
show vul neutral x behind ran with dis
"The words stick out like a sore thumb, freezing me up in fear."
show ran c annoyed r paw with dis
r "\"Shut up!\""
show ran c neutral with dis
"The kind wolf snorts at his friend and hunches next to me, leaning in closer."
show ran c smile with dis
"He's obviously trying to comfort me, but I can't help but notice his fangs poking out."
show vul eyeroll with dis
v "\"Hmph. You feel it too, don’t deny it. I can see you’re all tensed up.\""
show ran c embarrassed
show vul intrigued
with dis
"That statement makes me notice how Ranok’s fur is standing up ever so slightly, his body barely containing some subconscious exhilaration."
show ran c shocked with dis
"I flinch away from his grey paw, but the wolf persists."
show ran c smile with dis
"I run out of room to recede into, as he gently takes hold of my chin and guides my gaze back towards his."
"I meet his docile smile with caution, the world still distorted by adrenaline haze."
show ran c talk with dis
r "\"Calm down… No one’s going to hurt you.\""
"I don’t feel that’s entirely true, recalling what the black wolf said just a moment ago."
show ran c shocked with dis
m "\"Go…for the…thro—\""
"I cut off, shielding my neck with a hand."
show ran c talk e with dis
r "\"Don’t listen to him. Your racing heart is just messing with our heads a little.\""
"He admits with slight embarrassment as his paw touches my shoulder."
show ran c smile with dis
r "\"Just an uneasy feeling. Nothing we would lose control over.\""
show ran c awkward with dis
r "\"I’m more worried you’re going to have a heart attack.\""
show ran c smile with dis
"The grey wolf squeezes my shoulder slightly, as if trying to pull me back from my fit of terror."
show ran c smile e
show vul eyeroll
with dis
"He then takes a long inhale, his nose close enough to draw strands of my hair in his direction."
r "\"Breathe in.\""
show vul neutral behind ran with dis
"He holds his breath for a moment and without realising, I do as he instructs."
show ran c talk with dis
r "\"And breathe out.\""
"I chuckle as a large huff of air brushes over me."
show ran c smile with dis
r "\"That’s it.\""
"My heart regains a bit of its rhythm."
"I am unsure how I feel about those beast-men's ability to sense my heartbeat, but for the moment it seems to allow Ranok to guide me back from the panic attack."
"His gestures and words somehow match my pulse, as he squeezes me gently with every thump inside my chest, almost as if giving cues to my startled heart."
"Finally I am back to normal, or at least a semblance of it."
"The wolf keeps a paw on my shoulder for a while longer, still squeezing in rhythm."
show ran c smile e with dis
r "\"Welcome back.\""
show ran c smile with dis
"He smiles again, certain I have calmed down."
"Only now does he let me go to face his comrade."
show ran c annoyed r paw with dis
r "\"I know it’s a {i}lot{/i} to ask of you, but could you stop freaking him out?\""
show vul eyeroll
show ran c annoyed r
with dis
"Vulgor grimaces, his arms still crossed as he drills his cold gaze into me."
show vul intrigued with dis
"I can’t help but flinch at the sight of him eyeing me out."
"To me he’s fear incarnate."
show ran c shocked
show vul talk pu
with dis
v "\"I think it’s too late for that.\""
show ran c resigned with dis
r "\"Look, I’ll fix this…\""
show ran c smile
show vul intrigued l behind ran
with dis
"Ranok draws my gaze towards him as he points to the white, round necklace on his chest."
show ran c smile hip with dis
r "\"See this? Those are our moonstones. Every wolf is given them at birth, to represent the phase of Aluna when we came to the world.\""
show ran c shocked with dis
m "\"Full moon…\""
show ran c smile e with dis
r "\"Yes.\""
"He smiles."
show ran c talk with dis
r "\"I was born during the full moon—an auspicious sign for sure. So was he, actually, just an hour earlier, which makes us Moon Brothers.\""
show ran c smile with dis
"I look to the similar necklace on Vulgor’s chest. "
"His stone, however, is black."
"For some unknown reason, it keeps unsettling me ever since I first saw it."
show ran c shocked with dis
m "\"Black stone…\""
show ran c neutral r with dis
"I say with a worried expression, almost as if repeating someone."
show ran c talk r paw with dis
r "\"Heh… He was born during an eclipse, something we call Darkmoon. These necklaces are the most valuable possession we have.\""
show vul talk l
show ran c shocked r
with dis
v "\"What are you doing?\""
show ran c mutter r
show vul neutral l
with dis
r "\"Explaining to him the significance, so that he can understand what I'm about to ask-.\""
show vul talk l
show ran c annoyed r
with dis
v "\"No.\""
show vul neutral with dis
"Whatever is being discussed is causing the black male a great deal of discomfort."
show ran c neutral rt with dis
r "\"Vul, I want you to swear—\""
show ran c neutral r
show vul growl kl
with dis
v "\"You’re fucking {i}insane{/i}! I won’t do it!\""
"The black wolf snarls, causing me to shudder."
r "\"Swear on your moonstone that you won’t harm [mc].\""
show vul growl u with dis
v "\"You want me do {i}that{/i} for a human?!\""
show ran c worried rt with dis
r "\"I want you to do it for {i}me{/i}, as your Moon Brother.\""
show ran c annoyed r with dis
"I dart my eyes between Ranok’s pleading expression and Vulgor gritting his teeth."
"This request causes him great deal of pain, I can see clearly that the wolf is not taking this lightly."
hide vul growl u with dis
"Without warning, Vulgor punches the wall next to the bed, causing me to yelp."
show ran c shocked r with dis
play sound "sfx/wall_punch.ogg"
with vpunch
"The entire house shakes as the plaster cracks, bits and pieces of it falling to the ground."
show ran c worried r
show vul facepalm growl at right
with dis
v "\"Argh, this is fucking bullshit!\""
show vul growl with dis
"I wouldn’t want to be on receiving end of that punch; the strength of this beast made perfectly clear."
"He wasn't bluffing when he claimed he was being 'gentle' with me..."
"He could snap me like a twig."
show ran c worried rt with dis
r "\"Vul, please.\""
show ran c worried r with dis
"The black wolf’s rattled breath fills the room for a few moments as the growl deep inside his chest begins to subside."
show vul unhappy e with dis
"Finally, he releases a long-drawn sigh and looks at Ranok, fully composed."
show vul unhappy x with dis
"His red eyes drift to me, and I can see his massive paw touch the rims of his black necklace."
show vul talk p with dis
v "\"On my moonstone, I swear I won’t harm your little Piglet.\""
show vul neutral
show ran c smile r
with dis
r "\"Thank you.\""
show ran c smile with dis
"The grey wolf turns to face me with a smile."
r "\"See?\""
show ran c talk with dis
r "\"He will {i}never{/i} harm you again; you can be certain of it.\""
r "\"He might be cynical, and a bit rough around the edges, but he’s the most {i}honourable{/i} wolf I know.\""
show ran c smile with dis
"I do actually believe him; I could see that getting the promise out of the black wolf was not easy."
"Regardless, I will still feel anxious around him but at least I know there is no immediate danger."
show ran c worried r
show vul talk l
with dis
v "\"Your father will not swallow this lightly. We’re looking at an exile.\""
show ran c worried rt
show vul neutral
with dis
r "\"If my father hasn't banished me so far, I doubt {i}this{/i} will make any difference.\""
r "\"And if it does, I've had it {i}long{/i} coming.\""
show ran c neutral r with dis
"Sounds like Ranok gets in trouble a lot."
"I’m not sure if his self-awareness should be commended or not, considering he keeps causing more trouble."
"Then again, in this instance I'm glad as so far it seems he saved my life..."
"Somehow."
show vul talk p with dis
v "\"Are you really willing to risk everything over this… puny human?\""
show ran c neutral rt
show vul neutral
with dis
r "\"The spirits wanted me to find him.\""
show vul eyeroll with dis
"I can see Vulgor roll his eyes."
show ran c smile with dis
r "\"Now that we know he {i}speaks{/i} our language; I am more certain of it than before.\""
"He looks at me with a hopeful smile, his voice filled with conviction."
show vul talk x with dis
v "\"What would our ancestors even want with a human whelp?\""
show vul neutral x with dis
"Good question."
show ran c neutral rt with dis
r "\"I don’t know. But all will be revealed in time.\""
"I still don’t understand how I fall into all of this."
show ran c neutral with dis
m "\"You said that you found me.\""
m "\"Where? How?\""
show ran c sad with dis
"Ranok regards me with worry, uncertain if he should reveal it or not."
"That’s when Vulgor spares him the dilemma."
show vul talk x
show ran c shocked r
with dis
v "\"He found you in our forest, some distance from our village.\""
show vul neutral x
show ran c neutral
with dis
"I nod to the black wolf in appreciation."
m "\"You mentioned some sort of a ceremony that sent you there...\""
"I look to Ranok expectantly."
show ran c neutral t with dis
r "\"It was my coming-of-age. I was to receive guidance from the Ancestors, to find my path.\""
show ran c bemused
show vul facepalm
with dis
v "\"And the fool mistook you for it.\""
"The black wolf sneers while Ranok looks away, slightly embarrassed."
show vul neutral
show ran c embarrassed
with dis
m "\"What does that mean?\""
"The grey wolf seems troubled, and it makes me think that his previous confidence was completely unfounded."
"However, he quickly looks back at me with a smile on his muzzle."
show ran c smile e with dis
r "\"Don’t worry about that now.\""
"That’s a non-answer."
show ran c talk with dis
r "\"Just know that our fates are intertwined. The spirits have charged me with protecting you."
r "\"You speaking our language only proves that us crossing paths during my ceremony was {i}not{/i} a coincidence.\""
show vul talk l
show ran c bemused
with dis
v "\"For you, hardly anything is.\""
show vul neutral
show ran c neutral e
with dis
"Cynical as Vulgor may be, I can see his point."
"Ranok is clearly into the idea of this whole mess being fated, but whatever his beliefs are, signs can always be misinterpreted."
"I am not a path, whatever that means."
"I don’t even know who I am."
"What could I possibly have to do with that wolf’s fate?"
show ran c shocked
show vul intrigued
with dis
m "\"Am I really speaking your…\""
show ran c embarrassed
with dis
"I pause for a moment, still not understanding the implication."
m "\"…your language?\""
"Am I barking and growling without even realising?"
"Have I gone completely mad?"
show vul talk ang with dis
v "\"You really don’t hear it?\""
show vul worried with dis
"The black wolf's expression shows that he finally starts to believe me."
m "\"No, it’s…as natural to me as if I were born into it.\""
show ran c awkward with dis
r "\"Surely you know your {i}own{/i} language.\""
"The grey wolf smiles awkwardly, almost as if begging me to really think about it."
"But this is my own language."
show ran c talk with dis
r "\"You must speak human—whatever dialect you call it back home.\""
show ran c shocked
show vul intrigued
with dis
m "\"This…is human—\""
show ran c sad with dis
"I cut off, trying to really contextualise the words I’m using."
m "\"Isn’t it?\""
"Ranok shakes his head."
show ran c neutral e with dis
r "\"You’re confused… which is to be expected after what you've been through.\""
m "\"I—\""
show ran c neutral with dis
"None of this makes any sense."
"Despite my mind being wiped clean, I know that talking beasts aren’t normal."
"I know this isn’t my home."
"A terrible feeling of being lost fills me, and my heart sinks."
show ran c shocked with dis
m "\"I want to go home.\""
"Ranok’s ears perk up."
show ran c talk with dis
r "\"Fine. That's exactly where I intend to take you.\""
r "\"Just tell me where it is and once you’ve rested; we’ll be on our way.\""
show ran c smile with dis
"He smiles, and his tone tells me he genuinely means to do just that."
"But where is my home?"
show ran c neutral with dis
m "\"I… don’t know.\""
m "\"I don’t remember.\""
show ran c sad
show vul neutral
with dis
"The answer clearly unsettles Ranok, as he frowns with worry."
"Nothing comes to me when I try to think about anything before waking up here."
"My mind is just one empty void, and the more I try to explore it, the more uneasy I feel as if something unpleasant lurked in the shadows."
"Finally, Vulgor breaks the silence, looking at me intently."
show vul talk p with dis
v "\"What were you doing in our woods?\""
show vul neutral with dis
m "\"I don’t know.\""
"I don’t even remember being in the woods to begin with."
show vul growl p
show ran c worried r
with dis
v "\"There’s something you’re not telling us!\""
m "\"I have told you everything!\""
show vul growl x with dis
"Why can’t he see that I’m the one in distress?"
"Regardless of what trouble they claim they've gotten themselves into, I am the one lost and completely baffled by my own existence."
"But I can see the black wolf isn’t satisfied, his red eyes looking at me with distrust."
"I finally snap."
show ran c sad
show vul shocked x
with dis
m "\"I don’t know what happened to me. All I remember is waking up in this {i}fucking{/i} room and then you {i}attacking{/i} me!\""
show vul growl u with dis
v "\"You were squealing like a dying pig. I had to shut you up, otherwise we’d be discovered!\""
show vul shocked x with dis
m "\"You should’ve {i}explained{/i} that to me!\""
show vul talk ang with dis
v "\"I didn’t know you spoke our language. And even if I did, you really think you would listen?\""
show vul growl behind ran
show ran c annoyed r
with dis
v "\"I know when I see prey fighting for its life. You were far gone the moment you laid your eyes on me.\""
"His tone is very much like mine: fed up and betraying a hint of hurt."
"Before we can escalate our argument, Ranok steps between us."
show ran c growl r paw with dis
r "\"Enough! This is getting us nowhere.\""
show vul talk pl with dis
v "\"We don’t know who this human is or where he comes from—\""
show vul neutral
show ran c neutral
with dis
m "\"I don’t know that either!\""
m "\"I mean, talking wolves? What is all this?\""
"I throw my arms out in resignation."
"This is complete and utter nonsense."
"Why can’t they see I have nothing to gain from this?"
show vul intrigued with dis
"I lock my eyes with Vulgor, who’s the only one treating me like some sort of a wildcard."
"I arch my brows upwards, eyes getting glossy despite my efforts to not get emotional."
m "\"You’ve hurt me, you wanted to {i}kill{/i} me…\""
show vul unhappy with dis
m "\"How can you think I asked for any of this?\""
show vul unhappy e with dis
"The black wolf’s expression softens, almost as if for the first time he considered putting himself in my shoes."
"Eventually he turns his gaze away with a deep sigh."
show vul talk pl with dis
v "\"The human obviously suffered some sort of trauma.\""
show vul neutral x
show ran c bemused r
with dis
r "\"Yes, you {i}choking{/i} him certainly could be called that.\""
"Ranok scoffs in annoyance."
show vul intrigued
show ran c shocked
with dis
m "\"No.\""
"I shake my head."
show ran c neutral
show vul smile
with dis
m "\"I mean YES, that {i}is{/i} going to stay with me for a while, but…\""
m "\"I didn’t remember anything before he attacked me.\""
show vul intrigued with dis
"As traumatic as the encounter was, my problems started much, much earlier."
"I shudder, sensing some sort of darkness deep in the recesses of my memory almost preventing me from digging any deeper."
"It’s almost as if that darkness consumed all that made up who I was."
"There are no memories of anything before this day."
m "\"I can’t remember my parents, or friends…\""
"I feel warmth trickling down my cheeks, as I realise, I might as well be an orphan."
m "\"I can’t even remember a single other human.\""
m "\"I… I know I am one, but—\""
"I cannot even picture it…"
"What do I even look like?"
"I regard my hands and feet, then glance around the room."
show ran c shocked with dis
m "\"Do you have a mirror?\""
show vul neutral with dis
"Only after asking do I realise I know what a mirror is."
"My memory loss seems to be very selective and restricted to anything directly linked to my past."
show vul intrigued with dis
"Vulgor looks at me with one brow risen, while Ranok smiles apologetically."
show ran c sad at left with dis
r "\"Sorry… I don’t have such luxuries.\""
"Luxuries?"
"Despite lacking any context, I know that mirrors aren’t that."
show vul eyeroll behind ran
show ran c shocked
with dis
play sound "sfx/knife.ogg"
"That’s when I hear a metallic cling."
show ran annoyed r with dis
"Both me and Ranok gaze towards Vulgor, who has unsheathed a long dagger."
show vul neutral
show ran c growl hard
with dis
"He approaches us casually, while I see Ranok’s hackles raising."
scene bg black with dis
play music "music/entity.ogg" fadein 3.0
"Suddenly everything goes black for a moment, and time freezes."
"A faint whisper fills my mind… I don’t know where it’s coming from, and I don’t recognize it either."
ow "\"His blade will taste your flesh…\""
"Although it penetrates my very soul with cold fear, my heart almost yells at me not to listen."
scene bg broom_day
show door
stop music fadeout 3.0
play ambience "ambience/birds.ogg" fadein 6.0
show ran c growl hard at left
show vul intrigued behind ran at right
with dis
"Is it a warning, or is my frightened mind playing tricks on me?"
"Vulgor wouldn’t hurt me after he made that promise, would he?"
menu:
    "Trust Vulgor":
        $ Vulgor += 1
        "The grey male issues a warning growl towards his friend, but I find myself placing a hand on the back of his neck."
        show ran c shocked with dis
        "The wolf twitches at the sensation, looking at me inquisitively."
        show ran c sad with dis
        "Although it feels counterintuitive, I rub his fur, letting him know that everything is fine."
        m "\"It’s ok…\""
        show vul neutral with dis
        "I trust the black wolf."
        "Despite my initial knee-jerk reaction, I realise what he wants to do."
        scene blade with slow_dissolve
        "And just like that, Vulgor kneels next to the bed, presenting me with the dagger resting across both his paws."
        "It is clear he takes great pride in it, as it is polished to perfection, the glistening surface reflecting my image without a blemish."
        "I reach to his paws, not to pick up the blade—I trust the wolf to keep it steady—but to adjust the angle so that I can see myself clearer."
        "I touch my lips, tracing them slowly as my eyes follow the mirrored gesture on the metallic surface."
        "I feel up my cheek bones, then touch the tip of my nose; eyes fixed on the reflection."
        "I ruffle my hair, pulling at stray strands of my fringe, pretty much exploring myself in the same fashion I was exploring Ranok earlier."
        "Without even noticing it, I've begun weeping again."
        "Two streaks of tears cut through my image, clearly visible in the blade."
        "A strange sensation twists my stomach, as if I am seeing myself for the first time."
        "My reflection is both strange and so familiar…"
        "I am human."
        "This is what humans are."
        scene bg broom_day
        show door
        show ran c sad at left
        show vul talk l at right
        with dis
        v "\"This is serious, Ranok.\""
        show vul neutral with dis
        "The black wolf says with a grim tone."
        "Not that he had any semblance of levity before, but at least now he’s not being insulting."
        "For the first time, I can see him looking at me with an actual concern."
        "Vulgor stands up, sheathing his blade back behind his belt and looking to his friend."
    "Trust the Whisper":

        "Try as I might, I cannot bring myself to trust him... not after what he did!"
        "I huddle behind Ranok, letting him know I don't want the black male anywhere near me."
        "The grey wolf issues a warning growl towards his friend, reaching behind to comfort me."
        show vul unhappy with dis
        "The ominous whisper rattled me enough to cause my eyes to well up in panic."
        "Seeing this, Vulgor stops in his tracks and sheaths back his knife, looking down at us with visible disappointment."
        show vul talk
        show ran c shocked r
        with dis
        v "\"I was going to let the Piglet use my knife as a mirror.\""
        show ran c annoyed r
        show vul unhappy
        with dis
        r "\"Well, you can’t blame him for being rather weary.\""
        v "\"I know.\""
        show vul growl kl with dis
        v "\"You on the other hand...\""
        "The black wolf lets the words hang in the air, regarding his friend with narrowed eyes, he’s clearly hurt by Ranok's caution."
        show ran c worried r
        show vul growl p
        with dis
        v "\"So much for making me swear on the moonstone.\""
        "I feel Ranok slump a little, as his ears fold back, I cannot help but feel as if I just unintentionally caused a rift between the two."
        show ran c worried rt with dis
        r "\"Vul…\""
        v "\"Doesn’t matter.\""
        show ran c sad
        show vul eyeroll
        with dis
        "The black wolf shrugs, his attitude once again cold and uncaring."

show vul eyeroll
show ran c worried r
with dis
v "\"If you insist on this foolishness, we should bring Verissa in.\""
show vul neutral with dis
"Ranok remains silent for a moment, as if weighing his options."
"I pull myself together, rubbing away stray tears."
show ran c neutral with dis
m "\"Who’s Verissa?\""
show vul talk with dis
v "\"The tribe’s shaman.\""
show vul neutral
show ran c talk
with dis
r "\"She’s both a spiritual guide and a healer.\""
show ran c smile with dis
"I'm glad the grey wolf clarifies that, because despite being vaguely familiar with the word, I am not sure what it fully entails."
m "\"Well, you said she’s the one who sent you into the woods.\""
show ran shocked with dis
m "\"Besides, she could help with my memory loss.\""
m "\"I don't exactly feel myself since I've woken up...\""
show ran c sad with dis
"I realise that if there is someone here who could give me medical attention, I’d rather have them check me up."
"Despite Ranok’s best intentions, he’s clearly conflicted about something, and as calming and reassuring as he tries to be, he’s no medic."

if Vulgor == 1:
    show vul smile u with dis
    "Vulgor looks at me with a smile in understanding."
    v "\"At least the Piglet can see some reason.\""
else:

    show vul unhappy with dis
    "Vulgor looks to me and nods in understanding."
    v "\"Even the human can see reason.\""

show vul neutral behind ran
show ran c neutral
with dis
"What I want to see is an end to this emotional rollercoaster."
"Rollercoaster…"
"Those words that come to my mind…"
"They make no sense, but at the same time, I understand them."
"I shake my head in frustration."
"What is going on?"
show ran c worried rt paw with dis
r "\"What if she doesn’t see it the way I do?\""
show vul eyeroll
show ran c worried r
with dis
v "\"If you claim this is what was meant to be, Verissa is as much a part of it as you are.\""
show vul talk p
show ran c pouty
with dis
v "\"Besides, without her help we’re already fucked.\""
show vul neutral with dis
"That’s when my eyes drift to the black wolf, brows risen in confusion."
show ran c neutral with dis
m "\"You keep saying ‘we’, but if it’s Ranok who found me, how did you get involved?\""
"I’m not suspicious or accusatory—simply curious."
show vul talk ang
show ran c worried r
with dis
v "\"I went looking for the fool when he was gone too long.\""
m "\"Don’t spiritual journeys take long?\""
show vul facepalm with dis
"The black wolf covers his eyes in annoyance."
show vul facepalm growl with dis
v "\"It’s {i}just{/i} a tradition. You’re told to go into the woods, find a rabbit eating moss, and realize we’re all connected or some other crap.\""
"Vulgor nearly snarls in annoyance."
"I can sense he’s not the one to believe in superstitions, and I find myself agreeing."
show vul neutral at right with dis
v "\"When it took him an entire night to return, I decided to look for him. And there he was, fiddling with a naked mole rat.\""
m "\"If you hate me so much, why didn’t you just turn us in?\""

if Vulgor == 1:
    show vul shocked with dis
    "Vulgor’s eyes widen as he looks at me with surprise, but only for a moment before he composes himself again."
    show vul talk ang with dis
    v "\"I don’t {i}hate{/i} you, Piglet. You just happened to be in the wrong place at a wrong time. Besides, Ranok is my Moon Brother; I would never betray him.\""
    show vul shocked with dis
    m "\"Then you’re a good friend.\""
    show vul unhappy e with dis
    "Vulgor nods, as if me saying it has made it any more valid."
    show vul talk lx with dis
    show ran c embarrassed with dis
    v "\"Every time he gets into trouble, I have to be there to save his furry ass!\""
    show vul neutral x with dis
    "I look up towards Ranok with a slightly amused smile, noticing the wolf’s embarrassment."
    m "\"Does he often find strange creatures in the woods?\""
    "I don’t know why I'm trying to break the tension, but both of the wolves look at me with surprise."
    "We laugh it off."
    show vul amused
    show ran c bemused
    with dis
    v "\"No, this is a first. His ultimate fuckup.\""
    "The black male jabs, but this time in a playful manner."
    show vul intrigued
    show ran c shocked
    with dis
    m "\"No.\""
    "I smile but find myself disagreeing with the big wolf."
    show ran c smile with dis
    m "\"He saved a life. That’s not a mistake.\""
    "Whatever happened to me, if I weren’t found, I would surely have died."
    "If not from exposure, then some animal would have done it."
    "I chuckle at the absurdity; a thought of a wild wolf comes immediately to my mind, the beast simply eating me alive while I’m unconscious."
    "Yet here I am because a wolf-man rescued me."
    show ran c smile e with dis
    m "\"Had he not found me, I would most likely be dead by now.\""
    show vul unhappy with dis
    v "\"Most likely.\""
    "The black wolf tries to shrug indifferently, but there's almost a hint of discomfort in his voice."
    show ran c shocked with dis
    "I look up at Ranok, touching his paw."
    m "\"Thank you.\""
    show ran c smile with dis
    "I place all the gratitude into those words I can muster."
    "The wolf smiles, closing his eyes and nodding."
    show vul intrigued with dis
    m "\"Both of you.\""
    "I smile at Vulgor, to which he only shrugs."
    show vul unhappy with dis
    v "\"Hmph.\""
    "He looks away, but I can see his tail give an idle flick."
    show ran c talk r with dis
    r "\"Bring Verissa.\""
    show ran c smile r with dis
    "The black wolf nods in satisfaction and leaves the room."
    hide vul unhappy with dis
    v "\"Be careful though; that sneaky Piglet is quite proficient with combs.\""
    play sound "sfx/door close.ogg"
    show ran c shocked
    hide door
    with dis
    "I almost choke on a chuckle, completely thrown off by the remark."
    show ran c confused with dis
    r "\"Combs?\""
    "Ranok looks at me expectantly, clearly feeling left out from our inside joke."
    show ran c neutral with dis
    m "\"Never mind.\""
    "I wave him away."
    "As good as the joke was in the moment, I don’t want to relive my first encounter with Vulgor just yet."
else:

    show ran c shocked
    show vul intrigued
    with dis
    "My question catches Vulgor’s by surprise as his eyes widen for a moment."
    show vul growl
    show ran c annoyed r
    with dis
    v "\"I have a sense of honour, something you clearly have {i}no{/i} idea about…\""
    show ran c worried r with dis
    v "\"I would {i}never{/i} betray Ranok.\""
    "He issues a stifled growl, sounding almost indignant."
    show vul growl k with dis
    v "\"I tried to convince him to leave you where he found you, but he wouldn’t listen.\""
    m "\"Had he left me there, I would most likely be dead now.\""
    show vul neutral
    show ran c sad
    with dis
    "Whatever happened to me, if I was not found, I would surely have died."
    "If not from exposure, then some animal would have done it."
    show vul unhappy e with dis
    v "\"Probably.\""
    "The black male shrugs indifferently."
    "I look up at Ranok, placing my hand on top of his paw."
    show ran c shocked with dis
    "Clearly he’s the only one I owe my life to."
    m "\"Thank you.\""
    show ran c smile e with dis
    "I place all the gratitude I can muster into those words, causing the wolf to smile."
    show ran c talk r
    show vul neutral
    with dis
    r "\"Bring Verissa.\""
    "Ranok nods to his friend."
    "The black wolf sighs in resignation and leaves the room."
    play sound "sfx/door close.ogg"
    hide vul
    hide door
    with dis

show ran c smile at center with move
play music "music/morning.ogg" fadein 6.0
"With the black wolf gone, an awkward silence falls over the room, but I don't mind..."
"Somehow this grey wolf makes me feel safe and at ease."
"I sit quietly on the bed, looking at the bright afternoon outside the window, anxiously kneading the sheets."
"Ranok keeps standing in his spot, not moving or saying anything."
"I can feel his gaze drill into me, as he carefully inspects every inch of my body with a rather odd smile."
m "\"What?\""
show ran c shocked with dis
r "\"What ‘what’?\""
m "\"You keep staring at me.\""
"Being called out, Ranok turns his gaze to the side in embarrassment."
show ran c pouty with dis
r "\"Well, I’ve never seen a human before.\""
m "\"Didn’t you get a pretty good look when you found me?\""
"He still avoids facing me, the inside of his ears growing red."
show ran c embarrassed with dis
r "\"N-no! You were unconscious!\""
show ran c embarrassed blush with dis
r "\"I only did what I had to save you!\""
"I chuckle at his troubled reaction."
"I guess he took it the wrong way."
m "\"If you’ve never seen a human before, how did you know I was one?\""
show ran c annoyed with dis
r "\"Well… we have stories.\""
m "\"Of humans?\""
show ran c talk e with dis
r "\"Among many others.\""
show ran c think with dis
r "\"We know you have pink skin, almost no fur aside from the head. That sort of stuff.\""
"I roll my eyes."
m "\"Beige.\""
show ran c shocked with dis
r "\"Huh?\""
show ran c neutral with dis
m "\"My skin is beige.\""
m "\"I’d have to stay out in the sun for quite a while to become ‘pink’.\""
m "\"And humans can have a much darker complexion as well.\""
show ran c smile with dis
r "\"Heh, is that so?\""
show ran c smirk shrug with dis
r "\"I guess we just haven’t dealt with those in the past.\""
show ran c smile with dis
"Ranok grins and we enter another awkward silence."
show ran c smile r with dis
"The bright sun and distinctive smell of flowers make me think of spring, although that doesn’t seem quite right to me."
"It’s almost as if the seasons got mixed up somehow."
show ran c smile re with dis
"However, cool air brushing over my naked body convinces me beyond doubt that it is indeed spring."
"I shiver slightly, reminded that I’m not wearing any clothes."
m "\"Why am I-\""
"I look down at my strange loincloth."
m "\"Almost naked? Where are my clothes?\""
show ran c shocked with dis
r "\"I found you how the Mother Moon made you.\""
m "\"And this?\""
"I point to the material covering my groin."
show ran c embarrassed blush with dis
r "\"I’ve put that on for… obvious reasons.\""
m "\"Right…\""
show ran c pouty with dis
"My eyes widen in realisation that this wolf had not only seen me naked, but also put on me what just as well could've been a diaper."
"I feel my face burning red, heat rising to my cheeks."
m "\"Thank you.\""
"I blurt out awkwardly."
"I can see the wolf pick up on my train of thought, as he looks to the side with his ears folded back, but he quickly regains his composure."
show ran c smile with dis
r "\"You’re welcome.\""
"As much as I want to change the subject, I need to make sure I understand what he meant."
m "\"So… I was passed out in the woods… butt naked.\""
show ran c embarrassed with dis
r "\"Pretty much.\""
"He shrugs, clearly as uncomfortable with the topic as I am."
"I’m not sure why, it’s not like he was the one whisked away in the nude by a strapping wolf-man."
"This is some first-class damsel in distress crap."
m "\"Weird.\""
show ran c awkward hard with dis
r "\"Yeah.\""
show ran c smile r with dis
"The wolf sits down on the bed, leaving some distance between us."
"We avoid looking at each other, although we both sneak a peek from time to time."
"I can’t understand what I was doing naked in the forest, it just doesn’t sound like something I would do."
show ran c smile re with dis
"It had to be someone else who did this to me and it’s an unsettling thought."
"Was I kidnapped?"
"Mugged and left for dead?"
show ran c smile r with dis
"Or maybe drugged and taken into the woods to…"
"No!"
"I shake my head."
"I don't even want to entertain THAT idea."
"However, I cannot help but wonder how I ended up there."
"And where’s my home?"
"I must have a family somewhere, someone who loves and cares about me."
"Someone who would be searching for me…"
"But… nothing comes to my mind, only this wolf."
"Without him I would be completely alone here and that's terrifying."
show ran c smile re with dis
"I can hear his tail swish across the linen; he’s either nervous or excited."
"His paw slides slowly across the bedding towards my leg."
show ran c smirk re with dis
"I try not to notice, curious what is he up to, until he pricks me with his dull claw."
m "\"What are you doing?\""
show ran c shocked with dis
"I scoff in amusement."
show ran c embarrassed blush with dis
r "\"Sorry… this is all new to me. I’m simply curious.\""
r "\"Didn’t mean any offense.\""
"He fidgets with his fingers, looking innocently at the window."
show ran c shocked blush with dis
m "\"No… it’s fine, I guess.\""
m "\"Seems only fair after I felt you up.\""
show ran c smirk with dis
r "\"Yeah… you took some liberties.\""
show ran c smile re with dis
"He smirks, giving me a side-eye."
m "\"Ok, then.\""
"I decide to move closer to him, pushing out my chest with a challenging smile."
m "\"Let’s get even.\""
"I gently tease him, watching him closely all the while."
show ran c shocked with dis
"Ranok looks at me with surprise in his eyes, but quickly smiles back, his tail wagging in obvious joy."
show ran c embarrassed blush with dis
"He slowly reaches out his paw, hesitant to touch me outright."
"I think he doesn’t want to come off as too eager and I smirk, tilting my head a little in a ‘really?’ expression."
show ran c smirk with dis
"He scoffs and finally musters the courage to make contact, touching my chest with his warm pads."
show ran c smile e with dis
"I look down at his paw and can’t help but feel amazed."
"It easily covers both my breasts, really driving home how tiny I am compared to this guy."
"Ranok rubs me gently for a moment and then moves his paw up to my shoulder."
show ran c smile with dis
"It tickles, but I try to maintain my composure; being touched like this is weird enough without me making it even weirder with girly giggles."
"If I’m really the first human he’s ever met, then I know perfectly well how confusing and mesmerising this has to be for him."
"After all, I lived through the same experience just a few moments ago."
show ran c talk with dis
r "\"You’re quite something…\""
show ran c smile with dis
"He mutters, sliding his fingertips along my arm."
show ran c talk e with dis
r "\"…soft and fragile… your skin almost like parchment.\""
show ran c smile with dis
"I furrow my brows at the comparison, but then again… I guess it’s true."
"And compared to them, I am quite fragile."
r "\"Aren’t you cold?\""
"He asks absentmindedly, while brushing his paw across my side."
"Another ticklish cramp shoots through my body and I can no longer reign in my instincts; I twist with a hearty laugh, pushing his paw away."
m "\"Stop! That tickles…\""
show ran c shocked with dis
r "\"Oh?\""
"He gasps in amusement."
show ran c smile e with dis
r "\"Good to know.\""
m "\"But yeah… I’m quite cold, actually. Do you have any shirts I could borrow?\""
show ran c embarrassed shrug with dis
r "\"Ummm…\""
show ran c awkward with dis
"Ranok grins awkwardly, pointing to his furry body."
m "\"Right… I guess you have no need for any.\""
r "\"The only thing I could offer is my spare gambeson, but I doubt it would be comfortable.\""
"He points to his padded quilt and I have to agree."
m "\"I’m not sure how I would even wear that… I just need to cover my top really.\""
"I sigh, looking around for something else to cover myself with."
show ran c shocked with dis
"I settle for one of the blankets that lays on the bed, tugging at it."
show ran c smile e with dis
"Ranok stands up for a moment, allowing me to pull it out from underneath him."
"I wrap it around myself almost like a poncho, shielding my body from the draft."
show ran c smile with dis
m "\"So… what do we do now?\""
"I ask, looking at the wolf with a risen brow."
show ran c talk with dis
r "\"We could talk, get to know each other-\""
"I shake my head."
m "\"I meant this whole mess we found ourselves in.\""
show ran c smile e paw with dis
r "\"Ah.\""
show ran c talk paw with dis
r "\"Well, I think I’m responsible for returning you back to your people.\""
show ran c shocked with dis
m "\"Whoever they may be.\""
"I shrug, knowing full well I have no idea where I would even return to."
show ran c embarrassed with dis
"None of this feels right."
"Even if it seems fairly real, I have a nagging feeling that I don’t belong here."
"Almost as if it were just a dream, something I just need to ride out until I finally wake up."
show ran c awkward with dis
r "\"Your memories will return in time, I’m sure of it.\""
"Well, I’m not."
show ran c wink with dis
r "\"In the meantime, I just need to protect you.\""
m "\"From what you two said earlier that might be easier said than done.\""
show ran c talk e with dis
r "\"That’s where Verissa comes in. She’s our shaman. If anyone can figure how to sort this out, it’s her.\""
m "\"Sort out how?\""
show ran c think with dis
r "\"Well… I can’t hide you in my home forever. Sooner or later, someone would sniff you out.\""
"He frowns for just a moment, but a confident smile quickly returns to his muzzle."
show ran c awkward with dis
r "\"I just need to find an angle to present your case to our chief and ensure your safety.\""
m "\"And what is my case?\""
show ran c talk with dis
r "\"That you have a right to sanctuary.\""
show ran c smile with dis
m "\"Meaning?\""
show ran c talk with dis
r "\"It’s an ancient Sylvan law, preceding any of the Wolven laws. It means that any gravely wounded creature should be granted protection within our forest.\""
show ran c shocked with dis
m "\"But… I’m not wounded.\""
show ran c embarrassed with dis
"I glance over my body, checking both the torso and the sides; I cannot see my back, so I reach out with my hand trying to feel out anything."
m "\"At least not gravely…\""
"I am sore, but my skin for the most part seems to be intact."
show ran c worried rt with dis
r "\"When I found you, I thought you were… and even now, although you’re not physically hurt, it’s clear you’ve suffered some sort of trauma.\""
show ran c sad with dis
m "\"If you found me naked, why would you think I was hurt?\""
"Ranok winces at the question."
"This doesn’t bid well."
show ran c worried r with dis
m "\"Ranok?\""
"He remains silent, clearly struggling with the answer and my voice fills with dread."
m "\"Why did you think I was gravely wounded?\""
show ran c worried rt with dis
r "\"You were covered in blood and viscera… a lot of it.\""
show ran c worried r with dis
"I blink."
m "\"W-what?\""
show ran c resigned with dis
r "\"I thought you were attacked and left for dead.\""
show ran c sad with dis
"What the hell?"
"I can’t even begin to imagine myself splayed out naked in the middle of the forest, let alone drenched in blood."
"But…"
"Again, I reach around to feel up my body and find nothing."
"The blood couldn’t have been mine; what was going on in that forest?"
"This whole situation gets weirder and weirder with each word this wolf utters."
r "\"You were unresponsive, and your heartbeat was so faint…\""
r "\"I thought you were dying.\""
"His voice falters slightly, causing me to swallow hard."
"I’m glad I was out for that part."
show ran c serious with dis
r "\"I had to try to save you… so I decided to bring you here.\""
show ran c worried rt with dis
r "\"I came upon Vulgor halfway to the village…\""
r "\"He might not want to admit it… but even he was shaken by your state.\""
r "\"At least it made it easier to convince him to help smuggle you.\""
show ran c sad with dis
"I can’t imagine Vulgor being moved by anything and that one sentiment alone drives home how terrifying I must’ve looked."
m "\"Hmmm...\""
show ran c resigned with dis
r "\"It seemed like you barely survived a massacre.\""
show ran c worried rt paw with dis
r "\"Once we got here, I began cleaning you of all the blood… washing you bit by bit.\""
show ran c worried r with dis
"I feel a hot flush as it dawns on me what this means."
"I was out cold, naked… and this wolf-"
show ran c shocked with dis
m "\"You… washed me?\""
show ran c embarrassed with dis
"I swallow heavily again, the lump in my throat growing larger."
"Even though it’s obvious he had to, the idea is quite embarrassing."
show ran c embarrassed blush with dis
"He mirrors my discomfort, looking away with a defensive tone in his voice."
r "\"I needed to find where the blood was coming from!\""
r "\"But I couldn’t find anything.\""
r "\"There was not a single scratch on your body.\""
"He’s so flustered that I almost feel bad for him, I didn’t mean to insinuate anything."
"I smile at his hasty explanation, just wanting to put him at ease."
show ran c shocked with dis
m "\"There are a few now.\""
"I say with a cheeky grin, showing a few scrapes and bruises left by the black wolf."
show ran c awkward with dis
"Although Ranok smiles for a moment, I can see his ears splay back."
show ran c sad with dis
"My good intentions seem to have backfired."
r "\"Sorry about that.\""
m "\"It’s not your fault.\""
"I touch his shoulder, trying to reassure him."
r "\"Well, I did leave you in his care.\""
m "\"True… and knowing him just for a few moments, I wouldn’t leave him alone with another living being.\""
"I chuckle, trying to cheer him up."
m "\"But you didn’t have a choice.\""
show ran c worried rt with dis
r "\"Yeah…\""
show ran c worried r with dis
"He sounds unconvinced, looking away towards the window."
"I can tell he feels responsible for me and what Vulgor did doesn’t sit well with him."
"I decide to drop the subject, but I appreciate seeing how much he cares about it."
m "\"So… the blood wasn’t mine?\""
"Ranok slumps, resting his elbows on his knees and looking straight at the floor."
show ran c resigned with dis
r "\"In retrospect, if it was yours, it would’ve meant that you were bled dry.\""
show ran c sad with dis
r "\"There was so much of it...\""
r "\"That’s one of the reasons why Vul quickly turned against you.\""
m "\"What? Why?\""
r "\"To him it meant you weren’t a victim, but rather-\""
m "\"He can’t think I had anything to do with that!\""
"I protest, throwing my arms out."
m "\"I mean, look at me! Do I look like I’m capable of eviscerating someone?\""
show ran c embarrassed with dis
r "\"Well, I don’t think you are, but it did unsettle him… besides, it goes deeper than that.\""
r "\"I had a moral right to save you, had you been hurt. But you were not.\""
show ran c sad with dis
r "\"I brought you into the village under a false pretence.\""
m "\"But you didn’t know that at the time.\""
show ran c neutral e with dis
r "\"I should’ve checked before I acted. As it stands, you are either dangerous, or somehow involved with blood magic.\""
show ran c neutral with dis
m "\"I’m not dange-\""
"I cut myself off, allowing his words to fully sink in."
m "\"Wait… did you just say 'blood magic'?\""
m "\"Are you for real?\""
"I scoff."
show ran c neutral t with dis
r "\"I am.\""
m "\"There’s magic?\""
show ran c serious with dis
"He looks at me with a serious gaze, as if ignoring my ‘silly’ question."
show ran c mutter paw with dis
r "\"The more Vulgor and I thought about it, the more convinced we became that you were part of some sort of dark ritual.\""
show ran c neutral with dis
m "\"What?\""
"I freeze, not out of fright but utter disbelief."
show ran c neutral t with dis
r "\"I think you were meant as a sacrifice.\""
show ran c neutral with dis
"My mind is spinning, unable to comprehend what I’m being told."
m "\"I… I don’t even-\""
"I pause, just staring blankly at the wall."
show ran c sad with dis
r "\"You ok?\""
"Talking wolves…"
"…strange feeling of dread…"
"…whispers in the dark…"
"…and now blood magic."
"It’s like a mad dream."
"I cannot contain the storm in my mind and I just spew out everything in quick succession."
show ran c shocked with dis
m "\"I think I need a pause here.\""
m "\"You keep saying these… {i}things{/i}… but I don’t understand {i}any{/i} of them!\""
m "\"You might as well be talking in a foreign language. \""
m "\"I get a massive headache just by listening to you.\""
m "\"It’s like you’re from {i}another{/i} fucking world!\""
show ran c smile e with dis
r "\"In a sense, we are.\""
"He shrugs casually, but to me nothing about this is casual."
"I want to say something but am immediately cut off by the sound of the door opening in the adjacent room."
"Someone entered the cabin."
stop music fadeout 6.0
show ran c shocked with dis
r "\"They’re here!\""
show ran c smile r at zero with move
"The grey wolf raises to his feet, approaching the doors."
m "\"Great… so much for my pause.\""
"I mumble in annoyance, knowing full well I’ll have to digest another portion of complete nonsense."
"A female’s voice reaches us from the other room, just as Ranok opens the doors."
play sound "sfx/door open.ogg"
show door behind ran with dis
"I bet it’s the shaman they spoke of."
show ver eyeroll behind ran at five with dis
ve "\"If this is another of your pathetic attempts at courtship, then-\""
"A white she-wolf snorts at Vulgor before she cuts off, entering the room."
"I’m immediately drawn to her moonstone - it’s a quarter moon."
show ver shocked with dis
ve "\"By Aluna! It’s an {i}actual{/i} human!\""
show vul eyeroll behind ver at thirteen with dis
v "\"As opposed to what? An imaginary one?\""
show vul neutral with dis
"She looks quite young to be a shaman and even though I’m not familiar with what shamans actually do, something tells me they should be bit more… experienced."
"Her golden eyes gaze at me with disbelief for a moment, before turning to Ranok."
show ver ang fl
show ran c worried r
show vul neutral l behind ver
with dis
ve "\"Have you lost your {i}damned{/i} mind?!\""
"She glares furiously at the grey wolf who winces and slumps slightly in deference."
show ver shocked
show vul smile
with dis
m "\"Verissa?\""
"Now it’s the female who stumbles back, evidently startled by the sound of her name coming from my lips."
ve "\"Did it speak my-\""
show vul amused with dis
v "\"Don’t get too excited, we mentioned your name to the human several times. No spiritual trickery involved.\""
show vul smile
show ran c smile r
show ver pouty
with dis
"I try to contain a smirk at Vulgor’s remark."
"His pragmatism and down to earth attitude are really starting to grow on me."
show ver neutral
show ran c smile
with dis
"The female’s eyes narrow as she moves closer, but she still keeps a safe distance between herself and the bed."
ve "\"Hmmm. So that’s what humans look like.\""
"Her eyebrows rise at my appearance, and I swear I can hear a hint of disappointment in her voice."
"It’s as if she expected something… well.. something more than I have to offer."
show vul talk pl
show ran c worried r
with dis
v "\"This one seems rather small, no?\""
show vul intrigued behind ver with dis
"I throw an annoyed gaze towards Vulgor; I know I’m not a body builder like those two, but I don't need them to rub it in every chance they get."
show ver talk with dis
ve "\"Yes, it does. But then again, I wouldn’t know…\""
show ver neutral e with dis
ve "\"Never seen one before.\""
"The female shrugs and all my hopes of her actually giving me some medical attention melt away."
"How can she treat a creature if she has never encountered it before?"
show ver pouty
show ran c annoyed r
with dis
r "\"Surely you have to know {i}something{/i}?!\""
"Ranok echoes my concern."
show ver eyeroll
show ran c worried r
with dis
ve "\"Yes, Ranok. I know they are two legged, upright creatures between 5 to 6 feet tall with little to no fur.\""
"Her voice conveys a sense of annoyance that I can almost relate to."
ve "\"I only have our texts to go by, and they don’t really deal with humans in detail. I don’t think anyone’s even seen one in almost two generations.\""
show ver neutral behind vul with dis
"If humans are indeed as rare as they make them out to be, how can they expect her to know any more than they do."
"Still, the idea of me being some sort of endangered species doesn’t seem quite right, almost as if I’m in a topsy-turvy world."
show vul facepalm with dis
v "\"Oh, joy… this is going to be {i}that{/i} more interesting to explain to his father.\""
show vul facepalm e
show ver shocked
show ran c neutral
with dis
m "\"Who is Ranok’s father? You’ve been making a huge fuss about him ever since I woke up.\""
show vul neutral l
show ran c neutral r
with dis
"The two males look at each other, while the female seems to be completely focused on me, her expression full of shock - no doubt caused by me speaking."
"I roll my eyes, knowing the conversation is going to be derailed by this at any moment."
show vul talk x with dis
v "\"He’s the chief.\""
show ver uncomfortable
show ran c embarrassed
with dis
m "\"The chief is Ranok’s father?\""
"I blurt out, thrown off by the revelation."
"Somehow, I thought those were two different wolves."
show vul talk ang
with dis
v "\"Wasn’t that obvious from the conversation?\""
show ran c sad
show vul neutral
with dis
m "\"Sorry, I didn’t keep track of all the nonsense you two are spewing!\""
"What else did I miss…?"
"But if the chief is Ranok’s father… that’s surely an advantage."
show vul neutral l behind ver
show ver grumble
show ran c worried r
with dis
ve "\"You weren’t bluffing. It does speak our language.\""
ve "\"Unnerving.\""
"Oh, great; here we go again."
show ver shocked
show ran c shocked
show vul smile
with dis
m "\"Yes, I can talk!\""
"I bark out in annoyance."
show ver annoyed
show ran c sad
with dis
m "\"So, can we {i}please{/i} not do this again?\""
"Verissa looks at me as one would look at an insolent child."
show vul talk l with dis
v "\"I told you - not a trace of an accent!\""
show vul neutral behind ver
show ran c worried rt
with dis
r "\"We already kinda exhausted the subject.\""
show ran c talk with dis
r "\"The kid speaks; let’s just leave it at that.\""
show ran c smile with dis
"The grey wolf comes to my aid and I smile at him with gratitude."
"I really do NOT want to revisit this conversation; it almost mentally broke me the last time."
show ver neutral e with dis
"Verissa sighs and nods in understanding."
ve "\"Listen, child.\""
show ver talk with dis
ve "\"You cannot speak a word to anyone else but us.\""
show ver neutral with dis
"I furrow my brows."
"Being talked down and patronised doesn’t sit right with me, they’re not that much older than I am."
show ver shocked
show ran c shocked
show vul intrigued
with dis
m "\"I’m not a child!\""
show ran c smile r with dis
"Then again, they ARE talking beasts."
"My ability to judge their age by looks must be somewhat limited, but I’m sure Ranok can’t be that much older than me."
"He mentioned that he just came of age, right?"
show ver intrigued
show ran neutral
with dis
ve "\"Oh? How old are you, then?\""
show ver neutral with dis
m "\"I’m-\""
"I cut myself off, again struggling with this ever-present nothingness in my mind."
"I can’t remember how old I am, but I know I’m not a child."
m "\"I’m of age.\""
show ran c smile e with dis
"I summarise, not exactly sure whatever that means to the wolves, but fairly certain that for a human that's exactly what I am."
show ver doubtful
show ran c worried r
with dis
ve "\"Curious. You don’t look it."
"She mutters unconvinced."
"I would take it as a compliment, but I can bet it’s another jab at how small I am."
show ver shocked
show vul smile
with dis
m "\"It doesn’t really matter, now does it?\""
show ran c laugh with dis
"My quip causes Ranok to laugh."
show ver grumble
show ran c smile
with dis
ve "\"Witty and sharp tongued…\""
"The female looks at Ranok with a hint of fear in her eyes."
show vul neutral l
show ver talk ang pl
show ran c worried r
with dis
ve "\"This is serious.\""
"Oh, for crying out loud!"
show vul neutral
show ver neutral
show ran c neutral
with dis
m "\"Why are you all so obsessed with my ability to speak?\""
show ver uncomfortable with dis
m "\"Why do you want me to play mute in front of the others?\""
"I can see that she gets more spooked out with each sentence I utter, and it only frustrates me more."
m "\"Are you telling me that humans are supposed to be some sort of primitive cavemen? Is that what it is?\""
m "\"Because let me tell you, this house and your outfits look like they’re out of a fucking history book!\""
show vul intrigued
show ver shocked
show ran c shocked
with dis
r "\"What?\""
show ver sad
show ran c worried rt paw
with dis
r "\"It’s a good house…\""
show ran c worried r with dis
"Ranok glances around his room with slight confusion, while Verissa briefly checks out her dress."
show ver talk with dis
ve "\"We know that your species isn’t primitive.\""
show ver neutral
show ran c neutral
with dis
m "\"Then why do you want me to play dumb?\""
"She finally snaps at me with a soft, almost melodic growl."
show ver ang
show ran c worried r
with dis
ve "\"Because others won’t understand!\""
show vul talk l with dis
v "\"And we do?\""
show vul neutral l
show ver annoyed
with dis
m "\"What is there to understand?\""
"I ask in resignation."
show ver annoyed t with dis
ve "\"No outsider speaks our language.\""
show vul unhappy
show ver eyeroll
show ran c annoyed r
with dis
ve "\"We don’t teach it to… otherkin.\""
show ver annoyed with dis
"She almost says it with disgust in her voice."
show vul neutral l
show ran c neutral t
with dis
r "\"The only creatures that can speak our tongue are other Avalan Wolves.\""
show ran c worried r
show ver eyeroll
with dis
ve "\"And Huskies. But they always have this unbearable twang to the way they speak.\""
show ver annoyed t with dis
ve "\"You speaking to us like you were born here... it's unheard of.\""
show ver facepalm with dis
ve "\"Bordering on sacrilegious.\""
"She rests her face in a paw, rubbing her temple."
show vul neutral
show ran c neutral
with dis
m "\"Sacrilegious?\""
show ver talk with dis
ve "\"Our language is a part of who we are as people… it was given to us by our ancestors, to keep and guard as our own, so that only we can communicate with them.\""
show ver talk ang x with dis
ve "\"We don’t take kindly to otherkin who try to learn it. Teaching outsiders is a capital offense.\""
show ver neutral with dis
m "\"I don’t know why or how I would learn it!\""
show vul neutral l
show ver eyeroll
show ran worried r
with dis
ve "\"Which is more the reason for you to keep quiet. It is clear someone had to teach you and from the way you speak… it was obviously one of our own.\""
show vul unhappy
show ver talk ang pl
with dis
ve "\"Not only is your life in danger. You could send the entire tribe into a frenzy.\""
show ver neutral with dis
m "\"Frenzy?\""
show vul talk p with dis
v "\"It’s clear someone betrayed us and broke our laws by teaching outsiders to speak. You’re the walking proof of that.\""
show vul neutral
show ver talk
with dis
ve "\"We’d have the elders clamouring for blood.\""
show ver annoyed t with dis
ve "\"And that's the last thing our tribe needs now; more paranoia. \""
show ver neutral with dis
"This is all utter nonsense."
show ran c sad with dis
m "\"I’ve never seen a talking wolf in my life!\""
show ver doubtful with dis
m "\"Until today that is.\""
"I shrug."
"The female looks at me expectantly, but I have nothing else to add."
show vul neutral l
show ver eyeroll
show ran c worried r
with dis
ve "\"Vulgor said you seem to be suffering from a memory loss.\""
show ver annoyed t with dis
ve "\"I’d say it’s far more likely you don’t remember meeting a wolf who taught you our language, rather than you miraculously gaining the ability out of the blue.\""
show vul neutral
show ver doubtful
show ran c neutral
with dis
ve "\"Wouldn’t you agree?\""
m "\"I guess.\""
show ver neutral with dis
"I reluctantly concede."
"In all fairness both options seem equally plausible, because to me none of this makes any sense, but I’m not about to argue that to a she-wolf who is convinced that her reality is more valid than mine."
"Especially since we apparently need her to save my skin."
show ver sigh with dis
ve "\"Now that we have this out of the way… let us deal with the more pressing matter...\""
show vul unhappy l
show ver ang fl
show ran c worried r
with dis
ve "\" ...what in the name of Aluna is the human even {i}doing{/i} here?\""
show vul neutral l
show ver neutral e
show ran c worried rt paw
with dis
"I rest my cheeks in my hands, slumping down as Ranok begins to explain his entire misadventure."
show ran c mutter paw with dis
"I pay as much attention as I can, as some parts of the story flew over my head earlier, however there are no surprises."
show ver neutral l
show ran c talk r
with dis
"Ranok went on his spiritual trip, couldn’t find any enlightenment so he decided to meditate underneath ‘his’ tree."
"Whatever that means."
show ran c talk with dis
"Apparently, that’s where he found me, drenched in blood."
"I have to question the Ancestors the wolves worship."
show vul neutral
show ver neutral
show ran c talk paw
with dis
"If this truly is all part of their plan, it’s a shoddy one at best."
"The whole setup seems more akin to a horror story than an actual spiritual journey, but then again… what do I know?"
show ver neutral e
show ran c awkward
with dis
"I watch as the female listens carefully to what is being said, but she doesn’t show any emotion, even when Ranok clumsily tries to implicate her through his coming of age ceremony, or suggests that I was part of some sort of dark ritual."
show ran c smile r with dis
"She is eerily calm, or at least good at hiding her inner thoughts."
show vul neutral l
show ver neutral l
show ran c shrug r
with dis
r "\"That’s pretty much it.\""
show ran c smile r with dis
"The grey wolf concludes his explanation and silence falls over the room."
show ver neutral with dis
"It drags on for a bit, while we all look at Verissa expectantly."
show ver neutral e
show ran c worried r with dis
"She keeps us in suspense a while longer, most likely weighing her options."
show ver facepalm with dis
ve "\"Sweet Ancestors, you are the {i}dumbest{/i} wolf in the tribe, if not the {i}whole{/i} of Avalan!\""
show ver sigh with dis
"She sighs, again not showing much of any emotion."
show ran c worried rt paw with dis
r "\"Can you help me protect him?\""
show ver talk ang pl
show ran c worried r
with dis
ve "\"What choice do I have?\""
show ver annoyed with dis
"Finally, something; a hint of annoyance."
"It’s not exactly filling me with hope, but Vulgor proves me wrong."
show vul intrigued tl
show ver neutral r
with dis
v "\"You really want to get involved?\""
show vul neutral l
show ver eyeroll
with dis
ve "\"You’ve already involved me… besides, otherkin or not, this human is not at fault.\""
show ver sad with dis
"She looks at me with pity."
show vul neutral
show ver sad t
with dis
ve "\"From what you both told me, the human was out cold. It’s Ranok who broke the law. I would not be able to sleep knowing that I allowed an innocent to pay for his stupidity.\""
show ver sad with dis
"I find it hardly fair to belittle Ranok like this, not when he saved my life."
show ran c sad with dis
m "\"He-\""
show ver talk ang x with dis
ve "\"No need to speak.\""
show ver annoyed with dis
"She cuts me off, addressing the two wolves."
show vul neutral l
show ver talk ang pl
show ran c worried r
with dis
ve "\"This is a very precarious situation. We are risking the fury of our tribe.\""
show ver annoyed
show ran c worried rt
with dis
r "\"But can you help us?\""
show ver sigh
show ran c worried r
with dis
ve "\"I need to commune with the spirits. I may have an idea how to fix this, but I want to make sure our Ancestors won’t find it objectionable.\""
show ver neutral r
show vul eyeroll
with dis
v "\"Yeah, sure. Go {i}huff{/i} some incense, while we worry about what to do with this whelp!\""
"Again, it’s hard not to chuckle at Vulgor’s jabs."
show vul unhappy e with dis
"It’s nice for once to not be on the receiving ends of those, however I find myself troubled that any plan involving my safety relies on substance abuse."
show ver ang r with dis
ve "\"Yes, I {i}will{/i} huff some incense, so that I can receive guidance on how to avoid us all getting banished.\""
show vul neutral l
show ver pouty
with dis
"The female reiterates through her fangs."
"They keep talking about banishment, but I can’t quite understand what for."
show vul neutral
show ver neutral
show ran c neutral
with dis
m "\"If it’s about me keeping my mouth shut, I will.\""
show vul neutral l
show ver talk ang x
show ran c worried r
with dis
ve "\"That’s only one of the problems.\""
show ver annoyed with dis
"The female retorts, looking at me with slight annoyance."
"I guess she really meant it when she said I shouldn’t talk, but I don’t care."
show ver talk ang pl with dis
ve "\"The forest around our village is sacred. No outsiders are allowed.\""
show ver annoyed with dis
m "\"So they said, but there must be some exceptions.\""
show ver talk ang x with dis
ve "\"There are none. Trespassing is punishable by death. Even Ranok’s delusion about the right of sanctuary is just that.\""
show ver talk ang pl with dis
ve "\"A delusion.\""
show ver annoyed with dis
"She waves her hand towards the grey wolf in dismissal."
show ver talk ang x with dis
ve "\"Our people haven’t been part of the Sylvan for nearly a thousand years… claiming ancient customs as defence for smuggling you in would be tricky to say the least.\""
show vul talk
show ver annoyed
show ran c annoyed r
with dis
v "\"The idiot should have {i}killed{/i} you where he found you.\""
show vul unhappy with dis
"I frown."
show ran c sad with dis
m "\"Seems a bit harsh.\""
show ver talk ang pl
show ran c worried r
with dis
ve "\"Maybe to you, but it is our forest and it is our duty to protect it.\""
show vul intrigued
show ver pouty
show ran c sad
with dis
m "\"Protect it from what? I don't even know how I got here in the first place! What could I possibly do?\""
"The she-wolf sighs, looking at the ceiling with annoyance."
"I have clearly exhausted her patience."
show vul neutral l
show ver eyeroll
show ran c worried r
with dis
ve "\"The human asks a lot of questions.\""
show vul intrigued
show ver pouty
show ran c sad
with dis
m "\"I’m sorry, but you keep saying my life is on the line… I’d like to at least understand why.\""
m "\"I get the language part, but what possible danger could I pose to your forest?\""
m "\"I’m not an arsonist.\""
show ran c worried r with dis
"The female continues to disregard me, causing a moment of silence."
show ver annoyed l with dis
"She throws an angry stare at Ranok and I can see his ears splay back, as he looks at me apologetically."
show vul neutral l
show ran c sad t
with dis
r "\"I’ll explain everything later.\""
show ran c awkward with dis
r "\"You said yourself you need a pause and we need to focus on our next steps.\""
show vul neutral
show ver neutral
show ran c sad
with dis
"I take a deep breath, giving him a defiant look, but eventually exhale with a drawn-out sigh."
"As much as I want to understand what’s going on, a break would allow me to digest all I have learned so far; my mind is still slightly spinning from all the revelations."
show ran c smile with dis
"I nod with a reluctant smile and I can see Ranok’s expression lighten up."
"It’s nice to know how much he cares about my mood."
show ran c smile r with dis
"Somehow, I feel like that’s not something I’m used to; someone caring."
show vul neutral l
show ver neutral l
show ran c talk r
with dis
r "\"We need to figure out how to present the facts to my father.\""
show vul talk l
show ver neutral r
show ran c smile r
with dis
v "\"And those are?\""
show vul neutral l
show ver neutral l
show ran c shrug r
with dis
r "\"That I was meant to find [mc]. And that he is meant to be here.\""
show vul growl lx
show ver neutral r
show ran c smile r
with dis
v "\"You’re putting our collective fur on the line.\""
"The black wolf issues a stifled growl."
show ver sigh with dis
ve "\"He is… but as insane as that sounds, claiming it was all fate is our best chance.\""
v "\"You can’t be serious!\""
show ran c talk r with dis
r "\"Everything will be fine, the Spirits willed it.\""
show ver facepalm
show ran c smile
with dis
ve "\"For all our sakes I really hope that's the case.\""
show ver sad with dis
"The female embraces herself, looking at me with a worried, almost empathetic expression."
show vul unhappy
show ver sad t
with dis
ve "\"This is going to be a tough nut to crack... I hope you two are ready for the potential fallout."
show ver sad t with dis
ve "\"Moon knows, I'm not sure I am...\""
show vul neutral l
show ver neutral l
show ran c talk r
with dis
r "\"Remember your own ceremony?\""
"Ranok looks up at her with determination."
show ran c talk r paw
r "\"'Your road will be hard, but you must never waver or stray from the path.' That was the message you got from the Ancestors.\""
show ran c smile re c with dis
"He nods confidently, causing the female to stare at him with a slightly open muzzle."
show ver smile e
show ran c shrug r
with dis
r "\"None of this was meant to be easy.\""
show vul intrigued
show ver smile
show ran c smile r
with dis
"Verissa smiles softly and finally approaches me, stopping right next to the bed and placing her paw on my head."
"It’s much smaller and lighter than Ranok's, however the gesture is equally tender."
show vul unamused
show ver amused
show ran c smile re c
with dis
ve "\"It’s surprising that for someone so stupid, you manage to come up with something almost eloquent.\""
show vul facepalm
show ver neutral r
show ran c worried r
with dis
v "\"Ah, come on!\""
show vul facepalm e with dis
"I hear the black male protest in the back with familiar mockery in his voice."
show vul facepalm growl with dis
v "\"'Life will be hard, so keep at it'?!\""
show vul growl lx
show ver pouty
with dis
v "\"How is that a prophecy?! It can apply to anyone in any given situation!\""
show vul growl p
show ran c annoyed r
with dis
v "\"It has {i}nothing{/i} to do with the human!\""
show vul unhappy
show ver sigh
with dis
ve "\"Shut up, Vul.\""
"She sighs, not even regarding him."
show ver neutral l
show ran c worried rt paw
with dis
r "\"I found [mc] lying underneath my Name Tree. He knew my name, speaks our language… the spirits willed it, it’s not a coincidence.\""
show ran c worried r with dis
"Vulgor issues an exhausted sigh."
show vul eyeroll
show ver neutral e
with dis
v "\"Or it is exactly that, a coincidence. Consider this:\""
"He proposes, drawing our attention with his paw."
show vul talk ang with dis
v "\"A confused human who speaks our language runs through the forest, stumbles upon a random tree and reads the inscription. When it faints, it mumbles the last thing it saw.\""
show vul talk pl with dis
v "\"No spirits involved.\""
show vul unhappy with dis
"Despite his crudeness, I have to agree with him on this."
"Even though I don’t remember anything prior to my awakening, I might have been running through the woods and if I did see a tree with a name on it, I’d most likely read it."
show vul neutral l
show ver sigh
with dis
ve "\"And you consider this:\""
"The female speaks up, slight mockery in her voice, yet she holds her composure."
show ver eyeroll with dis
ve "\"If that was the case, then we’re truly done for. All of us.\""
"She swooshes her paw around the room, encompassing everyone, even me."
show ver grumble p with dis
ve "\"If it’s all just a coincidence, as you claim, then the human broke the law by entering the grove. He’s dead.\""
show vul neutral
show ver neutral
show ran c sad
with dis
"Her paw points to me, which sends a cold shiver down my spine."
"I struggle to swallow as my throat clenches tight; I can feel a bead of sweat running down my forehead."
show vul neutral l
show ver talk ang lp
show ran c worried r
with dis
ve "\"This idiot is facing banishment for not protecting the grove from intrusion.\""
show ver sigh with dis
"She points to Ranok, then sighs, as her paw nonchalantly waves at the black male."
show vul worried l
show ver talk ang pl
with dis
ve "\"Worse yet, you helped him smuggle the outsider within the boundary of our village. That’s banishment for you, too.\""
show ver talk ang x with dis
ve "\"Not sure what double banishment would mean for Ranok, but I’m fairly certain his father would not kill him, even though the law demands it.\""
show ver annoyed with dis
"I look at the grey male with worry, the consequences he’s facing are almost as dire as mine."
"I guess Vulgor was telling the truth about his friend not thinking things through."
show ver sigh with dis
ve "\"And then there’s me.\""
"The female finally breaks the silence with a resigned exhale."
show ver facepalm with dis
ve "\"You damn well know that I haven’t finished my training. Everyone questions my abilities as a shaman.\""
show ver talk ang lp with dis
ve "\"My very first ceremony, first communion with the spirit world and I make Ranok drag a human into the village, breaking our most sacred laws…\""
show ver sigh with dis
ve "\"That’s the end of me being a shaman.\""
show ver neutral e with dis
"She lets the words hang for a moment."
show ver facepalm with dis
ve "\"And now, you brought me here, where instead of immediately sounding an alarm, I’m trying to help you two fix this. The penalty for being part of a conspiracy is banishment.\""
"The female points to each of us in quick succession, starting with me, Ranok, Vulgor and finishing on herself."
show ver talk ang x with dis
ve "\"Death, banishment, banishment, banishment.\""
show ver sigh with dis
ve "\"So…\""
show ver neutral r with dis
"She looks at the black wolf."
show ver eyeroll with dis
ve "\"This is not a silly misunderstanding, Vul. We can’t talk our way out of this or use our positions to mitigate the damage.\""
show ver talk ang x with dis
ve "\"Shall we then all agree that this is the will of the spirits, or should we simply march to the chopping block?\""
show ver annoyed with dis
"She asks with a melodic, almost taunting tone."

if Vulgor == 1:
    show vul talk
    show ver neutral r
    show ran c annoyed r
    with dis
    v "\"There is a simple solution, but I’m sure neither of you will approve.\""
    show ran c growl r with dis
    "Ranok issues a stifled growl."
    r "\"Then why bring it up?\""
    show vul talk e
    show ver neutral e
    show ran c annoyed r
    with dis
    v "\"Just putting it out there.\""
    show vul unhappy e with dis
    "The black wolf shrugs."
    show vul talk p with dis
    v "\"Snapping its neck would solve the problem, but it would be slightly awkward now that it has a name.\""
    show ran c growl r with dis
    r "\"Yes, he {i}does{/i}. So, you might as well start using it.\""
    show vul talk pu with dis
    v "\"I’m going to stick with ‘Piglet’ for now, no point getting attached just yet.\""
    show vul worried with dis
    "The black wolf tries to give me a cold gaze, but his muzzle is tinged with worry."
    show vul talk l with dis
    v "\"We’re all walking on thin ice here.\""
    show vul neutral l with dis
    "The female shakes her head in dismissal."
    show ver sigh
    show ran c shocked r
    with dis
    ve "\"Don’t you worry, I intend to save our pelts {i}as well{/i} as the human's life.\""
else:

    show vul growl with dis
    v "\"We could just snap its neck and get rid of-\""
    show ran c growl r with dis
    "Ranok’s snarl causes me to jump up, and even Verissa is startled by how angered the male got."
    r "\"You swore!\""
    "As much as seeing his lips curl up revealing his massive fangs is unsettling, I feel warm knowing I have such a loyal protector."
    show vul talk e with dis
    v "\"But she didn’t.\""
    show vul neutral l with dis
    "Vulgor shrugs shamelessly, raising his brow expectantly at Verissa."
    show ver eyeroll with dis
    ve "\"What part of me being a shaman don’t you understand? I {i}save{/i} lives, not end them!\""
    show vul growl with dis
    v "\"You have both lost your minds!\""
    show vul worried l
    show ran c shocked r
    with dis
    ve "\"No, Vul. What Ranok did was stupid and thoughtless, but his heart was in the right place.\""
    show ver smile
    show ran c worried r
    with dis
    "She gave me a kind look, again ruffling my hair."
    show ver amused with dis
    ve "\"And so is mine. Luckily for us, I am smarter than both of you combined.\""

show ver neutral e
show vul neutral
with dis
"The female approaches the doors, opening it."
show ran c worried rt with dis
r "\"So, you know how to fix this?\""
show ran c worried r
show ver talk l
with dis
ve "\"I already said I do; I just need to make sure I will not offend the Ancestors.\""
show ver neutral with dis
"As she is about to leave, she stops, turning towards the two wolves."
show ver talk ang pr with dis
ve "\"Our little congregation was most likely noted. I suggest we disperse not to raise any further suspicion.\""
show vul unhappy e
show ver neutral
show ran c neutral re
with dis
"The wolves nod to each other in agreement."
show vul intrigued
show ran c sad
with dis
m "\"Am I to stay here alone?\""
show ver talk ang x with dis
ve "\"[mc], was it? Since you claim you’re {i}not{/i} a child, I assume you’ll be fine on your own.\""
show ver neutral r with dis
"I frown at her snarky remark, but nod in agreement."
show vul neutral l
show ver talk ang pr
show ran c worried r
with dis
ve "\"Vul, you keep an eye on the house. Make sure no one’s snooping about.\""
show ver talk ang lp
show ran c shocked r
with dis
ve "\"Ranok, you must go and speak with Tano.\""
show ver neutral l with dis
r "\"Why?\""
show ran c annoyed r with dis
"The male scoffs seemingly appalled by her suggestion."
show ver eyeroll with dis
ve "\"Because not joining your father on the hunt already looked very odd. Chat him up about rangers, or patrols, or whatever it is you fur-for-brains do.\""
show ver sigh with dis
ve "\"Make up an excuse to put him at ease.\""
show vul intrigued
show ver neutral
show ran c neutral
with dis
m "\"Who's Tano?\""
show vul talk ang
show ran c neutral r
with dis
v "\"A nosy bastard.\""
show vul neutral l
show ver talk ang x
with dis
ve "\"And the last thing we need is {i}him{/i} sniffing about.\""
show vul neutral
show ver annoyed
show ran c sad
with dis
m "\"I don’t understand… can’t you just stay at home?\""
"She looks at me with a slightly risen brow, clearly annoyed I keep talking."
show ver talk with dis
ve "\"We are a tightly-knit community… meeting up in seclusion reeks of dissent.\""
show ver neutral with dis
"With that, she leaves the room, Vulgor following suit."
hide vul neutral
hide ver neutral
show ran c embarrassed
with dis
"Only Ranok stays behind for a moment, as if struggling to decide on something."
show ran c neutral at center with move
"Eventually he approaches me and crouches next to the bed, so that our eyes are on the same level."
show ran c smile with dis
"He gently squeezes my shoulder with his paw, one of his fangs poking out through a goofy smile."
show ran c talk with dis
r "\"I won’t be long.\""
show ran c smile with dis
"He says encouragingly."
show ran c talk with dis
r "\"Once I’m back, we’ll be able to talk some more, okay?\""
show ran c smile with dis
"I nod and snicker, hearing his tail swoosh against the wooden floor in excitement."
"The way he wags his tail with such enthusiasm almost begs to question why the whole place is so dirty… one does not even need a broom with a wolf like that around."
show ran c shocked with dis
ve "\"Ranok!\""
"The female calls out impatiently from the other room."
show ran c awkward with dis
r "\"Just stay out of sight.\""
show ran c smile e with dis
m "\"I’ll be fine.\""
show ran c smile with dis
"I reassure him, but then I hear a deep rumble inside my stomach."
"The cramps make me squirm as if I never eaten a meal before; I am ravenous, and I think the stress of the situation is the only thing that kept my attention away from it."
show ran c shocked with dis
m "\"If… I could only have something to eat.\""
"I see the wolf look at me with a troubled expression, as if he didn’t factor in that I require sustenance."
show ran c facepalm with dis
"Ranok slaps his forehead in deep annoyance."
r "\"Spirits, I’m {i}so{/i} stupid!\""
show ran c sad with dis
v "\"What is it now?\""
show vul neutral behind ran at thirteen with dis
"The black wolf calls out from the other room, appearing in the doorway."
show ran c worried rt paw with dis
r "\"How are we going to {i}feed{/i} him?\""
show vul intrigued
show ran c sad
with dis
m "\"I… can eat pretty much anything.\""
"I mumble, although the idea of raw meat is making me queasy."
show vul facepalm with dis
v "\"Fuck.\""
"Vulgor’s resigned curse makes me think that my diet is not the main problem here…"
show vul neutral
show ran c neutral t
with dis
r "\"We eat together as a tribe, only mothers with pups are allowed to eat separately.\""
show ran c embarrassed with dis
r "\"Smuggling food home is looked down upon as a sign of gluttony.\""
show vul talk
show ran c worried r
with dis
v "\"And would immediately rouse suspicion.\""
show vul neutral l with dis
"I look to Ranok’s troubled expression."
"I can see he didn’t think this through, none of it."
show ran c neutral e with dis
"But as he meets my worried gaze, his expression changes immediately."
show ran c talk with dis
r "\"I’ll get you some food.\""
show ran c smile with dis
"He says determined, but slight unease lines his voice."

if Vulgor == 1:
    show vul talk e
    show ran c shocked r
    with dis
    v "\"No, I'll do it.\""
    show vul unhappy e
    show ran c neutral r
    with dis
    "We both look to Vul with surprise."
    show vul talk with dis
    v "\"I'll be keeping an eye on the house anyway.\""
    show vul neutral
    show ran c smile r
    with dis
    "He shrugs with a hint of embarrassment and even Ranok picks up on it, smirking."
    show ran c talk r with dis
    r "\"You're warming up to [mc], aren't you?\""
    show vul eyeroll
    show ran c smile
    with dis
    v "\"Psh! As if, you idiot! It's just easier that way.\""
    "The black male scoffs indignantly."
    show vul talk ang with dis
    v "\"No one would dare follow me. Once the feast starts, I'll bring the Piglet some roast.\""
else:

    show vul growl lx
    show ran c shocked r
    with dis
    v "\"Seriously, how are you going to do that with Tano watching over your shoulder?\""
    show ran c worried rt with dis
    r "\"I'll think of something.\""
    show vul growl p
    show ran c annoyed
    with dis
    v "\"No, {i}fuck{/i} that! Last time you thought of something we ended up with this little shit here.\""
    "The black wolf points to me with a slight growl."
    show ran c eyeroll with dis
    r "\"Well, what would you have me do?\""
    show vul talk ang
    show ran c annoyed r
    with dis
    v "\"Let him starve...\""
    show ran c growl r with dis
    r "\"Vul!\""
    show vul eyeroll
    show ran c shocked
    with dis
    v "\"Fine... I'll bring him some scraps from the feast.\""
    show vul unhappy e
    show ran c smile e
    with dis
    "The black wolf sighs in resignation, looking at me with annoyance."

show ran c talk
show vul neutral
with dis
r "\"I hope roasted meat agrees with you.\""
show ran c smile e with dis
"I smile in relief as the thought of eating raw was banished by his words."
"Why did I assume they would eat anything uncooked when they’re clearly as civilized as I am?"
show vul talk l with dis
v "\"Let’s go.\""
show vul neutral with dis
"Vulgor utters impatiently, tapping his foot against the ground and causing Ranok to stand up."
hide vul neutral
show ran c wink
with dis
"The grey wolf winks at me, while tilting his head towards the small window."
show ran c talk with dis
r "\"Stay out of sight.\""
show ran c smile e with dis
"I nod as he follows his companions out of the bedroom."
hide ran c smile e
hide door
with dis
play sound "sfx/door close.ogg"
"They close the doors behind, and a moment later I can hear them leave the house altogether."
"I am finally alone."
"I look around the tiny room, idly patting at the bedding."
"There isn’t much noise, mostly some distant chatter I can’t make out; muffled voices too far away to be intelligible."
"What I do hear is the forest; wind ruffling the leaves and birds chirping in nearby trees."
"I am tempted to approach the window and simply take in the scenery, but I know better."
"…"
"I close my eyes and chuckle nervously."
"This is utter nonsense; I must be dreaming."
"Or maybe I am the one who huffed some incense?"
"Whatever the case, I’m exhausted by all of this, so I allow my head to fall freely onto the pillow."
play sound "sfx/bed_jump.ogg"
"I collapse into the fabric, allowing it to wrap around me in a warm embrace."
"It only takes me a moment to sink down into it."
"The snugness makes my eyelids droop instantly, as heavy as if they were made of lead."
"For some odd reason I feel extremely exhausted, almost as if staying awake was unnatural to me..."
"Guess that's what stress does to you."
"I try to look at the ceiling for a bit, seeking patterns in the naked woodwork, locating different burls and knots within the natural grain of the planks."
stop ambience fadeout 6.0
"I yawn, closing my eyes, as I let the fatigue overtake me and I drift away into a peaceful sleep."
scene bg black with slow_dissolve
scene bg broom_night with slow_dissolve
play ambience "ambience/forest_night.ogg" fadein 6.0
play sound "sfx/window_knock.ogg"
with vpunch
"I suddenly wake to a loud, resonating thud."
"I get up immediately, seeing the room covered in darkness."
"It's clearly night..."
"How long was I asleep?"
play sound "sfx/window_knock.ogg"
with vpunch
"Another thud makes me jump up, but this time I know where it's coming from: someone's banging on the window."
m "\"Ranok?\""
"I call out quietly towards the next room."
"I know the male went to deal with his tribesmen, but I hope he already returned."
play sound "sfx/window_knock.ogg"
with vpunch
"The banging continues, this time more impatient and I start to panic."
"I look towards the window, trying to remain hidden within the shadows of the room."
"I’m not supposed to be seen!"
"I can make out a large dark figure, obviously a wolf."
"I think it might be one of the tribesmen snooping around."
"Wasn’t Vulgor supposed to make sure this didn’t happen?"
v "\"Open the damn window!\""
"I hear the familiar cold voice and exhale in relief."
scene bg window_night with dis
"I approach the window feeling a lot less worried than before, quickly locating the latch holding it closed."
"Both wings open with a tortured creak, obviously not used to being swung ajar."
play sound "sfx/window_creak.ogg"
scene bg outdoor_n
show vul talk p at eight
with dis
v "\"Here’s your chow, Piglet.\""
show vul neutral with dis
"The wolf passes me a sizable bundle wrapped in linen cloth."
m "\"Thank you.\""
"I respond, taking the parcel."
"I smile, feeling the aroma of roasted meat hit my nostrils."
"I nearly forgotten how hungry I am."
show vul intrigued with dis
m "\"Aren’t you going to come in?\""
show vul talk with dis
v "\"No one lives with Ranok and he’s not home. Besides, it’s already night.\""
show vul neutral with dis
"I look around, noticing how dark the outside world has gotten."
m "\"Can’t he have a friend over?\""
"I ask, slowly unfolding the cloth."
show vul talk ang with dis
v "\"Not overnight.\""
show vul unamused u with dis
"The black male responds almost appalled by the suggestion."
m "\"Why?\""
show vul talk p with dis
v "\"Because that would make them both look… {i}defective{/i}.\""
show vul neutral with dis
"I make a dumb ‘huh?’ sound, to which he only gives me a telling gaze."
m "\"Oh!\""
"Guess wolves don’t like homosexuality."
show vul intrigued with dis
m "\"But, just because two guys are alone in the same room at night, doesn’t mean they-\""
show vul unamused with dis
"I try to rationalise, but I can see his rising brow with each word I utter."
"Yeah… that does sound a bit off now that I think about it."
show vul unamused u with dis
m "\"Is that why you’re standing outside the window?\""
show vul shocked with dis
m "\"Afraid I would {i}seduce{/i} you?\""

if Vulgor == 1:
    show vul smile u with dis
    "To my surprise Vulgor snorts at the suggestion and almost smiles."
    show vul amused with dis
    v "\"An actual pig would have better chances at that...\""
    show vul smile with dis
    "I raise an eyebrow with a challenging smirk."
    m "\"It seems more suspicious to have males sneaking about windows, rather than having them over for a drink.\""
    "Vulgor narrows his brows, looking at me with slight amusement."
    show vul talk su with dis
    v "\"You couldn't drink your way out of a piss bucket, suckling.\""
    show vul talk s with dis
    "Ouch."
    show vul smile with dis
    "The jab wasn't malicious, but... ouch."
    "He's definitely being playful, but considering choking me out was his 'gentler' side, why would I expect his verbal spars to be any tamer?"
    "I just shake my head with a smile."
    "At least having a female over has to be normal around here, right?"
    "I don’t believe even for a moment that this village is full of celibate homophobes."
    show vul intrigued with dis
    m "\"How about a lady caller, then? Can’t he have those over?\""
    "Vulgor snorts again."
    show vul talk su with dis
    v "\"He can… and as much as you {i}do{/i} sound like a little bitch… it’s a small tribe.\""
    show vul smirk with dis
    "I nearly choke at the sharp remark, looking at Vul with obvious annoyance."
    show vul smile with dis
    "He clearly enjoys that at least one of his jabs finally landed."
    show vul talk s with dis
    v "\"Having a female over is quite hard to misunderstand.\""
    show vul talk e with dis
    v "\"A mate leads to rumours, rumours raise suspicion, and suspicion leads to wolves sniffing about.\""
    show vul talk ang with dis
    v "\"We wouldn’t want that, would we?\""
    show vul neutral with dis
    "I shrug, finally opening the parcel to reveal its contents."
else:

    show vul growl with dis
    v "\"Not even remotely funny.\""
    show vul unhappy with dis
    "He says coldly, obviously not keen to joke around."
    "I simply shrug, finally opening the parcel to reveal its contents."
    m "\"Suit yourself.\""
    m "\"It’s still more suspicious to have you snooping about and whispering through a window.\""

"It's filled with succulent cuts of meat."
"They don’t look the most appetizing; mostly shredded apart without a care, but the smell alone is enough to make my mouth water."
"I quickly glance around, really troubled by our little rendezvous; it does look quite conspicuous. "
show vul talk with dis
v "\"Don’t worry, I’ll know if anyone gets close enough to vanish in time.\""
show vul neutral with dis
"I flash my brows indifferently; guess not only Ranok is full of himself."
"I quickly grab one of the chunks and bring it to my lips."
show vul intrigued with dis
"Vulgor gazes at me with extreme curiosity, but I’m far too hungry to pay him any mind."
show vul shocked with dis
"I take a ravenous bite."
"The meat falls apart at the slightest touch of my tongue, almost melting inside my mouth."
show vul unamused with dis
"I gasp in satisfaction, closing my eyes in complete bliss."
m "\"Mmmmm.\""
"It’s good."
"It’s {i}very{/i} good."
"But no matter how hard I try, I cannot figure out what it is that I’m actually eating…"
"Despite my memory being wiped clean, I can still recall certain things."
"I remember how chicken tastes, or beef…"
"This is something different entirely."
"I take another chunk, hastily stuffing it whole into my mouth."
"God, I’m hungry, and this meat is hitting the spot."
"It tastes like nothing I ever knew… it’s slightly sweet and has an earthy, almost nutty flavour to it."
m "\"Sho good! What ish it?\""
"I ask, still chewing through the sinew, forgetting my manners for a moment."
show vul talk lx with dis
v "\"Roasted boar.\""
show vul unhappy e with dis
"The male responds."
"There is an odd discomfort in his voice, but I ignore him."
"I am utterly consumed by this meal, as I can finally feel the large void in my stomach fill up."
"It's almost as if I haven’t eaten in forever."
"I take another piece of meat, revelling in its tenderness and juices."
show vul unamused with dis
v "\"This… is going to make me sick.\""
"The black male finally catches my attention with his troubled confession."
"I can see his distress, as if he was truly struggling to keep down his own meal."
m "\"Whaf?\""
"I ask, mouth still full of meat as I lick my greasy fingers."
show vul talk p with dis
v "\"I wondered how you can eat without a muzzle… but this...\""
show vul unamused with dis
"He struggles, covering his snout as one does to stop a reflux."
v "\"You’re just stuffing it into a hole in your head!\""
"I blink in confusion, as the male turns away from me."
"Is he serious?"
"He’s really unsettled just by watching me eat!"
"I chuckle, making nothing of it and continue with my meal."
"The idea of this large, cold warrior getting weak at the knees because of my mouth is too much."
"I’m about to laugh when-"
hide vul unamused with dis
v "\"BLEUGH!\""
play sound "sfx/splatter.ogg"
"What the?!"
"Vulgor has just retched a few steps away from the window."
"I look at his crouching figure in momentary disbelief, but as he purges again, I immediately take my food off the ledge."
play sound "sfx/splatter.ogg"
"I know that if the acidy smell hits my nose, I will join him in emptying my own stomach, so I quickly close the window."
play sound "sfx/window_creak_c.ogg"
"I stand there, looking for any signs of him getting better, but after a while I bring another piece of meat to my mouth with a shrug."
"I’m still hungry, after all."
show vul unamused at eight with dis
"Finally, Vulgor appears on the other side of the glass, looking at me with an accusatory gaze."
"I pause, but his embarrassment makes me chuckle… and then I lose it."
show vul shocked x with dis
"I explode in loud laughter, which causes the male to wave at me in panic."
"It only makes me laugh harder."
"I can’t believe I made this wolf sick just by eating!"
show vul talk ang with dis
v "\"Shhhh! Be quiet!\""
"He shushes me, but I am unable to reign myself in."
show vul growl u with dis
v "\"Shut up, flatface, or I’ll come in there and {i}choke{/i} you again!\""

if Vulgor == 1:
    "He finally growls in playful annoyance."
else:

    "He finally growls in annoyance."

"I hush down, looking at him with a smirk."
m "\"Flatface?\""
show vul growl x with dis
v "\"You really need to keep quiet. If anyone finds you here-\""
m "\"I know, I know…\""
"I roll my eyes."
show vul unhappy x with dis
m "\"But I really think you three are exaggerating a little bit.\""
"I blurt out, causing the black wolf’s eyes to narrow."
m "\"Your people wouldn’t kill me just because I got lost in their woods. I mean, even you understand this isn't right.\""
show vul talk e with dis
v "\"You know nothing, Piglet.\""
show vul unhappy x with dis
"I shrug, continuing to nibble on the meat."
show vul talk with dis
v "\"I’ll only tell you this so that you have no illusions about this not being serious.\""
v "\"Long ago, a Tigerii noble desecrated our grove.\""
show vul unhappy x with dis
m "\"Desecrate how?\""
show vul talk e with dis
v "\"He carved his name into one of the Name Trees.\""
show vul unhappy e with dis
"I narrow my brow, looking at him with confusion."
m "\"Isn't that what a Name Tree is for?\""
m "\"Like a… I’ve been here kinda thing?\""
show vul unhappy x with dis
v "\"No.\""
"He says with a deadly serious tone, his joviality now completely gone."
show vul talk ang with dis
v "\"They are sacred to my people. They supposedly keep the spirits of our ancestors tethered to this world.\""
show vul unamused u with dis
m "\"How does that work?\""
"The wolf waves his paw at me dismissively."
show vul talk ang with dis
v "\"It doesn’t matter.\""
show vul talk p with dis
v "\"What does matter is that we issued punishment, as was our right, despite knowing it would cause a war… a war we had little hope of winning.\""
show vul neutral with dis
m "\"Wait, you {i}killed{/i} someone just because of graffiti?\""
show vul talk e with dis
v "\"Maybe, if you live long enough, you will understand.\""
show vul talk with dis
v "\"For now, just accept that to us damaging a Name Tree is one of the worst crimes one can commit.\""
show vul neutral with dis
"I shake my head in disbelief."
m "\"Was it really worth starting a war over?\""
show vul growl with dis
v "\"We didn’t start it. The Tigers did.\""
m "\"Because you killed one of their own over something so-\""
show vul growl u with dis
v "\"Don’t talk about things you have NO understanding of!\""
show vul unamused u with dis
"He raises his voice ever so slightly, as he stifles a growl."
"Those trees are definitely a sore spot for the wolves."
show vul talk e with dis
v "\"Our world ceased to exist long, long ago. Otherkin saw to it.\""
show vul talk p with dis
v "\"This forest and our traditions are all we have left of what was lost.\""
show vul unhappy with dis
"I can detect an odd twinge of sadness and longing in his voice, something I’ve never heard before from the male."
show vul talk ang with dis
v "\"The wolves will go to any lengths to protect what’s left, even if it means going to war.\""
show vul talk pu with dis
v "\"If anyone learns that you’re here… a lynch mob would’ve torn you to shreds before any of us had a chance to react.\""
show vul neutral with dis
"I stop eating, feeling the weight of his words finally sink in."
"Despite not really understanding the full context of what he said, it’s clear that the wolves hate Otherkin."
m "\"I’m sorry.\""
m "\"I didn’t mean to upset you.\""
"The black male looks at me with annoyance for a moment, before exhaling heavily."
show vul talk e with dis
v "\"Just... take this seriously. It's enough that Ranok makes light of the situation.\""
show vul talk ang with dis
v "\"I don’t want to lose my Moon Brother. Not because of-\""
show vul worried with dis
"He cuts himself off, looking at me with almost apologetic gaze."
m "\"…me.\""
"I finish the sentence for him, although I’m sure he meant to use some sort of an insult."
show vul talk e with dis
v "\"It’s nothing personal.\""
show vul neutral with dis
m "\"I know. And I’ll be careful.\""
m "\"Believe me, I do not have a death wish.\""
show vul smile with dis
"The black wolf smirk at me, most likely trying to lighten the situation."
show vul talk s with dis
v "\"Oh? Well, you could’ve fooled me.\""
show vul talk l with dis
v "\"I better go. If I stay much longer, others will wonder where I disappeared to.\""
show vul shocked with dis
m "\"Vul…\""
show vul unamused u with dis
"He throws me a surprised gaze and I can see his brow narrow slightly in annoyance."
"Should’ve used his full name but fuck it."
m "\"Thanks.\""
show vul unhappy with dis
v "\"Hmph.\""
hide vul unhappy with dis
"He shrugs, leaving me alone and I return to the bed."
stop music fadeout 6.0
scene bg broom_night with dis
play sound "sfx/bed_jump.ogg"
"I plop onto the mattress, bouncing up and down a bit, trying to calm myself down."
"I really hope I didn't annoy him as much as it seemed I did…"
"The delicious, meaty smell that drifts through the air from the parcel invites me to dig in once again."
"My mood instantly lifts, if only slightly, as I bite into another succulent cut."
"It’s tasty, but I really wouldn’t mind having something else to go with it."
"…"
"Bread!"
"I close my eyes, instantly smiling upon the recollection of what bread is."
"The crunchy rim of a freshly baked loaf… the smell of it as it comes out straight from the oven."
"How do I even know these things?"
"I shrug, continuing to eat."
"No point dwelling on it, if I can’t really do anything about it."
"Ranok’s right; everything will be revealed in time."
"If I can randomly remember what bread is, I’m sure I’ll remember something more tangible from my previous life."
m "\"Previous life…\""
"I stop chewing and chuckle, considering what I’m actually saying."
"Whatever happened before these wolves found me seems completely seperated from who I am now."
"Almost as if I've been severed from my past."
"I look at the crumpled cloth containing my dinner."
"I only ate half of it, if not less."
"The portion is generous, true, but I also lost my appetite."
"What is exactly going on with me?"
"I have no idea."
"I fold the cloth back up, deciding to keep the rest of the meat for later."
"Slowly, I approach the small dresser, the very same one I had climbed when I first set my eyes on Vulgor."
"My feet brush an object across the floor and I notice the comb still lying there."
"I pick it up with a smile, remembering my defiant stand against the black wolf."
play sound "sfx/drawer_open.ogg"
"With a shrug, I open the drawer from which I retrieved it and place it back in there."
"I shut it, not even looking inside; I’m a guest here, I shouldn’t pry."
"Gently, I set the parcel down on the flat top, and turn to approach the door."
"From what I understand this house has at least one more room."
"I’m curious to see it."
"I put my ear to the door, trying to determine if anyone’s there."
m "\"Ranok?\""
"I mutter, mostly to confirm what I already know."
play sound "sfx/door open.ogg"
show door_n with dis
"I slowly crack the doors open, to see what’s actually behind them."
scene bg kitchen_night with dis
"The room is similar in size to the bedchamber I woke up in, however it has two windows instead of one."
"I can see the orange glow of a large bonfire coming from outside and I hear the sound of wolves talking and laughing."
"It almost makes me want to approach the window and have a look, but I realise I’d be immediately spotted."
"My pale skin would reflect the glow of the fire making me look like a ghost behind the glass."
"I sigh and instead look around the room properly."
"There’s a table with a set of chairs, another cupboard, and a large fireplace."
"All of it looks comfy, but incredibly rustic."
"Huh… another thing I know."
"This is an incredibly old-timey looking house… though what a normal house should look like… I can’t recall."
"I frown, realizing there is no other bed, there’s only a stack of blankets in front of the hearth."
"Ranok gave me his own bed."
"I approach his makeshift bedding, crouching down beside it."
"I can tell it was slept in recently, strands of grey fur dotting the fabric."
"How long was I out before I woke up for the first time?"
"A shadow moves by the front window, causing me to drop to my knees, hiding out of sight."
"There’s a lot of movement outside, so the village is still up and going despite the darkness."
"I can’t tell the time, though."
"The passage of time is almost impossible to work out here, and although I don’t know why, not being able to measure it fills me with incredible frustration."
"Why would I feel the need to know what time it is; night is night."
"Where does the idea to even measure it comes from?"
"I shake my head."
"All of this is giving me a massive headache."
"I look around to find something to wash the meat down and find a jug on the table."
"I grab a cup and pour myself a glass."
"Taking a reluctant sip, I half expected wine or ale, but thankfully it's just plain water."
"I empty the entire cup thirstily, pouring myself another round. "
"I almost feel as if I’m having a drink for the first time in my life…"
m "\"Fuck… so weird…\""
"I gasp, finally having my fill."
"At some point I will have to use the toilet, however I can clearly see there’s none in the house."
"I wince, realising that most likely there’s an outhouse somewhere in the back… not only does that seem spartan, but also… I’m not allowed to leave."
"I guess I’ll have to hold it in for a bit… luckily my body feels utterly empty, so I don’t need to go just yet."
"Hopefully, everything will be settled before I do, and I’ll be able to get out…"
"The only thing worse than an outhouse would be a chamber pot."
"I cringe, shivering at the thought."
"Nope."
"I decide to return to my bed."
scene bg broom_night
show door_n
with dis
"Ranok is most likely occupied, and hearing how merry everyone is outside, this might take a while."
play sound "sfx/door close.ogg"
hide door_n with dis
"I close the doors to the bedroom behind me and approach the bed."
"Sound of faint music reaches my ears; it's very upbeat and almost invites one to dance."
"The feast seems to be quite a party, a pity I have to miss it."
"I allow myself to sway in the rhythm, moving from one leg to another almost as if remembering something I used to do once upon a time."
"I must look incredibly foolish."
"I drop onto the mattress chuckling, filled with a little bit of nostalgia."
"Just sitting on the bed makes me incredibly tired."
"I yawn uncontrollably."
"I’ve been out for at least a day, considering Ranok had to sleep on the floor."
"Then why am I so exhausted?"
"Staying awake doesn't come naturally to me."
"My eyelids become incredibly heavy again, and I feel as if I am wrapped in a warm, snug embrace."
"It must be the meal I ate, so much meat is quite heavy for your stomach."
"That must be it – I’m just getting drowsy from eating."
stop ambience fadeout 6.0
"I rest my head on the pillow and close my eyes… allowing myself to drift away into that familiar nothingness."
scene bg black with slow_dissolve
play music "music/entity.ogg" fadein 6.0
"But it isn’t nothingness."
"This time I don’t lose awareness."
"Panic grips at my heart as I realise that I’m back where I was at the beginning of all of this."
"NO!"
"I don’t want to feel this again!"
"My body begins to fade into oblivion, all senses abandoning me aside from my consciousness."
"That’s when the familiar voice returns, a multitude of words spoken all at once."
"I want to scream, but all I can do is simply think."
"WHAT DO YOU WANT?!"
with vpunch
w "\"...one chance...\""
"I feel a searing pain within my soul, as if the words hurt me."
with vpunch
w "\"...stop...\""
"My whole being is screaming in unimaginable agony."
"NO, {i}YOU{/i} STOP IT!"
"I demand, unable to contain myself in this pit of despair."
with vpunch
w "\"...too late...\""
"I want to fight back, but each word pushes me closer and closer to the brink of madness."
"I don’t know whether the voices stop themselves, or did I simply give in, but after the last wave of pain I pass out."
"Everything returns to that familiar feeling of abandon."
stop music fadeout 6.0
scene bg black with slow_dissolve
"Not a single dream reaches me, or at least that’s what I think."
"It’s as if I drifted away on the pillow, filled with a delicious meal, and everything simply paused."
"However, I can’t shake off this odd feeling of dread."
"I feel… something ominous at the edge of my consciousness."
"I feel like I’m being…"
"…watched."
"A creaking plank stirs me from my sleep."
play sound "sfx/floor_creak.ogg"
scene bg broom_night
show door_n
with slow_dissolve
play ambience "ambience/forest_night.ogg" fadein 6.0
"I open my eyes in a panic, seeing nothing but darkness before me. "
"I quickly locate the window, trying to confirm I haven’t returned to the void."
"It’s simply night and I’m still here… in this strange world filled with talking wolves."
"Another creek causes me to jump up."
m "\"W-who’s there?\""
"A shadow of a large beast moves slightly, sitting at the foot of my bed, its eyes glistening in the dark."
"My blood freezes and I’m about to scream when a hint of light betrays a familiar grey coat."
show ran p smile with dis
m "\"Ranok!\""
show ran p shocked with dis
m "\"God! Why?!\""
"I squeak out in both relief and panic."
show ran p shrug with dis
r "\"Couldn’t sleep…\""
"The wolf shrugs casually."
show ran p talk x with dis
r "\"And I wanted to get to know you better, without others hanging onto our every word.\""
show ran p smile x with dis
m "\"And you intend to do that by creeping onto the bed in the middle of the night?\""
show ran p awkward with dis
r "\"Was held up longer than expected.\""
"Ranok gives me a goofy smile, as if he doesn’t understand why this could be unsettling."
show ran p smile x with dis
m "\"It’s the middle of the {i}night{/i}.\""
"I try to reiterate."
m "\"You’re a {i}wolf{/i}.\""
show ran p talk x with dis
r "\"Yes... and you’re a human. We've established that already.\""
show ran p smile x with dis
m "\"My point exactly.\""
"He gives me another naïve smile, causing me to sigh in resignation."
m "\"Most humans would find this whole setup extremely terrifying.\""
show ran p smirk with dis
r "\"Most wolves would find {i}you{/i} extremely terrifying.\""
"The grey wolf retorts teasingly."
show ran p shocked x with dis
m "\"Disgusting, maybe.\""
"I smirk, rolling my eyes as I recall Vulgor’s earlier reaction."
show ran p talk x with dis
r "\"I don’t find you disgusting!\""
"He protests laughing."
show ran p smile s with dis
r "\"Do you find me terrifying?\""
"He grins, playfully baring his fangs at me, but I try not to flinch."
"I’m not really sure what answer he expects, but I decide to be honest."
m "\"I… do?\""
show ran p wink with dis
r "\"Good.\""
"He nods with satisfaction."
show ran p talk x with dis
r "\"What good is a wolf if a tiny human doesn’t fear him?\""
"He laughs, widening his smile and jokingly punching my shoulder."
show ran p smile x with dis
m "\"You want me to fear you?\""
"I ask teasingly, drawing a mischievous growl from Ranok’s throat."
"Despite it being just a game, it did startle me, but I keep my composure."
"Or so I think, because Ranok simply laughs at me, his tail swooshing on the bed in glee."
show ran p laugh with dis
r "\"Doesn’t take much to get your heart pumping, does it?\""
show ran p smile x with dis
"Fuck… I forgot that he has a heart rate monitor in his head."
"Wait… what?"
play sound "sfx/heart_monitor.ogg" fadein 3.0
"Just for a moment, I can almost hear a rhythmic beeping before it vanishes into nothingness."
stop sound fadeout 3.0
"I heard it before… just before everything went black."
"Before I woke up in this room!"
scene bg black with dis
ow "\"To die so young…\""
scene bg broom_night
show door_n
show ran p smile x
with dis
m "\"I think I died...\""
show ran p shocked x with dis
"The wolf blinks, completely thrown off by my remark."
show ran p smile sp with dis
r "\"Is that your usual pick up line?\""
show ran p smile with dis
"Ranok smirks slyly, his tail slapping the bed in anticipation."
"This time I'm the one blinking."
m "\"What?\""
show ran p smile sp with dis
r "\"{i}‘I think I died and went to heaven?’{/i}\""
"He grins flirtatiously, sliding closer towards me."
show ran p shocked with dis
m "\"What? NO!\""
"I protest, pushing myself away."
show ran p embarrassed with dis
m "\"What’s {i}wrong{/i} with you?\""
m "\"None of this is funny!\""
"I almost shout out in annoyance."
"I know I’m not angry at him, I don’t even understand why I’m angry in the first place, but…"
show ran p sad with dis
"I feel… as if I’m mourning my own passing."
"I couldn’t be dead… but then… where the hell am I?"
"What the fuck is going on?"
"I look at him wide-eyed, feeling as they swell with tears."
"The wolf moves back to his original spot, looking defeated."
"He’s slouching with ears folded back, and his tail tucked to the side."
show ran p sad t with dis
r "\"I’m sorry… I-I didn’t-\""
show ran p sad with dis
m "\"You act like this is fun and games, but I am {i}truly{/i} terrified!\""
"My voice cracks as my mind races out of control."
"I’m at the edge of the abyss, just a step away from falling back into that dark hole."
m "\"I’m really scared!\""
"The wolf stands up, causing the mattress to perk back up as his weight disappears."
show ran p sad t with dis
r "\"That much is… clear.\""
show ran p sad with dis
"He mutters sorrowfully."
"He sulks towards the door, obviously taking my outburst to heart."
"Ever since I woke up in this strange world, he’s been nothing but kind and caring towards me."
"Even through my memory loss, deep in my heart I know it’s something I rarely experienced."
"It’s not fair for him to feel dejected just because I’m paranoid."
show ran p sad te with dis
r "\"I’ll leave you be.\""
"With a solemn expression, he grabs the doorhandle, intent to give me space."
show ran p shocked with dis
m "\"Wait!\""
"His brow raises at my sudden request."
show ran p sad with dis
m "\"I’m… really sorry! I didn't mean to explode like this...\""
m "\"Please, don’t leave me alone… not now…\""
"He tilts his head in bewilderment at my pleading expression."
show ran p sad t with dis
r "\"I thought you didn’t want me here.\""
show ran p shocked x with dis
m "\"No, I do! I {i}really{/i} do!\""
show ran p sad with dis
m "\"It's just hard to stay in the moment with all the thoughts spinning in my head.\""
m "\"I think that’s why I’m sleeping so much…\""
m "\"To get a break.\""
play sound "sfx/door close.ogg"
hide door_n with dis
"He closes the doors and hastily returns to my side."
show ran p sad t with dis
r "\"What happened?\""
show ran p sad with dis
m "\"I had… not a memory, but… something flashed through my mind.\""
m "\"It really spooked me.\""
show ran p sad t with dis
r "\"I can see that.\""
show ran p sad with dis
"The wolf sits down next to me, his fur brushing against my skin; it's soft and inviting."
"He looks at me inquisitively, but I only sit there, struggling to maintain my composure."
show ran p smile e with dis
"As I’m about to lose that battle, he reaches around my back and pulls me close into a warm embrace."
"Resisting crosses my mind, but I instantly banish the thought."
"All I want is to feel safe, and for whatever reason… every time he's around he makes me feel just that."
"I surrender myself completely and allow him to cradle me into his chest."
"I try to calm myself down as he idly ruffles my hair."
show ran p neutral te with dis
r "\"What was it?\""
show ran p smile e with dis
m "\"I don’t know… but it makes me feel dead.\""
show ran p talk with dis
r "\"You aren’t dead.\""
show ran p smile with dis
m "\"Certainly doesn’t feel like I am… but still…\""
show ran p smile eh with dis
"I breathe heavily into his chest, his musk and smell of the forest filling my nose."
"He must have been drinking, since I can detect the faint whiff of wine coming from him."
"It’s a calming combination, almost like some sort of inhaling balm."
"His gentle stroking and steady rising and falling of his chest soothes me further."
"Within moments I manage to compose myself, and once I can hear his tail wag again, I gently push myself away from the wolf."
"I sigh, resting my face against my arms in resignation."
show ran p neutral with dis
m "\"This whole thing is so messed up!\""
show ran p sad with dis
"I feel him place a paw on my head."
m "\"I feel so vulnerable…\""
"He ruffles my hair softly, the paw’s weight matching the feeling in my gut."
show ran p sad t with dis
r "\"It’s okay. You know that none of us would hurt you, right?\""
show ran p sad with dis
m "\"That’s not it.\""
"I find myself looking up, his paw still gently stroking my head, as my blurry eyes meet his."
show ran p sad e with dis
m "\"You keep saying that everything is going to be fine, but none of this {i}is{/i} fine.\""
m "\"I don’t know who I am… who {i}you{/i} are.\""
"I stretch out my arms as if trying to encompass the entire world."
m "\"You say that talking wolves are normal… that there are other beastfolk out there… like it’s something obvious.\""
"I look down at my twitching leg."
m "\"All of this is news to me… as if I was born yesterday.\""
"Ranok just sits there, petting my head and listening."
"That simple gesture is the most comforting thing I felt since I woke up."
show ran p sad t with dis
r "\"You simply lost your memory. With time, everything will come back to you, I’m sure of it.\""
show ran p smile with dis
"The wolf forces a soft smile onto his muzzle."
"He’s trying to encourage me, but we both know that’s all it is: an encouragement."
m "\"How can you be so sure?\""
show ran p talk with dis
r "\"Because I trust the Ancestors… our paths crossed for a reason.\""
show ran p smile e with dis
"I roll my eyes… "
"I’m not his damn wish away."
"Talking wolves, Ancestors and Name Trees…"
m "\"I feel like I’m dreaming.\""
show ran p neutral t with dis
r "\"Well, even if it is a dream…\""
show ran p neutral with dis
"He cuts off, biting his lip."
"I see his expression shift, as he's thinking something over and the paw on top of my head comes to a stop."
show ran p talk with dis
r "\"Aside from the whole memory loss… is it a bad dream to have?\""
show ran p awkward with dis
r "\"Or am I that much of a nightmare to be around?\""
show ran p smirk with dis
"I look up at his teasing expression and blink."
show ran p smile with dis
"The paw starts to softly ruffle my hair again and I can’t help but chuckle, forcing my welled-up eyes to release two stray tears."
"It’s so surreal, but I have to give Ranok credit: he’s a smooth talker."
m "\"No, you’re not.\""
show ran p smile e with dis
"I scoff and this time he chuckles."
"I envy his light-hearted attitude."
"Even though he faces almost as harsh consequences of this misadventure as I do, he doesn’t seem to mind."
"If anything, he seems very set on protecting me and making me feel safe."
"Once he sees me smile, he withdraws his paw and we sit like that for a moment until I finally break the silence."
show ran p shocked with dis
m "\"Why did you save me?\""
show ran p talk e with dis
r "\"Like I said, the Ancestors guided me towards my path.\""
show ran p smile with dis
"I shake my head."
show ran p shocked with dis
m "\"I’m not a path.\""
show ran p talk e with dis
r "\"First let me walk it and then we’ll decide.\""
show ran p smile with dis
"He smiles slyly."
m "\"You’re betting quite a lot on me.\""
show ran p neutral with dis
r "\"Hm?\""
m "\"If you found me next to your Name Tree, why did you take me in?\""
m "\"Vul told me that your people are willing to go to war over them.\""
"Ranok laughs."
show ran p embarrassed with dis
r "\"Don’t call him Vul to his muzzle unless you want to be choked again.\""
"He pauses, thinking over what I said."
show ran p neutral tr with dis
r "\"As for the tree…\""
show ran p talk e with dis
r "\"...you didn’t harm it.\""
show ran p shocked with dis
m "\"But what if it was harmed…?\""
show ran p embarrassed with dis
"I pose a question, despite being troubled by what his answer may be."
r "\"It wasn’t.\""
m "\"Hypothetically…\""
m "\"What if whoever left me in the forest damaged it? And I was only collateral...\""
m "\"What would you do then?\""
show ran p eyeroll with dis
r "\"I don’t want to talk about it.\""
show ran p annoyed e with dis
m "\"Just answer the question.\""
"Ranok looks away, clearly disturbed by the scenario."
"His ears splay back as he struggles to give me an answer, but the silence speaks for itself."
"Had someone damaged the tree, I would pay the price."
"Despite my worst suspicion being confirmed, I’m glad the wolf at least is being honest with me."
m "\"I’m not offended… just saying that our situation is quite circumstantial.\""
m "\"For something you believe to be fated, a lot of things could have played out differently.\""
"The wolf looks at me with an irritated expression."
show ran p annoyed tp with dis
r "\"Why do you do this?\""
r "\"I saved you, didn’t I?\""
show ran p annoyed with dis
"He clearly doesn’t enjoy this little mental exercise."
m "\"Because if the tree {i}was{/i} damaged, you wouldn’t have.\""
m "\"And if that’s the case, it’s hard for me to see this as fate.\""
show ran p annoyed tp with dis
r "\"You’re reading too much into this.\""
show ran p annoyed with dis
m "\"I’m not! Had I damaged the tree, even by accident, you would’ve killed me!\""
"The wolf finally stands up, snarling at me with genuine anger, his muzzle baring his fangs like I never seen before."
show ran p growl with dis
r "\"Yes, I would’ve {i}killed{/i} you!\""
show ran p growl p with dis
r "\"Is that what you WANT to hear?!\""
show ran p with dis
"I pull away from him in fear."
"I can’t bare seeing him like this – like the feral beast he actually is."
show ran p sad with dis
"Noticing my reaction, the wolf’s expression softens, and his fangs hide behind a remorseful expression."
show ran p sad e with dis
"He sighs in resignation and silence falls over us."
show ran p neutral with dis
"Eventually, Ranok smiles at me, giving me a patronising look."
show ran p neutral t with dis
r "\"That’s what fate is though, isn’t it? A lot of things falling into place in just the right way.\""
show ran p smile with dis
"I roll my eyes again, I guess that’s something I’m going to do a lot around this wolf."
"There is no point in arguing about this, he’s too set in his ways."
m "\"I still don’t understand why you would be willing to kill someone over a tree…\""
show ran p neutral t with dis
r "\"There’s more to it than that.\""
show ran p sad with dis
"His expression sours."
m "\"Well, then… enlighten me!\""
"Ranok looks at me concerned, as if unsure if he should elaborate on the subject. "
m "\"Please?\""
show ran p smile eh with dis
"He nods reluctantly, sitting back on the bed but keeping appropriate distance."
show ran p talk with dis
r "\"Whenever a pup is born, we plant a special sapling within the grove.\""
r "\"It’s fashioned from the seeds of their parent’s Name Trees.\""
show ran p shocked with dis
m "\"How does that work?\""
show ran p smile with dis
"I can see a cheeky grin paint on the grey wolf’s muzzle."
show ran p smirk with dis
r "\"Well… when a mommy tree loves daddy tree very, very much-\""
show ran p laugh x with dis
m "\"Oh, fuck off!\""
"I scoff through a chuckle accompanied by Ranok's laughter."
show ran p awkward with dis
r "\"Well, what do you want me to say?\""
"He barks out defensively."
show ran p smile with dis
m "\"Sorry that I don’t know how you make tree babies!\""
show ran p talk e with dis
r "\"It’s simple, really. You just pollinate a seed of one tree with the other.\""
show ran p smile with dis
m "\"Uh-huh, and then what?\""
"I’m certain I have a very confused look on my face, as the wolf regards me with mild frustration."
show ran p bemused t with dis
r "\"You just plant it.\""
show ran p talk with dis
r "\"As the pup lives long enough to earn a name, that name is then carved into his growing tree.\""
show ran p talk r with dis
r "\"When we die, we are buried beneath them, so that we can become one. This allows our spirits to stay in this world a little while longer, to guide our people.\""
show ran p talk e with dis
r "\"As long as the tree lives, our Ancestors are still with us.\""
show ran p smile with dis
"I take a moment to digest the information."
m "\"So that’s what Vul meant by saying the Ancestors reside inside of them. It’s their resting place.\""
show ran p shocked with dis
"The grey wolf blinks, looking at me in shock."
r "\"Vul talked about it?\""
show ran p awkward with dis
r "\"I’m surprised… he doesn’t open up to just anyone about spiritual stuff.\""
show ran p smile with dis
"I’m not sure if he’s trying to make me feel better or speaking the truth about the black male."
"Despite Vulgor’s earlier actions, I’m already warming up to him and I’d like to think that he’s starting to warm up to me in turn."
"We sit like this for a moment in silence, but I don’t mind."
"His presence alone is enough to put me at ease, or at least as much at ease as he himself is."
"Despite sitting next to each other, I have to look up to meet his gaze; his form towering above mine."
show ran p shocked with dis
m "\"If…\""
show ran p sad with dis
"I say slowly, thinking back to the dark void which held me so enviously before I opened my eyes."
"It almost feels as if it’s still here somewhere, hiding at the edges of my vision and waiting to reclaim me."
"The persistent thought of me actually being dead doesn’t help either..."
"…perhaps those are just last imaginings of my slowly fading mind."
"What a horrible thought."
m "\"If this is just a dream…\""
show ran p shocked with dis
m "\"…then I’m not sure I want to wake up.\""
show ran p talk e with dis
r "\"Then don’t.\""
show ran p smile eh with dis
"He closes his eyes, smiling."
"Everything is so simple for him."
show ran p smile with dis
m "\"I feel like I don’t have a choice in the matter. I’ve lost all sense of agency.\""
show ran p smile r with dis
"The wolf looks at me with a worried expression, but then proceeds to look at the window."
"We sit like this for a moment and I find myself staring at the world outside."
"The calm of the night claimed the forests and the moonlight bathes it in hues of midnight blue."
show ran p talk with dis
r "\"Maybe it’s the exact opposite.\""
show ran p smile with dis
"I look up at the wolf, confusion obviously painted on my face."
show ran p talk r with dis
r "\"You have a clean slate. You can start life anew. No mistakes of the past to weigh you down. No attachments, no strings.\""
show ran p smile r with dis
"I narrow my brows, almost feeling as if he made light of my circumstance."
show ran p shocked with dis
m "\"Would you trade places with me, then?\""
show ran p talk e with dis
r "\"I would.\""
show ran p smile with dis
"He says without hesitation."
"I blink, caught off guard by the statement; it sounded almost sincere."
show ran p talk with dis
r "\"I’ve made many mistakes in my life, and my future was already decided long before I was born.\""
show ran p talk r with dis
r "\"I knew who I would be, when and who I had to mate with… everything predetermined without my say.\""
show ran p laugh x with dis
r "\"You’re the first actual choice I had.\""
show ran p smirk with dis
r "\"Who’s without agency here?\""
"He forces a challenging smirk and I reciprocate it with a smile."
show ran p shocked with dis
m "\"Wait… {i}mate{/i}?\""
"I cough, surprised that I actually asked that out loud."
"Ranok looks at me with a bit of confusion, but quickly laughs loudly."
show ran p lol with dis
"I look at his massive jaw, teeth glittering in the dim light of the moon."
"It used to send shivers down my spine, but now it makes me smile in amazement."
show ran p smirk with dis
r "\"Funny how that’s the only thing that stuck out to you.\""
"I cough, pulled back into the conversation."
show ran p wink with dis
"Oh god."
show ran p smile with dis
"My face flushes red as I realise what he just implied."
m "\"It was the odd one out!\""
show ran p talk e with dis
r "\"Right…\""
show ran p smile with dis
"He muses, looking at me teasingly."
m "\"Honestly! I don’t know anything about your… traditions.\""
show ran p smirk with dis
r "\"I could teach you.\""
"I bite my lip, sensing a trap."
show ran p smile with dis
"But at the same time, learning their customs isn’t such a bad idea."
"Especially if I were to stay here until I get better."
"{i}If{/i} I were to get better."
"And hey, might even jog some of my memories."
"I finally smile, nodding."
show ran p shocked with dis
m "\"Ok. Teach me.\""
show ran p talk e with dis
r "\"Well, we are set up to mate with a compatible peer in our childhood. Once we come of age, we-\""
m "\"NOT THAT!\""
show ran p laugh x with dis
"The heat rises to my cheeks, and I try to shoo away the mental image of him having sex."
show ran p smile with dis
"Oh god… now it’s in my head."
"I feel my face burning up and hide it in my palms as the wolf laughs merrily."
m "\"I meant the culture!\""
"I mumble, still guarding my face from ridicule."
show ran p talk with dis
r "\"Well, it is our culture.\""
show ran p smirk with dis
r "\"Might even say one of its most important aspects.\""
"Can’t argue with that."
show ran p smile with dis
m "\"So…\""
"I finally manage to compose myself."
"I’m not a child anymore, I shouldn’t act like one; giggling and blushing upon hearing a no-no."
"I raise my head and look up at Ranok."
m "\"You basically grow up knowing who you’ll have to… be with?\""
show ran p talk e with dis
r "\"I know you humans do things differently. We don’t stay with our mates.\""
show ran p talk r with dis
r "\"We generally just mate to produce the most desirable offspring, to further the tribe.\""
show ran p smile with dis
"He states matter-of-factly."
"The thought of living like that almost makes me feel sad."
show ran p shocked with dis
m "\"Don’t wolves feel… love?\""
show ran p lol with dis
"Ranok laughs again, this time even louder, as if I cracked the best joke he’d heard the entire day."
show ran p talk p with dis
r "\"What does love have to do with it?\""
m "\"It has a lot to me!\""
show ran p shocked with dis
"I blurt out, almost gasping and covering my mouth."
show ran p smile with dis
"Somehow, I manage to reign in that impulse, I don’t want the wolf to misconstrue me."
show ran p talk with dis
r "\"We do love, [mc], but it doesn’t factor into procreation. We mate for the tribe; we love for ourselves.\""
show ran p smile with dis
"I look at him confused."
"It sounds so wrong, yet… do I even have a point of reference?"
"I can’t remember my life before this whole mess… how am I so sure it’s not the case for everyone?"
"However, my gut tells me that this is not what I agree with."
"The wolf looks at me, seeing the gears turning behind my mask of silence."
"He decides to break it."
show ran p talk r with dis
r "\"I know humans take mating seriously. I’ve heard they vow loyalty to each other, which also includes…\""
show ran p smile s with dis
"This time, he bites his lip."
"I almost shiver seeing the fang perk out… but again, the wolf laughs."
show ran p smile sp with dis
r "\"…the carnal side of things.\""
show ran p wink with dis
"This makes me blush again, as the image of me having sex pops into my head."
show ran p smile with dis
"How would that even work?"
"Did I ever have sex?"
show ran p shocked with dis
"I try to imagine the act and I jump up in bed with a yelp, startling the wolf."
r "\"What happened?!\""
show ran p sad with dis
"I turn as red as a bricks, quickly looking away from him."
"Why?"
"Why does my mind do this to me?"
"Why did it show… me… with him?!"
"He’s a talking beast man; what the hell brain?!"
show ran p shocked x with dis
"I shake my head."
show ran p sad with dis
"There’s NOTHING to it, I know there isn’t!"
"I just don’t remember what other people look like… all I know is him!"
"Ugh…"
"Why do I even explain myself to… myself?!"
"I just need to reign my thoughts in, that’s all."
show ran p sad t with dis
r "\"Are you okay? Did you remember something?\""
show ran p sad with dis
"The wolf sounds worried, placing his massive paw on my shoulder."
"The sheer sensation causes me to inexplicably shiver."
show ran p neutral t with dis
r "\"Perhaps you took the vows with someone?\""
show ran p shocked x with dis
m "\"What?\""
show ran p wtf with dis
m "\"NO!\""
"I protest as hard as I can, almost offended at the insinuation."
show ran p awkward with dis
"But quickly my resolve melts away as I realise that I don’t know."
"I have no clue."
"I might have…?"
"I slump back into my hands, struggling to contain tears once again."
show ran p shocked x with dis
m "\"This is so messed up!\""
show ran p sad with dis
m "\"Who even am I?\""
show ran p smile ex with dis
"Out of the corner of my eye I see his big paws surround me, with massive claws at their end."
"My heart skips a beat, but I don’t allow myself to be terrified."
"It wouldn’t be fair, not to him."
"The wolf leans in closer, and again I feel his embrace."
"The warmth of his fur completely envelops me, and I feel his heavy breath brush my hair and fall down my neck."
show ran p talk e with dis
r "\"You’re [mc]. That’s all that matters.\""
show ran p smile with dis
"He murmurs softly, rubbing my back with his paws."
"I chuckle into his chest, feeling so safe in his embrace, as if nothing could happen to me while he holds me close."
show ran p neutral h with dis
m "\"I feel those things… certain truths, but I can’t be certain of them at all.\""
"The wolf still holds me tight in his arms. "
"I wonder if he even hears me through his fur, but he quickly disperses my doubts."
show ran p talk e with dis
r "\"If you feel strongly about anything… don’t doubt it.\""
show ran p smile ex with dis
m "\"Even if I can’t remember?\""
show ran p talk x with dis
r "\"{i}Especially{/i} if you can’t remember.\""
show ran p smile x with dis
"The wolf gently pushes me away, so that our eyes can meet again."
"He has a soft smile; with the most reassuring gaze he can muster."
show ran p talk with dis
r "\"Your feelings are your compass. Follow them.\""
show ran p smile with dis
m "\"Then…\""
show ran p shocked with dis
m "\"I know I never took the vows.\""
show ran p laugh x with dis
"I chuckle, rubbing away the tears."
show ran p smile x with dis
"I look back up towards him and laugh as I realise, I’m taking life advice from a talking wolf, while simultaneously assuring both of us that I’m not taken."
"He smiles back while reaching up to my cheek."
"With one finger, he gently rubs it, clearing a single stray tear that I missed."
"Panic begins to take hold of me as the very same finger ventures towards my eye, claw glistening in the faint light, but I manage to reign my fear."
"Ranok picks up a loose eyelash and presents it to me with a smile."
"Not even knowing why, I just make a wish and blow it away."
show ran p shocked with dis
"The wolf blinks in astonishment and then smiles."
r "\"What was that?\""
show ran p smile with dis
m "\"I don’t know… it’s just something I felt like doing.\""
"Ranok smiles."
show ran p talk with dis
r "\"See?\""
show ran p talk e with dis
r "\"You’ve got a good compass.\""
show ran p smile with dis
"Indeed."
"And if this is all but a dream, then I don’t mind if it lasts a little while longer."
scene bg black with slow_dissolve

jump b1c2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
