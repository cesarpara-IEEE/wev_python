from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

#------CAPTAR----------#####

def desplegar(num):
  direccion = 'https://www.erocurves.com/model-archives/'

  subPage = []
  pagina = requests.get(direccion)
  pag = BeautifulSoup(pagina.content, 'html.parser')
  for i in pag.find_all(class_="%post-title%"):
      subPage.append(i.get('href'))    
  acc = []

  subpag = requests.get(subPage[num-1])    
  spag = BeautifulSoup(subpag.content, 'html.parser')
  cla = spag.find_all(class_="img_hover_trans")
  for i in cla:
    pg = requests.get(i.get('href'))
    pg_s = BeautifulSoup(pg.content, 'html.parser')
    arr = pg_s.find_all(class_="gallery-icon portrait")
    arr2 = pg_s.find_all(class_="thumb")

    for i in arr:
      hr = i.a
      acc.append(hr.get('href'))

    for i in arr2:
      acc.append(i.get('href'))
  return acc
###----------------------------###


app = Flask(__name__, template_folder='template')  #Importante señores es una nueva configuracion

@app.route('/')
def home():
  acc = desplegar(1)
  return render_template('home.html', lin = acc )

@app.route('/', methods=["POST"])
def some_function():
    text = request.form.get('textbox')
    acc = desplegar(int(text))
    return render_template('home.html', lin = acc)

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)



  