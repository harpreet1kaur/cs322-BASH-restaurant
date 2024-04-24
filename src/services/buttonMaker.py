import pygame

def makeButton(x: int, y: int, width: int, height: int, text: str="", color: tuple=(0, 0, 0)):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    font = pygame.font.Font(None, 36)
    text = font.render(text, True, (255, 255, 255))
    text_rect = text.get_rect(center=(x + width // 2, y + height // 2))

    button = pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
    screen.blit(text, text_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(pygame.mouse.get_pos()):
                    print("Button clicked!")