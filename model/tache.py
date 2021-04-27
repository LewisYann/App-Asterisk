from config import db


class Tache(db.Model):
    __tablename__="Tache"
    id = db.Column(db.Integer, primary_key=True)
    idPersonne = db.Column(db.Integer, nullable=False)
    designation = db.Column(db.String(255), nullable=False)
    statu = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255), nullable=False)
    dateFin = db.Column(db.String(255), nullable=True)


    def _to_json(self):
        return {
            "id": self.id,
            "idPersonne": self.idPersonne,
            "designation": self.designation,
            "statu":self.statu,
            "date":self.date,
            "dateFin":self.dateFin,
        }

    def __repr__(self):
        return '<id %r>' % self.id
