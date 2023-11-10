from re import I
from urllib.request import urlopen

import time
url1='https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png'
url2='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png'
links=[url1,url2]##arreglo que contiene las url de las imágenes
def main():
  i=0
  while(i<2):
    with urlopen(links[i]) as page:
      image_data=page.read
      i=i+1

if __name__ == '__main__':
  t1=time.perf_counter()
  main()
  t2=time.perf_counter()
  tiempo=t2-t1
  print(f"Tiempo de ejecucion {tiempo} segundos")
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from urllib.request import urlopen
from threading import Thread
import time
url1='https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png'
url2='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png'
def im1():
  with urlopen(url1) as page:
    image_data=page.read
def im2():
  with urlopen(url2) as page:
    image_data=page.read

if __name__ == '__main__':
  i=0
  tiempo=0
  while(i<5):
    t1=time.perf_counter()
    f1=Thread(target=im1)
    f2=Thread(target=im2)
    f1.start()
    f2.start()
    f1.join()
    f2.join()
    t2=time.perf_counter()
    tiempo=tiempo+t2-t1
    print(f"Tiempo de ejecucion {t2-t1} segundos")
    i=i+1
  mediana=tiempo/5
  print(f"Tiempo de ejecucion media {mediana} segundos")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from urllib.request import urlopen
from threading import Thread
import time
url1='https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png'
url2='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png'
links=[url1,url2]##arreglo que contiene las url de las imágenes
def main(link):
  with urlopen(link) as page:
    image_data=page.read
   
if __name__ == '__main__':
  t1=time.perf_counter()
  i=0
  while(i<2):
    a=links[i]
    f=Thread(target=main,args=(a))
    f.start()
    i=i+1
  f.join()
  t2=time.perf_counter()
  tiempo=t2-t1
  print(f"Tiempo de ejecucion {tiempo} segundos")
