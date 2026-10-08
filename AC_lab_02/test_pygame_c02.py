import pygame
import math

def Exemplul_1():
    def minsincos(s):
        return min(abs(math.sin(s)), abs(math.cos(s)))

    white = 255, 255, 255
    red = 255, 0, 0
    dim = 600
    ddim = dim * math.sqrt(2.0)
    screen = pygame.display.set_mode((dim, dim))

    screen.fill(white)
    t = 0
    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        x = round(ddim * minsincos(t))
        y = round(ddim * minsincos(1.201 * t + 0.2024))
        screen.set_at((x, y), red)
        pygame.display.flip()
        t += 0.001
    print("Gata!")


if __name__ == '__main__':
    pygame.init()
    Exemplul_1()
