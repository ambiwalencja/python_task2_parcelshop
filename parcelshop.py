
#global variables
number_of_parcels = 0
total_weight = 0

# variables for while
parcel_weight = 0
item_weight = 1 # initial value is 1 so we can enter the loop
condition1 = item_weight >= 1
condition2 = item_weight <= 10
# welcome message
print("""Welcome to parcel loading service. 
Please type the weight of each item you want to send respectively.
Remember: the weight of one item must be between 1 and 10 kg!")
When you are finished entering your items, type "0" as you have 0 more kilograms to send :)""")

#entering data
while item_weight != 0: # until the user types 0 we repeat adding items
    item_weight = int(input("Type the weight of the item:"))
    if item_weight >= 1 and item_weight <= 10:  # if the item has the right weight (when i used conditions, it did not work)
        if parcel_weight + item_weight <= 20:  # if the item fits
            parcel_weight += item_weight  # we add the item to the parcel
        else:
            number_of_parcels += 1  # we send the parcel
            total_weight += parcel_weight  # we add the weight of current parcel
            parcel_weight = item_weight # last item goes to new parcel
    else:
        print("ERROR - ")  # if the item is not the right weight
        break
total_weight += parcel_weight  # we add the weight of the last parcel
if total_weight > 0:
    number_of_parcels += 1  # we send the last parcel
    print(f'We finished completing your order.\n'
      f'The total weight of sent items is {total_weight} kg.\n'
      f'The number of parcels sent is {number_of_parcels}.\n'
      f'The sum of empty space left is {number_of_parcels * 20 - total_weight} kg.\n' #thanks for the hint xD
      f'Bye!')

