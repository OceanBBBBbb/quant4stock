import time

def doEmail():
    print("I will email you later")


if __name__=="__main__":
    print('do main')
    while 1:
        print("do doEmail")
        doEmail()
        time.sleep(1)