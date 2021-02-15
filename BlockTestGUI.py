import pyautogui as auto
import PySimpleGUI as sg
import pandas as pd
import time

# Supposed to get the number of pixels
x, y = auto.size()
print(x)
print(y)

# Create a dictionary of all possible row and column values to loop through all possible options

# Number of blocks in each row and column
MAX_ROWS = 2
MAX_COL = 2

# Number of pixels per block?
print(x/MAX_COL)
print(y/MAX_ROWS)

df = pd.DataFrame()

# Creates the usable space of the window
# Initializes settings
# Creates an instance of the window
board = [[1 for j in range(MAX_COL)] for i in range(MAX_ROWS)]
layout = [[sg.Button(size=(int(x/8/MAX_COL), int(y/17/MAX_ROWS)), button_color=('red', 'green'), key=(i,j)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
window = sg.Window(title="6q-Interface", size=(x, y), layout=layout)  # margins=(1200 ,1000)).read()

# print(window)
while True:
    # While the window is open, waits for input
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    else:
        # If a click even occurs, button changes from green to red, waits half a second, the changes back to green
        window[event].update(button_color=('green', 'red'))
        window = window.refresh()
        time.sleep(.5)
        window[event].update(button_color=('red', 'green'))
        window = window.refresh()

        # Records the how many rows and columns are in the window, the block the event ocurred in,
        # and has a place holder of 'None' for future image data
        df = df.append([[MAX_ROWS, MAX_COL, event, None]], ignore_index=True)

headers = ['Max Rows', 'Max Cols', 'Block', 'Image']
df.columns = headers

# Transforms dataframe to CSV
file = 'block_test_results.csv'
df.to_csv(file, na_rep='-', header=True, index=False)

print(df)
window.close()
