from app import app, db
from app.models import Constituency, Voter
from flask import make_response, jsonify, request

@app.route('/api/voter/', methods=['POST'])
def register_voter():
    content = request.json
    print(request.json, request.data, request.form)
    if not (u'name' in content.keys() and u'constituency' in content.keys() and u'address' in content.keys() and u'age' in content.keys()):
        return make_response(
                    jsonify({"message": "Missing data."}),
                    400)
    if(u'age'<18):
        return make_response(
            jsonify({"message": "Minimum age is 18."}),
            400)
    voter = Voter(name=content[u'name'], age=content[u'age'], address=content[u'address'])
    constituency = Constituency.query.filter_by(name=str(content['constituency'])).first()
    if constituency == None:
        return make_response(
            jsonify({"message": "No such constituency."}),
            400)
    
    voter.constituency = constituency
    
    db.session.add(voter)
    db.session.commit()

    return make_response(
            jsonify({"message": "Voter Id is "+str(voter.id)}),
            200)