from rest_api.database import db
from rest_api.database.models import NGO,NGO_Branch, Requirement, RequirementType,Donation



def create_ngo(data):
	
    name = data.get('name')
    description = data.get('description')
    password = data.get('password')
    Lat = data.get('lat')
    Long = data.get('long')
    
    NewNgo = NGO(name,description,password)
    ngo_branch = NGO_Branch(NewNgo.id,Lat,Long)

    db.session.add(NewNgo)
    db.session.add(ngo_branch)
    db.session.commit()


def update_NGO(ngo_id, data):
    ngo = NGO.query.filter(NGO.id == category_id).one()
    ngo.name = data.get('name')
    db.session.add(ngo)
    db.session.commit()


def delete_ngo(ngo_id):
    ngo = NGO.query.filter(NGO.id == ngo_id).one()
    db.session.delete(ngo)
    db.session.commit()
