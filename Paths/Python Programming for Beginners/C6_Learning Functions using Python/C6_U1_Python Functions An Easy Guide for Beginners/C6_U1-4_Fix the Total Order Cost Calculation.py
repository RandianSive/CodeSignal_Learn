# Define your function
def total_order_cost(food_cost, delivery_cost):
    total_cost = food_cost + delivery_cost
    return total_cost

# Call the function
complete_order_cost = total_order_cost(10.5, 5)
print("Your complete order cost is: $" + str(complete_order_cost))