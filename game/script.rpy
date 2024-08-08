##############################################################
# Name: Branden Platka                                       #
# Student ID: 41122535                                       #
# Start Date: 6/4/2024                                       #
# End Date: TBD  still in progress                           #
# CST8333 Programming Language Research Project              #
# Instructor: Duncan Anderson                                #
##############################################################


define mc = "???"
define mc_hp = 5
define attack = 0
default boss_attack = 3
define skill_used = False
define mc_hp_max = 5
default mcb = Character(mc, mc_hp, mc_hp_max, attack)
default boss1 = Character("???", 80, 80, boss_attack)
define background_music = "audio/Darkened_Echoes.mp3"
define fountian_music = "audio/Fountain_of_Healing.mp3"
define door_open_sf = "audio/metal-door-creaking.mp3"
define door_close_sf = "audio/metal-door-slam.mp3"
define orb_break_sf = "audio/orb-break.mp3"
define locked_door_sf = "audio/trying-to-open-a-locked-door.mp3"
define boss_music = "audio/Eclipsed-Memory-Duel.mp3"
default pastlabel = ""
default memorie_1 = False
default memorie_2 = False
default memorie_3 = False
default weapon = "Cower!"
default skill = "Cry!"

default mf1 = 0
default mf2 = 0
default mf3 = 0
image bg dh = im.Scale("images/dungeon_hallway.png", 1920,1080)
image bg dh_s_l = im.Scale("images/dungeon_hallway_straight_left.png", 1920,1080)
image bg dh_s_r = im.Scale("images/dungeon_hallway_straight_right.png", 1920,1080)
image bg dh_l_r = im.Scale("images/dungeon_hallway_left_right.png", 1920,1080)
image bg dh_de = im.Scale("images/dungeon_hallway_end.png", 1920,1080)
image bg dh_r = im.Scale("images/dungeon_hallway_right.png", 1920,1080)
image bg dh_l = im.Scale("images/dungeon_hallway_left.png", 1920,1080)
image bg dh_i = im.Scale("images/dungeon_hallway_intersection.png", 1920,1080)
image bg dh_h = im.Scale("images/dungeon_hallway_healing.png", 1920,1080)
image bg dh_d = im.Scale("images/dungeon_hallway_door.png", 1920,1080)
image bg game_over = im.Scale("images/black.png", 1920,1080)
image bg Chapter_2 = im.Scale("images/Chapter2.png", 1920,1080)


# The game starts here.

label start:
    
    play music background_music loop
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg dh

    mc "Where am I? It's cold, and damp. How did I get here?"

    $ mc = renpy.input("Wait who am I? Why can't I remember... think ... think...")


    if mc == "":
        $ mc = "Jack"
    mc "Thats right my name is [mc]!"
    mc "What should I do?"
    show screen character_status()

    menu:
        
            "Press on I need to get out of here!": 
                $ direction = "straight"
            "I can't think of anything. It's so cold... I am just going to lie back down this must be a dream!":
                $ direction = "end"

    if direction == "straight":
        mc "I think I see a door ahead someone else must be here, or at least an exit"
        play sound door_open_sf
        pause 5.0
        $ pastlabel = "start"
        jump h_7_12
    else:
        $ pastlabel = "start"
        jump game_over

label h_7_12:
    scene bg dh
    if pastlabel == "start":
        $ pastlabel = "h_7_12"
        play sound door_close_sf

        "The door slams behind you after you exit, [mc] tries the door, it looks locked"
        mc "Looks like I can't go back. I better explore this place, I need to get out! I have to get to... to..."
        "A sharp pain enters your mind. What were you trying to say?"
    
        menu:
            "Let's go":
                $ direction = "straight"
        
        if direction == "straight":
            jump h_7_11
    else:
        $ pastlabel = "h_7_12"

        play sound locked_door_sf
        "The door is still locked."

        menu:
            "Let's go":
                $ direction = "back"

        if direction == "back":
            jump h_7_11

label h_7_11:

    if pastlabel == "h_7_12":
        $ pastlabel = "h_7_11"
        scene bg dh_s_l

        "The path splits here"
        mc "Hmmm... Should I go left or straight"

        menu:

            "Lets go left":
                $ direction = "left"
            "Lets keep going straight":
                $ direction = "straight"
            "Or I could head back?":
                $ direction = "back"

        if direction == "left":
            jump h_6_11
        elif direction == "straight":
            jump h_7_10
        else:
            jump h_7_12

    elif pastlabel == "h_6_11":
        $ pastlabel = "h_7_11"
        scene bg dh_l_r

        "The path splits here"
        mc "Hmmm... Should I go left or rightt"

        menu:

            "Lets go left":
                $ direction = "left"
            "Lets go right":
                $ direction = "right"
            "Or I could head back?":
                $ direction = "back"

        if direction == "left":
            jump h_7_10
        elif direction == "right": 
            jump h_7_12
        else:
            jump h_6_11 

    else:
        $ pastlabel = "h_7_11"
        scene bg dh_s_r

        "The path splits here"
        mc "Hmmm... Should I go lright or straight"

        menu:

            "Lets go right":
                $ direction = "right"
            "Lets keep going straight":
                $ direction = "straight"
            "Or I could head back?":
                $ direction = "back"

        if direction == "right":
            jump h_6_11
        elif direction == "straight": 
            jump h_7_12
        else:
            jump h_7_10 


