from datetime import datetime
from config import db
from model.tache import Tache


class CrudTache:
    @staticmethod
    def get_Tache_by_id(id):
        cursor = Tache.query.filter_by(id=id).all()
        return [Tache._to_json() for Tache in cursor]

    @staticmethod
    def get_Tache_by_statu(statu):
        cursor = Tache.query.filter_by(statu=statu).all()
        return [Tache._to_json() for Tache in cursor]

    @staticmethod
    def get_all():
        cursor = Tache.query.all()
        return [Tache._to_json() for Tache in cursor]


    @staticmethod
    def create_tache(idPersonne, designation, statu):
        t = Tache()
        t.idPersonne=idPersonne
        t.designation=designation
        t.statu=statu
        t.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        db.session.add(t)
        db.session.commit()
        return CrudTache.add_Note(t)

    @staticmethod
    def del_Tache(id):
        t = Tache.query.get(id)
        db.session.delete(t)
        db.session.commit()

    @staticmethod
    def update_tache(id,designation):
        t = Tache.query.get(id)
        t.designation=designation
        db.session.commit()
        return "True"

    @staticmethod
    def update_statu(id,statu):
        t = Tache.query.get(id)
        t.statu=statu
        t.dateFin=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        db.session.commit()

    def add_Note(t):
        return {
            "id": t.id,
            "idPersonne": t.idPersonne,
            "statu": t.statu,
            "date": t.date,
        }

