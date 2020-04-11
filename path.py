#importar caminhos

from pathlib import Path

basepath = Path('/media/bruno/DATA/eproc_test/')
#basepath = Path('/media/bruno/DATA/Auto-eproc/arquivos')
files_in_basepath = basepath.glob('**/*')
for item in files_in_basepath:
    if item.is_file():
        print(item.name)
