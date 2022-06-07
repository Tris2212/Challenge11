import time

a = "frans"
b = "duits"


while True:
    temp = a
    a = b
    b = temp
    print(temp)
    time.sleep(1)