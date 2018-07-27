import arcade
#Draws a Smiley face

#set window dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#Open the window and set the title and dimensions
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Smiley Face")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
#Make Head of Smiley
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)
#Make Left Eye
x = 200
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)
x = 200
y = 345
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)
#Make Right Eye
x = 400
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)
x = 400
y = 345
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

x = 300
y = 200
radius = 50
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)
X = 300
y = 205
radius = 50
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

x=200
y= 250
arcade.draw_line(start_x=175, end_x=200, start_y=260, end_y= 280, color= arcade.color.PINK_SHERBET)
arcade.draw_line(start_x=200, end_x=225, start_y=260, end_y= 280, color= arcade.color.PINK_SHERBET)
arcade.draw_line(start_x=225, end_x=250, start_y=260, end_y= 280, color= arcade.color.PINK_SHERBET)
arcade.draw_line(start_x=250, end_x=275, start_y=260, end_y= 280, color= arcade.color.PINK_SHERBET)
arcade.draw_line(start_x=275, end_x=300, start_y=260, end_y= 280, color= arcade.color.PINK_SHERBET)
arcade.draw_line(start_x=300, end_x=325, start_y=260, end_y= 280, color= arcade.color.PINK_SHERBET)
arcade.draw_line(start_x=325, end_x=350, start_y=260, end_y= 280, color= arcade.color.PINK_SHERBET)
arcade.draw_line(start_x=350, end_x=375, start_y=260, end_y= 280, color= arcade.color.PINK_SHERBET)
arcade.draw_line(start_x=375, end_x=400, start_y=260, end_y= 280, color= arcade.color.PINK_SHERBET)
arcade.draw_line(start_x=400, end_x=425, start_y=260, end_y= 280, color= arcade.color.PINK_SHERBET)

arcade.finish_render()
arcade.run()


