#var1 = 1
#var2 = 200
#if var2 > var1:
#    print("var2 is greater than var1")
#
#var1 = 1000
#var2 = 200
#if var2 > var1:
#    print("var2 is smaller than var1")


#var1 = 1000
#var2 = 200
#if var2 > var1:
#    print("var2 is greater than var1")
#else:
#    print("var2 is smaller than var1")
#
#var1 = 1000
#var2 = 200
#if var2 > var1:
#    print("var2 is greater than var1")
#else:
#    print("var1 is greater than var2")

age = int(input("Enter age: "))
# age = int(age)

#if age > 11 and age < 35 :  # 11 < age < 35
#    print("You get a 15% discount")
#elif age < 11:
##    print("You are still young to be a teen")
#else:
#    print("You don't get discount")

if age >= 35:
    print("You get a 15% discount")
    if age < 11:
        print("You are still young to be a teen")
else:
    print("You don't get discount")
