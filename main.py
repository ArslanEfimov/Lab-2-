import csv


def esc(code):
    return f'\u001b[{code}m'


red = esc(41)
green = esc(42)
end = esc(0)
white = esc(47)
black = esc(40)
print("Флаг Бангладеша")
for i in range(6):
    if i <= 1:
        print(f'{green}{" " * 24}{end}')
    if 1 < i <= 3:
        print(f'{green}{" " * (8 - i + 1)}{red}{" " * (i + 2)}{red}{" " * (i + 2)}{green}{" " * (10 - (i - 1))}{end}')
    if 3 < i <= 4:
        print(f'{green}{" " * (3 + i)}{red}{" " * (i + 4)}{green}{" " * 9}{end}')
    if i > 4:
        print(f'{green}{" " * 24}{end}')


def uzor_b(count_slov):
    for i in range(6):
        if i <= 0.5:
            print(f'{black}{" " * 14}{white}{" " * 5}{end}' * int(count_slov))
        if 0.5 < i <= 1.5:
            print(f'{black}{" " * 3}{white}{" " * 8}{black}{" " * 3}{white}{" " * 5}{end}' * int(count_slov))
        if 1.5 < i <= 2.5:
            print(f'{black}{" " * 3}{white}{" " * 3}{black}{" " * 8}{white}{" " * 5}{end}' * int(count_slov))
        if 2.5 < i <= 3.5:
            print(f'{black}{" " * 3}{white}{" " * 3}{black}{" " * 3}{white}{" " * 10}{end}' * int(count_slov))
        if 3.5 < i <= 4.5:
            print(f'{black}{" " * 3}{white}{" " * 3}{black}{" " * 13}{end}' * int(count_slov))


print()
print()
print()

print("Узоры под буквой b:")


def uzor_sh(time):
    if not time.isdigit():
        start()
    elif time.isdigit:
        uzor_b(time)


def start():
    count_slov = input("Введите кол-во" + "\n")
    uzor_sh(count_slov)


start()

print()
print()
print()


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
print()
print()
with open("venv/books.csv", "r", encoding="cp1251") as csvfile:
    table = csv.reader(csvfile, delimiter=";")
    row_count = 0
    row_countbef2015 = 0
    row_countaf2015 = 0
    data = []
    for row in table:
        row_count += 1
        data.append(list(row[6].split("-")))

    for i in range(1, row_count):
        if int(data[i][0]) < 2015:
            row_countbef2015 += 1
        if int(data[i][0]) >= 2015:
            row_countaf2015 += 1
    procent_rowbef2015 = (row_countbef2015 / row_count) * 100
    procent_rowaf2015 = (row_countaf2015 / row_count) * 100
    array_plot1 = [[0 for col in range(10)] for row in range(10)]


    def array_init1(array_in):
        for i in range(10):
            for j in range(10):
                if j == 0 and i == 6:
                    array_in[i][j] = str(round(procent_rowbef2015)) + "%"
                if j == 0 and i == 1:
                    array_in[i][j] = str(round(procent_rowaf2015)) + "%"
                if array_in[i][0] == 0:
                    array_in[i][0] = "   "
                if i == 0 and j == 0:
                    array_in[i][j] = "100%"

        return array_in


    def array_fill(array_fi):
        for i in range(9):
            for j in range(10):
                if i >= 6:
                    array_fi[i][2] = 1
                if i >= 1:
                    array_fi[i][5] = 1


    def draw_plot1(array_pl):
        for i in range(9):
            line = " "
            for j in range(10):
                if j == 0:
                    line += white + str(array_pl[i][j])
                if array_pl[i][j] == 0:
                    line += "  "
                if array_pl[i][j] == 1 and j == 2:
                    line += red + "  " + white
                if array_pl[i][j] == 1 and j == 5:
                    line += green + "   " + white
            line += end
            print(line)
        print("   ", "<2015", ">=2015")


    print("Диаграмма")
    array_init1(array_plot1)
    array_fill(array_plot1)
    draw_plot1(array_plot1)
