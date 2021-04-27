from flask import request, jsonify
import requests
from crud.equipe import CrudEquipe
from crud.personne import CrudPersonne
from crud.tache import CrudTache
from flask import render_template
from config import app, url, auth, urlFreepbx, headers

#Personne&membre
@app.route('/', methods=['GET'])
def get():
    return render_template("test.html")

@app.route('/personne', methods=['GET'])
def get_all_personne():
    return jsonify(CrudPersonne.get_all())


@app.route('/personne/<id>', methods=['GET'])
def get_personne_by_id(id):
    return jsonify(CrudPersonne.get_personne_by_id(id))

@app.route('/membre/<equipe>', methods=['GET'])
def get_member_by_id(equipe):
    return jsonify(CrudPersonne.get_membreequipe_by_id(equipe))


@app.route('/create/personne', methods=['POST'])
def create_personne():
    nom = request.form['nom']
    prenom= request.form['prenom']
    idequipe = request.form['idequipe']
    poste = request.form['poste']
    return jsonify(CrudPersonne.create_personne(nom,prenom,idequipe,poste))

@app.route('/delete/personne', methods=['POST'])
def del_personne():
    id = request.form['id']
    return jsonify(CrudPersonne.del_Personne(id))

@app.route('/update/personne', methods=['POST'])
def update_personne():
    id = request.form['id']
    nom = request.form['nom']
    prenom = request.form['prenom']
    idequipe = request.form['idequipe']
    poste = request.form['poste']
    return jsonify(CrudPersonne.update_Personne(id,nom,prenom,poste,idequipe))



#Equipe
@app.route('/equipe', methods=['GET'])
def get_all_equipe():
    return jsonify(CrudEquipe.get_all())

@app.route('/equipe/<id>', methods=['GET'])
def get_equipe_by_id(id):
    return jsonify(CrudEquipe.get_equipe_by_id(id))

@app.route('/create/equipe', methods=['POST'])
def create_equipe():
    name = request.form['name']
    cp = request.form['cp']
    return jsonify(CrudEquipe.create_equipe(name,cp))

@app.route('/delete/equipe', methods=['POST'])
def del_equipe():
    id = request.form['id']
    return jsonify(CrudEquipe.del_equipe(id))

@app.route('/update/equipe', methods=['POST'])
def update_equipe():
    id = request.form['id']
    cp= request.form['cp']
    return jsonify(CrudEquipe.update_equipe(id, cp))



#Tache
@app.route('/tache', methods=['GET'])
def get_all_tache():
    return jsonify(CrudTache.get_all())

@app.route('/tache/<id>', methods=['GET'])
def get_tache_by_id(id):
    return jsonify(CrudTache.get_Tache_by_id(id))

@app.route('/create/tache', methods=['POST'])
def create_tache():
    idPersonne = request.form['idPersonne']
    designation = request.form['designation']
    statu = "En cours"
    return jsonify(CrudTache.create_tache(idPersonne,designation,statu))

@app.route('/delete/tache/<tache>', methods=['GET'])
def delel_tache(tache):
    return jsonify(CrudTache.del_Tache(tache))

@app.route('/update/tache', methods=['POST'])
def update_tache():
    id = request.form['id']
    designation = request.form['designation']
    return jsonify(CrudTache.update_tache(id,designation))

@app.route('/end', methods=['POST'])
def update_statu():
    id = request.form['id']
    statu = "Terminer"
    id=int(id)
    return jsonify(CrudTache.update_statu(id, statu))

#ARI

@app.route('/extension/create', methods=['POST'])
def create_sip(sipnumbeer, ):
    payload = "{\"query\":\"mutation {\\r\\n    addCoreExten(\\r\\n        input: {\\r\\n            extension: 9001\\r\\n            name: \\\"api test\\\"\\r\\n            tech: \\\"pjsip\\\"\\r\\n            umgroups:\\\"1\\\"\\r\\n            outboundcid:\\\"\\\"\\r\\n          vm:\\\"\\\"\\r\\n            \\r\\n        }\\r\\n    ) {\\r\\n        status\\r\\n        \\r\\n    }\\r\\n}\\r\\n\\r\\n\",\"variables\":{}}"

    response = requests.request("POST", url, headers=headers, data=payload)
    re = requests.get(url + 'ari/endpoints', auth=auth)

    return jsonify(re.json())


@app.route('/extension/list', methods=['GET'])
def get_all_sip():
    re = requests.get(url + 'ari/endpoints', auth=auth)

    return jsonify(re.json())


@app.route('/extension/<numero>', methods=['GET'])
def get_sip_by_id(numero):
    re = requests.get(url + 'ari/endpoints/PJSIP/' + numero, auth=auth)

    return jsonify(re.json())


@app.route('/extension/<numero>/statu', methods=['GET'])
def get_statu_sip_by_id(numero):
    re = requests.get(url + 'ari/endpoints/PJSIP/' + numero, auth=auth)
    res = re.json()
    return jsonify(res['state'])


@app.route('/extension/e-message/<source>/<destinataire>/<message>', methods=['GET'])
def sendMessage_by_id(source, destinataire, message):
    re = requests.put(url + 'ari/endpoints/PJSIP/' + destinataire + '/sendMessage', auth=auth,
                      json={'from': source, 'body': message})

    return jsonify(re.json())


# channel
@app.route('/appel')
def channellist():
    re = requests.get(url + 'ari/channels', auth=auth)
    return jsonify(re.json())







if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port="5000")
