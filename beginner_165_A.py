K = int(input())
A, B = map(int, input().split())

if A % K == 0 or B % K == 0:
    print("OK")
    exit()

if A // K < B // K:
    print("OK")
else:
    print("NG")
