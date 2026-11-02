# Exercise 7-9: No Pastrami
sandwichOrders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'roast beef', 'egg salad', 'pastrami', 'keju']
finishedSandwiches = []

print("Maaf, toko deli kami sedang kehabisan pastrami.\n")

# Menghapus semua kemunculan pastrami
while 'pastrami' in sandwichOrders:
    sandwichOrders.remove('pastrami')

while sandwichOrders:
    currentSandwich = sandwichOrders.pop(0)
    print(f"Saya telah membuat sandwich {currentSandwich} Anda.")
    finishedSandwiches.append(currentSandwich)

print("\nSemua sandwich yang telah dibuat:")
for finishedSandwich in finishedSandwiches:
    print(f"- {finishedSandwich}")