label h_6_11:
    scene bg dh
    if pastlabel == "h_7_11":
        $ pastlabel = "h_6_11"
                
        menu:

            "Lets keep going straight":
                $ direction = "straight"
            "Or I could head back?":
                $ direction = "back"

        if direction == "straight":
            jump h_5_11
        else:
            jump h_7_11
    else:
        $ pastlabel = "h_6_11"
        menu:

            "Lets keep going straight":
                $ direction = "straight"
            "Or I could head back?":
                $ direction = "back"

        if direction == "straight":
            jump h_7_11
        else:
            jump h_5_11


label h_5_11:

    if pastlabel == "h_6_11":
        $ pastlabel = "h_5_11"
        scene bg dh_s_r

        menu:

            "Lets keep going straight":
                $ direction = "straight"
            "Looks like there is a path to the right as well":
                $ direction = "right"
            "Or I could head back?":
                $ direction = "back"

        if direction == "straight":
            jump h_4_11
        elif direction == "right":
            jump h_5_10
        else:
            jump h_6_11

    elif pastlabel == "h_5_10":
        $ pastlabel = "h_5_11"
        scene bg dh_l_r

        menu:

            "Looks like there is a path Left":
                $ direction = "left"
            "Looks like there is a path to the right as well":
                $ direction = "right"
            "Or I could head back?":
                $ direction = "back"

        if direction == "left":
            jump h_6_11
        elif direction == "right":
            jump h_4_11
        else:
            jump h_5_10
    else:
        $ pastlabel = "h_5_11"
        scene bg dh_s_l

        menu:

            "Looks like there is a path Left":
                $ direction = "left"
            "Striaght ahead!":
                $ direction = "straight"
            "Or I could head back?":
                $ direction = "back"

        if direction == "left":
            jump h_5_10
        elif direction == "straight":
            jump h_6_11
        else:
            jump h_4_11

label h_5_10:

    scene bg dh_de

    menu:

        "Looks like a dead end, have to turn around":
            $ direction = "back"
    $ pastlabel = "h_5_10"
    jump h_5_11


label h_4_11:

    scene bg dh
    if pastlabel == "h_5_11":
        $ pastlabel = "h_4_11"
        menu:

            "Lets keep going straight":
                $ direction = "straight"
            "Or I could head back?":
                $ direction = "back"

        if direction == "straight":
            jump h_3_11
        else:
            jump h_5_11
    else:
        $ pastlabel = "h_4_11"

        menu:

            "Lets keep going straight":
                $ direction = "straight"
            "Or I could head back?":
                $ direction = "back"

        if direction == "straight":
            jump h_5_11
        else:
            jump h_3_11


label h_3_11:

    scene bg dh
    if pastlabel == "h_4_11":
        $ pastlabel = "h_3_11"

        menu:

            "Lets keep going straight":
                $ direction = "straight"
            "Or I could head back?":
                $ direction = "back"

        if direction == "straight":
            jump h_2_11
        else:
            jump h_4_11

    else:
        $ pastlabel = "h_3_11"
        menu:

            "Lets keep going straight":
                $ direction = "straight"
            "Or I could head back?":
                $ direction = "back"

        if direction == "straight":
            jump h_4_11
        else:
            jump h_2_11

label h_2_11:

    if pastlabel == "h_3_11":
        $ pastlabel = "h_2_11"
        scene bg dh_r

        menu:

            "Lets go right":
                $ direction = "right"
            "Or I could head back?":
                $ direction = "back"

        if direction == "right":
            jump h_2_10
        else:
            jump h_3_11

    else:
        $ pastlabel = "h_2_11"
        scene bg dh_l
        menu:

            "Lets go left":
                $ direction = "left"
            "Or I could head back?":
                $ direction = "back"

        if direction == "left":
            jump h_3_11
        else:
            jump h_2_10


label h_2_10:
    scene bg dh
    if pastlabel == "h_2_11":
        $ pastlabel = "h_2_10"
        menu:

            "Lets go straight":
                $ direction = "straight"
            "Or I could head back?":
                $ direction = "back"

        if direction == "straight":
            jump h_2_9
        else:
            jump h_2_11

    else:
        $ pastlabel = "h_2_10"
        menu:

            "Lets go straight":
                $ direction = "straight"
            "Or I could head back?":
                $ direction = "back"

        if direction == "straight":
            jump h_2_11
        else:
            jump h_2_9


label h_2_9:
    scene bg dh
    if pastlabel == "h_2_10":
        $ pastlabel = "h_2_9"
        menu:

            "Lets go straight":
                $ direction = "straight"
            "Or I could head back?":
                $ direction = "back"

        if direction == "straight":
            jump h_2_8
        else:
            jump h_2_10

    else:
        $ pastlabel = "h_2_9"
        menu:

            "Lets go straight":
                $ direction = "straight"
            "Or I could head back?":
                $ direction = "back"

        if direction == "straight":
            jump h_2_10
        else:
            jump h_2_8


label h_2_8:

    if pastlabel == "h_2_9":
        $ pastlabel = "h_2_8"
        scene bg dh_r

        menu:

            "Lets go right":
                $ direction = "right"
            "Or I could head back?":
                $ direction = "back"

        if direction == "right":
            jump h_3_8
        else:
            jump h_2_9

    else:
        $ pastlabel = "h_2_8"
 
        scene bg dh_l

        menu:

            "Lets go left":
                $ direction = "left"
            "Or I could head back?":
                $ direction = "back"

        if direction == "left":
            jump h_2_9
        else:
            jump h_3_8

