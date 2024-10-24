import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
HEADER_HEIGHT = 40  # Add this line
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GAME_AREA_HEIGHT = WINDOW_HEIGHT - HEADER_HEIGHT  # Add this line
GRID_HEIGHT = GAME_AREA_HEIGHT // GRID_SIZE  # Add this line

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
DARK_GREEN = (0, 100, 0)  # For the boundaries
GRID_COLOR = (30, 30, 30)  # Dark gray for grid lines

# Fix the window creation
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.length = 1
        self.has_boundaries = True  # Add this line

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        
        if self.has_boundaries:
            # With boundaries: hitting the wall ends the game
            new_x = cur[0] + x
            new_y = cur[1] + y
            if new_x < 0 or new_x >= GRID_WIDTH or new_y < 0 or new_y >= GRID_HEIGHT:
                return False
            new = (new_x, new_y)
        else:
            # Without boundaries: wrap around the screen
            new = ((cur[0] + x) % GRID_WIDTH, (cur[1] + y) % GRID_HEIGHT)
        
        if new in self.positions[3:]:
            return False
        
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()
        return True

    def reset(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.length = 1

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1), 
                        random.randint(0, GRID_HEIGHT-1))

def show_game_over_screen(window, score):
    window.fill(BLACK)
    
    # Game Over text
    font_large = pygame.font.Font(None, 72)
    font_small = pygame.font.Font(None, 36)
    
    game_over_text = font_large.render('GAME OVER', True, WHITE)
    score_text = font_small.render(f'Final Score: {score}', True, WHITE)
    play_again_text = font_small.render('Press SPACE to Play Again', True, GRAY)
    title_screen_text = font_small.render('Press ENTER for Title Screen', True, GRAY)
    
    game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 50))
    score_rect = score_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 20))
    play_again_rect = play_again_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 70))
    title_screen_rect = title_screen_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 120))
    
    window.blit(game_over_text, game_over_rect)
    window.blit(score_text, score_rect)
    window.blit(play_again_text, play_again_rect)
    window.blit(title_screen_text, title_screen_rect)
    pygame.display.update()
    
    # Wait for player input
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True  # Continue with same mode
                elif event.key == pygame.K_RETURN:
                    return None  # Return to title screen
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return False
    return True

def show_title_screen(window):
    window.fill(BLACK)
    
    # Title text
    font_large = pygame.font.Font(None, 100)
    font_small = pygame.font.Font(None, 36)
    
    title_text = font_large.render('SNAKE', True, GREEN)
    option1_text = font_small.render('1. Play with Boundaries', True, WHITE)
    option2_text = font_small.render('2. Play without Boundaries', True, WHITE)
    start_text = font_small.render('Press 1 or 2 to Start', True, GRAY)
    
    title_rect = title_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 100))
    option1_rect = option1_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    option2_rect = option2_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 50))
    start_rect = start_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 120))
    
    window.blit(title_text, title_rect)
    window.blit(option1_text, option1_rect)
    window.blit(option2_text, option2_rect)
    window.blit(start_text, start_rect)
    pygame.display.update()
    
    # Wait for player input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return True  # With boundaries
                elif event.key == pygame.K_2:
                    return False  # Without boundaries
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return None

def draw_boundaries():
    boundary_thickness = 2
    boundary_rect = pygame.Rect(0, HEADER_HEIGHT, WINDOW_WIDTH, GAME_AREA_HEIGHT)
    pygame.draw.rect(window, DARK_GREEN, boundary_rect, boundary_thickness)

def draw_grid():
    # Vertical lines
    for x in range(0, WINDOW_WIDTH, GRID_SIZE):
        pygame.draw.line(window, GRID_COLOR, 
                        (x, HEADER_HEIGHT), 
                        (x, WINDOW_HEIGHT))
    # Horizontal lines
    for y in range(HEADER_HEIGHT, WINDOW_HEIGHT, GRID_SIZE):
        pygame.draw.line(window, GRID_COLOR, 
                        (0, y), 
                        (WINDOW_WIDTH, y))

def draw_header(score):
    # Draw header background
    header_rect = pygame.Rect(0, 0, WINDOW_WIDTH, HEADER_HEIGHT)
    pygame.draw.rect(window, GRID_COLOR, header_rect)
    
    # Draw bottom border of header
    pygame.draw.line(window, DARK_GREEN, 
                    (0, HEADER_HEIGHT), 
                    (WINDOW_WIDTH, HEADER_HEIGHT), 2)
    
    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, WHITE)
    score_rect = score_text.get_rect(midleft=(20, HEADER_HEIGHT/2))
    window.blit(score_text, score_rect)

def main():
    clock = pygame.time.Clock()
    
    while True:
        # Show title screen and get game mode
        has_boundaries = show_title_screen(window)
        if has_boundaries is None:  # User quit the game
            return
            
        snake = Snake()
        snake.has_boundaries = has_boundaries
        food = Food()
        score = 0
        game_active = True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN and game_active:
                    if event.key == pygame.K_UP and snake.direction != (0, 1):
                        snake.direction = (0, -1)
                    elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                        snake.direction = (0, 1)
                    elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                        snake.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                        snake.direction = (1, 0)

            if game_active:
                # Update snake position
                if not snake.update():
                    game_active = False
                    result = show_game_over_screen(window, score)
                    if result is False:  # User quit
                        return
                    elif result is None:  # User wants title screen
                        break  # Break inner loop to return to title screen
                    # else result is True, reset game with same mode
                    snake.reset()
                    food.randomize_position()
                    score = 0
                    game_active = True
                    continue

                # Check if snake ate food
                if snake.get_head_position() == food.position:
                    snake.length += 1
                    score += 1
                    food.randomize_position()

                # Draw everything
                window.fill(BLACK)
                
                # Draw grid first
                draw_grid()
                
                # Draw boundaries if in boundary mode
                if snake.has_boundaries:
                    draw_boundaries()
                
                # Draw food (adjust y position for header)
                rect = pygame.Rect(
                    food.position[0] * GRID_SIZE, 
                    food.position[1] * GRID_SIZE + HEADER_HEIGHT,
                    GRID_SIZE, GRID_SIZE
                )
                pygame.draw.rect(window, RED, rect)

                # Draw snake (adjust y position for header)
                for pos in snake.positions:
                    rect = pygame.Rect(
                        pos[0] * GRID_SIZE, 
                        pos[1] * GRID_SIZE + HEADER_HEIGHT,
                        GRID_SIZE, GRID_SIZE
                    )
                    pygame.draw.rect(window, GREEN, rect)

                # Draw header last (so it's on top)
                draw_header(score)

                pygame.display.update()
                clock.tick(10)  # Control game speed

if __name__ == '__main__':
    main()
