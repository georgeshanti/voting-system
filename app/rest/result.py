from app import app, db
from app.models import Party
from app.models.party import PartyConstituencyAssociation
from flask import make_response, jsonify, request

@app.route('/api/result/', methods=['GET'])
def get_all_result():

    parties = Party.query.all()
    
    results = []
    for party in parties:
        votes = 0
        for assoc in party.constituencies:
            votes = votes + assoc.vote
        results.append({"name": party.name, "votes": votes})
    
    return make_response(
        jsonify(results),
        200)


@app.route('/api/result/winner', methods=['GET'])
def get_winner():
    max_votes = db.session.query(db.func.max(PartyConstituencyAssociation.vote)).scalar()
    winning_parties = PartyConstituencyAssociation.query.filter_by(vote = max_votes).all()
    results = []
    for p in winning_parties:
        results.append({"name": p.party.name, "votes": p.vote})
    return jsonify(results)