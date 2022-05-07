# 입력받은 숫자의 각 자리수를 더하여 일의자리가 될때까지 연산
def solve(n) :
    result = 0
    
    result = result + n%10    #result에 n의 1의 자리 할당
    n = n//10   #n에 n의 10의자리 할당
    
    if n + result < 10 :
        return result + n
    
    elif n + result >=10:
        return solve(result + n)
    
def main() :
    n = int(input())
    print(solve(n))
    
if __name__ == "__main__" :
    main()