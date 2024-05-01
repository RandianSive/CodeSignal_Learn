def order_total(*args):
    return sum(args)

total_cost = order_total(10.5, 5.99, 2.75, 4)
print(f"The total cost of your food order is: ${total_cost:.2f}")