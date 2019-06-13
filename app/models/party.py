from app import db

class PartyConstituencyAssociation(db.Model):
    __tablename__ = 'party_constituency_association'
    left_id = db.Column(db.Integer, db.ForeignKey('constituency.id'), primary_key=True)
    right_id = db.Column(db.Integer, db.ForeignKey('party.id'), primary_key=True)
    vote = db.Column(db.Integer, default=0, nullable=False)

    constituency = db.relationship("Constituency", back_populates="parties")
    party = db.relationship("Party", back_populates="constituencies")

class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(128), nullable=False)
    constituencies = db.relationship(
        "PartyConstituencyAssociation",
        back_populates="party")