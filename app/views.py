from flask import Flask, render_template, request, url_for, redirect
from app        import app


# Render the user page
@app.route('/usuario.html')
def user():
    pagina='Usuário  '
    return render_template('layouts/default.html',  pagina=pagina,
                            content=render_template( 'pages/usuario.html') )

# Render the table page
@app.route('/tabela.html')
def table():
    pagina = 'Tabelas  '
    return render_template('layouts/default.html', pagina=pagina,
                            content=render_template( 'pages/tabela.html', ) )

# Render the typography page
@app.route('/tipografia.html')
def typography():
    pagina = 'Tipografia  '
    return render_template('layouts/default.html', pagina=pagina,
                            content=render_template( 'pages/tipografia.html') )

# Render the icons page
@app.route('/icones.html')
def icons():
    pagina = 'Ícones  '
    return render_template('layouts/default.html',  pagina=pagina,
                            content=render_template( 'pages/icones.html') )

# Render the icons page
@app.route('/notificacoes.html')
def notifications():
    pagina = 'Notificações  '
    return render_template('layouts/default.html',  pagina=pagina,
                            content=render_template( 'pages/notificacoes.html') )

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):

    content = None

    try:

        # try to match the pages defined in -> pages/<input file>
        return render_template('layouts/default.html',   pagina='Dashboard: TRK 735 ',
                                content=render_template( 'pages/'+path) )
    except:
        
        return 'Oupsss :(', 404
