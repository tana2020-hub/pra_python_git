S = input()

for i in range(97, 123):
    if chr(i) not in S:
        print(chr(i))
        exit()
print('None')
