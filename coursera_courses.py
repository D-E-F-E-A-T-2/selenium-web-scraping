from bs4 import BeautifulSoup
from urllib.request import urlopen

website = 'https://www.coursera.org/browse/'

links = ['arts-and-humanities', 'business', 'computer-science', \
         'data-science', 'information-technology', 'health', \
         'math-and-logic', 'personal-development', 'physical-science-and-engineering', \
         'social-sciences', 'language-learning']

for x in links:
    f = open(x+'.txt', 'w+')
    link = website+x
    
    raw = urlopen(link)
    data = raw.read()
    raw.close()
    soup = BeautifulSoup(data)
    soup = BeautifulSoup(data, 'html.parser')
    for linker in soup.find_all('a'):
        name = linker.get('aria-label')
        if name!=None and  name!='Coursera' and name!='Browse' and name!='Search' and name!='For Enterprise. See information about Coursera for Business':
            try:
                f.write(name+',.'+'https://www.coursera.org'+linker.get('href')+'\n')
            except:
                print('[!] Check for '+x)
    f.close()
    print(x+'\n')
    
