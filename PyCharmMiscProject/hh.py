try:
    number_of_items = int(input("How many items?"))
    total_price = 200 * number_of_items
    average_price = total_price / number_of_items
    print("average prive:",average_price)

except Exception:
    print("o items cannot be ordered:")
finally:
    print("always exceute")

print("next code block")0