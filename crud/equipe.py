from datetime import datetime
from config import db
from model.equipe import equipe
import utils

class CrudEquipe:
    @staticmethod
    def get_equipe_by_id(equipe_id):
        cursor = equipe.query.filter_by(idequipe=equipe_id)
        return [equipe._to_json() for equipe in cursor]

    @staticmethod
    def get_all():
        cursor = equipe.query.all()
        return [equipe._to_json() for equipe in cursor]





    @staticmethod
    def create_equipe(nomequipe, idchefprojet):
        t = equipe()
        t.idequipe = utils.generate_numero()
        t.nomequipe = nomequipe
        t.nombremembre = 0
        t.idchefprojet = idchefprojet
        t.date_creation = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        db.session.add(t)
        db.session.commit()
        return CrudEquipe.add_equipe(t)

    @staticmethod
    def del_equipe(idequipe):
        t = equipe.query.get(idequipe)
        db.session.delete(t)
        db.session.commit()

    @staticmethod
    def update_equipe(id, cp):
        t = equipe.query.get(id)
        t.idchefprojet=cp
        db.session.commit()


    @staticmethod
    def add_equipe(t):
        return {
            "id": t.id,
            "idequipe": t.idequipe,
            "nomequipe": t.nomequipe,
            "idchefprojet": t.idchefprojet,
            "idequipe": t.idequipe,
        }