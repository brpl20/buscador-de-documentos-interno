#converter 
from pathlib import Path
from pdf2image import convert_from_path

basepath = Path('/media/bruno/DATA/cnhs')
count = 0

#basepath = Path('/media/bruno/DATA/Auto-eproc/arquivos')
files_in_basepath = basepath.glob('**/*.pdf')
for item in files_in_basepath:
	count += 1
	pages = convert_from_path(item)
	for page in pages:
		page.save('out' + str(count) + '.jpg')
print()