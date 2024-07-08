from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

class Blog(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    content: Mapped[str]


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", blogs = Blog.query.all())


@app.route("/", methods=["POST"])
def submit():
    title = request.form.get('title')
    content = request.form.get('content')
    blog = Blog(title=title, content=content)
    db.session.add(blog)
    db.session.commit()

    return render_template("index.html", blogs = Blog.query.all())

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
