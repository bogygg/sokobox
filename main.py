# Logic of the sokobox
import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "SokoBox"
PLAYER_MOVEMENT_SPEED = 5
#damping is amount of speed lost per second when an force not acting on object (deceleration)
DEFAULT_DAMPING= 100
BOX_FRICTION = 0.7

class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()


        # If you have sprite lists, you should create them here,
        self.player_list = None
        self.box_list = None

        #basic crap
        self.background_color = arcade.color.AMAZON
        self.window.set_mouse_visible(False)

        

    def setup(self):
        #setup game here AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

        #sprite lists
        self.player_list = arcade.SpriteList()
        self.box_list = arcade.SpriteList()

        #Bigboy setup 
        self.player_texture= arcade.load_texture("resources/bigboy-removebg-preview.png")
        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.scale = 0.18
        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 200
        self.player_list.append(self.player_sprite)

        #LIGHTWEIGHTT
        box_texture = arcade.load_texture("resources/lightweight-removebg-preview.png")
        box_sprite= arcade.Sprite(box_texture)
        box_sprite.scale = 0.5
        box_sprite.center_x = 200
        box_sprite.center_y = 250
        self.box_list.append(box_sprite)

        #physics engine (constantly updating to detect movement and collisions, has to be below sprites)
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite,self.box_list
        )

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below
        arcade.draw_rect_filled(arcade.rect.XYWH(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, 600, 600), arcade.color.AIR_FORCE_BLUE)
        self.player_list.draw()
        self.box_list.draw()


    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.physics_engine.update(self.box_list)

        box_hit_list=arcade.check_for_collision_with_list(
            self.player_sprite, self.box_list
        )


        




    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key == arcade.key.UP or key == arcade.key.W:
           self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

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