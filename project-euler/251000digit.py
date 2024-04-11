a = 1
i = 3
temp = 0
prev_a = 1
while True:

    temp = a
    a = a + prev_a
    prev_a = temp


    print(a, temp, i)
    if len(str(a)) == 1000:
        break
    
    i += 1