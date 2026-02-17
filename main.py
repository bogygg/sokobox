# Logic of the sokobox
import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Sokobox"
PLAYER_MOVEMENT_SPEED = 60
TILE_SIZE = 60


class GameView(arcade.View):
    """
    Main application class.
    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()

        self.game_won = False
        self.move_direction = None
        self.background_color = arcade.color.DARK_BROWN
        # If you have sprite lists, you should create them here,
        # and set them to None
        self.player_list = None
        self.wall_list = None
        self.player_list = None
        self.box_list = None
        self.goal_list = None

        self.win_text = arcade.Text(
            text="YOU WIN",
            x=self.width / 2,
            y=self.height / 2,
            anchor_x="center",
            anchor_y="center",
            color=(255, 215, 0, 255),  # Alpha should be 255, not 1
            font_size=48
        )


        
    
    def setup(self):
        #walls
        self.wall_list = arcade.SpriteList()
        self.wall_texture = arcade.load_texture("resources/stone4.png")
        counter = 0
        sub = 0
        for i in range(10):
            self.wall = arcade.Sprite(self.wall_texture)
            self.wall.center_x = 370 + counter
            self.wall.center_y = 90
            counter += 60 
            self.wall_list.append(self.wall)
            if i > 7:
                self.wall = arcade.Sprite(self.wall_texture)
                self.wall.center_x = 670
                self.wall.center_y = 570 - sub
                sub += 60
                self.wall_list.append(self.wall)
        counter1 = 0
        sub1 = 0
        for i in range(10):
            self.wall = arcade.Sprite(self.wall_texture)
            self.wall.center_x = 370 + counter1
            self.wall.center_y = 630
            counter1 += 60 
            self.wall_list.append(self.wall)
            if i > 7:
                self.wall = arcade.Sprite(self.wall_texture)
                self.wall.center_x = 550
                self.wall.center_y = 570 - sub1
                sub1 += 60
                self.wall_list.append(self.wall)

        counter2 = 0
        sub3 = 0
        for i in range(8):
            self.wall = arcade.Sprite(self.wall_texture)
            self.wall.center_x = 370 
            self.wall.center_y = 150 + counter2
            counter2 += 60 
            self.wall_list.append(self.wall)
            if i > 5:
                self.wall = arcade.Sprite(self.wall_texture)
                self.wall.center_x = 550
                self.wall.center_y = 270 - sub3
                sub3 += 120
                self.wall_list.append(self.wall)
        counter3 = 0
        sub4 = 0
        for i in range(8):
            self.wall = arcade.Sprite(self.wall_texture)
            self.wall.center_x = 910 
            self.wall.center_y = 150 + counter3
            counter3 += 60 
            self.wall_list.append(self.wall)
            if i > 5:
                self.wall = arcade.Sprite(self.wall_texture)
                self.wall.center_x = 790 - sub4 
                self.wall.center_y = 390 - sub4
                sub4 += 120 
                self.wall_list.append(self.wall)

        #Player
        self.player_list = arcade.SpriteList()
        self.player_texture= arcade.load_texture("resources/bigboy2.png")
        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.scale = 0.16
        self.player_sprite.center_x = 490
        self.player_sprite.center_y = 510
        self.player_list.append(self.player_sprite)
        
        #Lightweight Box
        self.box_list = arcade.SpriteList()
        box_texture = arcade.load_texture("resources/lightweight-removebg-preview.png")
        box_positions = [
            (490,330),
            (610,450),
            (670,450),
            (670,210),
        ]
        for x,y in box_positions:
            box_sprite= arcade.Sprite(box_texture)
            box_sprite.scale = 0.3
            box_sprite.center_x = x
            box_sprite.center_y = y

            box_sprite.start_x = x
            box_sprite.start_y = y
            self.box_list.append(box_sprite)

        #goal
        self.goal_list = arcade.SpriteList()
        goal_texture = arcade.load_texture("resources/x.png")
        goal_positions = [
            (550,330),
            (610,570),
            (490,150),
            (850,390),
        ]

        for x,y in goal_positions:
            goal_sprite = arcade.Sprite(goal_texture)
            goal_sprite.scale = 0.2
            goal_sprite.center_x = x
            goal_sprite.center_y = y
            self.goal_list.append(goal_sprite)

    def reset(self):
        """Reset the game to the initial state."""
        self.player_sprite.center_x = 490
        self.player_sprite.center_y = 510
        
        for box in self.box_list:
            box.center_x = box.start_x
            box.center_y = box.start_y

        self.game_won= False

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

        self.wall_list.draw()
        arcade.draw_sprite(self.player_sprite)
        self.player_list.draw()
        self.box_list.draw()
        self.goal_list.draw()

        if self.game_won:
            self.win_text.draw()


    def on_update(self, delta_time):
        pass
    
    def check_win(self):
        for goal in self.goal_list:
            found_box = False
            for box in self.box_list:
                if box.center_x == goal.center_x and box.center_y == goal.center_y:
                    found_box = True
                    break
            if not found_box:
                return False
        return True
    
    def try_move(self, dx, dy):
        move_x = dx * TILE_SIZE
        move_y = dy * TILE_SIZE

        player = self.player_sprite
        target_x = player.center_x + move_x
        target_y = player.center_y + move_y

        # wall blocking
        for wall in self.wall_list:
            if wall.center_x == target_x and wall.center_y == target_y:
                return

        # box logic
        for box in self.box_list:
            if box.center_x == target_x and box.center_y == target_y:

                box_target_x = box.center_x + move_x
                box_target_y = box.center_y + move_y

                for wall in self.wall_list:
                    if wall.center_x == box_target_x and wall.center_y == box_target_y:
                        return

                for other_box in self.box_list:
                    if other_box is not box:
                        if other_box.center_x == box_target_x and other_box.center_y == box_target_y:
                            return

                box.center_x = box_target_x
                box.center_y = box_target_y
                break
        
        if self.check_win() == True:
            self.game_won = True
        


        player.center_x = target_x
        player.center_y = target_y


    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        
        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if self.game_won:
            if key == arcade.key.R:
                self.reset()
            else:
                return
        elif key == arcade.key.UP or key == arcade.key.W:
            self.try_move(0,1)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.try_move(0,-1)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.try_move(-1,0)
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.try_move(1,0)
        elif key == arcade.key.R:
            self.reset()


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
    game.setup()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()



if __name__ == "__main__":
    main()