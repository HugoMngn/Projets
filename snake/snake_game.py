# importation de libraries
import pygame
import time
import random


# création class mère
class Case:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.position = (x, y)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"Case(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


# création class snake
class Snake:
    def __init__(self, initial_position_x, initial_position_y, max_length=2):
        self.head_position = Case(x=initial_position_x, y=initial_position_y)
        self.body = [
            self.head_position,
            Case(self.head_position.x - 10, self.head_position.y),
        ]
        self.direction = "RIGHT"
        self.max_length = max_length

    def head(self) -> Case:
        return self.body[0]

    def get_all_cases(self) -> Case:
        return self.body

    def move(self, new_case=None, remove_tail=True):
        if new_case:
            # nouvelle case
            self.body.insert(0, new_case)
            self.head_position = new_case
        else:
            # continuer même direction
            if self.direction == "UP":
                new_case = Case(x=self.head_position.x, y=self.head_position.y + 10)
            elif self.direction == "DOWN":
                new_case = Case(x=self.head_position.x, y=self.head_position.y - 10)
            elif self.direction == "LEFT":
                new_case = Case(x=self.head_position.x - 10, y=self.head_position.y)
            elif self.direction == "RIGHT":
                new_case = Case(x=self.head_position.x + 10, y=self.head_position.y)

            self.body.insert(0, new_case)
            self.head_position = new_case

        # virer la queue
        if remove_tail:
            if len(self.body) > self.max_length:
                self.body.pop()

    def is_out_of_frame(self, WINDOW_X, WINDOW_Y):
        head = self.body[0]
        return (
            head.x < 0 or head.y < 0 or head.x > WINDOW_X - 10 or head.y > WINDOW_Y - 10
        )

    def is_head_touching_body(self):
        head = self.body[0]
        return any(body == head for body in self.body[1:])


