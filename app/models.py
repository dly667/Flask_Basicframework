from . import db
print(db,33)
class User(db.Model):
    __table__ = 'user1'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    def __repr__(self):
        return '<User %r>' %self.name
