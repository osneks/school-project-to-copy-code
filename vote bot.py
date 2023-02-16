people = int(input("how many people are voting"))
for i in range(people):
    age = int(input("enter you age to vote : "))
    name = str(input("enter you name to veryfy your self : "))
    print("what party are you voting for , BJP Bharatiya Janata press 1 , CPI Communist Party of India press 2, CPM Communist Party of India press 3")
    party =  float(input(": "))
    listofpeople = ["none"]
    BJPBharatiyaJanata = 0
    CPICommunistPartyofIndia = 0
    CPMCommunistPartyofIndia = 0

    if age > 18 :
        listofpeople.append(name)
    else:
        print("you are under age to vote")
        print("try angin you are 18")
    if party == 1 :
        print(BJPBharatiyaJanata + 1)
        print("you voted for BJP Bharatiya Janata")
    elif party == 2 :
        print(CPICommunistPartyofIndia + 1)
        print("you voted for CPI Communist Party of India")
    else :
        if party == 3 :
                print(CPMCommunistPartyofIndia + 1)
                print("you voted for CPM Communist Party of India")
        else :
             print("pls check you are voting for a party")
if (BJPBharatiyaJanata > CPICommunistPartyofIndia):
    if (BJPBharatiyaJanata > CPMCommunistPartyofIndia):
        print ("BJP Bharatiya Janata won")
    else:
        print ("")
elif (CPICommunistPartyofIndia > CPMCommunistPartyofIndia):
    print ("CPI Communist Party of India won")
else:
    print ("CPM Communist Party of India won")
print("election is over now ")
print("people how voted given below ")
for d in listofpeople :
    print(d)


