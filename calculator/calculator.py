
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
dot = pygame.image.load("dot.png")
calculator = pygame.image.load("calc_gui.png")
calculator = pygame.transform.scale(calculator, (int(calculator.get_width() * 0.75), int(calculator.get_height() * 0.75)))
cur_num_disp = []
mouse_pos_x = 0
mouse_pos_y = 0
mouse_column = 0
mouse_row = None
nums = ["", ""]
cur_num = 0
sol_num = 0
operation = 7
num_char_map = {"0": zero, "1": one, "2": two, "3": three, "4": four, "5": five, "6": six, "7": seven, "8": eight, "9": nine, ".": dot}
num_gui_map1 = {0: "7", 1: "8", 2: "9"}
num_gui_map2 = {0: "4", 1: "5", 2: "6"}
num_gui_map3 = {0: "1", 1: "2", 2: "3"}


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
        if mouse_row == 0:
            if mouse_column == 3:
                cur_num = 0
                nums = ["", ""]
        if mouse_row == 1:
            if mouse_column == 3:
                cur_num = 1
                opperation = 4
        elif mouse_row == 2:
            if mouse_column == 3:
                cur_num = 1
                opperation = 3
            else:
                nums[cur_num] += num_gui_map1[mouse_column]
        elif mouse_row == 3:
            if mouse_column == 3:
                cur_num = 1
                opperation = 2
            else:
                nums[cur_num] += num_gui_map2[mouse_column]
        elif mouse_row == 4:
            if mouse_column == 3:
                cur_num = 1
                opperation = 1
            else:
                nums[cur_num] += num_gui_map3[mouse_column]
        elif mouse_row == 5:
            if mouse_column == 1:
                nums[cur_num] += "0"
            if mouse_column == 2: # add check to make sure no previous .
                nums[cur_num] += "."
            elif mouse_column == 3:
                if opperation == 1:
                    sol_num = float(nums[0]) + float(nums[1])
                elif opperation == 2:
                    sol_num = float(nums[0]) - float(nums[1])
                elif opperation == 3:
                    sol_num = float(nums[0]) * float(nums[1])
                elif opperation == 4:
                    sol_num = float(nums[0]) / float(nums[1])
                cur_num = 0
                nums[0] = str(sol_num)
                nums[1] = str("")
        mouse_was_pressed = True
    if not pygame.mouse.get_pressed()[0]:
        mouse_was_pressed = False
    if len(nums[0]) > 15:
        nums[0] = ""
    if len(nums[1]) > 15:
        nums[1] = ""
    #print(nums[cur_num])
    screen.fill((0, 0, 0)) 
    screen.blit(calculator, (0, 0))
    cur_num_disp.clear()
    for i in range(len(nums[cur_num])):
        cur_num_disp.append(num_char_map[nums[cur_num][i]])
    for i in range(15):
        if len(cur_num_disp) <= i:
            break
        screen.blit(cur_num_disp[i], (-200 + i * 30, -135))

    pygame.display.flip()