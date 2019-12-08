"""
NAMA        : DHEVAN MUHAMAD ANTHAREZA
NIM         : A11.2019.12293
KELOMPOK    : A11.4118
"""
import os, sys
numbers = [i for i in range(1,101)]
def soal1():
  print("1. Mencetak angka 1-100")
  for i in numbers:
    print(i, end=" ")
  print("\n")
def soal2():
  print("2. Mencetak angka ganjil diantara 1-100")
  for i in numbers:
    if(i % 2 != 0): print(i, end=" ")
  print("\n")
def soal3():
  print("3. Mencetak angka yang hanya dapat dibagi 3 atau 5 diantara 1-100")
  for i in numbers:
    if(i%3 == 0 or i%5 == 0): print(i, end=" ")
  print("\n")
def soal4():
  print("4. Membuat list 2 dimensi yang mencetak baris angka dari angka 1 sampai 5 lalu melakukan kuadrat terhadap nilai list tersebut ")
  matrik = [[x for x in range(1,6)] for x in range(0, 5)]
  for baris in range(0,5) :
    for kolom in range(0,5) :
      print(matrik[baris][kolom], end= " ")
    print('     ', end=" ")
    for kolom in range(0,5) :
      print(matrik[baris][kolom] ** 2, end=" ")
    print("")
  print('\n')
if __name__ == "__main__":
  soal1()
  soal2()
  soal3()
  soal4()