num=list(range(1,31))

for i in num:
    if "3" in str(i) or "6" in str(i) or "9" in str(i):
        print("짝")
        continue
    print(i)