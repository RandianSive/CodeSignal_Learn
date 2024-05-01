# Function to calculate total price for food order
def calculate_order_price(appetizers, main_course, desserts, tax_rate):
    price = appetizers + main_course + desserts
    tax = tax_rate * price # 7% tax
    total_price = price + tax
    return total_price

# Call the function for a specific order
order_price = calculate_order_price(15, 25, 10, 0.07)
print('The total price for your order is: $', order_price)