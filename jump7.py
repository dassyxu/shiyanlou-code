range = range(1,100)
for i in range:
    if i % 7 ==0 or i // 10 ==7 or i % 10 == 7:
        continue
    else:
        print(i)
