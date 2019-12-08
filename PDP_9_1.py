"""
NAMA        : DHEVAN MUHAMAD ANTHAREZA
NIM         : A11.2019.12293
KELOMPOK    : A11.4118
"""
import os,sys
matrikA = [
  [5, 4, 6, 5, 6],
  [7, 8, 9, 9, 9],
  [9, 8, 7, 8, 5],
  [8, 7, 4, 6, 7],
  [8, 7, 9, 9, 9]
]
matrikB = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 8],
  [7, 6, 5, 4, 3],
  [2, 1, 2, 3, 4],
  [5, 6, 7, 8, 7]
]
def soal1():
  print("1. Cetak Matriks")
  print("Matriks A :     Matriks B : ")
  for baris in range(0,5) :
    for kolom in range(0,5) :
      print(matrikA[baris][kolom], end= " ")
    print('     ', end=" ")
    for kolom in range(0,5) :
      print(matrikB[baris][kolom], end=" ")
    print("")
  print('\n')
def soal2():
  print("2. Penjumlahan Matriks")
  for baris in range(0,5) :
    for kolom in range(0,5) :
      print(matrikA[baris][kolom], end= " ")
    print('  +  ' if baris == 2 else '     ', end=" ")
    for kolom in range(0,5) :
      print(matrikB[baris][kolom], end=" ")
    print('  =  ' if baris == 2 else '     ', end=" ")
    for kolom in range(0,5) :
      val = matrikA[baris][kolom] + matrikB[baris][kolom]
      print(val, end="  " if len(str(val))==1 else " ")
    print("")
  print('\n')
def soal3():
  print("2. Pengurangan Matriks")
  for baris in range(0,5) :
    for kolom in range(0,5) :
      print(matrikA[baris][kolom], end= " ")
    print('  -  ' if baris == 2 else '     ', end=" ")
    for kolom in range(0,5) :
      print(matrikB[baris][kolom], end=" ")
    print('  =  ' if baris == 2 else '     ', end=" ")
    for kolom in range(0,5) :
      val = matrikA[baris][kolom] - matrikB[baris][kolom]
      print(val, end="  " if len(str(val))==1 else " ")
    print("")
  print('\n')
def soal4():
  print("2. Perkalian Matriks")
  for baris in range(0,5) :
    for kolom in range(0,5) :
      print(matrikA[baris][kolom], end= " ")
    print('  x  ' if baris == 2 else '     ', end=" ")
    for kolom in range(0,5) :
      print(matrikB[baris][kolom], end=" ")
    print('  =  ' if baris == 2 else '     ', end=" ")
    for kolom in range(0,5) :
      val = 0
      for i in range(0,5):
        val += matrikA[baris][i] * matrikB[i][kolom]
      print(val, end="  " if len(str(val))==1 else " ")
    print("")
  print('\n')
if __name__ == "__main__" :
  soal1()
  soal2()
  soal3()
  soal4()