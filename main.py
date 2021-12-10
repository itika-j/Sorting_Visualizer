from tkinter import *
from tkinter import ttk
import random
from colors import *

# Importing algorithms 
from algorithms.bubbleSort import *
from algorithms.selectionSort import selection_sort
from algorithms.insertionSort import insertion_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
from algorithms.heapSort import heap_sort
from algorithms.countingSort import counting_sort



# Main window 
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg = WHITE)


algorithm_name = StringVar()
speed_name = StringVar()
data_length = StringVar()
data_type = StringVar()
data_size = 0
passS = 0
data = []
algo_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort', 'Counting Sort']
speed_list = [20, 30, 40, 50, 100, 200, 300, 400, 500, 1000]
length_list = [5,10,20,30,40,50,60,70,80,90,100]
type_list = ['random', 'input']

# Drawing the numerical array as bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()


# Randomly generate array
def generate():
    global data
    global passS
    passS = 0
    data = []
    
    n = int(data_menu.get())
    for i in range(0, n):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawData(data, [BLUE for x in range(len(data))])


def set_speed():
    sp = int(speed_menu.get())
    return sp/100

def sort():
    global data
    global passS
    passS = 0
    timeTick = set_speed()
    
    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Heap Sort':
        heap_sort(data, drawData, timeTick)
    else:
        counting_sort(data, drawData, timeTick)
        
        
def nextPass():
    global data
    global passS
    
    passS+=1
    
    if algo_menu.get() == 'Bubble Sort':
        bubble_pass(data, drawData, passS)



### User interface ###
UI_frame = Frame(window, width= 900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

l3 = Label(UI_frame, text="Data Type: ", bg=WHITE)
l3.grid(row=2, column=0, padx=10, pady=5, sticky=W)
type_menu = ttk.Combobox(UI_frame, textvariable=data_type, values=type_list)
type_menu.grid(row=2, column=1, padx=5, pady=5)
type_menu.current(0)

l4 = Label(UI_frame, text="Data Length: ", bg=WHITE)
l4.grid(row=3, column=0, padx=10, pady=5, sticky=W)
data_menu = ttk.Combobox(UI_frame, textvariable=data_length, values=length_list)
data_menu.grid(row=3, column=1, padx=5, pady=5)
data_menu.current(0)


canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=4, column=2, padx=5, pady=5)

b1 = Button(UI_frame, text="Pass", command=nextPass, bg=LIGHT_GRAY)
b1.grid(row=4, column=1, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=4, column=0, padx=5, pady=5)


window.mainloop()