from flask import session
from flask import Flask, render_template, request, jsonify, redirect, url_for
from models import db, Aluno
app = Flask(__name__)
app.config['SECRET_KEY'] = 'seu_segredo_aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alunos.db'
db.init_app(app)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'raquel' and password == '123':
            return redirect(url_for('raquel_abreu_html'))
        elif username == 'hudson' and password == '321':
            return redirect(url_for('area_professor'))
        elif username == 'iara' and password == '321':
            return redirect(url_for('iara_abreu_html'))
        elif username == 'janaina' and password == '321':
            return redirect(url_for('janaina_html'))
        elif username == 'daiane' and password == '321':
            return redirect(url_for('daiane_html'))
        elif username == 'alvaro' and password == '321':
            return redirect(url_for('alvaro_html'))
        elif username == 'telma' and password == '321':
            return redirect(url_for('telma_html'))
        elif username == 'lucas' and password == '321':
            return redirect(url_for('lucas_html'))  
        else:
            error = 'Usuário ou senha incorretos!'
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/raquel_abreu')
def raquel_abreu_html():
    return render_template('raquel_abreu.html')

@app.route('/iara_abreu')
def iara_abreu_html():
    return render_template('iara_abreu.html')

@app.route('/daiane')
def daiane_html():
    return render_template('daiane.html')

@app.route('/janaina')
def janaina_html():
    return render_template('janaina.html')

@app.route('/telma')
def telma_html():
    return render_template('telma.html')

@app.route('/alvaro')
def alvaro_html():
    return render_template('alvaro.html')

@app.route('/lucas')
def lucas_html():
    return render_template('lucas.html')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/area_professor')
def area_professor():
    return render_template('area_professor.html')


if __name__ == '__main__':
    app.run(debug=True)

