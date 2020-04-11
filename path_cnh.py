#importar caminhos

from pathlib import Path
from shutil import copyfile

basepath = Path('/media/bruno/DATA/Dropbox')
count = 0

#basepath = Path('/media/bruno/DATA/Auto-eproc/arquivos')
files_in_basepath = basepath.glob('**/CNH.pdf')
for item in files_in_basepath:
	count += 1
	if item.is_file():
		copyfile(item, '/media/bruno/DATA/cnhs/' + 'cnh' + str(count) + '.pdf')
		#copyfile(item, '/media/bruno/DATA/cnhs/' + str(n))
print()



# https://stackoverflow.com/questions/3162271/get-loop-count-inside-a-python-for-loop


'''

files_in_basepath = basepath.glob('**/CNH.pdf')
for item in files_in_basepath:
	print(item)
	n = str(item) #cria uma lista mas ele vem com o string 
	n_listar = list()
	n_listar_contar = n_listar.count('CNH')
	n_listar.append(n_listar_contar)
	if item.is_file():
		copyfile(item, '/media/bruno/DATA/cnhs/teste.pdf')
		#copyfile(item, '/media/bruno/DATA/cnhs/' + str(n))

'''