def new_fruit():
    x = random.randint(0, ((WINDOW_X - 10) // 10) * 10)
    y = random.randint(0, ((WINDOW_Y - 10) // 10) * 10)
    return Case(x, y)


# defining colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
RED = (255, 0, 0)

# Initialising pygame et variables initiales
pygame.init()

SNAKE_SPEED = 10
WINDOW_X = 800
WINDOW_Y = 600

snake = Snake(
    (random.randint(0, ((WINDOW_X - 10) // 10) * 10)),
    (random.randint(0, ((WINDOW_Y - 10) // 10) * 10)),
)
fruit = new_fruit()
score = 0
tick_count = SNAKE_SPEED
paused = False

# verification serpent et fruit n'apparaissent pas hors écran
while (
    snake.head_position.x < 0
    or snake.head_position.x > WINDOW_X
    or snake.head_position.y < 0
    or snake.head_position.x > WINDOW_Y
):
    del snake
    snake = Snake(
        (random.randint(0, ((WINDOW_X - 10) // 10) * 10)),
        (random.randint(0, ((WINDOW_Y - 10) // 10) * 10)),
    )

while fruit.x < 0 or fruit.x > WINDOW_X + 10 or fruit.y < 0 or fruit.x > WINDOW_Y:
    del fruit
    fruit = new_fruit()

# Initialise game window
pygame.display.set_caption("Jeu du serpent")
game_window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Main Function
while True:
    # handling pause
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused

    if not paused:
        # handling key events
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = "UP"
                # new_case = Case(x=snake.head_position.x, y=snake.head_position.y - 10)       ///pour déplacer tout en appuyant plutot que de simplement changer de direction
                # snake.move(new_case)                                                         ///à activer pour rendre le jeu plus rapide
            if event.key == pygame.K_DOWN:
                snake.direction = "DOWN"
                # new_case = Case(x=snake.head_position.x, y=snake.head_position.y + 10)
                # snake.move(new_case)
            if event.key == pygame.K_LEFT:
                snake.direction = "LEFT"
                # new_case = Case(x=snake.head_position.x - 10, y=snake.head_position.y)
                # snake.move(new_case)
            if event.key == pygame.K_RIGHT:
                snake.direction = "RIGHT"
                # new_case = Case(x=snake.head_position.x + 10, y=snake.head_position.y)
                # snake.move(new_case)

        # Frame Per Second /Refresh Rate
        fps.tick(SNAKE_SPEED)

        # déplacer snake toutes les SNAKE_SPEED ticks
        tick_count += 2  # à changer sur 1,2,5 ou 10 pour accélerer le jeu, si SNAKE_SPEED est toujours sur 10

        if tick_count % SNAKE_SPEED == 0:  # permet le déplacement auto
            if snake.direction == "UP":
                new_case = Case(x=snake.head_position.x, y=snake.head_position.y - 10)
                snake.move(new_case)
            if snake.direction == "DOWN":
                new_case = Case(x=snake.head_position.x, y=snake.head_position.y + 10)
                snake.move(new_case)
            if snake.direction == "LEFT":
                new_case = Case(x=snake.head_position.x - 10, y=snake.head_position.y)
                snake.move(new_case)
            if snake.direction == "RIGHT":
                new_case = Case(x=snake.head_position.x + 10, y=snake.head_position.y)
                snake.move(new_case)

        # Représentation graphique
        game_window.fill(BLACK)

        # Dessin du fruit (case `fruit`)
        pygame.draw.rect(game_window, WHITE, pygame.Rect(fruit.x, fruit.y, 10, 10))

        # Dessin du serpent
        for case in snake.get_all_cases():
            pygame.draw.rect(game_window, GREEN, pygame.Rect(case.x, case.y, 10, 10))

        # eviter fruit hors-screen si besoin (optionnel)
        # while fruit.x < 0 or fruit.x > WINDOW_X or fruit.y < 0 or fruit.x > WINDOW_Y:
        #     del fruit
        #     fruit = new_fruit()

        # manger un fruit (comme pas sur une grille, approximation pour détecter si snake.head==fruit)
        if (fruit.x - 9 <= snake.head_position.x <= fruit.x + 9) and (
            fruit.y - 9 <= snake.head_position.y <= fruit.y + 9
        ):
            del fruit
            snake.max_length += 1
            score += 10
            fruit = new_fruit()

        # Affichage du score
        surface = pygame.font.SysFont("times new roman", 20).render(
            "Score : " + str(score), True, WHITE
        )
        rect = surface.get_rect()
        game_window.blit(surface, rect)

        # Mise à jour de l'écran
        pygame.display.update()

        # gestion game over
        # texte du game over
        game_over = pygame.font.SysFont("times new roman", 36).render(
            "Game Over", True, RED
        )
        game_over_score = pygame.font.SysFont("times new roman", 36).render(
            "Your Score: " + str(score), True, RED
        )

        rect_game_over = game_over_score.get_rect()
        rect_game_over.center = (WINDOW_X // 2, WINDOW_Y // 2)

        rect_go_score = game_over.get_rect()
        rect_go_score.center = (WINDOW_X // 2, WINDOW_Y // 2 - 50)

        # condition game over + affichage
        if (
            snake.is_out_of_frame(WINDOW_X, WINDOW_Y) == True
            or snake.is_head_touching_body() == True
        ):
            game_window.blit(game_over, rect_go_score)
            game_window.blit(game_over_score, rect_game_over)
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            quit()

    else:  # si pause activé (bouton p actuellement)
        # affiché "PAUSE" + petit tuto
        pause = pygame.font.SysFont("times new roman", 36).render("PAUSE", True, WHITE)
        rect_pause = game_over_score.get_rect()
        rect_pause.center = (WINDOW_X // 2 + 50, WINDOW_Y // 2 - 100)
        game_window.blit(pause, rect_pause)

        tuto1 = pygame.font.SysFont("times new roman", 20).render(
            "UP arrow= snake go up", True, WHITE
        )
        rect_tuto1 = game_over_score.get_rect()
        rect_tuto1.center = (WINDOW_X // 2, (WINDOW_Y // 2) - 50)
        game_window.blit(tuto1, rect_tuto1)

        tuto2 = pygame.font.SysFont("times new roman", 20).render(
            "LEFT arrow = snake go left", True, WHITE
        )
        rect_tuto2 = game_over_score.get_rect()
        rect_tuto2.center = (WINDOW_X // 2, WINDOW_Y // 2)
        game_window.blit(tuto2, rect_tuto2)

        tuto3 = pygame.font.SysFont("times new roman", 20).render(
            "DOWN arrow= snake go down", True, WHITE
        )
        rect_tuto3 = game_over_score.get_rect()
        rect_tuto3.center = (WINDOW_X // 2, (WINDOW_Y // 2) + 50)
        game_window.blit(tuto3, rect_tuto3)

        tuto4 = pygame.font.SysFont("times new roman", 20).render(
            "RIGHT arrow= snake go right", True, WHITE
        )
        rect_tuto4 = game_over_score.get_rect()
        rect_tuto4.center = (WINDOW_X // 2, (WINDOW_Y // 2) + 100)
        game_window.blit(tuto4, rect_tuto4)

        pygame.display.update()

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = False

        pygame.display.update()
