import numpy as np

# Gauss Eleme Yontemi - Ust ucgen forma getirerek - Geri Yerine koyma Iceren
def gauss_eleme_ust_ucgen(katsayiMat, sonucVec):
    # Boyut
    n= len(sonucVec)
    # Katsayı ve sonuç matrislerini float tipine çevir.
    katsayiMat= katsayiMat.astype(float)
    sonucVec= sonucVec.astype(float)
    # Üst üçgensel matris oluştur.
    for k in range(0, n-1): # k: pivot satırı
        for i in range(k+1, n): # i: pivot satırından sonraki satırlar
            #print(f"katsayiMat Once\n {katsayiMat}")
            if katsayiMat[i, k] != 0:
                lamb = katsayiMat[i, k]/ katsayiMat[k, k]
                #print(f"lamb: {lamb}")
                # Katsayı matrisini değiştir
                #print(f"i, k: {i}, {k}")
                #print(f"katsayiMat[i, k:n]: {katsayiMat[i, k:n]}")
                #print(f"lamb*katsayiMat[k, k:n]: {lamb*katsayiMat[k, k:n]}")
                #print(f"katsayiMat[i, k:n]- lamb* katsayiMat[k, k:n]: {katsayiMat[i, k:n]- lamb* katsayiMat[k, k:n]}")
                katsayiMat[i, :]= katsayiMat[i, :]- lamb* katsayiMat[k, :]
                # Sonuç vektörünü değiştir
                sonucVec[i]= sonucVec[i]- lamb* sonucVec[k]
            #print(f"katsayiMat Sonra\n {katsayiMat}")
    # Geri Yerine Koyma Yap
    cozumVek= np.zeros(n)
    # Son satırdan başlayarak geriye doğru ilerleme
    for i in range(n-1, -1, -1):
        cozum= sonucVec[i]
        # Üst üçgensel formülde yerine koyma
        for j in range(i+1, n):
            cozum= cozum- katsayiMat[i,j] * cozumVek[j]
        # Katsayı matrisinde doğrudan çözümü bulma
        cozumVek[i]= cozum/ katsayiMat[i,i]
    return cozumVek

def faktoriyel(sayi):
    if not isinstance(sayi, int):
        return False
    sonuc = 1
    for i in range(1, sayi + 1):
        sonuc *= i
    return sonuc
def topla(sayi):
    if not isinstance(sayi, int):
        return False
    sonuc = 0
    for i in range(1, sayi + 1):
        sonuc += i
    return sonuc
def obeb(sayi1, sayi2):
    if not isinstance(sayi1, int) or not isinstance(sayi2, int):
        return False
    buyukSayi= min(sayi1, sayi2)
    sonuc = 1
    for it in range(1, buyukSayi + 1):
        if sayi1 % it == 0 and sayi2 % it == 0:
            sonuc = it
    return sonuc
def okek(sayi1, sayi2):
    if not isinstance(sayi1, int) or not isinstance(sayi2, int):
        return False
    return (sayi1/ obeb(sayi1, sayi2)) * (sayi2)
def dik_mi(sayi1, sayi2, sayi3):
    if not isinstance(sayi1, int) or not isinstance(sayi2, int) or not isinstance(sayi3, int):
        return False
    sirali_array= np.sort([sayi1, sayi2, sayi3])
    if sirali_array[0] ** 2 + sirali_array[1] ** 2 == sirali_array[2] ** 2:
        return True
    return False
def mat_carp(mat1, mat2):
    boy1= np.shape(mat1)
    boy2= np.shape(mat2)
    if len(boy1) == 1:
        boy1= (1, boy1[0])
    if len(boy2) == 1:
        boy2= (1, boy2[0])
    if not isinstance(mat1, np.ndarray):
        return False
    if boy1[1] != boy2[0]:
        return False
    if np.array_equal(mat1, np.zeros(boy1)) or np.array_equal(mat2, np.zeros(boy2)):
        print("Bir matrisin tüm elemanları sıfırdır.")
        print(f"mat1:\n {mat1}")
        print(f"mat2:\n {mat2}")
        return np.zeros((boy1[1], boy2[0]))
    if np.array_equal(mat1, np.eye(boy1[0])):
        print("Bir matris birim matristir.")
        print(f"mat1:\n {mat1}")
        return mat2
    if np.array_equal(mat2, np.eye(boy2[0])):
        print("Bir matris birim matristir.")
        print(f"mat2:\n {mat2}")
        return mat1
    sonuc= np.zeros((boy1[0], boy2[1]))
    for it1 in range(boy1[0]):
        for it2 in range(boy2[1]):
            sonuc[it1,it2]= np.sum(mat1[it1,:] * mat2[:,it2])
    return sonuc
def normalize_et_dalgaFonk(arr1):
    if np.ndim(arr1) != 1:
        print("Bu fonksiyon sadece arrayler için çalışmaktadır.")
        return None
    sonuc= 0
    for it in arr1:
        sonuc += np.conj(it)* it
    normalizasyonKatsayisi= 1/np.sqrt(sonuc)
    return arr1* normalizasyonKatsayisi
