def calculate_tax(item, price, rate):
    print(f"The tax of a {item} is ${float(price) * float(rate)}")

item = input("What item?\n> ")
price = input("How much does it cost in dollars?\n> ")

calculate_tax(item, price, 0.06875)