import pygame

def table_clicked(screen, box_rect, display_box):
    if not display_box:
        print("Table 1 clicked!")
        pygame.draw.rect(screen, (255, 90, 0), box_rect)
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

    # Create button rectangles for the menu items
    chicken_rect = pygame.Rect(screen_width // 2 - 150, screen_height - 75, 100, 50)
    beef_rect = pygame.Rect(screen_width // 2 - 50, screen_height - 75, 100, 50)
    carrots_rect = pygame.Rect(screen_width // 2 + 50, screen_height - 75, 100, 50)

    font = pygame.font.Font(None, 24)  # Font for the order text
    order_text = ["Orders:", "Table 1:"]

    display_box = False

    running = True
    while running:
        screen.fill((255, 255, 255))  # Fill the screen with white color

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # If the escape key is pressed
                    return  # Return to the main menu
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if table_rect.collidepoint(event.pos):
                        display_box = table_clicked(screen, box_rect, display_box)
                    elif display_box and box_rect.collidepoint(event.pos):
                        display_box = False
                    elif chicken_rect.collidepoint(event.pos):
                        order_text[1] = "Table 1: Chicken"  # Update the "Table 1" order
                    elif beef_rect.collidepoint(event.pos):
                        order_text[1] = "Table 1: Beef"  # Update the "Table 1" order
                    elif carrots_rect.collidepoint(event.pos):
                        order_text[1] = "Table 1: Carrots"  # Update the "Table 1" order

        pygame.draw.rect(screen, (0, 0, 255), table_rect)  # Draw the table rectangle
        screen.blit(font.render("Table 1", True, (0, 0, 0)), (table_rect.x + 10, table_rect.y + 10))  # Draw "Table 1" on the table rectangle

        pygame.draw.rect(screen, (0, 255, 0), chicken_rect)  # Draw the chicken button
        pygame.draw.rect(screen, (0, 255, 0), beef_rect)  # Draw the beef button
        pygame.draw.rect(screen, (0, 255, 0), carrots_rect)  # Draw the carrots button

        # Draw the text on the buttons
        screen.blit(font.render("Chicken", True, (0, 0, 0)), (chicken_rect.x + 10, chicken_rect.y + 10))
        screen.blit(font.render("Beef", True, (0, 0, 0)), (beef_rect.x + 30, beef_rect.y + 10))
        screen.blit(font.render("Carrots", True, (0, 0, 0)), (carrots_rect.x + 10, carrots_rect.y + 10))

        if display_box:
            pygame.draw.rect(screen, (255, 90, 0), box_rect)
            for i, line in enumerate(order_text):
                order_surface = font.render(line, True, (0, 0, 0))  # Black text
                screen.blit(order_surface, (box_rect.x + 10, box_rect.y + 10 + i*30))  # Draw the text inside the box

        pygame.display.flip()

    pygame.quit()

def main():
    run_waiter_button()

if __name__ == "__main__":
    main()