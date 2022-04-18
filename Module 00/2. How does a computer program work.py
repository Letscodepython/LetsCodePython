speed = 0
distance = int(input("Enter distance travelled: "))
time = int(input("Enter Time it took: "))

speed = distance / time
distance = speed * time
time = distance / speed
print()
print(f'Speed is {int(speed)}KM/H')
print(f'Distance is {int(distance)}KM\'s')
print(f'Time is {int(time)}H\'s')
