import os
from time import sleep

clear = lambda: os.system("cls")


def esc(code):
    return f'\u001b[{code}m'


red = esc(41)
green = esc(42)
end = esc(0)
white = esc(47)
black = esc(40)


class fg:
    green = "\u001b[32m"
    white = "\u001b[37m"


class bg:
    red = "\u001b[41m"
    white = "\u001b[47m"
    end = "\u001b[0m"


print(bg.white + fg.green + "l" + bg.end)
print(bg.red + " " * 2 + fg.white + "14%" + bg.end)
sleep(2)
clear()
print(bg.white + fg.green + "lO" + bg.end)
print(bg.red + " " * 4 + fg.white + "28%" + bg.end)
sleep(2)
clear()
print(bg.white + fg.green + "lOA" + bg.end)
print(bg.red + " " * 6 + fg.white + "42%" + bg.end)
sleep(2)
clear()
print(bg.white + fg.green + "lOAD" + bg.end)
print(bg.red + " " * 8 + fg.white + "56%" + bg.end)
sleep(2)
clear()
print(bg.white + fg.green + "lOADI" + bg.end)
print(bg.red + " " * 10 + fg.white + "70%" + bg.end)
sleep(2)
clear()
print(bg.white + fg.green + "lOADIN" + bg.end)
print(bg.red + " " * 12 + fg.white + "84%" + bg.end)
sleep(2)
clear()
print(bg.white + fg.green + "lOADING" + bg.end)
print(bg.red + " " * 14 + fg.white + "100%" + bg.end)
sleep(2)
clear()


def array_init(array_in):
    for i in range(11):
        for j in range(10):
            if j == 0:
                array_in[i][j] = step * (9 - i) + 3
            if i == 10:
                array_in[i][j] = j
    return array_in


def array_fill(array_fi, st):
    for i in range(10):
        for j in range(10):
            if abs(array_fi[i][0] - result[9 - j]) < st:
                for k in range(9):
                    if 8 - k == j:
                        array_fi[i][k + 1] = 1
    return array_fi


def draw_plot(array_pl):
    for i in range(9):
        line = " "
        for j in range(10):
            if j == 0:
                line += white + str(array_pl[i][j]) + "\t"
            if array_pl[i][j] == 0:
                line += "   "
            if array_pl[i][j] == 1:
                line += red + "   " + white
                sleep(1)
        line += end
        print(line)
    print(f' {white}0.0\t1  2  3  4  5  6  7  8  9  {end}')


print("График функции 3x+2")
array_plot = [[0 for col in range(10)] for row in range(11)]
result = [0 for col in range(10)]
for i in range(10):
    result[i] = 2 * i + 3
step = round(abs(result[9] - result[0]) / 9, 1)
array_init(array_plot)
array_fill(array_plot, step)
draw_plot(array_plot)
clear()
