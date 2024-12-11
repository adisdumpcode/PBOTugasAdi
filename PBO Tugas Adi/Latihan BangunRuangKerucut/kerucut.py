sisi = int(input("masukkan sisi-sisi Prisma: "))
alas = int(input("masukkan nilai Alas: "))
tinggi = int(input("masukkan nilai tinggi Prisma: "))

def volume_prisma(alas, tinggi):
    return (0.5 * alas * tinggi) * tinggi

def keliling_alas(sisi):
    return (sisi + sisi + sisi)


print ("volume prisma:",volume_prisma(alas, tinggi))
print ("keliling alas:",keliling_alas(sisi))