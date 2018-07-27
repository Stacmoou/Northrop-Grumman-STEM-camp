import arcade

#set window dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#Open the window and set the title and dimensions
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Smiley Face")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
#draw functions here
arcade.finish_render()
arcade.run()
