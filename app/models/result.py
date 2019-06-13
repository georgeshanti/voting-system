from app import db
from app.models.party import party_constituency_association_table

class Result(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	party_id = db.Column(db.Integer, db.ForeignKey('party.id'), nullable=False)
	party = db.relationship("Party", back_ref="results")
	constituency_id = db.Column(db.Integer, db.ForeignKey('constituency.id'), nullable=False)
	constituency = db.relationship("Constituency", back_ref="results")
	parties = db.relationship(
		"Party",
		secondary=party_constituency_association_table,
		back_populates="constituencies")

	def dict(self):
		return {
			"id": self.id,
			"name": self.name
		}