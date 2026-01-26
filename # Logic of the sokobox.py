# Logic of the sokobox
import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Starting Template"


class GameView(arcade.View):
    """
    Main application class.
    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.DARK_BROWN
        # If you have sprite lists, you should create them here,
        # and set them to None
        
        self.walls = arcade.SpriteList()
        self.wall_texture = arcade.load_texture("stone4.png")
        counter = 0
        for i in range(10):
            self.wall = arcade.Sprite(self.wall_texture)
            self.wall.center_x = 370 + counter
            self.wall.center_y = 90
            counter += 60 
            self.walls.append(self.wall)
        counter1 = 0
        for i in range(10):
            self.wall = arcade.Sprite(self.wall_texture)
            self.wall.center_x = 370 + counter1
            self.wall.center_y = 630
            counter1 += 60 
            self.walls.append(self.wall)
        counter2 = 0
        for i in range(8):
            self.wall = arcade.Sprite(self.wall_texture)
            self.wall.center_x = 370 
            self.wall.center_y = 150 + counter2
            counter2 += 60 
            self.walls.append(self.wall)
        counter3 = 0
        for i in range(8):
            self.wall = arcade.Sprite(self.wall_texture)
            self.wall.center_x = 910 
            self.wall.center_y = 150 + counter3
            counter3 += 60 
            self.walls.append(self.wall)

        self.player_texture= arcade.load_texture("качок.png")
        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.scale = 0.25
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128

        

    def reset(self):
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below
        
        arcade.draw_rect_filled(arcade.rect.XYWH(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, 600, 600), arcade.color.AIR_FORCE_BLUE)

        add = 0
        for i in range(11):
            arcade.draw_line((WINDOW_WIDTH-600)/2+add,(WINDOW_HEIGHT-600)/2 , (WINDOW_WIDTH-600)/2+add, (WINDOW_HEIGHT-600)/2+600, arcade.color.BLACK, 2) 
            add += 60
        add2 = 0
        for i in range(11):
            arcade.draw_line((WINDOW_WIDTH-600)/2,(WINDOW_HEIGHT-600)/2+add2, (WINDOW_WIDTH-600)/2+600, (WINDOW_HEIGHT-600)/2+add2, arcade.color.BLACK, 2) 
            add2 += 60

        self.walls.draw()
        arcade.draw_sprite(self.player_sprite)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        '''if arcade.check_for_collision(self.player_sprite, self.walls):
            print("Hit Wall!")'''
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()



if __name__ == "__main__":
    main()