def calculate_average(age_range):
    if age_range == '90+':
        return 90
    else:
        try:
            start, end = age_range.split('-')
            start = float(start)
            end = float(end)
            return (start + end) / 2
        except ValueError:
            # Eğer split işlemi başarılı olmazsa, örneğin '90+' gibi tek değer varsa
            return None

import pandas as pd
multeci = pd.read_html("https://multeciler.org.tr/turkiyedeki-suriyeli-sayisi/", header=0)
df = pd.DataFrame(multeci[0])

# Yaş ortalamasını hesaplamak için
df['YAŞ ORTALAMA'] = df['YAŞ ARALIĞI'].apply(calculate_average)

# KADIN ve ERKEK sütunlarındaki sayılarda noktalardan temizleme yapıyoruz
df['KADIN'] = df['KADIN'].str.replace('.', '', regex=False).astype(float)
df['ERKEK'] = df['ERKEK'].str.replace('.', '', regex=False).astype(float)
df['TOPLAM'] = df['TOPLAM'].str.replace('.', '', regex=False).astype(float)

# Çocuk sayıları
kizCocuk = df['KADIN'].iloc[0:4].sum()  # 0-4 yaş arası
erkekCocuk = df['ERKEK'].iloc[0:4].sum()  # 0-4 yaş arası
toplamCocuk = df['TOPLAM'].iloc[0:4].sum()  # 0-4 yaş arası

# Toplam Suriyeli sayısını hesaplıyoruz
toplamKadin = df['KADIN'].iloc[:-1].sum()
toplamErkek = df['ERKEK'].iloc[:-1].sum()
toplamSuriyeli = df['TOPLAM'].iloc[:-1].sum()

print(toplamCocuk, toplamKadin)

# Genç Suriyeli sayısı
gencSuriyeli = df['TOPLAM'].iloc[3:5].sum()  # 3-4 yaş arası

# Yaş çarpı sayı hesaplama
yaşÇarpiSayi = 0
for i in range(0, 18):
    yaşÇarpiSayi += df['TOPLAM'][i] * df['YAŞ ORTALAMA'][i]

yasOrtalamasi = yaşÇarpiSayi / toplamSuriyeli

# Çıktıları yazdırıyoruz
print(df)
print("TOPLAM SURİYELİ SAYISI: ", toplamSuriyeli)
print("0-18 YAŞ ARALIĞINDAKİ TOPLAM SURİYELİ İNSAN SAYISI: ", toplamCocuk)
print("SURİYELİLERİN YAŞ ORTALAMASI: ", round(yasOrtalamasi, 1))
print("SURİYELİ KADINLARIN ORANI: ", round(toplamKadin / toplamSuriyeli * 100 , 1))
print("SURİYELİ KADIN VE COCUKLARIN ORANI: ", round((toplamCocuk + toplamKadin - kizCocuk) / toplamSuriyeli * 100, 1))
print("GENC SURİYELİLERİN SAYİSİ:" ,round(gencSuriyeli / toplamSuriyeli * 100, 1))


df2 = pd.DataFrame(multeci[1])

print(df2)
df2['Suriyeli Sayısı'] = df2['Suriyeli Sayısı'].astype(str)
df2['Suriyeli Sayısı'] = round(df2['Suriyeli Sayısı'].str.replace('.', '', regex=False).astype(float), 1)


print("EN AZ SURİYELİ BULUNAN 1. ŞEHİR: " , df2["Şehir"][80] , ":" , df2["Suriyeli Sayısı"][80])
print("EN AZ SURİYELİ BULUNAN 2. ŞEHİR: " , df2["Şehir"][79] , ":" , df2["Suriyeli Sayısı"][79])
print("EN AZ SURİYELİ BULUNAN 3. ŞEHİR: " , df2["Şehir"][78] , ":" , df2["Suriyeli Sayısı"][78])
print("EN ÇOK SURİYELİ BULUNAN 1. ŞEHİR: " , df2["Şehir"][0] , ":" , df2["Suriyeli Sayısı"][0])
print("EN ÇOK SURİYELİ BULUNAN 2. ŞEHİR: " , df2["Şehir"][1] , ":" , df2["Suriyeli Sayısı"][1])
print("EN ÇOK SURİYELİ BULUNAN 3. ŞEHİR: " , df2["Şehir"][1] , ":" , df2["Suriyeli Sayısı"][2])

print("en az şehirdeki suriyeli sayısının tüm suriyelilere oranı: " ,round(df2["Suriyeli Sayısı"][80] / float(toplamSuriyeli)* 100,5))

