import time

def Fibonacci_sequence():
    num=int(input("需要几项？"))
    n1=0
    n2=1
    count=2
    if num<=0:
        print("请输入一个整数")
    elif num==1:
        print("斐波那契数列：")
        print(n1)
    elif num==2:
        print("斐波那契数列：")
        print(n1,',',n2)
    else:
        print("斐波那契数列:")
        print(n1,",",n2,end=",")
    while count<num:
        sum=n1+n2
        print(sum,end=",")
        n1=n2
        n2=sum
        count+=1
    print()
def Armstrong_number():
    num = int(input("请输入一个数字："))
    sum = 0
    n = len(str(num))
    temp = num 
    while temp>0:
        digit = temp%10
        sum += digit**n
        temp //=10
    if num==sum:
        print(num,"是阿姆斯特朗数")
    else:
        print(num,"不是阿姆斯特朗数")
def multiplication_table():
    for i in range(1,10):
        for j in range(1,i+1):
            print("%d*%d=%d\t"%(j,i,i*j),end="")
        print()    
def draw_table():
    words = input('The word you want say:')
    for item in words.split():
        print('\n'.join([''.join([(item[(x-y)% len(item)]if
             ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else '')
        for x in range(-30,30)]) for y in range(12,-12,-1)]))
        time.sleep(1.5);            


            
if __name__ == '__main__':
   
    draw_table()                
    


