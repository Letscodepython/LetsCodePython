# var1 = 200
# var2 = 20
#
# if var2 > var1:
#     print("Start of Code Block if exp == True")
#     print("var2 is greater than var1")  # exp. is True
#     print("End of block")
# elif var2 == var1:
#     print("They are eql.")
# elif var2 != var1:
#     print("They are not eql.")
# else:
#     print("Start of Code Block if exp == False")
#     print("var1 is greater than var2")  # exp. is False
#     print("End of block")
#

NAME = "tumelo"
VIP_LIST = ["Kefilwe", "Mpho"]
first_name = input("Enter name: ")

if first_name.lower() == NAME:
    print(f'{NAME} you are not welcomed here.')
elif first_name != NAME:
    print(f'{first_name}, Welcome to the party')

    # Nested if statement
    if first_name.capitalize() in VIP_LIST:
        print(f'{first_name.capitalize()} head to the VIP section')
else:
    pass
