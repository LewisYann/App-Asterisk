from config import db


class Note(db.Model):
    __tablename__="Notes"
    id = db.Column(db.Integer, primary_key=True)
    idNote = db.Column(db.String(255), nullable=False)
    idPersonne = db.Column(db.String(255), nullable=False)
    sujet = db.Column(db.String(255), nullable=False)
    contenu = db.Column(db.text, nullable=False)
    date = db.Column(db.String(255), nullable=False)

    def _to_json(self):
        return {
            "id": self.id,
            "idNote": self.category_id,
            "idPersonne": self.name,
            "sujet":self.sujet,
            "contenu":self.contenu,
            "date": self.date,

              }

    def __repr__(self):
        return '<Service %r>' % self.name
