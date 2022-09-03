n = 10
guests = 0
i = 1

while i <= n:
    print(f'Old value of guests = {guests}')
    print()
    guests += 1
    name = input("Enter Guest name: ")
    print(f"{name} you are guest number {guests}")
    if guests == 10:
        print(f"{name} you are the last guest")
    i += 1
    print()
    print(f'New value of guests = {guests}')
    print(f'New Value of i ={i}')
print(f"{guests}")



#i = 1
#while i <= 4:  # exp. == True
#    print("We want to see whats happening")
#    print(f'Old value of i = {i}')
#    # i = i + 1  # addition
#    i += 1
#    print(f'The new value of i = {i}')
#    print()

