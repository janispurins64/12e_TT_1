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
    aa = request.args.get('a',default='0',type=str)
    bb = request.args.get('b',default='0',type=str)
    
    aa1 = int(aa)
    bb1 = int(bb)
    b1=[]
    for k in range(aa1):
      for j in range(bb1):
        per = 2*(k+1+j+1)
        lauk = (k+1)*(j+1)
        rinda = "Mala a="
        rinda = rinda + str(k+1) + " mala b=" + str(j+1) +"; "
        rinda = rinda + "perimetrs P="+str(per)
        rinda = rinda + " laukums S="+str(lauk)
        b1.append(rinda)
    
    return render_template("rezultats.html",vards="Taisnstūra elementi",rezultats=b1)

@app.route('/pogas')
def pogas():
    return render_template("pogas.html",vards="Podziņas")

@app.route('/tests')
def health():
  return "Serveris darbojas Uh!"

if __name__ == '__main__':
  app.run()
