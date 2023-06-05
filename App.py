from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# create db DATABASE
class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=False)
    text = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return self.title

# Home
@app.route("/")
def start():
    item = Items.query.order_by(Items.price).all()
    return render_template("space.html", data=item)


@app.route("/create", methods=['POST', 'GET'])
def add_product():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        price = request.form['price']

        item = Items(title=title, text=text, price=price)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return 'Сталась помилка'
    else:
        return render_template('add_product.html')

if __name__ == "__main__":
    app.run(debug=True)