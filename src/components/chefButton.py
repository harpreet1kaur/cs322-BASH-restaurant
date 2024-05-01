import pygame

def testchef_clicked(screen, box_rect, display_box, font):
    if not display_box:
        print("Chef clicked!")
        pygame.draw.rect(screen, (255, 90, 0), box_rect)
        return True
    elif display_box and box_rect.collidepoint(pygame.mouse.get_pos()):
        return False
    return display_box

def testrun_chef_button():
    pygame.init()

    # Set up the window
    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Chef Button")
    # Create rectangles for the boxes
    box_rects = [pygame.Rect(screen_width // 2 - 75 + i*200, screen_height // 2 - 100, 150, 200) for i in range(3)]

    # Create button rectangles for sending out orders
    send_rects = [pygame.Rect(screen_width // 2 - 75 + i*200, screen_height // 2 + 125, 150, 50) for i in range(3)]

    font = pygame.font.Font(None, 24)  # Font for the order text
    order_texts = [["Orders:", "Table 1: test"], ["Orders:", "Table 2: Fish"], ["Orders:", "Table 3: Steak"]]

    display_boxes = [True, True, True]  # Initialize as True to display the order text immediately

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
                    order_texts.append(["Orders:", "Table 1: New Order".format(len(order_texts) + 1)])  # Add a new order
                    box_rects.append(pygame.Rect(screen_width // 2 - 75 + len(box_rects)*200, screen_height // 2 - 100, 150, 200))  # Add a new box
                    send_rects.append(pygame.Rect(screen_width // 2 - 75 + len(send_rects)*200, screen_height // 2 + 125, 150, 50))  # Add a new send button
                    display_boxes.append(True)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i, box_rect in enumerate(box_rects):
                        if box_rect.move(scroll_x, 0).collidepoint(event.pos):
                            display_boxes[i] = chef_clicked(screen, box_rect, display_boxes[i], font)
                    for i, send_rect in enumerate(send_rects):
                        if send_rect.move(scroll_x, 0).collidepoint(event.pos):
                            order_texts.pop(i)  # Remove the finished order
                            box_rects.pop(i)  # Remove the corresponding box
                            send_rects.pop(i)  # Remove the corresponding send button
                            display_boxes.pop(i)  # Remove the corresponding display box flag
                            # Shift over the remaining orders
                            for j in range(i, len(box_rects)):
                                box_rects[j].x -= 200
                                send_rects[j].x -= 200
                elif event.button == 4:  # Scroll left
                    scroll_x = min(scroll_x + 15, 0)
                elif event.button == 5:  # Scroll right
                    scroll_x -= 15

        for i, box_rect in enumerate(box_rects):
            if display_boxes[i]:
                pygame.draw.rect(screen, (255, 90, 0), box_rect.move(scroll_x, 0))
                pygame.draw.rect(screen, (0, 255, 0), send_rects[i].move(scroll_x, 0))  # Draw the send orders button
                done_surface = font.render("Done", True, (0, 0, 0))  # Black text for "Done"
                screen.blit(done_surface, (send_rects[i].centerx - done_surface.get_width() // 2 + scroll_x, send_rects[i].centery - done_surface.get_height() // 2))  # Draw the "Done" text in the center of the send orders button
                for j, line in enumerate(order_texts[i]):
                    order_surface = font.render(line, True, (0, 0, 0))  # Black text
                    screen.blit(order_surface, (box_rect.x + 10 + scroll_x, box_rect.y + 10 + j*30))  # Draw the text inside the box

        pygame.display.flip()

    pygame.quit()
