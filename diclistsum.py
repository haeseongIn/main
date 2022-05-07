test_num = int(input())
indic = {}
for i in range(test_num):
        a = list(map(int, input().split()))
        indic[i] = a
for i in range(test_num):
    print(indic[i][0] + indic[i][1])