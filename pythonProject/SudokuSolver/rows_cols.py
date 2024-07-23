import pyautogui as pg
import numpy as np
import time

grid = []

# Input grid
while True:
    row = list(input('Row: '))
    ints = [int(n) for n in row]
    grid.append(ints)

    if len(grid) == 9:
        break

    # print('Row: ' + str(len(grid)) + ' complete')

time.sleep(3)

# Possible function
def possible(x, y, n):
    for i in range(9):
        if grid[i][x] == n and i != y:
            return False
    for i in range(9):
        if grid[y][i] == n and i != x:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for X in range(x0, x0 + 3):
        for Y in range(y0, y0 + 3):
            if grid[Y][X] == n:
                return False
    return True

# Print function for pyautogui

def Print(matrix):
    for i in range(9):
        for j in range(9):
            num = str(matrix[i][j])
            pg.press(num)
            if j < 8:
                pg.hotkey("right")
        if i < 8:
            pg.hotkey("down")
            for _ in range(8):
                pg.hotkey("left")
        time.sleep(0.01)  # Small delay for better simulation

# Solve function
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.array(grid))
    Print(grid)
    input('More?')

solve()
