from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def entrar():
    return render_template('home.html')

@app.route('/paginacriacao')
def paginacriacao():
   return render_template('criacao.html')

@app.route('/criar', methods=['POST'])
def criar_post():
    
    try:
        cor_pele = request.form.get('cor-pele')
        formato_cabelo = request.form.get('formato-cabelo')
        cor_cabelo = request.form.get('cor-cabelo')
        imagem=cor_pele+"-"+formato_cabelo+"-"+cor_cabelo+".png"

        return render_template('resultado.html',imagem=imagem)
    except:
       return render_template('criacao.html',erro="Por favor selecione um de cada")
        
if __name__ == '__main__':
 app.run()