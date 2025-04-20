from App.database import db

class I_user(db.Model):
    __tablename__ = 'i_user'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'), nullable=False)
    #__table_args__ = (db.PrimaryKeyConstraint('user_id', 'ingredient_id'),)  # Composite primary key