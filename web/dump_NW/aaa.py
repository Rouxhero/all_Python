# coding: utf-8

import sys
import glob

from bs4 import BeautifulSoup
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def pygments_file(pathname):
    # On ouvre le fichier
    with open(pathname, "r" ) as f:
        html_doc = f.read()
        
    soup = BeautifulSoup(html_doc)
    # On boucle sur les pre trouvés
    for pre in soup.find_all('pre'):
        try:
            if "code" in pre.get("class"):
                texte = highlight(pre.get_text(), PythonLexer(), \
                HtmlFormatter(nowrap=True))
                n = BeautifulSoup('%s' % texte)        
                pre.replace_with(n.body.contents[0])
        except:
            print("Erreur avec {}".format(pre,))
        
    if soup.body:
        with open(pathname, "w") as f:
            f.write(soup.body.encode_contents())
       
# p = "*.html"

if sys.argv[1]:
    p = str(sys.argv[1])

pathnames = glob.glob(p)
for pathname in pathnames:
    pygments_file(pathname)