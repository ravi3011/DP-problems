
def maxDivide(a,b):
    while(a%b == 0):
        a = a/b
    return a    

def isUgly(no):
    no = maxDivide(no,2)
    no = maxDivide(no,3)
    no = maxDivide(no,5)
    return 1 if no == 1 else 0

def getNthUgly(n):
    i = 1
    count = 1
    while(n > count):
        i +=1
        if(isUgly(i)):
            count +=1
    return i        

# print("Ugly numbet is :",getNthUgly(150))

def checkUgly(num):
    arr = [0] * num
    arr[0] = 1
    i2 = i3 = i5 = 0
    num2 = 2
    num3 = 3
    num5 = 5
    for i in range(1,num):
        arr[i] = min(num2,num3,num5)

        if(arr[i] == num2):
            i2 +=1
            num2 = arr[i2] *2
        if(arr[i] == num3):
            i3 +=1
            num3 = arr[i3] * 3
        if(arr[i] == num5):
            i5 +=1
            num5 = arr[i5] * 5        
    return arr[-1]
if __name__ == '__main__':
    print(checkUgly(150))