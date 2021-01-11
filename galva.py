# Musu Flask serveris
from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
from module import funci


app = Flask(__name__)

@app.route('/',methods=['GET'])
def root():
    aa = ""
    bb = ""
    cc = ""    
    aa = request.args.get('a',default='0.',type=str)
    bb = request.args.get('b',default='0.',type=str)
    cc = request.args.get('c',default='0.',type=str)
    a1 = float(aa)
    b1 = float(bb)
    c1 = float(cc)
    rez = "Perimetrs=" + funci.tr_per(a1,b1,c1)
    return render_template("sveikaPasaule.html",vards="Trīsstūra parametri",rezultats=rez)

@app.route('/pogasall',methods=['GET'])
def pogasall():
    aa = request.args.get('a',default='0.',type=str)
    bb = request.args.get('b',default='0.',type=str)
    #aa= "Ievadītā vērtība: " + aa
    aa1 = int(aa)
    b1=[]
    for k in range(aa1):
      b1.append("Vērtība "+str(k)+" un tā kvadrāts= "+str(k*k))
    
    return render_template("rezultats.html",vards="Kontroļu pārbaude",rezultats=b1)

@app.route('/pogas')
def pogas():
    return render_template("pogas.html",vards="Podziņas")

@app.route('/tests')
def health():
  return "Serveris darbojas Uh!"

if __name__ == '__main__':
  app.run()
