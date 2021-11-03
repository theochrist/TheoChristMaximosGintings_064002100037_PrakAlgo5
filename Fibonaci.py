print ("---DERET FIBONACCI---")

def fibonacci(jumlahBilangan, BilPertama, BilKedua):
    count = 0
    temp = 0
    while count <= jumlahBilangan:
        print(BilPertama)
        temp = BilPertama + BilKedua
        BilPertama = BilKedua
        BilKedua = temp
        count = count + 1

jumlahBilangan = int(input('Masukkan Jumlah Bilangan : '))
BilPertama = int(input('Masukkan Bilangan Pertama : '))
BilKedua = int(input('Masukkan Bilangan Kedua :'))

fibonacci(jumlahBilangan, BilPertama, BilKedua)