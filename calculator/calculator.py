
import pygame

screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Calculator")
zero = pygame.image.load("zero.png")
one = pygame.image.load("onefr.png")
two = pygame.image.load("two.png")
three = pygame.image.load("three.png")
four = pygame.image.load("four.png")
five = pygame.image.load("five.png")
six = pygame.image.load("six.png")
seven = pygame.image.load("seven.png")
eight = pygame.image.load("eight.png")
nine = pygame.image.load("nine.png")
dot = pygame.image.load("Dot.png")
calculator = pygame.image.load("calc_gui.png")
calculator = pygame.transform.scale(calculator, (int(calculator.get_width() * 0.75), int(calculator.get_height() * 0.75)))
cur_num_disp = [one, two, three, four, five, six, dot, seven, eight, nine, zero, one]

pygame.init()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    print("working")

    screen.fill((0, 0, 0)) 
    screen.blit(calculator, (0, 0))
    for i in range(12):
        screen.blit(cur_num_disp[i], (-200 + i * 30, -135))
    
    #screen.blit(zero, (-200, 0))
    #screen.blit(one, (-150, 0))
    #screen.blit(two, (-100, 0))
    #screen.blit(three, (-50, 0))
    #screen.blit(four, (0, 0))
    #screen.blit(five, (50, 0))
    #screen.blit(six, (100, 0))
    #screen.blit(seven, (150, 0))
    #screen.blit(eight, (200, 0))
    #screen.blit(nine, (250, 0))
    #screen.blit(dot, (270, 0))

    pygame.display.flip()