label h_3_8:

    scene bg dh
    if pastlabel == "h_2_8":
        $ pastlabel = "h_3_8"
        menu:

            "Lets go straight":
                $ direction = "straight"
            "Or I could head back?":
                $ direction = "back"

        if direction == "straight":
            jump h_4_8
        else:
            jump h_2_8

    else:
        $ pastlabel = "h_3_8"
        menu:

            "Lets go straight":
                $ direction = "straight"
            "Or I could head back?":
                $ direction = "back"

        if direction == "straight":
            jump h_2_8
        else:
            jump h_4_8


label h_4_8:

    scene bg dh
    if pastlabel == "h_3_8":
        $ pastlabel = "h_4_8"
        menu:

            "Lets go straight":
                $ direction = "straight"
            "Or I could head back?":
                $ direction = "back"

        if direction == "straight":
            jump h_5_8
        else:
            jump h_3_8

    else:
        $ pastlabel = "h_4_8"
        menu:

            "Lets go straight":
                $ direction = "straight"
            "Or I could head back?":
                $ direction = "back"

        if direction == "straight":
            jump h_3_8
        else:
            jump h_5_8


# Memorie room (treasure)
label h_5_8:

    scene bg dh_de
    
    if memorie_1 == False:
        show image "orb_one.png":
            xpos 0.36, ypos 0.3
        
        mc "What is this floating orb?"

        menu:
            "Dont touch it, it might be dangerous":
                $ direction = "back"
            "I feel a warmth from it, I should reach out to it":
                $ direction = "touch"

        if direction == "back":
            $ pastlabel = "h_5_8"
            jump h_4_8
        else:
            "Warmth floods your body reminding you of someone"
            menu:
                "Is, is that a child is that who I need to get back to?":
                    $ mf1 = 1
                    $ mcb.hp_max = 30
                    $ mc_hp_max = 30
                "Who is that, why do I remember this person my heart feels as tho it misses them so I must get back to them!":
                    $ mf1 = 2
                    $ mcb.hp_max  = 25
                    $ mc_hp_max = 25
                "Hmmm this person is my friend, wait what is a friend? I feel safe seeing them, like we could challenge the world!":
                    $ mf1 = 3
                    $ mcb.hp_max  = 20
                    $ mc_hp_max = 20
            hide image "orb_one.png"
            $ mc = mc.strip()
            play sound orb_break_sf
            show image "orb_one_b.png":
                xpos 0.36 ypos 0.6
            "The orb falls to the ground and breaks, but the coldness you were feeling drifts away"
            $ memorie_1 = True
            menu:
                "I need to get out of here":
                    $ direction = "back"
            $ pastlabel = "h_5_8"
            hide image "orb_one_b.png"
            jump h_4_8
    else:

        show image "orb_one_b.png":
            xpos 0.36 ypos 0.6
        menu:

            "Lets head back looks like the orb is broken nothing left for me to do here":
                $ direction = "back"
        $ pastlabel = "h_5_8"
        hide image "orb_one_b.png"
        jump h_4_8

label h_7_10:

    scene bg dh
    if pastlabel == "h_7_11":
        $ pastlabel = "h_7_10"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_7_9
        else:
            jump h_7_11
    else:
        $ pastlabel = "h_7_10"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_7_11
        else:
            jump h_7_9


label h_7_9:

    scene bg dh
    if pastlabel == "h_7_10":
        $ pastlabel = "h_7_9"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_7_8
        else:
            jump h_7_10
    else:
        $ pastlabel = "h_7_9"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_7_10
        else:
            jump h_7_8

label h_7_8:

    if pastlabel == "h_7_9":
        $ pastlabel = "h_7_8"
        scene bg dh_r

        menu:
    
            "Lets go right":
                $ direction = "right"
            "Or I can head back":
                $ direction = "back"

        if direction == "right":
            jump h_8_8
        else:
            jump h_7_9

    else:
        $ pastlabel = "h_7_8"
        scene bg dh_l

        menu:
    
            "Lets go left":
                $ direction = "left"
            "Or I can head back":
                $ direction = "back"

        if direction == "left":
            jump h_7_9
        else:
            jump h_8_8


label h_8_8:

    scene bg dh
    if pastlabel == "h_7_8":
        $ pastlabel = "h_8_8"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_9_8
        else:
            jump h_7_8

    else:
        $ pastlabel = "h_8_8"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_7_8
        else:
            jump h_9_8


label h_9_8:

    scene bg dh
    if pastlabel == "h_8_8":
        $ pastlabel = "h_9_8"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_10_8
        else:
            jump h_9_7
        
    else:
        $ pastlabel = "h_9_8"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_8_8
        else:
            jump h_10_8
        

label h_10_8:

    scene bg dh
    if pastlabel == "h_9_8":
        $ pastlabel = "h_10_8"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_11_8
        else:
            jump h_9_8

    else:
        $ pastlabel = "h_10_8"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_9_8
        else:
            jump h_11_8


label h_11_8:

    scene bg dh
    if pastlabel == "h_10_8":
        $ pastlabel = "h_11_8"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_8
        else:
            jump h_10_8

    else:
        $ pastlabel = "h_11_8"
        menu:  
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_10_8
        else:
            jump h_12_8


