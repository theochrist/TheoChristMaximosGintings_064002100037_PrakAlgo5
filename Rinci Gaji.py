print("<<< Program Gaji Harian Pekerja >>>")
jamKerja = 8
GajiHarian = 175000

waktuMasuk = input("\nJam Masuk Kerja (JJ MM) : ")
waktu1 = waktuMasuk.split(" ")
jj = int(waktu1[0])
mm = int(waktu1[1])

waktuKeluar = input("\nJam Keluar Kerja (JJ MM) : ")
waktu2 = waktuKeluar.split(" ")
HH = int(waktu2[0])
LL = int(waktu2[1])

Lembur = (HH - jj) - jamKerja
TotalGaji = (Lembur * 15000) + GajiHarian

if Lembur >= 0 :
    print("\n---Rincian Gaji---")
    print("Waktu Bekerja \t: ",waktu1[0],waktu1[1],"sd",waktu2[0],waktu2[1])
    print("Gaji Perhari \t: Rp.", GajiHarian)
    print("Lembur \t\t: Rp.", Lembur * 15000, "(",Lembur,"jam x @Rp 15.000 )")
    print("Total Gaji \t: Rp.",TotalGaji)
else :
    print("Inputan Yang Anda Masukkan Salah")