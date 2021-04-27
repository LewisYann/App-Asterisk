from datetime import datetime
from config import db
from model.noteService import Note


class CrudNote:
    @staticmethod
    def get_note_by_id(id):
        cursor = Note.query.filter_by(idNote=id).all()
        return [Note._to_json() for Note in cursor]

    @staticmethod
    def get_all():
        cursor = Note.query.all()
        return [Note._to_json() for Note in cursor]


    @staticmethod
    def create_note(idPersonne, sujet, contenu):
        t = Note()
        t.idPersonne=idPersonne
        t.sujet=sujet
        t.contenu=contenu
        t.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        db.session.add(t)
        db.session.commit()
        return CrudNote.add_Note(t)

    @staticmethod
    def del_Personne(id):
        t = Note.query.filter_by(idNote=id).all()
        db.session.delete(t)
        db.session.commit()

    @staticmethod
    def update_Note(idNote,sujet, contenu):
        t = Note.query.filter_by(idNote=idNote).all()
        t.sujet=sujet
        t.contenu=contenu
        db.session.commit()

    def add_Note(t):
        return {
            "id": t.id,
            "idNote": t.idNote,
            "idPersonne": t.idPersonne,
            "sujet": t.sujet,
            "contenu": t.contenu,
            "date": t.date,
        }

