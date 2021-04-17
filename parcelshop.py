import random

# global variables
number_of_parcels = 0
total_weight = 0
max_empty_space = 0

# variables for while
parcel_weight = 0
item_weight = 1  # initial value is 1 so we can enter the loop
counter = 0 # variable for iterating inside the while loop

# welcome message
print("""Welcome to our parcelshop! We will send all your items! 
Please type the weight of each item you want to send respectively.
Remember: the weight of one item must be between 1 and 10 kg!")
When you are finished entering your items, type "0" as you have 0 more kilograms to send :)""")

# entering data
# while item_weight:  # until the user types 0 we repeat adding items
while counter < 100:
    # item_weight = int(input("Type the weight of the item: "))
    item_weight = random.randint(1, 10)
    if item_weight != 0:  # we proceed if the current item is not zero
        condition1 = item_weight >= 1
        condition2 = item_weight <= 10
        if condition1 and condition2:  # if the item has the right weight
            if parcel_weight + item_weight <= 20:  # if the item fits
                parcel_weight += item_weight  # we add the item to the parcel
            else:
                number_of_parcels += 1  # we send the parcel
                total_weight += parcel_weight  # we add the weight of current parcel
                if 20 - parcel_weight > max_empty_space:  # if empty space in current parcel is bigger than previous
                    max_empty_space = 20 - parcel_weight
                parcel_weight = item_weight # last item goes to new parcel
        else:
            print("YOU ARE DOING IT WRONG (ERROR)")  # if the item is not the right weight
            break
    counter += 1
total_weight += parcel_weight  # we add the weight of the last parcel
if 20 - parcel_weight > max_empty_space:  # again: if empty space in last parcel is bigger than previous
    max_empty_space = 20 - parcel_weight
if total_weight > 0:
    number_of_parcels += 1  # we send the last parcel
    print(f'We finished completing your order.\n'
      f'The total weight of sent items is {total_weight} kg.\n'
      f'The number of parcels sent is {number_of_parcels}.\n'
      f'The sum of empty space left is {number_of_parcels * 20 - total_weight} kg.\n' # thanks for the hint xD
      f'Maximum empty space in a parcel is {max_empty_space}. \n' 
      f'Bye!')

