from app import app, db
from app.models import Constituency, Voter, Party
from flask import make_response, jsonify, request

@app.route('/api/constituency/', methods=['GET'])
def get_constituencies():
    constituencies = Constituency.query.all()
    constituencies_arr = []
    for c in constituencies:
        constituencies_arr.append(c.dict())
    print (jsonify(constituencies_arr))
    return jsonify(constituencies_arr)

@app.route('/api/constituency/<constituency_name>/party/', methods=['GET'])
def get_constituency_parties(constituency_name):
    constituency = Constituency.query.filter_by(name=constituency_name).first()

    if constituency == None:
        return make_response(
            jsonify({"message": "No such constituency."}),
            400)

    party_assocs = constituency.parties
    party_arr = []

    for p in party_assocs:
        party_arr.append({"party_name": p.party.name, "party_id": p.party.id})

    return jsonify(party_arr)


@app.route('/api/constituency/<constituency_name>/voter/<voter_id>/', methods=['GET'])
def get_constituency_voter(constituency_name, voter_id):
    constituency = Constituency.query.filter_by(name=constituency_name).first()

    if constituency == None:
        return make_response(
            jsonify({"message": "No such constituency."}),
            400)

    voters = constituency.voters
    print(voters)
    for voter in voters:
        if voter.id == int(voter_id):
            voter_json = voter.dict()
            return make_response(
                jsonify({"voter": voter_json}),
                200)

    return make_response(
        jsonify({"message": "Invalid voter id or voter not registered in constituency."}),
        400)

@app.route('/api/constituency/<constituency_name>/result/', methods=['GET'])
def get_result(constituency_name):

    constituency = Constituency.query.filter_by(name=constituency_name).first()

    if constituency == None:
        return make_response(
            jsonify({"message": "No such constituency."}),
            400)
    
    results = []
    for assoc in constituency.parties:
        results.append({"name": assoc.party.name, "votes": assoc.vote})
    
    return make_response(
        jsonify(results),
        200)
    


@app.route('/api/constituency/<constituency_name>/vote/', methods=['POST'])
def cast_vote(constituency_name):

    constituency = Constituency.query.filter_by(name=constituency_name).first()

    if constituency == None:
        return make_response(
            jsonify({"message": "No such constituency."}),
            400)
    
    content = request.json
    if not (u'voter_id' in content.keys() and u'party_id' in content.keys()):
        return make_response(
                    jsonify({"message": "Missing data."}),
                    400)
    
    voter = Voter.query.filter_by(id=int(content[u'voter_id'])).first()
    if( voter == None or not (voter in constituency.voters)):
        return make_response(
                    jsonify({"message": "Voter not in constituency."}),
                    400)
    
    party = Party.query.filter_by(id=int(content[u'party_id'])).first()
    party_in = False
    for assoc in constituency.parties:
        if( party == assoc.party):
            party_in = True
            break
    if( party == None or party_in==False):
        return make_response(
                    jsonify({"message": "Party not in constituency."}),
                    400)

    

    if voter.voted == True:
        return make_response(
                    jsonify({"message": "Voter has already voted."}),
                    400)

    for assoc in constituency.parties:
        if assoc.party == party:
            assoc.vote = assoc.vote + 1
            break

    voter.voted = True
    db.session.commit()

    return make_response(
                    jsonify({"message": "Your vote hs been registered."}),
                    200)