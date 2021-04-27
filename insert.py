from model.equipe import equipe
from config import db
from model.personne import Personne

equipe = equipe(idequipe=4, nomequipe='ddddddd, nombremembre='2', idchefprojet='2', date_creation='13/02/2021')
personne = Personne(idPersonne="test1", idequipe=equipe)

db.session.add(equipe)
db.session.add(personne)
db.session.commit()