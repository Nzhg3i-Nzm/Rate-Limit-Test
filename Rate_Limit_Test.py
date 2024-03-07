#Tests a login page for rate limiting.
#The standard test for "lack of rate limiting" is 300 requests in under 1 minute.
import requests, threading, time, math


url=input("Type the full url that you want to test, including https:// and the path\nEx: https://example.com/login\n")
method=input("Select request method (GET/POST)\n").lower()

def createRequestObj(text):
    #username=USERNAME&password=PASSWORD&csrf=xxxxxxxxxx
    data=input(text)
    params=data.split("&")
    myobj={}
    i=0
    while (i<len(params)):
        a=params[i].split("=")
        myobj[a[0]]=a[1]
        i+=1
    return myobj

realLogin=createRequestObj("Enter the request data here\nEx: user=username&pass=password\n")

pw_param=input("Which parameter contains the password?\n")
fakeLogin=realLogin
fakeLogin[pw_param]="INVALIDPASSWORD123"

numReqs=int(input("How many requests do you want to make?\n"))
numReqs=math.floor(numReqs/3)

start=time.time()
end=0

exitFlag=0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        try_login(self.name, numReqs)


def correct_login(num):
    if num==3:
        if method=="get":
            x=requests.get(url, json=realLogin)
            print(x.text)
        else:
            x=requests.post(url, json=realLogin)
            print(x.text)
        end = time.time()
        print(str(numReqs*3)+" requests in "+str(math.floor(end-start))+" seconds\n")


def try_login(threadname, reqs):
    global stop
    stop=0
    i=reqs
    while i>0:
        if exitFlag:
            threadname.exit()
        if method=="get":
            x=requests.get(url, fakeLogin)
            i-=1
        else:
            x=requests.post(url, fakeLogin)
            i-=1
    print("Final response data for "+threadname+" :\n"+x.text)
    stop+=1
    print("Threads completed: ", stop)
    correct_login(stop)


thread1=myThread(1, "Thread-1", 1)
thread2=myThread(2, "Thread-2", 2)
thread3=myThread(3, "Thread-3", 3)

thread1.start()
thread2.start()
thread3.start()

print("All threads started\n")
