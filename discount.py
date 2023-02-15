x = float(input("price"))
if x < 500 or x == 500 :
    z = (7/100)*x
    w = x - z
    print(w)
else :
    s = int(input("discount"))
    z = (s/100)*x
    w = x - z
    print(w)