label h_12_8:

    if pastlabel == "h_11_8":
        $ pastlabel = "h_12_8"
        scene bg dh_l_r

        menu:
    
            "Lets go left":
                $ direction = "left"
            "Lets go right":
                $ direction = "right"
            "Or I can head back":
                $ direction = "back"

        if direction == "left":
            jump h_12_7
        elif direction == "right":
            jump h_12_9
        else:
            jump h_11_8

    elif pastlabel == "h_12_9":
        $ pastlabel = "h_12_8"
        scene bg dh_s_l

        menu:
    
            "Lets go left":
                $ direction = "left"
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "left":
            jump h_11_8
        elif direction == "straight":
            jump h_12_7
        else:
            jump h_12_9

    else:
        $ pastlabel = "h_12_8"
        scene bg dh_s_r

        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Lets go right":
                $ direction = "right"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_9
        elif direction == "right":
            jump h_11_8
        else:
            jump h_12_7


label h_12_9:

    scene bg dh
    if pastlabel == "h_12_8":
        $ pastlabel = "h_12_9"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_10
        else:
            jump h_12_8

    else:
        $ pastlabel = "h_12_9"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_8
        else:
            jump h_12_10


label h_12_10:

    scene bg dh
    if pastlabel == "h_12_9":
        $ pastlabel = "h_12_10"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_11
        else:
            jump h_12_9
    
    else:
        $ pastlabel = "h_12_10"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_9
        else:
            jump h_12_11


label h_12_11:

    scene bg dh
    if pastlabel == "h_12_10":
        $ pastlabel = "h_12_11"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_12
        else:
            jump h_12_10
    else:
        $ pastlabel = "h_12_11"
        menu:   
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_10
        else:
            jump h_12_12


label h_12_12:

    if pastlabel =="h_12_11":
        $ pastlabel = "h_12_12"
        scene bg dh_r

        menu:
    
            "Lets go right":
                $ direction = "right"
            "Or I can head back":
                $ direction = "back"

        if direction == "right":
            jump h_11_12
        else:
            jump h_12_11

    else:
        $ pastlabel = "h_12_12"
        scene bg dh_l

        menu:
    
            "Lets go left":
                $ direction = "left"
            "Or I can head back":
                $ direction = "back"

        if direction == "left":
            jump h_12_11
        else:
            jump h_11_12


label h_11_12:

    scene bg dh
    if pastlabel == "h_12_12":
        $ pastlabel = "h_11_12"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_10_12
        else:
            jump h_12_12

    else:
        $ pastlabel = "h_11_12"

        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_12
        else:
            jump h_10_12


label h_10_12:

    scene bg dh
    if pastlabel == "h_11_12":
        $ pastlabel = "h_10_12"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_9_12
        else:
            jump h_11_12
    else:
        $ pastlabel = "h_10_12"

        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_11_12
        else:
            jump h_9_12

label h_9_12:

    if pastlabel == "h_10_12":
        $ pastlabel = "h_9_12"
        scene bg dh_r

        menu:
    
            "Lets go right":
                $ direction = "right"
            "Or I can head back":
                $ direction = "back"

        if direction == "right":
            jump h_9_11
        else:
            jump h_10_12

    else:
        $ pastlabel = "h_9_12"
        scene bg dh_l

        menu:
    
            "Lets go left":
                $ direction = "left"
            "Or I can head back":
                $ direction = "back"

        if direction == "left":
            jump h_10_12
        else:
            jump h_9_11

label h_9_11:

    scene bg dh
    if pastlabel == "h_9_12":
        $ pastlabel = "h_9_11"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_9_10
        else:
            jump h_9_12

    else:
        $ pastlabel = "h_9_11"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_9_12
        else:
            jump h_9_10

label h_9_10:
    if pastlabel == "h_9_11":
        $ pastlabel = "h_9_10"
        scene bg dh_r

        menu:
    
            "Lets go right":
                $ direction = "right"
            "Or I can head back":
                $ direction = "back"

        if direction == "right":
            jump h_10_10
        else:
            jump h_9_11

    else:
        $ pastlabel = "h_9_10"
        scene bg dh_l

        menu:
    
            "Lets go left":
                $ direction = "left"
            "Or I can head back":
                $ direction = "back"

        if direction == "left":
            jump h_9_11
        else:
            jump h_10_10


# Memorie room (teasure room)
label h_10_10:

    scene bg dh_de
    
    if memorie_2 == False:
        show image "orb_two.png":
            xpos 0.36, ypos 0.3
        
        mc "What is this floating orb?"

        menu:
            "Dont touch it, it might be dangerous!":
                $ direction = "back"
            "I feel strength returning when I get close, I should reach out to it":
                $ direction = "touch"

        if direction == "back":
            $ pastlabel = "h_10_10"
            jump h_9_10
        else:
            "A memory flows into me reminding you of a moment"
            menu:
                "Someone is charging towards me! I react quickly punching them in the jaw knocking them out!":
                    "A part of the orb wraps itself around my fists"
                    $ mf2 = 1
                    $ weapon = "Punch"
                    $ mcb.attack = 5
                    $ attack = 5
                "A ball is flying towards me! Swoosh! Crack! The ball makes a loud sound as I struck it with a bat.":
                    "A part of the orb cracks off,  I pick up a club off the ground that was once a section of the orb"
                    $ mf2 = 2
                    $ weapon = "Smash"
                    $ mcb.attack = 10
                    $ attack = 10
                "Pull! A clay disk flys in the distance, I take aim BANG! Clay shards fall to the ground":
                    "A part of the orb breaks off and is flying towards me. I grabbed it out of instinct it has become a pistol"
                    $ mf2 = 3
                    $ weapon = "Shoot"
                    $ mcb.attack = 15
                    $ attack = 15
            hide image "orb_two.png"
            play sound orb_break_sf
            show image "orb_two_b.png":
                xpos 0.36 ypos 0.6
            "The orb falls to the ground and breaks, This weapon could be usefull I am unsure of what else could be in here"
            $ memorie_2 = True
            menu:
                "I need to get out of here":
                    $ direction = "back"
            $ pastlabel = "h_10_10"
            hide image "orb_two_b.png"
            jump h_9_10
    else:

        show image "orb_two_b.png":
            xpos 0.36 ypos 0.6
        menu:

            "Lets head back looks like the orb is broken nothing left for me to do here":
                $ direction = "back"
        $ pastlabel = "h_5_8"
        hide image "orb_two_b.png"
        jump h_9_10


