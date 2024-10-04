# Входные данные
n, m = map(int, input().split())
ad_banner = [input().strip() for _ in range(n)]
screen = [tuple(map(int, input().split())) for _ in range(n)]

# Соответствие цветов цифрам на табло (в виде кортежей)
color_map = {
    'R': (4, 5, 6, 7),
    'G': (2, 3, 6, 7),
    'B': (1, 3, 5, 7),
    '.': (0, 1, 2, 3, 4, 5, 6, 7)
}

# Проверка
for i in range(n):
    for j in range(m):
        if screen[i][j] not in color_map[ad_banner[i][j]]:
            print("NO")
            exit()

print("YES")