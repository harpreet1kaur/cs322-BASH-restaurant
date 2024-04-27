import pygame

def makeButton(screen, x: int, y: int, width: int, height: int, text: str="", color: tuple=(0, 0, 0)):
    font = pygame.font.Font(None, 36)
    text = font.render(text, True, (0, 0, 0))  # Black text
    text_rect = text.get_rect(center=(x + width // 2, y + height // 2))

    button = pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
    screen.blit(text, text_rect)
    
    return button