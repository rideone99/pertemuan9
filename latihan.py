hewan =["harimau","singa","cheetah","serigala","sapi"]
print('\nhewan =["harimau","singa","cheetah","serigala","sapi"]\n')
print('akses list')
print('elemen ke 3 adalah', hewan[2])
del hewan[1:4]
print('setelah nilai elemen ke 2 sampai ke 4 diambil maka akan menjadi', hewan)
del hewan[1]
print('setelah elemen terakhir diambil maka akan mejadi', hewan)
print('\nubah list')
hewan =["harimau","singa","cheetah","serigala","sapi"]
hewan[3]=8
print('setelah nilai elemen ke 4 diubah maka akan menjadi', hewan)
hewan[3:]=9,5
print('setelah nilai elemen ke 4 dan terakhir diubah maka akan menjadi', hewan)
print('\ntambah list')
hewanA =["harimau","singa","cheetah","serigala","sapi"]
hewanB=[]
hewanB.extend(hewanA[:2])
print('setelah list pertama diambil 2 bagian dan dijadikan list kedua maka akan menjadi', hewanB)
hewanB.append("7")
print('setelah list B ditambahkan dengan nilai string akan menjadi', hewanB)
hewanB.extend(["4","6","9"])
print('pada list B ditambahkan 3 nilai akan menjadi',hewanB)
h =hewanB+hewanA
print('setelah list B dengan list A digabungkan maka akan menjadi', h)
