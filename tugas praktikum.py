B={}
while True :
    E=input('apakah ingin menambahkan data? y/t : ')
    if E=="y" :
        print()
        print("tambah data mahasiswa")
        print('\n')
        Nama=input("masukan nama : ")
        NIM=input("masukan NIM : ")
        Nilaitugas=int(input("masukan nilai tugas : "))
        NilaiUTS=int(input("masukan nilai UTS : "))
        NilaiUAS=int(input("masukan nilai UAS : "))
        Nilaiakhir=(0.30*Nilaitugas)+(0.35*NilaiUTS)+(0.35*NilaiUAS)
        B[Nama]=NIM,Nilaitugas,NilaiUAS,NilaiUTS,Nilaiakhir
        print('data berhasil ditambahkan')
    elif E=="t" :
        if B.items():                                                                     
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            i = 0
            for x in B.items():
                i += 1
                print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))  
            print("==================================================================")
        else:
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            print("|                          TIDAK ADA DATA!                       |")
            print("==================================================================")
    else:
        break            