# Exercise 7-8: Deli
sandwichOrders = ['tuna', 'turkey', 'roast beef', 'egg salad', 'keju']
finishedSandwiches = []

while sandwichOrders:
    currentSandwich = sandwichOrders.pop(0)
    print(f"Saya telah membuat sandwich {currentSandwich} Anda.")
    finishedSandwiches.append(currentSandwich)

print("\nDaftar sandwich yang sudah dibuat:")
for sandwich in finishedSandwiches:
    print(f"- Sandwich {sandwich}")