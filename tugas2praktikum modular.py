
import math

# Fungsi input nilai
def input_nilai():
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    return tugas, uts, uas

# Fungsi validasi nilai
def validasi_nilai(nilai):
    if 0 <= nilai <= 100:
        return True
    else:
        return False

# Fungsi hitung nilai akhir
def hitung_nilai(tugas, uts, uas):
    return (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

# Fungsi menentukan grade
def tentukan_grade(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"

# Fungsi tampilkan hasil
def tampilkan_hasil(nilai, grade):
    print("Nilai Akhir:", nilai)
    print("Grade:", grade)

# Program utama
tugas, uts, uas = input_nilai()

if validasi_nilai(tugas) and validasi_nilai(uts) and validasi_nilai(uas):
    nilai_akhir = hitung_nilai(tugas, uts, uas)
    grade = tentukan_grade(nilai_akhir)
    tampilkan_hasil(nilai_akhir, grade)
else:
    print("Input tidak valid! Nilai harus 0-100")