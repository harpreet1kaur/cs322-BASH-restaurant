import pygame

def insert_new_text(new_text):
    screen_width = 800
    box_rects = [pygame.Rect(screen_width // 2 - 75 + i*200, 800 // 2 - 100, 150, 200) for i in range(3)]
    stats_texts = [["Stats:", "Example Text 1"], ["Stats:", "Example Text 2"], ["Stats:", "Example Text 3"]]
    display_boxes = [True, True, True]

    box_rects.append(pygame.Rect(screen_width // 2 - 75 + len(box_rects)*200, 800 // 2 - 100, 150, 200))  # Add a new box
    stats_texts.append(["Stats:", new_text])  # Add the new text
    display_boxes.append(True)  # Display the new box immediately

    return box_rects, stats_texts, display_boxes

def run_stats_button():
    pygame.init()

    # Set up the window
    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Stats Button")

    # Create rectangles for the boxes
    box_rects = [pygame.Rect(screen_width // 2 - 75 + i*200, screen_height // 2 - 100, 150, 200) for i in range(3)]

    font = pygame.font.Font(None, 24)  # Font for the text
    stats_texts = [["Popular Item:", "Chicken"], ["Stats:", "Example Text 2"], ["Stats:", "Example Text 3"]]

    display_boxes = [True, True, True]  # Initialize as True to display the text immediately

    scroll_x = 0  # Initialize scroll_x to 0

    running = True
    while running:
        screen.fill((255, 255, 255))  # Fill the screen with white color

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # If the escape key is pressed
                    return  # Return to the main menu
                elif event.key == pygame.K_a:  # If the 'a' key is pressed
                    insert_new_text(box_rects, stats_texts, display_boxes, "New Example Text {}".format(len(stats_texts) + 1))  # Insert a new text box
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll left
                    scroll_x = min(scroll_x + 15, 0)
                elif event.button == 5:  # Scroll right
                    scroll_x -= 15

        for i, box_rect in enumerate(box_rects):
            if display_boxes[i]:
                pygame.draw.rect(screen, (255, 90, 0), box_rect.move(scroll_x, 0))
                for j, line in enumerate(stats_texts[i]):
                    stats_surface = font.render(line, True, (0, 0, 0))  # Black text
                    screen.blit(stats_surface, (box_rect.x + 10 + scroll_x, box_rect.y + 10 + j*30))  # Draw the text inside the box

        pygame.display.flip()

    pygame.quit()

def main():
    run_stats_button()

if __name__ == "__main__":
    main()