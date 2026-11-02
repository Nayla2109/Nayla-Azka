# Exercise 4-8: Cubes
# Membuat daftar kubik dari 1 sampai 10
cubes = []

for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)  

# Menampilkan kubik dari 1 sampai 10
for cube in cubes:
    print(cube)