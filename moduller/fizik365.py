'''
Bu modül MSGSU Fizik Bölümü
FIZ365 - Fizikte Bilgisayarlı Yöntemler 
dersinde kullanacak fonksiyonları içermektedir.
 
!=== GÜNCELLEME ===!
!=== 2023-11-17 ===!
'''
import numpy as np

# ===========================================
# Doğrusal Cebir Fonksiyonları
# ===========================================
# LU Yöntemi Kullanarak Matris Tersi Alma
def matris_tersi_al_LU(katsayiMat):
    '''
    LU ayrıştırma yöntemi ile katsayı matrisinin tersini hesaplar.
    '''
    # Katsayı matrisinin boyutu kontrol edilir
    n = int(len(katsayiMat))
    katsayiMatTers = np.zeros((n,n))

    # LU ayrıştırma
    for i in range(n):
        katsayiMatTers[:,i] = LU_ayrisma_cozucu(katsayiMat, np.identity(n)[i])
    return katsayiMatTers

# LU Ayrıştırma Yöntemi İle Denklem Çözme
# LU Ayrıştırma ile L, U elde etme
def LU_ayrisma(katsayiMat):
    '''
    LU ayrıştırma yöntemi ile katsayı matrisi ayrıştırılır.
    
    coeffMat: Katsayı matrisi
    '''
    # Katsayı matrisinin boyutu kontrol edilir
    n = int(len(katsayiMat))
    if n != len(katsayiMat[0]):
        print("Katsayı matrisinin boyutu uyumlu değil.")
        return None
    # Eğer katsayı matrisi int verilirse float'a çevrilmesi gerekir, çünkü
    # LU ayrıştırma yapılırken katsayı matrisi ondalık sayı olabilir.
    katsayiMat= katsayiMat.astype(float)
    # L ve U matrisleri oluşturulur.
    L = np.zeros((n,n))
    U = np.zeros((n,n))
    # LU ayrıştırma
    for k in range(0, n):
        L[k,k] = 1.0
        # U matrisi
        for j in range(k, n): 
            sum = 0.0
            for s in range(0, k):
                sum = sum + L[k,s]* U[s,j]
            U[k,j] = katsayiMat[k,j] - sum
        # L matrisi
        for i in range(k+1, n):
            sum = 0.0
            for s in range(0, k):
                sum = sum + L[i,s]* U[s,k]
            L[i,k] = (katsayiMat[i,k] - sum)/ U[k,k]
    return L, U
# LU Ayrıştırma Yöntemi Denklem Çözme
def LU_ayrisma_cozucu(katsayiMat, sonucVec):
    '''[Numerical Methods in Engineering with Python 3]
    LU ayrıştırma yöntemi ile denklem sistemini çözer.
    
    katsayiMat: Katsayı matrisi
    sonucVec: Sonuç vektörü
    '''
    # Katsayı matrisinin boyutu kontrol edilir
    n = int(len(katsayiMat))
    
    # LU ayrıştırma
    L, U= LU_ayrisma(katsayiMat)
    # Ax = b -> LUx = b -> Ly = b (Ux=y)
    # Önce Ly = b denklemi çözülür.
    
    # İleri yerine koyma fazı
    y = np.zeros(n)
    for k in range(0, n):
        y[k] = sonucVec[k]- np.dot(L[k,0:k], y[0:k])
    # Son olarak Ux = y denklemi çözülür.
    # Geri yerine koyma fazı
    cozumVek= np.zeros(n)
    for i in range(n-1, -1, -1):
        cozum= y[i]
        # Üst üçgensel formülde yerine koyma
        for j in range(i+1, n):
            cozum= cozum- U[i,j] * cozumVek[j]
        # Katsayı matrisinde doğrudan çözümü bulma
        cozumVek[i]= cozum/ U[i,i]
    return cozumVek

# Gauss Eleme Yontemi - Ust ucgen forma getirerek - Geri Yerine koyma Iceren
def gauss_eleme_ust_ucgen(katsayiMat, sonucVec):
    '''[Numerical Methods in Engineering with Python 3]
    Gauss eleme yöntemi ile dogrusal denklem sisteminin çözümü bulur.
    
    coeffMat: Katsayı matrisi
    resultVec: Sonuç vektörü
    '''
    # Boyut
    n= len(sonucVec)
    if n != len(katsayiMat):
        print("Katsayı matrisi ve sonuç vektörünün boyutları uyumlu değil.")
        return None
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

# ===========================================
# Python Alıştırma Fonksiyonları
# ===========================================
# Faktöriyel Alma
def faktoriyel(sayi):
    if not isinstance(sayi, int):
        return False
    sonuc = 1
    for i in range(1, sayi + 1):
        sonuc *= i
    return sonuc

# 1'den n'e kadar olan sayıların toplamı
def topla(sayi):
    if not isinstance(sayi, int):
        return False
    sonuc = 0
    for i in range(1, sayi + 1):
        sonuc += i
    return sonuc

# En büyük ortak bölen
def obeb(sayi1, sayi2):
    if not isinstance(sayi1, int) or not isinstance(sayi2, int):
        return False
    buyukSayi= min(sayi1, sayi2)
    sonuc = 1
    for it in range(1, buyukSayi + 1):
        if sayi1 % it == 0 and sayi2 % it == 0:
            sonuc = it
    return sonuc

# En büyük ortak kat
def okek(sayi1, sayi2):
    if not isinstance(sayi1, int) or not isinstance(sayi2, int):
        return False
    return (sayi1/ obeb(sayi1, sayi2)) * (sayi2)

# Verilen sayilardan dik üçgen oluşturulabilir mi?
def dik_mi(sayi1, sayi2, sayi3):
    if not isinstance(sayi1, int) or not isinstance(sayi2, int) or not isinstance(sayi3, int):
        return False
    sirali_array= np.sort([sayi1, sayi2, sayi3])
    if sirali_array[0] ** 2 + sirali_array[1] ** 2 == sirali_array[2] ** 2:
        return True
    return False

# Matrislerin çarpımı
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

# Dalga fonkiyonunun normalizasyonu
def normalize_et_dalgaFonk(arr1):
    if np.ndim(arr1) != 1:
        print("Bu fonksiyon sadece arrayler için çalışmaktadır.")
        return None
    sonuc= 0
    for it in arr1:
        sonuc += np.conj(it)* it
    normalizasyonKatsayisi= 1/np.sqrt(sonuc)
    return arr1* normalizasyonKatsayisi
