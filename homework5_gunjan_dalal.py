groceries = ["bread", "eggs", "milk", "apples", "oranges", "tomatoes"]
print (groceries)
groceries1 = groceries[0:2]
first2groceries = f"The first two items in the list are: {groceries1}"
print (first2groceries)
groceries2 = groceries[2:4]
middle2groceries = f"The middle two items in the list are: {groceries2}"
print (middle2groceries)
firstlastgroceries = f"The first and last items in the list are: {groceries[0]},{groceries[5]}"
print (firstlastgroceries)

Restaurantmenu = ("pizza", "french fries", "sandwich", "burger", "soup")
print ("Old menu:")
for menu in Restaurantmenu:
    print (menu)

Restaurantmenu = ("pizza", "french fries", "chicken", "salad", "soup")
print ("New menu:")
for menu in Restaurantmenu:
    print (menu)