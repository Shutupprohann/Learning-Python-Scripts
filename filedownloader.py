import requests
from sys import argv
import pyfiglet

print(pyfiglet.figlet_format('FileDownloader'))
print('-'*75)
url = argv[1]
r = requests.get(url)
open(argv[2],'wb').write(r.content)