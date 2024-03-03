
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
mouse_pos_x = 0
mouse_pos_y = 0
mouse_column = 0
mouse_row = None
num1 = "0"
pygame.init()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    for i in range(5):
        if mouse_pos_x >= (i) * 125 and mouse_pos_x < (i + 1) * 125:
            mouse_column = i
            break
    for i in range(6):
        if mouse_pos_y >= 170:
            if mouse_pos_y >= i * 71 + 170 and mouse_pos_y <= (i + 1) * 71 + 170:
                mouse_row = i
                break
        else:
            break
    if pygame.mouse.get_pressed()[0] and not mouse_was_pressed:
        if mouse_column == 0:
            if mouse_row == 2:
                num1 += "7"
                mouse_was_pressed = True
    if not pygame.mouse.get_pressed()[0]:
        mouse_was_pressed = False
    print(num1)
    screen.fill((0, 0, 0)) 
    screen.blit(calculator, (0, 0))
    for i in range(12):
        screen.blit(cur_num_disp[i], (-200 + i * 30, -135))

    pygame.display.flip()