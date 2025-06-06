from App.database import db

class Category (db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    category_id= db.Column(db.String(5), nullable= False)
    category_name=  db.Column(db.String(80), nullable=False)
    category_thumbnail= db.Column(db.String(200), nullable=False) 

    def __init__(self, category_id, category_name, category_thumbnail):
        self.category_id=category_id
        self.category_name=category_name
        self.category_thumbnail=category_thumbnail

       