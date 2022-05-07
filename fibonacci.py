#입력한 숫자까지의 피보나치 수열을 출력

num=int(input())
i=1
num1=1
num2=0
fib=0

while True:
    print(fib)
    i=i+1
    fib=num1+num2
    num1=num2
    num2=fib
    if fib>=num:
        break