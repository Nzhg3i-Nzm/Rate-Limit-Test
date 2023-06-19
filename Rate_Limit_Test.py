import requests, threading, time, math


url=input("Type the full url that you want to test, including https:// and the page name\n")
username=input("Type the username or email that you want to use to login")
password=input("Type the passsword that you want to use to login")
myobj={"SignInForm-email": username, "SignInForm-password": "AnInvalidPassword123"}

exitFlag=0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        try_login(self.name)


def correct_login(num):
    if num==3:
        myobj={"SignInForm-email": username, "SignInForm-password": password}
        x=requests.post(url, json=myobj)
        print(x.text)


def try_login(threadname):
    global stop
    stop=0
    i=int(input("How many requests do you want to make?"))
    i=math.floor(i/3)
    myobj={"SignInForm-email": username, "SignInForm-password": "111111"}
    while i>0:
        if exitFlag:
            threadname.exit()
        x=requests.post(url, json=myobj)
        i-=1
    print(x.text)
    stop+=1
    print("Threads completed: ", stop)
    correct_login(stop)


thread1=myThread(1, "Thread-1", 1)
thread2=myThread(2, "Thread-2", 2)
thread3=myThread(3, "Thread-3", 3)

thread1.start()
thread2.start()
thread3.start()

print("All threads started")

