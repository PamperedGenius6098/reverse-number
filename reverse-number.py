ch='y'
while (ch=='y') or (ch=='Y'):
    n=input("Enter a number:")
    print(n[::-1])
    ch=input("Do you want more y/n:")
    while (ch!='y') or (ch!='Y'):
        if (ch=='n') or (ch=='N'):
            print("Goodbye")
            break
        else:
            while (ch!='y') or (ch!='Y') or (ch!='n') or (ch!='N'):
                print("Wrong input")
                break
            ch=input("Do you want more y/n:")
print("Thanks for testing")
