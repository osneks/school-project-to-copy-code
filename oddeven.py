for c in range(10000):
    num = str(input("odd or even to get a table : "))
    z = int(input("how many number you want in your table : "))
    if len(num) == 3 :
        for x in range(1,z*2,2):
            print(x)
    elif len(num) == 4 :
        for x in range(0,z+1,2):
            print(x)
    else: 
        print("pls check you are right ")
    print("your table is done")
