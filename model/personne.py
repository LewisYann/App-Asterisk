from config import db


class Personne(db.Model):
    __tablename__="personnes"
    id = db.Column(db.Integer, primary_key=True)
    idPersonne = db.Column(db.String(255), nullable=False)
    nom = db.Column(db.String(255), nullable=False)
    prenom = db.Column(db.String(255), nullable=False)
    poste = db.Column(db.String(255), nullable=False)
    idequipe = db.Column(db.Integer)
    date = db.Column(db.String(255), nullable=False)
    # equipe = db.relationship("equipe", back_populates="membreequipe")

    def _to_json(self):
        return {
            "id": self.id,
            "idPersonne": self.idPersonne,
            "name": self.nom,
            "prenom": self.prenom,
            "poste": self.poste,
            "idequipe": self.idequipe,
            "date d'inscription":self.date
        }

    def __repr__(self):
        return '<Service %r>' % self.idPersonne
