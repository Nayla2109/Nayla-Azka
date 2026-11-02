# Exercise 8-12: Sandwiches
def makeSandwich(*items):
    """Merangkum pesanan sandwich dengan berbagai topping"""
    print("\nMembuat sandwich dengan bahan-bahan berikut:")
    for item in items:
        print(f"- {item}")

makeSandwich('keju', 'tomat', 'selada')
makeSandwich('daging sapi', 'telur')
makeSandwich('ayam crispy', 'keju ekstra', 'saus sambal', 'tomat')