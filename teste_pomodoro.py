import time 

class Pomodoro:
    def __init__(self):
        self.t =t

    def countdown(t): 
        
        while t:
            mins, secs = divmod(t, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(timer, end="\r") 
            time.sleep(1) 
            t -= 1
        
    print('Fire in the hole!!')
  

tm = int(input('Enter the time in minutes: '))
t = tm * 60

