latte_volume = 16
cappuccino_volume = 12
total_volume = 0

for i in range(3):
    total_volume += latte_volume

for i in range(2):
    total_volume += cappuccino_volume

print("Total coffee volume brewed today:", total_volume)