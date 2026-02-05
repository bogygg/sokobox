# Logic of the sokobox
import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Starting Template"
PLAYER_MOVEMENT_SPEED = 5


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
        
        self.walls = arcade.SpriteList(use_spatial_hash=True)
        self.wall_texture = arcade.load_texture("stone4.png")
        counter = 0
        sub = 0
        for i in range(10):
            self.wall = arcade.Sprite(self.wall_texture)
            self.wall.center_x = 370 + counter
            self.wall.center_y = 90
            counter += 60 
            self.walls.append(self.wall)
            if i > 7:
                self.wall = arcade.Sprite(self.wall_texture)
                self.wall.center_x = 670
                self.wall.center_y = 570 - sub
                sub += 60
                self.walls.append(self.wall)
        counter1 = 0
        sub1 = 0
        for i in range(10):
            self.wall = arcade.Sprite(self.wall_texture)
            self.wall.center_x = 370 + counter1
            self.wall.center_y = 630
            counter1 += 60 
            self.walls.append(self.wall)
            if i > 7:
                self.wall = arcade.Sprite(self.wall_texture)
                self.wall.center_x = 550
                self.wall.center_y = 570 - sub1
                sub1 += 60
                self.walls.append(self.wall)

        counter2 = 0
        sub3 = 0
        for i in range(8):
            self.wall = arcade.Sprite(self.wall_texture)
            self.wall.center_x = 370 
            self.wall.center_y = 150 + counter2
            counter2 += 60 
            self.walls.append(self.wall)
            if i > 5:
                self.wall = arcade.Sprite(self.wall_texture)
                self.wall.center_x = 550
                self.wall.center_y = 270 - sub3
                sub3 += 120
                self.walls.append(self.wall)
        counter3 = 0
        sub4 = 0
        for i in range(8):
            self.wall = arcade.Sprite(self.wall_texture)
            self.wall.center_x = 910 
            self.wall.center_y = 150 + counter3
            counter3 += 60 
            self.walls.append(self.wall)
            if i > 5:
                self.wall = arcade.Sprite(self.wall_texture)
                self.wall.center_x = 790 - sub4 
                self.wall.center_y = 390 - sub4
                sub4 += 120 
                self.walls.append(self.wall)

        
        self.player_list = arcade.SpriteList()
        self.box_list = arcade.SpriteList(use_spatial_hash=True)
        
        self.player_texture= arcade.load_texture("bigboy2.png")
        self.player_sprite = arcade.Sprite(self.player_texture, hit_box_algorithm='Simple')
        self.player_sprite.scale = 0.16
        self.player_sprite.center_x = 490
        self.player_sprite.center_y = 510
        self.player_list.append(self.player_sprite)

        box_texture = arcade.load_texture("lightweight.png")
        box_sprite= arcade.Sprite(box_texture)
        box_sprite.scale = 0.3
        box_sprite.center_x = 490
        box_sprite.center_y = 330
        self.box_list.append(box_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.walls
        )

        self.move_direction = None
        

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
        
        arcade.draw_rect_filled(arcade.rect.XYWH(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, 600, 600), arcade.color.DARK_YELLOW)

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
        self.player_list.draw()
        self.player_sprite.draw_hit_box(arcade.color.RED)

        for wall in self.walls:
            self.wall.draw_hit_box(arcade.color.BLUE)
        self.box_list.draw()

    def on_update(self, delta_time):
        
        '''All the logic to move, and the game logic goes here.'''
        self.physics_engine.update()
       
        if arcade.check_for_collision_with_list(self.player_sprite, self.walls):
            print("Hit Wall!")
        

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        
        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        
        '''if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED'''
    
    def try_move(self, dx, dy):
        old_x = self.player_sprite.center_x
        old_y = self.player_sprite.center_y

        self.player_sprite.center_x += dx
        self.player_sprite.center_y += dy

        if arcade.check_for_collision_with_list(self.player_sprite, self.walls):
            # Hit a wall → go back
            self.player_sprite.center_x = old_x
            self.player_sprite.center_y = old_y

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        

        if key  == arcade.key.UP:
            self.try_move(0, 60)
        elif key == arcade.key.DOWN:
            self.try_move(0, -60)
        elif key == arcade.key.LEFT:
            self.try_move(-60, 0)
        elif key == arcade.key.RIGHT:
            self.try_move(60, 0)

        '''if not arcade.check_for_collision_with_list(self.player_sprite, self.walls):
            self.player_sprite.center_x = next_x
            self.player_sprite.center_y = next_y
        # Reset direction and velocity
        self.move_direction = None
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0'''

        

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