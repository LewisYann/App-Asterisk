from config import db


class equipe(db.Model):
    __tablename__="equipe"
    id = db.Column(db.Integer, primary_key=True)
    idequipe = db.Column(db.Integer, nullable=False)
    nomequipe = db.Column(db.String(255), nullable=False)
    nombremembre = db.Column(db.Integer, nullable=False)
    idchefprojet = db.Column(db.String(255), nullable=True)
    date_creation = db.Column(db.String(255), nullable=False)
   # membreequipe = db.relationship("Personne", back_populates="equipe")

    def _to_json(self):
        return {
            "id": self.id,
            "idequipe": self.idequipe,
            "nomequipe": self.nomequipe,
            "nombremembre": self.nombremembre,
            "idchefprojet": self.idchefprojet,
            "idequipe": self.idequipe,
            #"membreequipe": [membreequipe._to_json() for membreequipe in self.membreequipe]
        }


    def __repr__(self):
        return '<Category %r>' % self.idequipe
