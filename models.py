import os
from sqla_wrapper import SQLAlchemy

db_url = os.getenv("DATABASE_URL", "sqlite:///db.sqlite").replace("postgres://", "postgresql://", 1)
db = SQLAlchemy(db_url, connect_args={'check_same_thread': False})

class Ucenik(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ime_prezime = db.Column(db.String, unique=False)
    god_rod = db.Column(db.String, unique=False)
    smjer = db.Column(db.String, unique=False)
    razred = db.Column(db.String, unique=False)
    prosjek = db.Column(db.Float, unique=False)