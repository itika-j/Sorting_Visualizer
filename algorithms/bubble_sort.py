import time
from colors import *

def bubble_sort(data, drawData, timeTick):
    p = 0
    size = len(data)
    for i in range(size-1):
        for j in range(size-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))] )
                time.sleep(timeTick)
        p+=1       
    drawData(data, [YELLOW for x in range(len(data))])
    

def bubble_pass(data, drawData, passS):
    size = len(data)
    p=1
    for i in range(size-1):
        for j in range(size-i-1):
            if p==passS:
                drawData(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))] )
                if data[j] > data[j+1]:
                    
                    data[j], data[j+1] = data[j+1], data[j]
                    drawData(data, [BLACK if x == j or x == j+1 else PURPLE for x in range(len(data))] )
                return
            p+=1
        
                
    drawData(data, [DARK_BLUE if x>size-i-1 else PURPLE for x in range(len(data))] )  
  