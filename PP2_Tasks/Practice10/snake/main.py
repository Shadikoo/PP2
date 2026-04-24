import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Improved")

BLACK = (15, 15, 15)
GRID = (30, 30, 30)
GREEN = (0, 200, 100)
HEAD = (0, 255, 150)
RED = (255, 80, 80)
WHITE = (240, 240, 240)
GRAY = (80, 80, 80)

font = pygame.font.SysFont("Arial", 22)
big_font = pygame.font.SysFont("Arial", 42)

clock = pygame.time.Clock()


def reset_game():
    global snake, dx, dy, score, level, foods_eaten, FPS, game_over, food

    snake = [(100, 100), (80, 100), (60, 100)]
    dx, dy = CELL, 0

    score = 0
    level = 1
    foods_eaten = 0
    FPS = 8

    game_over = False
    food = random_free_cell()


def out_of_bounds(x, y):
    return x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT


def random_free_cell():
    while True:
        cell = (
            random.randrange(0, WIDTH, CELL),
            random.randrange(0, HEIGHT, CELL)
        )
        if cell not in snake:
            return cell


reset_game()

running = True

while running:

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -CELL
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, CELL
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -CELL, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = CELL, 0

        if game_over and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if restart_button.collidepoint(mouse_pos):
                    reset_game()

    if not game_over:
        new_head = (snake[0][0] + dx, snake[0][1] + dy)

        if out_of_bounds(*new_head) or new_head in snake[1:]:
            game_over = True
        else:
            snake.insert(0, new_head)

            if new_head == food:
                foods_eaten += 1
                score += 1

                if foods_eaten % 4 == 0:
                    level += 1
                    FPS += 2

                food = random_free_cell()
            else:
                snake.pop()

    screen.fill(BLACK)

    for x in range(0, WIDTH, CELL):
        pygame.draw.line(screen, GRID, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(screen, GRID, (0, y), (WIDTH, y))

    for i, part in enumerate(snake):
        color = HEAD if i == 0 else GREEN
        pygame.draw.rect(screen, color, (part[0], part[1], CELL, CELL))

    pygame.draw.circle(
        screen,
        RED,
        (food[0] + CELL // 2, food[1] + CELL // 2),
        CELL // 2
    )

    hud_rect = pygame.Rect(0, 0, WIDTH, 40)
    pygame.draw.rect(screen, (25, 25, 25), hud_rect)

    hud = font.render(f"Score: {score}   Level: {level}", True, WHITE)
    screen.blit(hud, (10, 8))

    if game_over:
        text = big_font.render("GAME OVER", True, WHITE)
        screen.blit(text, (170, 220))

        restart_button = pygame.Rect(220, 300, 160, 50)
        pygame.draw.rect(screen, GRAY, restart_button)
        pygame.draw.rect(screen, WHITE, restart_button, 2)

        restart_text = font.render("RESTART", True, BLACK)
        screen.blit(restart_text, (250, 315))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()