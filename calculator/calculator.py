
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
cur_num_disp = []
mouse_pos_x = 0
mouse_pos_y = 0
mouse_column = 0
mouse_row = None
nums = ["", ""]
num1 = ""
num2 = ""
cur_num = 0
sol_num = 0
operation = 7

test_var = "1234.56789"
print(test_var[4])

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
        if mouse_row == 1:
            if mouse_column == 3:
                cur_num = 1
                opperation = 4
        elif mouse_row == 2:
            if mouse_column == 0: 
                nums[cur_num] += "7"
            elif mouse_column == 1:
                nums[cur_num] += "8"
            elif mouse_column == 2:
                nums[cur_num] += "9"
            elif mouse_column == 3:
                cur_num = 1
                opperation = 3
        elif mouse_row == 3:
            if mouse_column == 0: 
                nums[cur_num] += "4"
            elif mouse_column == 1:
                nums[cur_num] += "5"
            elif mouse_column == 2:
                nums[cur_num] += "6"
            elif mouse_column == 3:
                cur_num = 1
                opperation = 2
        elif mouse_row == 4:
            if mouse_column == 0: 
                nums[cur_num] += "1"
            elif mouse_column == 1:
                nums[cur_num] += "2"
            elif mouse_column == 2:
                nums[cur_num] += "3"
            elif mouse_column == 3:
                cur_num = 1
                opperation = 1
        elif mouse_row == 5:
            if mouse_column == 1:
                nums[cur_num] += "0"
            elif mouse_column == 3:
                if opperation == 1:
                    sol_num = int(nums[0]) + int(nums[1])
                elif opperation == 2:
                    sol_num = int(nums[0]) - int(nums[1])
                elif opperation == 3:
                    sol_num = int(nums[0]) * int(nums[1])
                elif opperation == 4:
                    sol_num = int(nums[0]) / int(nums[1])
                cur_num = 0
                nums[0] = str(sol_num)
                nums[1] = str("")
        mouse_was_pressed = True
    if not pygame.mouse.get_pressed()[0]:
        mouse_was_pressed = False
    #print(nums[cur_num])
    screen.fill((0, 0, 0)) 
    screen.blit(calculator, (0, 0))
    cur_num_disp.clear()
    for i in range(len(nums[cur_num])):
        #if len(nums[cur_num]) <= i:
            #break
        if nums[cur_num][i] == "0":
            cur_num_disp.append(zero)
        elif nums[cur_num][i] == "1":
            cur_num_disp.append(one)
        elif nums[cur_num][i] == "2":
            cur_num_disp.append(two)
        elif nums[cur_num][i] == "3":
            cur_num_disp.append(three)
        elif nums[cur_num][i] == "4":
            cur_num_disp.append(four)
        elif nums[cur_num][i] == "5":
            cur_num_disp.append(five)
        elif nums[cur_num][i] == "6":
            cur_num_disp.append(six)
        elif nums[cur_num][i] == "7":
            cur_num_disp.append(seven)
        elif nums[cur_num][i] == "8":
            cur_num_disp.append(eight)
        elif nums[cur_num][i] == "9":
            cur_num_disp.append(nine)
    for i in range(12):
        if len(cur_num_disp) <= i:
            break
        screen.blit(cur_num_disp[i], (-200 + i * 30, -135))

    pygame.display.flip()