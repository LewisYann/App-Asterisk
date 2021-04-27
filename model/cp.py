from config import db


class CP(db.Model):
    __tablename__="CP"
    idCP = db.Column(db.Integer, primary_key=True)
    idPersonne = db.Column(db.String(255), nullable=False)
    idequipe = db.Column(db.Integer)
    date = db.Column(db.String(255), nullable=False)
    # equipe = db.relationship("equipe", back_populates="membreequipe")

    def _to_json(self):
        return {
            "idCP": self.idCP,
            "idPersonne": self.name,
            "idEquipe": self.idequipe
        }

    def __repr__(self):
        return '<Service %r>' % self.name