label h_12_7:

    scene bg dh
    if pastlabel == "h_12_8":
        $ pastlabel = "h_12_7"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_6
        else:
            jump h_12_8
    else:
        $ pastlabel = "h_12_7"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_8
        else:
            jump h_12_6


label h_12_6:

    scene bg dh
    if pastlabel == "h_12_7":
        $ pastlabel = "h_12_6"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_5
        else:
            jump h_12_7

    else:
        $ pastlabel = "h_12_6"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_7
        else:
            jump h_12_5


label h_12_5:

    scene bg dh
    if  pastlabel == "h_12_6":
        $ pastlabel = "h_12_5"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_4
        else:
            jump h_12_6

    else:
        $ pastlabel = "h_12_5"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_6
        else:
            jump h_12_4


label h_12_4:

    scene bg dh
    if pastlabel == "h_12_5":
        $ pastlabel = "h_12_4"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_3
        else:
            jump h_12_5

    else:
        $ pastlabel = "h_12_4"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_5
        else:
            jump h_12_3


label h_12_3:

    scene bg dh
    if pastlabel == "h_12_4":
        $ pastlabel = "h_12_3"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_2
        else:
            jump h_12_4

    else:
        $ pastlabel = "h_12_3"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_4
        else:
            jump h_12_2


label h_12_2:
    if pastlabel == "h_12_3":
        $ pastlabel = "h_12_2"
        scene bg dh_l

        menu:
    
            "Lets go left":
                $ direction = "left"
            "Or I can head back":
                $ direction = "back"

        if direction == "left":
            jump h_11_2
        else:
            jump h_12_3

    else:
        $ pastlabel = "h_12_3"
        scene bg dh_r

        menu:
    
            "Lets go right":
                $ direction = "right"
            "Or I can head back":
                $ direction = "back"

        if direction == "right":
            jump h_12_3
        else:
            jump h_11_2


label h_11_2:

    scene bg dh
    if pastlabel == "h_12_2":
        $ pastlabel = "h_11_2"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_10_2
        else:
            jump h_12_2

    else:
        $ pastlabel = "h_11_2"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_12_2
        else:
            jump h_10_2


label h_10_2:

    scene bg dh
    if pastlabel == "h_11_2":
        $ pastlabel = "h_10_2"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_9_2
        else:
            jump h_11_2

    else:
        $ pastlabel = "h_10_2"

        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_11_2
        else:
            jump h_9_2


label h_9_2:

    scene bg dh
    if pastlabel == "h_10_2":
        $ pastlabel = "h_9_2"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_8_2
        else:
            jump h_10_2

    else:
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_10_2
        else:
            jump h_8_2




label h_8_2:
    if pastlabel == "h_9_2":
        scene bg dh_l
        $ pastlabel = "h_8_2"
        menu:
    
            "Lets go left":
                $ direction = "left"
            "Or I can head back":
                $ direction = "back"

        if direction == "left":
            jump h_8_3
        else:
            jump h_9_2
        $ pastlabel = "h_8_2"
        
    else:
        scene bg dh_r
        $ pastlabel = "h_8_2"
        menu:
    
            "Lets go right":
                $ direction = "right"
            "Or I can head back":
                $ direction = "back"

        if direction == "right":
            jump h_9_2
        else:
            jump h_8_3


label h_8_3:

    scene bg dh
    if pastlabel == "h_8_2":
        $ pastlabel = "h_8_3"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_8_4
        else:
            jump h_8_2

    else:
        $ pastlabel = "h_8_3"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_8_2
        else:
            jump h_8_4


label h_8_4:

    scene bg dh
    if pastlabel == "h_8_3":
        $ pastlabel = "h_8_4"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_8_5
        else:
            jump h_8_3
    else:
        $ pastlabel = "h_8_4"
        menu:
    
            "Lets go straight":
                $ direction = "straight"
            "Or I can head back":
                $ direction = "back"

        if direction == "straight":
            jump h_8_3
        else:
            jump h_8_5


