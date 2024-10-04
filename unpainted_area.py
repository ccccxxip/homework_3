#ввод ширины, высоты холста и кол-ва прямоугольников
w, h = map(int, input().split())
n = int(input())

#создаем холст (двумерный список), помеченный нулями (незакрашенные области)
canvas = [[0] * w for _ in range(h)]

#читаем и обрабатываем каждый прямоугольник
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    #отмечаем ячейки холста, которые попадают в текущий прямоугольник
    for y in range(y1, y2):
        for x in range(x1, x2):
            canvas[y][x] = 1

#подсчитываем кол-во не закрашенных ячеек (нулей)
unpainted_area = 0
for row in canvas:
    unpainted_area += row.count(0)

print(unpainted_area)


