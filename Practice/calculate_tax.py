def calculate_tax(item, price, rate):
    return f"The tax of a/n {item} is ${float(price) * float(rate)}"

item = input("What item?\n> ")
price = input("How much does it cost in dollars?\n> ")

tax = calculate_tax(item, price, 0.06875)
print(tax)