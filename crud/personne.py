from datetime import datetime
from config import db
from model.personne import Personne
import utils

class CrudPersonne:
    @staticmethod
    def get_personne_by_id(id):
        cursor = Personne.query.filter_by(idPersonne=id).all()
        return [Personne._to_json() for Personne in cursor]

    @staticmethod
    def get_membreequipe_by_id(id):
        cursor = Personne.query.filter_by(idequipe=id).all()
        return [Personne._to_json() for Personne in cursor]

    @staticmethod
    def get_all():
        cursor = Personne.query.all()
        return [Personne._to_json() for Personne in cursor]


    @staticmethod
    def create_personne(nom, prenom,idequipe,poste):
        t = Personne()
        t.idPersonne = utils.generate_numero()
        t.nom = nom
        t.prenom = prenom
        t.idequipe= idequipe
        t.poste= poste
        t.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        db.session.add(t)
        db.session.commit()
        return CrudPersonne.add_Personne(t)

    @staticmethod
    def del_Personne(id):
        t = Personne.query.get(id).all()
        db.session.delete(t)
        db.session.commit()

    @staticmethod
    def update_Personne(id,nom, prenom,poste,idequipe):
        t = Personne.query.get(id)
        t.nom=nom
        t.prenom=prenom
        t.poste=poste
        t.idequipe=idequipe
        db.session.commit()
        return "True"

    def add_Personne(t):
        return {
            "id": t.id,
            "idPersonne": t.idPersonne,
            "nom": t.nom,
            "prenom": t.prenom,
            "poste": t.poste,
            "idequipe": t.idequipe,
        }

