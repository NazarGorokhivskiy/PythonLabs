from app import db


class Toy(db.Model):
    __tablename__ = "toys"
    toy_id = db.Column('id', db.Integer, primary_key=True)
    toy_size = db.Column('size', db.String(20))
    toy_age = db.Column('age', db.String(20))

    def __str__(self):
        return str("toys id: " + str(self.toy_id) + "\ntoys size: " + str(self.toy_size)
                   + "\ntoys age: " + str(self.toy_age))
