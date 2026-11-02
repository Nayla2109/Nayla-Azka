# Exercise 8-14: Cars
def makeCar(manufacturer, model, **carInfo):
    """Menyimpan informasi tentang mobil dalam sebuah dictionary"""
    carInfo['manufacturer'] = manufacturer
    carInfo['model'] = model
    return carInfo

car = makeCar('subaru', 'outback', color='blue', towPackage=True)

print(car)