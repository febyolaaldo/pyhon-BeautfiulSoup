from bs4 import BeautifulSoup
import requests

# i'm use content http://internasional.metrotvnews.com/asia/RkjPoE6N-penjelasan-kemenlu-soal-tki-ilegal-ditahan-di-malaysia
def interMetro():
    page = requests.get('http://internasional.metrotvnews.com/asia/RkjPoE6N-penjelasan-kemenlu-soal-tki-ilegal-ditahan-di-malaysia')
    soup = BeautifulSoup(page.content, "html.parser")
    
    artikels = soup.find_all('div', {'class': 'detail'})
    for z in artikels:
        title = z.find('h1').getText()
        content = z.find('div',{'class':'tru'}).getText()
        print "Title = ", title.strip()
        print "Content = ", content.strip()
        # if you use python 3, comment above and uncomment below
        # print ("Title = ", title.strip())
        # print ("Content = ", content.strip())

# i'm use content https://metro.tempo.co/read/news/2017/07/07/083889609/djarot-pastikan-kjp-tak-bisa-ditarik-tunai-hingga-desember
def metroTempo():
    page = requests.get('https://metro.tempo.co/read/news/2017/07/07/083889609/djarot-pastikan-kjp-tak-bisa-ditarik-tunai-hingga-desember')
    soup = BeautifulSoup(page.content, "lxml")
    
    artikels = soup.find_all('div', {'class': 'artikel'})
    for z in artikels:
        title = z.find('h1').getText()
        content = z.find('p').getText()
        print "Title = ", title.strip()
        print "Content = ", content.strip()
        # if you use python 3, comment above and uncomment below
        # print ("Title = ", title.strip())
        # print ("Content = ", content.strip())

# call function
interMetro()
metroTempo()