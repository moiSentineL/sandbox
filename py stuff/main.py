from datetime import datetime
import time
import os
import sys


def main():
    # while True:
    #     start = datetime.now().strftime("%H:%M:%S"):
    second = 0    
    minute = 0    
    hours = 0    
    while True:    
        print('\t\t\t\t  %d : %d : %d '%(hours,minute,second))    
        time.sleep(1)    
        second+=1    
        if(second == 60):    
            second = 0    
            minute+=1    
        if(minute == 60):    
            minute = 0    
            hour+=1;    
        os.system('cls')

if __name__ == "__main__":
    main()