label h_8_5:

    scene bg dh_i
    mc "There is lots of directions I can go here, hope I dont get lost"

    if pastlabel == "h_8_4":
        $ pastlabel = "h_8_5"

        menu:

            "I can go straight":
                $ direction = "straight"
            "I can go left":
                $ direction = "left"
            "I can go right":
                $ direction = "right"
            "Or I could always head back":
                $ direction = "back"

        if direction == "straight":
            jump h_8_6
        elif direction == "left":
            jump h_9_5
        elif direction == "right":
            jump h_7_5
        else:
            jump h_8_4

    elif pastlabel == "h_8_6":
        $ pastlabel = "h_8_5"
        menu:

            "I can go straight":
                $ direction = "straight"
            "I can go left":
                $ direction = "left"
            "I can go right":
                $ direction = "right"
            "Or I could always head back":
                $ direction = "back"

        if direction == "straight":
            jump h_8_4
        elif direction == "left":
            jump h_7_5
        elif direction == "right":
            jump h_9_5
        else:
            jump h_8_6

    elif pastlabel == "h_9_5":
        $ pastlabel = "h_8_5"
        menu:

            "I can go straight":
                $ direction = "straight"
            "I can go left":
                $ direction = "left"
            "I can go right":
                $ direction = "right"
            "Or I could always head back":
                $ direction = "back"

        if direction == "straight":
            jump h_7_5
        elif direction == "left":
            jump h_8_6
        elif direction == "right":
            jump h_8_4
        else:
            jump h_9_5

    else:
        $ pastlabel = "h_8_5"
        menu:

            "I can go straight":
                $ direction = "straight"
            "I can go left":
                $ direction = "left"
            "I can go right":
                $ direction = "right"
            "Or I could always head back":
                $ direction = "back"

        if direction == "straight":
            jump h_9_5
        elif direction == "left":
            jump h_8_4
        elif direction == "right":
            jump h_8_6
        else:
            jump h_7_5


label h_8_6:

    scene bg dh_de

    mc "This is a dead end I must have taken a wrong turn"

    menu:

        "I got to go back there is nothing here":
            $ direction = "back"
    $ pastlabel = "h_8_6"
    jump h_8_5

label h_9_5:

    scene bg dh
    if pastlabel == "h_8_5":
        $ pastlabel = "h_9_5"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_10_5
        else:
            jump h_8_5
    else:
        $ pastlabel = "h_9_5"

        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_8_5
        else:
            jump h_10_5


label h_10_5:
    if pastlabel == "h_9_5":
        $ pastlabel = "h_10_5"
        scene bg dh_l

        menu:

            "I can go left":
                $ direction = "left"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "left":
            jump h_10_4
        else:
            jump h_9_5

    else:
        $ pastlabel = "h_10_5"
        scene bg dh_r

        menu:

            "I can go right":
                $ direction = "right"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "right":
            jump h_9_5
        else:
            jump h_10_4


# Memorie room (Tearsure room)
label h_10_4:

    scene bg dh_de
    
    if memorie_3 == False:
        show image "orb_three.png":
            xpos 0.36, ypos 0.3
        
        mc "What is this floating orb?"

        menu:
            "Dont touch it, it might be dangerous!":
                $ direction = "back"
            "I feel like this holds a memory of something I forgot how to do":
                $ direction = "touch"

        if direction == "back":
            $ pastlabel = "h_10_4"
            jump h_10_5
        else:
            "A memory flows into me reminding something I was skilled at doing"
            menu:
                "A blur of fists wiz past my head as I avoid them with ease":
                    $ mf3 = 1
                    $ skill = "Dodge"
                "Pain surgers through my arm, I pull out some bandages wraping up the wound":
                    "A shard becomes a box filled with bandages, this could be handy"
                    $ mf3 = 2
                    $ skill = "Mend"
                "A person is barreling quickly towards me, I don't have time to get out of the way I need to Guard myself from the impact":
                    $ mf3 = 3
                    $ skill = "Guard"
            hide image "orb_three.png"
            play sound orb_break_sf
            show image "orb_three_b.png":
                xpos 0.36 ypos 0.6
            "The orb falls to the ground and breaks, I think I gained a usefull skill out of this"
            $ memorie_3 = True
            menu:
                "I need to get out of here":
                    $ direction = "back"
            $ pastlabel = "h_10_4"
            hide image "orb_three_b.png"
            jump h_10_5
    else:

        show image "orb_two_b.png":
            xpos 0.36 ypos 0.6
        menu:

            "Lets head back looks like the orb is broken nothing left for me to do here":
                $ direction = "back"
        $ pastlabel = "h_5_8"
        hide image "orb_two_b.png"
        jump h_9_10

label h_7_5:

    scene bg dh
    if pastlabel == "h_8_5":
        $ pastlabel = "h_7_5"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_6_5
        else:
            jump h_8_5
    else:
        $ pastlabel = "h_7_5"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_8_5
        else:
            jump h_6_5


label h_6_5:
    if pastlabel == "h_7_5":
        $ pastlabel = "h_6_5"
        scene bg dh_s_r

        menu:

            "I can go straight":
                $ direction = "straight"
            "I can go right":
                $ direction = "right"
            "Or I could go back the way I came":
                $ direction = "back"

        if direction == "straight":
            jump h_5_5
        elif direction == "right":
            jump h_6_4
        else:
            jump h_7_5
    elif pastlabel == "h_5_5":
        $ pastlabel = "h_6_5"
        scene bg dh_s_l

        menu:

            "I can go straight":
                $ direction = "straight"
            "I can go left":
                $ direction = "left"
            "Or I could go back the way I came":
                $ direction = "back"

        if direction == "straight":
            jump h_7_5
        elif direction == "left":
            jump h_6_4
        else:
            jump h_5_5

    else:
        $ pastlabel = "h_6_5"
        scene bg dh_l_r

        menu:

            "I can go left":
                $ direction = "left"
            "I can go right":
                $ direction = "right"
            "Or I could go back the way I came":
                $ direction = "back"

        if direction == "left":
            jump h_7_5
        elif direction == "right":
            jump h_5_5
        else:
            jump h_6_4


label h_5_5:

    scene bg dh
    if pastlabel == "h_6_5":
        $ pastlabel = "h_5_5"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_4_5
        else:
            jump h_6_5

    else:
        $ pastlabel = "h_5_5"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_6_5
        else:
            jump h_4_5


