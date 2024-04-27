import pygame

def table_clicked(screen, box_rect, display_box, font):
    if not display_box:
        print("Table 1 clicked!")
        pygame.draw.rect(screen, (255, 90, 0), box_rect)
        order_text = "Orders:\nTable 1: Chicken"
        order_surface = font.render(order_text, True, (0, 0, 0))  # Black text
        screen.blit(order_surface, (box_rect.x + 10, box_rect.y + 10))  # Draw the text inside the box
        return True
    elif display_box and box_rect.collidepoint(pygame.mouse.get_pos()):
        return False
    return display_box

def run_waiter_button():
    pygame.init()

    # Set up the window
    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Waiter Button")

    # Create a button rectangle for the table
    table_rect = pygame.Rect(screen_width // 2 - 50, screen_height // 2 - 25, 100, 50)

    # Create a rectangle for the box
    box_rect = pygame.Rect(screen_width // 2 + 75, screen_height // 2 - 125, 150, 200)

    font = pygame.font.Font(None, 24)  # Font for the order text

    display_box = False

    running = True
    while running:
        screen.fill((255, 255, 255))  # Fill the screen with white color

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if table_rect.collidepoint(event.pos):
                        display_box = table_clicked(screen, box_rect, display_box, font)
                    elif display_box and box_rect.collidepoint(event.pos):
                        display_box = False

        pygame.draw.rect(screen, (0, 0, 255), table_rect)  # Draw the table rectangle

        if display_box:
            pygame.draw.rect(screen, (255, 90, 0), box_rect)
            pygame.draw.line(screen, (0, 0, 0), (table_rect.right, table_rect.centery), (box_rect.left, box_rect.centery), 2)  # Draw a line from the table to the box

        pygame.display.flip()

    pygame.quit()

def main():
    run_waiter_button()

if __name__ == "__main__":
    main()