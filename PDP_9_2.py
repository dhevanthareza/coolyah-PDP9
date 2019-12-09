"""
NAMA        : DHEVAN MUHAMAD ANTHAREZA
NIM         : A11.2019.12293
KELOMPOK    : A11.4118
"""
import PDP_9_1
matrikA = PDP_9_1.matrikA
matrikB = PDP_9_1.matrikB
matrik = [
  [2, 4, 7, 7, 1],
  [8, 9, 1, 8, 2],
  [5, 3, 6, 3, 1],
  [7, 8, 1, 0, 5],
  [2, 1, 3, 4, 9]
]
def soal1() :
  print('1. Apakah Matrik A sama dengan Matrik B ?')
  isSame = True
  if(len(matrikA) != len(matrikB)): isSame = False
  for baris in range(0,5):
    if(len(matrikA[baris]) != len(matrikB[baris]) or isSame == False):
      isSame = False
      break
    for kolom in range(0,5) :
      if(matrikA[baris][kolom] != matrikB[baris][kolom]):
        isSame = False
        break
  print('Matriks A sama dengan matriks B' if isSame else 'Matriks A tidak sama dengan matriks B \n')
def soal2() :
  sum = 0
  for baris in range(0, len(matrik)):
    sum += matrik[baris][baris]
  print('2. Jumlah Elemen yang Berwarana Merah adalah {} \n'.format(sum))
def soal3() :
  print('3. Menghitung Elemen ')
  words = ['pertama', 'kedua', 'ketiga', 'keempat', 'kelima']
  for baris in range(0, len(matrik)) :
    print('Jumlah baris {}\t= {}'.format(words[baris], sum(matrik[baris])))
  datas = [
    {'word' : 'pertama', 'value': 0},
    {'word' : 'kedua', 'value': 0},
    {'word' : 'ketiga', 'value': 0},
    {'word' : 'keempat', 'value': 0},
    {'word' : 'kelima', 'value': 0}
  ]
  for baris in range(0,5):
    for kolom in range(0,5):
      datas[kolom]['value'] += matrik[baris][kolom]
  for data in datas:
    print("Jumlah kolom {}\t= {}".format(data['word'], data['value']))
def soal4() :
  print('4. Input Data Beasiswa')
  datas = []
  needs = ['Nama\t\t', 'Nim\t\t', 'Semester\t', 'IPK\t\t']
  for i in range(0,10):
    value = []
    for need in needs:
      value.append(input("{}= ".format(need)))
    datas.append(value)
    if(input("Lanjutkan (Y/y) ? ") not in ['y', 'Y']): break
  showBy = int(input('1.Nama\n2.Nim\n3.IPK\nTampilkan Mahasiswa yang terdaftar berdasarkan? '))
  for data in datas:
    print(data[showBy-1 if showBy != 3 else 3])
    
if __name__ == "__main__":
  soal1()
  soal2()
  soal3()
  soal4()