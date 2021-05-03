













define config.name = _("Far Beyond the World")





define gui.show_name = False




define config.version = "4.5.5"





define gui.about = _p("Written and Illustrated by Kael Tiger  [{a=https://twitter.com/kael_tiger}@kael_tiger{/a}]    \n\nYou can support this project on [{a=https://www.patreon.com/kaeltiger}Patreon{/a}]    \n\nFar Beyond the World ©2020    \nAll rights reserved.")






define build.name = "FBTW"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True
init python:
    renpy.music.register_channel("ambience","sfx",True,tight=True)













define config.main_menu_music = "music/main title.ogg"










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 40





default preferences.afm_time = 15
















define config.save_directory = "FBTW-1588013193"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)






    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("music", "all")
    build.archive("sfx", "all")
    build.archive("ambience", "all")


    build.classify("game/**.rpy", "scripts")
    build.classify("game/**.rpyc", "scripts")


    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")


    build.classify("game/music/**.ogg", "music")


    build.classify("game/sfx/**.ogg", "sfx")


    build.classify("game/ambience/**.ogg", "ambience")




    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
