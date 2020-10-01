label meet_lit_club:
    stop music fadeout 2.0
    play music t2
    scene bg corridor
    with wipeleft_scene

    "We arrive at school and say goodbye."

    show sayori 1b at t11 zorder 1

    s "Hey [player]."
    mc "Yea?"
    s "Can we try to stay in touch more?"
    s "I’ve really missed you!"
    mc "Don’t worry Sayori I promise you I’ll make more of an effort to see you."

    hide sayori

    "We split off and head to our classes."
    "That settles it."
    "Guess I'm checking out the literature club today."
    
    scene bg class_day
    with wipeleft_scene
    
    "The final bell rings signaling the end of the day."
    "I pack up my stuff and make my way to the classroom Sayori mentioned."
    
    scene bg corridor
    with wipeleft_scene
    
    "I enter the room, and am greeted by a bunch of people in anime merchandise."
    
    scene bg class_day
    with wipeleft_scene
    
    "I consider staying here with my people but eventually apologize and leave the room."
    
    scene bg corridor
    with wipeleft_scene
    
    "I went to 38... not 28."
    "I make my way over to the correct room, and enter."
    
    scene bg club_day
    with wipeleft_scene
    
    show monika 1a at t41 zorder 1
    show sayori 1a at t42 zorder 1
    show natsuki 1a at t43 zorder 1
    show yuri 1a at t44 zorder 1

    "Everyone's heads turn."

    hide sayori
    hide natsuki
    hide yuri

    show monika 1b at t11 zorder 1

    m "Hello, can we help you?"

    "I’d recognize that girl anywhere, as I’m sure anyone else would too."
    "That's Monika, the most popular girl in the school."

    m 1j "Oh, [player]! Glad to see you again!"

    "She says this when she realizes it's me."
    "We did share a class together last year but I'm surprised she remembers me."
    "Sayori looks my way."

    show monika 1a at t21 zorder 1
    show sayori 1a at t22 zorder 1

    # faster way to just switch expressions?

    s "[player] what are you doing here?"
    mc "I'm... actually kind of interested in the club."
    mc "My heart’s not set on joining quite yet but I came to check it out, see if I’d want to stay."

    "At those words Monika and Sayori beam."

    "For the first time I get a good look at the other two girls."

    hide monika
    hide sayori

    show yuri 1a at t11 zorder 1

    "The first one has long purple hair and is tall and slender."
    "She gives me a timid smile."

    hide yuri
    show natsuki 1a at t11 zorder 1

    "The other one is her polar opposite."
    "She’s a short girl with pink hair with half of it in pigtails."
    "It's a very cute style."

    hide natsuki

    Girl 1 "A boy? That’ll ruin the atmosphere of the club!"
    Girl 2 "Natsuki that's rather rude. I for one am glad to have a new member."
    Girl 1 "Hmp I don't think it's rude Yuri. I'm just saying how it is."

    "So as far as I can tell, the short girl is Natsuki and the tall girl is Yuri."

    m "Guys, lets not scare away a potential new member."

    "Monika smiles at me."

    m "Welcome to the literature club! We welcome anyone who is into literature, or even if you're not and just want to expand your horizons!"
    s "[player] is this what you meant when you said we would see each other more this morning."

    "I give her a smile."

    mc "Yep! I totally was thinking of joining before that but that sealed the deal."

    "I notice Sayori begin to tear up."

    s "[player] you’re a great friend."
    mc "Woah, Sayori let’s try not to get too emotional."
    mc "No need to be sad, we can hangout more now!"

    "She sniffles a little and nods."

    mc "Care to introduce me to everyone?"
    s "Well you seem to already know Monika."
    m "Oh yeah, we had a class together last year."
    m "We worked together on some projects from time to time."
    m "He made one of the best partners in the class."
    m "Everyone else was so lazy."
    
    "I smile at this praise."
    "It’s one thing to hear that from someone like Sayori and it’s another to hear it from the most popular girl in the school."
    
    s "Anyways she’s the president of the club."
    s "She handles all the complicated stuff like funding for the club."
    s "We couldn't have asked for a better president."
    
    s "Next up there’s me, the vice president!"
    s "I discuss matters with Monika giving idea’s but most the club decisions are left to her."
    
    s "We also have our first member Yuri."
    s "She was eyeing us hanging up posters and we approached her asking if she wanted to join."
    s "She seemed a little startled but we managed to convince her to sign up."
    s "She's a bit shy so give her time to warm up to you."
    
    "She whispers that last bit in my ear."
    "Yuri gives me a smile."
    
    y "A-again it’s great to have a n-new member."
    
    s "And lastly there’s Natsuki."
    s "She was our last required member."
    s "I met her out in the courtyard and asked her to join."
    s "I somehow managed to get her to."
    s "She’s a bit hostile to new people so don't take it too hard."
    
    "She whispers that last bit to me once again"
    "I give Natsuki a smile."
    "She just looks away."
    
    mc "So what exactly do you guys do in this club?"
    m "Well most of the time we just hang out and talk about what we have been reading or writing."
    m "It's mostly just a place to hang out though and we mostly just do our own things."
    m "Yuri reads her books, me and Sayori talk about the club, and Natsuki reads her m-"
    n "Books. I read my books."
    m "Yeah… Books... Anyways we are glad to have you join!"
    
    "That catches me by surprise."
    
    mc "Hold on I haven’t agreed to join just yet."
    
    "The girls all look at me sadly."
    "Except Natsuki who looks angry."
    
    m "Oh, right. Sorry, I guess I jumped a bit too far ahead."
    s "Ah right sorry for jumping to conclusions [player]... I was just excited."
    
    "Yuri doesn’t say anything she just looks down."
    "Natsuki glares at me."
    
    mc "*Sigh.*"
    
    "I really can't leave them hanging now."
    
    mc "But I guess it can’t hurt to join."
    mc "I don’t really have any other clubs in mind."
    
    "All the girls instantly smile upon hearing this, even Natsuki cracks a little smile."
    
    m "Well, on that note it's getting rather late."
    m "Let's call it for today and all head home."
    m "See you guys tomorrow!"
    
    "Monika quickly leaves likely because she has somewhere to be."
    
    y "I-I’ll be on my way too then."
    
    "She picks up her bag and leaves."
    
    n "See you losers later."
    
    "Natsuki walks out seeming like she almost doesn't want to go."
    "She must really love the club."
    "As I pick up my stuff to leave Sayori pops into my vision."
    
    s "Want to walk home together [player]?"
    
    "I smile at her and decide I'll tease her a little."
    
    mc "Nah."
    s "Wait why not?"
    mc "I just don’t really feel up to it."
    
    "She looks at me with sad eyes and I laugh."
    
    mc "Of course I’ll walk home with you idiot."
    mc "You are my best friend still."
    mc "Even if we have been a bit distant lately."
    mc "I wouldn’t trade our time together for the world."
    
    "She looks at me almost about to cry."
    
    s "Y-you don’t know what that means to me [player]!"
    
    "I smile at her."
    
    mc "Come on let's go home you little idiot."
    
    "I pat her on the head as I walk by."
    "She quickly catches up with me."
    "..."
    
    "We arrive at Sayori’s place and wave goodbye to each other."
    "I head home and do my homework"
    "..."
    
    "It's already 8:00pm by the time I’m done."
    "After eating some instant ramen, I lay in bed and think about the day."
    "I got to reconnect with Sayori, see the lovely Monika, and meet two new girls."
    "I can’t wait to get to know them all more."
    "I’ll have some new friends… that hasn’t happened in a long time."
    "And who knows maybe I'll have a shot at becoming something more."
