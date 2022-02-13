how_many_p = int(input('Enter how many pockman do you wnat to catch?  '))
powers = []
i = 0
while i < how_many_p:
    pockman_p = int(input('Enter a pockman '))
    powers.append(pockman_p)
    i = i+1
min_p = min(powers)
max_P = max(powers)

if len(powers) == 1:
    print(powers[0], powers[0])
elif len(powers) == 2:
    print(min(powers),min(powers))
    print(min(powers), max(powers))
else:
    main_l = []
    x = 1
    count2 = len(powers)
    count = 3
    print(min_p, min_p)
    while True:
        if min_p == 0 and max_P == 0:
            if count2!= 1:
                print(min_p, max_P)
                count2 = count2 -1
            else:
                break
        elif count != len(powers):
            if max_P-x in powers:
                count+=1
                print(min_p, max_P-x )
            x = x+1
        else:
            count = 'elif'
            break
    if count == 'elif':
        print(min_p, max_P)
        print(min_p, max_P)


