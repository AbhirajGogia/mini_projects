import pygame
import time
import random
import pygame_menu


class SnakeGame:

    def __init__(self):
        # Initializes Pygame modules and parameters
        pygame.init()

        self.display_width = 600
        self.display_height = 400

        # Initializing colors
        self.blue, self.red, self.green, self.white, self.black = (
            63, 61, 161), (235, 94, 52), (105, 207, 171), (255, 255, 255), (66, 64, 63)
        self.background_color = self.white
        self.snake_color = self.blue
        self.food_color = self.black

        # Creates surface
        self.dis = pygame.display.set_mode(
            (self.display_width, self.display_height))
        pygame.display.set_caption("Snake by Abhiraj Gogia")

        # Initializing elements of the game
        self.game_over = False
        self.game_close = False
        self.clock = pygame.time.Clock()
        self.snake_block = 10
        self.start_speed = 15
        self.font_style = pygame.font.SysFont("monospace", 15)
        self.score_font = pygame.font.SysFont("monospace", 30)
        self.menu = pygame_menu.Menu(
            self.display_height / 2,
            self.display_width / 2,
            "Snake",
            theme=pygame_menu.themes.THEME_SOLARIZED)

        # Snake starting position
        self.snake_x = self.display_width / 2
        self.snake_y = self.display_height / 2

        self.snake_x_change = 0
        self.snake_y_change = 0

    def player_score(self, score):
        """ Outputs text with the player's current score. """
        value = self.score_font.render("Score: " + str(score), True, self.red)
        self.dis.blit(value, [0, 0])

    def player_snake(self, snake_block, snake_list):
        """ Draws in player's snake based upon length """
        for i in snake_list:
            pygame.draw.rect(
                self.dis, self.snake_color, [
                    i[0], i[1], snake_block, snake_block])

    def message(self, msg, color):
        """ Outputs a message across screen """

        mes = self.font_style.render(msg, True, color)
        self.dis.blit(mes, [self.display_width / 10, self.display_height / 5])

    def start_game(self):
        """ Starts game when menu button is clicked """
        self.gameLoop(self.start_speed)

    def boundary_hit(self, x, y, width, height):
        """ Closes game if the snakes position leaves the boundary """
        if x < 0 or x >= width or y < 0 or y >= height:
            self.game_close = True

    def keyboard_input(self, event, action):
        if action == "endgame":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.game_over = True
                    self.game_close = False
                if event.key == pygame.K_r:
                    self.gameLoop(self.start_speed)
                if event.key == pygame.K_m:
                    self.game_over = False
                    self.game_close = False
                    self.menu.mainloop(self.dis)
            elif event.type == pygame.QUIT:
                self.game_over = True
                self.game_close = False
        elif action == "exit":
            if event.type == pygame.QUIT:
                self.game_over = True

        elif action == "movement":
            if event.type == pygame.QUIT:
                self.game_over = True
            # Mapping arrow key presses to changes in x and y coordinates
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake_x_change = - self.snake_block
                    self.snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    self.snake_x_change = self.snake_block
                    self.snake_y_change = 0
                elif event.key == pygame.K_UP:
                    self.snake_x_change = 0
                    self.snake_y_change = -self.snake_block
                elif event.key == pygame.K_DOWN:
                    self.snake_x_change = 0
                    self.snake_y_change = self.snake_block

    def gameLoop(self, snake_speed):
        """ Runs game application by updating parameters such as food and snake location,
        snake length, score and is responsible for keyboard inputs to control snake"""

        self.game_over = False
        self.game_close = False

        # Resets snake position
        self.snake_x = self.display_width / 2
        self.snake_y = self.display_height / 2
        self.snake_x_change = 0
        self.snake_y_change = 0

        snake_list = []
        snake_length = 1

        # Sets the position of the first food
        food_x = round(
            random.randrange(
                0, self.display_width - self.snake_block) / 10.0) * 10.0
        food_y = round(
            random.randrange(
                0, self.display_height - self.snake_block) / 10.0) * 10.0

        while not self.game_over:

            # Displays end game message
            while self.game_close:
                self.dis.fill(self.background_color)
                self.message(
                    "Game Over! Press Q-Quit or R-Play Again or M-Main Menu",
                    self.red)
                self.player_score(snake_length - 1)
                pygame.display.update()

                # Ends game if Q or (x) button is pressed, restarts if R is
                # pressed, main menu if M is pressed
                for event in pygame.event.get():
                    self.keyboard_input(event, "endgame")

            # Pressing (x) button ends game
            for event in pygame.event.get():
                self.keyboard_input(event, "exit")

                # Mapping arrow key presses to changes in x and y coordinates
                if event.type == pygame.KEYDOWN:
                    self.keyboard_input(event, "movement")

            # Ends game if boundary is hit
            self.boundary_hit(
                self.snake_x,
                self.snake_y,
                self.display_width,
                self.display_height)

            # Updates snake position
            self.snake_x += self.snake_x_change
            self.snake_y += self.snake_y_change

            # Changes screen colour to black
            self.dis.fill(self.background_color)

            # Creating food
            pygame.draw.rect(
                self.dis, self.food_color, [
                    food_x, food_y, self.snake_block, self.snake_block])

            snake_head = []
            # stores current position of snake head
            snake_head.append(self.snake_x)
            snake_head.append(self.snake_y)
            snake_list.append(snake_head)

            # updates snake head position
            if len(snake_list) > snake_length:
                del snake_list[0]

            # ends game if snake head touches any part of the body
            for i in snake_list[:-1]:
                if i == snake_head:
                    self.game_close = True

            # generates player's snake
            self.player_snake(self.snake_block, snake_list)

            # outputs player score
            self.player_score(snake_length - 1)

            pygame.display.update()

            # If food is eaten, new food is created. Snake length and speed
            # increase
            if self.snake_x == food_x and self.snake_y == food_y:
                food_x = round(
                    random.randrange(
                        0, self.display_width - self.snake_block) / 10.0) * 10.0
                food_y = round(
                    random.randrange(
                        0, self.display_height - self.snake_block) / 10.0) * 10.0
                snake_length += 1
                snake_speed += 1

            # Updates clock
            self.clock.tick(snake_speed)

        # Uninitializes everything and ends program
        pygame.quit()
        quit()

    def game_setup(self, colour='Light', value=1):
        """ Makes changes to color modes and sets up interactive menu. """

        if value == 1:
            self.background_color = self.white
            self.snake_color = self.blue
            self.food_color = self.black
            # Resets menu to be light mode
            self.menu = pygame_menu.Menu(
                self.display_height / 2,
                self.display_width / 2,
                "Snake",
                theme=pygame_menu.themes.THEME_SOLARIZED)
            self.menu.add_button('Play', self.start_game)
            self.menu.add_selector(
                'Colour :', [
                    ('Light', 1), ('Dark', 2)], onchange=self.game_setup)
            self.menu.add_button('Quit', pygame_menu.events.EXIT)
            self.menu.mainloop(self.dis)
        elif value == 2:
            self.background_color = self.black
            self.snake_color = self.green
            self.food_color = self.white
            # Resets menu to be dark mode
            self.menu = pygame_menu.Menu(
                self.display_height / 2,
                self.display_width / 2,
                "Snake",
                theme=pygame_menu.themes.THEME_DARK)
            self.menu.add_button('Play', self.start_game)
            self.menu.add_selector(
                'Colour :', [
                    ('Dark', 2), ('Light', 1)], onchange=self.game_setup)
            self.menu.add_button('Quit', pygame_menu.events.EXIT)
            self.menu.mainloop(self.dis)


if __name__ == "__main__":
    game = SnakeGame()
    game.game_setup()
