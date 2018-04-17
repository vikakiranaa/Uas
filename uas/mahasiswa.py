nama = []
nim = []
tugas = []
uts = []
uas = []

n = int(input('Masukkan Jumlah Data :'))

for i in range(0,n):
	nama.append(input('%d. Nama : '%(i+1)))
	nim.append(input('    Nim : '))
	tugas.append(input('    Tugas : '))
	uts.append(input('    Uts : '))
	uas.append(input('    Uas : '))

print('=========================================')
print('No. \tNama\t\tNim\t\tTugas\t\tUts\t\tUas')
for i in range(0,n) :
	print('%d\t%s\t\t%s\t\t%s\t\t%s\t\t%s'% ((i+1),nama[i],nim[i],tugas[i],uts[i],uas[i]))