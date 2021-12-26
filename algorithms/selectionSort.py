import time
from colors import *

def selection_sort(data, drawData, timeTick):
    for i in range(len(data)-1):
        minimum = i
        for k in range(i+1, len(data)):
            drawData(data, [BLUE if x<i else
                        YELLOW if x == i else
                        PURPLE if x == minimum else 
                        GREEN if x<=k else
                        RED for x in range(len(data))])
            time.sleep(timeTick)
            if data[k] < data[minimum]:
                minimum = k

        data[minimum], data[i] = data[i], data[minimum]
        drawData(data, [BLUE if x<i else
                        YELLOW if x == i else 
                        GREEN if x<minimum else
                        PURPLE if x == minimum else
                        RED for x in range(len(data))])
        
        time.sleep(timeTick)
        
    drawData(data, [BLUE for x in range(len(data))])
    