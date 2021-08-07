# načtení potřebných modulů a funkcí
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import datetime
import os

app = Flask(__name__) # vytvoření objektu aplikace
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!' # nastavení klíče
path=os.path.dirname(os.path.abspath(__file__)).replace("\\","/") # adresní cesta k databázi
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path}/database.db'
bootstrap = Bootstrap(app) # deklarace bootstrap
db = SQLAlchemy(app) 

@app.route('/') # při zadání adresy lokálního serveru a znaku / se spustí funkce index a vykreslí stránku index.html, 
def index():
    date=datetime.datetime.now()
    den=format(date.day)
    mesic=format(date.month)
    rok=format(date.year)
    dnesni_Datum=den+"."+mesic+"."+rok
    dnesni_Datum=str(dnesni_Datum)
    return render_template('index.html',datum=dnesni_Datum) # při vykreslení předáváme parametr datum, díky kterému na dané stránce proběhne funkce tam kde předáme parametr do dvojitých složených závorek

if __name__ == '__main__': #zapnutí debug modu
    app.run(debug=True)
