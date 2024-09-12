dictionary={}
def check():

    if passs == 120:
        dictionary[UOWnumber]=("Progress"+str(inputs))
    if passs == 100 :
        dictionary[UOWnumber]=("Progress (moduler trailer)"+str(inputs))
    if passs == 80 or passs == 60 or (passs == 40 and defer != 0) or ((passs == 20 or passs == 0) and fail < 80):
        dictionary[UOWnumber]=("Do not Progress - moduler retriever"+str(inputs))
    if fail >= 80:
        dictionary[UOWnumber]=("Exclude"+str(inputs))
        





should=True
while (should):
    try:
        UOWnumber=input("\nEnter the UOW number :")
        if UOWnumber[0]!="w":
            print("Your input not valied")
            continue
        if len(UOWnumber)!=8:
            print("Invalid input try again")
            continue   
        passs=int(input("Enter the pass credits :"))
        if passs%20!=0 or passs>120:
            print("Invalied answer")
            continue
        defer=int(input("Enter the defer credit :"))
        if defer%20!=0 or defer>120:
            print("Invalied answer")
            continue
        fail=int(input("Enter the defer credit :"))
        if fail%20!=0 or fail>120:
            print("Invalied answer")
            continue
    except ValueError:
        print("\nINT required")
    inputs=passs,defer,fail
    check()
    answer=str(input("\nDo you want add another set of data (Y/N)"))
    if answer=="y" or answer=="Y":
        continue
    if answer=="N" or answer=="n":
        print(check)
        break
