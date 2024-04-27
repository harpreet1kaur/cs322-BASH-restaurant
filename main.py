import pygame
from src.services.buttonMaker import makeButton
from src.utils.MenuRender.waiterButton import run_waiter_button
from src.utils.MenuRender.chefButton import run_chef_button

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Button Example")



    while True:
        screen.fill((255, 255, 255))
        chefButton = makeButton(screen, 350, 150, 120, 50, "Chef", (50, 168, 82))
        waiterButton = makeButton(screen, 350, 225, 120, 50, "waiter", (50, 168, 82))
        ManagerButton = makeButton(screen, 350, 300, 120, 50, "manager", (50, 168, 82))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if chefButton.collidepoint(event.pos):
                    print("chef Button clicked!")
                    run_chef_button()
                if waiterButton.collidepoint(event.pos):
                    print("waiter Button clicked!")
                    run_waiter_button()
                if ManagerButton.collidepoint(event.pos):
                    print("manager Button clicked!")

        pygame.display.flip()

if __name__ == "__main__":
    main()