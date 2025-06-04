import pygame

pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed")