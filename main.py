<<<<<<< HEAD
# İçeri Aktarma
from flask import Flask, render_template,request, redirect
# Veritabanı kütüphanesini içe aktarma
=======
# Kütüphaneleri yükleme/Flask'a bağlanma
from flask import Flask, render_template, request, redirect, session
# Veti tabanı kütüphanesine bağlanma
>>>>>>> 3c24ef7e20d774beb873e460f866543e2ef77d72
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
<<<<<<< HEAD
# SQLite ile bağlantı kurma 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# DB oluşturma
db = SQLAlchemy(app )

#Görev #1. DB tablosu oluşturma
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(200), nullable=True)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Card {self.id}>'
=======
# Oturum için gizli anahtarın ayarlanması
app.secret_key = 'my_top_secret_123'
# SQLite bağlantısı kurma
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Veritabanı oluşturma
db = SQLAlchemy(app)
# Tablo oluşturma

class Card(db.Model):
    # Tablo giriş alanları oluşturma
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Başlık
    title = db.Column(db.String(100), nullable=False)
    # Alt başlık
    subtitle = db.Column(db.String(300), nullable=False)
    # Metin
    text = db.Column(db.Text, nullable=False)
    # Kart sahibinin e-posta adresi
    user_email = db.Column(db.String(100), nullable=False)

    # Nesneyi ve kimliğini çıktı olarak verme
    def __repr__(self):
        return f'<Card {self.id}>'
    

# Görev #1. Kullanıcı tablosunu oluşturun.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
>>>>>>> 3c24ef7e20d774beb873e460f866543e2ef77d72




<<<<<<< HEAD





# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    # DB nesnelerini görüntüleme
    # Görev #2. DB'deki nesneleri index.html'de görüntüleme
    cards = Card.query.order_by(Card.id).all()

    return render_template('index.html',
                           #kartlar = kartlar
                           cards = cards 
                           )

# Kartla sayfayı çalıştırma
@app.route('/card/<int:id>')
def card(id):
    # Görev #2. Id'ye göre doğru kartı görüntüleme
=======
# İçerik sayfasını başlatma
@app.route('/', methods=['GET','POST'])
def login():
    error = ''
    if request.method == 'POST':
        form_login = request.form['email']
        form_password = request.form['password']
            
        # Görev #4. Kullanıcı doğrulamasını uygulayın
        users_db = User.query.all()
        for user in users_db:
            if form_login == user.email and form_password == user.password:
                session['user_email'] = user.email
                return redirect('/index')
        
            else: 
                error = 'Yanlış kullanıcı adı veya şifre'
                return render_template('login.html', error=error)

     
    else:
        return render_template('login.html')



@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Görev #3. Kullanıcı doğrulamasını uygulayın
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()

        
        return redirect('/')
    
    else:    
        return render_template('registration.html')


# İçerik sayfasını başlatma
@app.route('/index')
def index():
    # Görev #4. Kullanıcının yalnızca kendi kartlarını görmesini sağlayın.
    cards = Card.query.order_by(Card.id).all()
    return render_template('index.html', cards=cards)

# Kart sayfasını başlatma
@app.route('/card/<int:id>')
def card(id):
>>>>>>> 3c24ef7e20d774beb873e460f866543e2ef77d72
    card = Card.query.get(id)

    return render_template('card.html', card=card)

<<<<<<< HEAD
# Sayfayı çalıştırma ve kart oluşturma
=======
# Kart oluşturma sayfasını başlatma
>>>>>>> 3c24ef7e20d774beb873e460f866543e2ef77d72
@app.route('/create')
def create():
    return render_template('create_card.html')

# Kart formu
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

<<<<<<< HEAD
        # Görev #2. Verileri DB'de depolamak için bir yol oluşturma
        card = Card(title=title, subtitle=subtitle, text=text)
        db.session.add(card)
        db.session.commit()




        return redirect('/')
    else:
        return render_template('create_card.html')


=======
        # Görev #4. Kullanıcı adına kart oluşturma işlemini gerçekleştirin.
        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')

>>>>>>> 3c24ef7e20d774beb873e460f866543e2ef77d72
if __name__ == "__main__":
    app.run(debug=True)