label h_4_5:

    scene bg dh
    if pastlabel == "h_5_5":
        $ pastlabel = "h_4_5"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_3_5
        else:
            jump h_5_5

    else:
        $ pastlabel = "h_4_5"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_5_5
        else:
            jump h_3_5


label h_3_5:

    scene bg dh
    if pastlabel == "h_4_5":
        $ pastlabel = "h_3_5"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_2_5
        else:
            jump h_4_5

    else:
        $ pastlabel = "h_3_5"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_4_5
        else:
            jump h_2_5


label h_2_5:
    if pastlabel == "h_3_5":
        $ pastlabel = "h_2_5"
        scene bg dh_r

        menu:

            "I can go right":
                $ direction = "right"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "right":
            jump h_2_4
        else:
            jump h_3_5

    else:
        $ pastlabel = "h_2_5"
        scene bg dh_l

        menu:

            "I can go left":
                $ direction = "left"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "left":
            jump h_3_5
        else:
            jump h_2_4


label h_2_4:

    scene bg dh
    if pastlabel == "h_2_5":
        $ pastlabel = "h_2_4"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_2_3
        else:
            jump h_2_5

    else:
        $ pastlabel = "h_2_4"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_2_5
        else:
            jump h_2_3


label h_2_3:

    scene bg dh
    if pastlabel == "h_2_4":
        $ pastlabel = "h_2_3"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_2_2
        else:
            jump h_2_4
    else:
        $ pastlabel = "h_2_3"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_2_4
        else:
            jump h_2_2


label h_2_2:

    if pastlabel == "h_2_3":
        scene bg dh_r
        $ pastlabel = "h_2_2"
        menu:

            "I can go right":
                $ direction = "right"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "right":
            jump h_3_2
        else:
            jump h_2_3

    else:
        scene bg dh_l
        $ pastlabel = "h_2_2"
        menu:

            "I can go left":
                $ direction = "left"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "left":
            jump h_2_3
        else:
            jump h_3_2


label h_3_2:

    scene bg dh
    if pastlabel == "h_2_2":
        $ pastlabel = "h_3_2"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_4_2
        else:
            jump h_2_2

    else:
        $ pastlabel = "h_3_2"
        menu:
        
            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_2_2
        else:
            jump h_4_2


label h_4_2:

    scene bg dh_i
    mc "There is lots of directions I can go here, hope I dont get lost"
    if pastlabel == "h_3_2":
        $ pastlabel = "h_4_2"
        menu:

            "I can go straight":
                $ direction = "straight"
            "I can go left":
                $ direction = "left"
            "I can go right":
                $ direction = "right"
            "Or I could always head back":
                $ direction = "back"   

        if direction == "straight":
            jump h_5_2
        elif direction == "left":
            jump h_4_1
        elif direction == "right":
            jump h_4_3
        else:
            jump h_3_2

    elif pastlabel == "h_4_3":
        $ pastlabel = "h_4_2"
        menu:

            "I can go straight":
                $ direction = "straight"
            "I can go left":
                $ direction = "left"
            "I can go right":
                $ direction = "right"
            "Or I could always head back":
                $ direction = "back"

        if direction == "straight":
            jump h_4_1
        elif direction == "left":
            jump h_3_2
        elif direction == "right":
            jump h_5_2
        else:
            jump h_4_3

    elif pastlabel == "h_4_1":
        $ pastlabel = "h_4_2"
        menu:

            "I can go straight":
                $ direction = "straight"
            "I can go left":
                $ direction = "left"
            "I can go right":
                $ direction = "right"
            "Or I could always head back":
                $ direction = "back"

        if direction == "straight":
            jump h_4_3
        elif direction == "left":
            jump h_5_2
        elif direction == "right":
            jump h_3_2
        else:
            jump h_4_1
    else:
        $ pastlabel = "h_4_2"
        menu:

            "I can go straight":
                $ direction = "straight"
            "I can go left":
                $ direction = "left"
            "I can go right":
                $ direction = "right"
            "Or I could always head back":
                $ direction = "back"

        if direction == "straight":
            jump h_3_2
        elif direction == "left":
            jump h_4_3
        elif direction == "right":
            jump h_4_1
        else:
            jump h_5_2


#Healing Spring (mc HP fully healed)
label h_4_3:
    stop music
    play music fountian_music loop
    scene bg dh_h
    $ pastlabel = "h_4_3"
    mc "There is a fountain here, I wonder if its safe to drink?"

    menu:
        
        "Take a sip":
            $ heal = "yes"
        "Best to avoid it":
            $ heal = "no"

    if heal == "yes":
        $ mcb.heal(50)
        $ mc_hp = mc_hp_max
        mc "That was refreshing! I should head back and find my way out"
        stop music
        play music background_music loop
        jump h_4_2
    else:
        mc "I should get going"
        stop music
        play music background_music loop
        jump h_4_2


#Boss Room
label h_4_1:

    scene bg dh_d
    $ pastlabel = "h_4_1"
    mc "I see a door something seems off about it, it may be dangerous"

    menu:

        "I have to find my way out no matter what dangers await!":
            $ fight = "yes"
        "I should look around more, there might be something that could help me with this":
            $ fight = "leave"
    
    if fight == "yes":
        jump boss_battle
    else:
        jump h_4_2


label h_5_2:

    scene bg dh
    if pastlabel == "h_4_2":
        $ pastlabel = "h_5_2"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_6_2
        else:
            jump h_4_2

    else:
        $ pastlabel = "h_5_2"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_4_2
        else:
            jump h_6_2


