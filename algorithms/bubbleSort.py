import time
from colors import *

def bubble_sort(data, drawData, timeTick):
    
    sorted = 1
    size = len(data)
    for i in range(size-1):
        for j in range(size-i-1):
            drawData(data, [YELLOW if x == j or x == j+1 
                            else BLUE if x+sorted > size
                            else RED for x in range(len(data))] )
            time.sleep(timeTick)
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, [PURPLE if x == j or x == j+1 
                                else BLUE if x+sorted > size
                                else RED for x in range(len(data))] )
                time.sleep(timeTick)
        sorted+=1
        #drawData(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))] )       
    drawData(data, [BLUE for x in range(len(data))])
    

def bubble_pass(data, drawData, passS):
    sorted = 1
    p=1
    size = len(data)
    for i in range(size-1):
        for j in range(size-i-1):
            drawData(data, [YELLOW if x == j or x == j+1 
                            else BLUE if x+sorted > size
                                    else RED for x in range(len(data))] )
            if p == passS:
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    drawData(data, [PURPLE if x == j or x == j+1 
                                else BLUE if x+sorted > size
                                        else RED for x in range(len(data))] )
                return
            p+=1
        sorted+=1
        #drawData(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))] )       
    drawData(data, [BLUE for x in range(len(data))]) 
  