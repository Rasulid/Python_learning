import time


defult = 'hello world'
symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
result = ''
counter = 0

while counter < len(defult):
    for val in symbols:
        print(val , result)
        if val == defult[counter]:
            result += val
            counter += 1
            break
        time.sleep(.01)
print(result)
