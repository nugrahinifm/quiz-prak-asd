###Nugrahini Fatma Manuhara
###L200200232

#no 1
import re
pola_uname = r'@+[a-zA-Z]+[0-9]+[_]+'
masukan = input('Masukkan Username: ')

if re.findall(pola_uname, masukan):
    print('PASS!!')
else:
    print('FAILED!!')
    
#####no2
import re
pola_email = '[a-zA-Z0-9]+[@]+[a-zA-Z0-9]+[.]+[a-zA-Z0-9]+'
masukan = input('Cari alamat email di dalam teks berikut: ')
cocokkan = re.findall(pola_email, masukan)
print(cocokkan)

####no3 membuat binary tree dan mencari simpul terluar

