# 숫자를 입력받습니다.
string_num = input()

# 숫자 한번씩 입력으로 변경
string_num=list(string_num)
change=[]
count=1
for i in string_num:
    if count%2==0:
        change.append(i)
    count=count+1
print(change)
# 2진수로 변환
final="".join(change)
final=int(final)
bin=format(final,'b')
print(bin)