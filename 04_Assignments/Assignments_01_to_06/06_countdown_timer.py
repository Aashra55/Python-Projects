import time

def main(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print("Time Over!")
    
t = input("Enter time in seconds: ")

if __name__ == "__main__":
    main(int(t))
    