label h_6_2:

    if pastlabel == "h_5_2":   
        $ pastlabel = "h_6_2"
        scene bg dh_r

        menu:

            "I can go right":
                $ direction = "right"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "right":
            jump h_6_3
        else:
            jump h_5_2
    else:
        $ pastlabel = "h_6_2"
        scene bg dh_l
        menu:

            "I can go left":
                $ direction = "left"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "left":
            jump h_5_2
        else:
            jump h_6_3


label h_6_3:

    scene bg dh
    if pastlabel == "h_6_2":
        $ pastlabel = "h_6_3"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_6_4
        else:
            jump h_6_2
    else:
        $ pastlabel = "h_6_3"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_6_2
        else:
            jump h_6_4


label h_6_4:

    scene bg dh
    if pastlabel == "h_6_3":
        $ pastlabel = "h_6_4"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_6_5
        else:
            jump h_6_3
    else:
        $ pastlabel = "h_6_4"
        menu:

            "I can go straight":
                $ direction = "straight"
            "Or I could turn back":
                $ direction = "back"
    
        if direction == "straight":
            jump h_6_3
        else:
            jump h_6_5

label boss_battle:

    scene bg dh_d
    stop music
    play music boss_music loop
    "As you aproach the door some sort of creature drops from the ceiling and attacks!"
    show image "boss.png":
        xpos 0.3, ypos 0.3
    # Combat Loop
    $ turn = 1
    while mcb.is_alive() and boss1.is_alive():
        #Player's turn
        "[mc] stats hp [mcb.hp], max hp [mcb.hp_max] attack [mcb.attack]"
        if turn > 3:
            "It looks like its going to use a big attack I should be careful"

        menu:
            "[weapon]":
                if weapon == "Punch":
                    $ mcb.attack_character(boss1)
                    "You [weapon]ed the monster for [mcb.attack] damage."
                    $ mcb.attack_character(boss1)
                    "You [weapon]ed the monster again for [mcb.attack] damage."
                else:
                    $ mcb.attack_character(boss1)
                    "You used [weapon] on the monster for [mcb.attack] damage."
            "[skill]":
                $ skill_used = True

        if not boss1.is_alive():
            "Its finally dead!"
            stop music
            jump clear_dungeon_halls

        #Monsters turn
        "monster stats hp [boss1.hp], max hp [boss1.hp_max] attack [boss1.attack]"
        if turn > 3 :
            $ boss_attack = 10
            $ boss1.attack = boss_attack
            if skill_used == True:
                $ skill_used = False
                if skill == "Dodge":
                    $ boss_attack = 0
                    $ boss1.attack = boss_attack
                    "You dodge out of the way of is attack"
                elif skill == "Guard":
                    $ boss_attack = 1
                    $ boss1.attack = boss_attack
                    "You prtoect yourself from most of the attack"
                else:
                    $ mcb.heal(5)
                    $ mc_hp = mcb.hp
                    "you patch your self up and heal 5 HP"
            $ boss1.attack_character(mcb)
            "The monster did [boss_attack] damage to you with a bite attack"
            $ mc_hp = mc_hp - boss_attack
            $ boss_attack = 3
            $ boss1.attack = boss_attack
            $ turn = 1
        else:
            if skill_used == True:
                $ skill_used = False
                if skill == "Dodge": 
                    $ boss_attack = 0
                    $ boss1.attack = boss_attack
                    "You dodge out of the way of is attack"
                elif skill == "Guard":
                    $ boss_attack = 1
                    $ boss1.attack = boss_attack
                    "You prtoect yourself from most of the attack"
                else:
                    $ mcb.heal(5)
                    $ mc_hp = mcb.hp
                    "you patch your self up and heal 5 HP"
            $ boss1.attack_character(mcb)
            "The monster did [boss_attack] damage to you with its claws"
            $ mc_hp = mc_hp - boss_attack
            $ boss_attack = 3
            $ boss1.attack = boss_attack
            $ turn = turn + 1

        if not mcb.is_alive():
            stop music
            jump game_over


label game_over:
    stop music
    scene game_over
    show image "game_over.png":
        xpos 0.36 ypos 0.6
    if pastlabel == 'start':
        "There is no hope here, this is not a dream. I have no hope to return to, I will accept this fate..."
        return

    if memorie_2 == True:
        if mf2 == 1:
            mc "Looks like I was not as good of a fighter as I thought."
        elif mf2 == 2:
            mc "Guess I struck out for the last time."
        else:
            mc "My aim was off today, couldn't hit the mark when I needed to most."

    if memorie_1 == True:
        if mf1 == 1:
            mc "Looks like I wont be making it back to that kid, hope they will be fine without me."
        elif mf1 == 2:
            mc "Please carry on witout me my love."
        else:
            mc "Maybe things would be different if my friend was with me, I dont remember them but looks like I could have used their help"

    if memorie_3 == True:
        if mf3 == 1:
            mc "Maybe things would have been different if I dodged that last attack."
        elif mf3 == 2:
            mc "I shouldnt have ignored my injuries, if I only looked after myself better."
        else:
            mc "I'm stronger then this, I could have blocked..."

    mc "Maybe if I had a second chance I could have found the answers I was looking for. There must be an escape, only if there was a way for a seccond chance."
    return

label clear_dungeon_halls:

    stop music
    scene bg Chapter_2
    "After the monster was defeat [mc] goes through the door"
    mc "Wait has the world always had these colours? Everything looks so much clearer."
    "The story will continue in Chapter 2, To be continued..."

    return
