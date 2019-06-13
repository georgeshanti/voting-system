from app import db

class Constituency(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Unicode(128), nullable=False)
	voters = db.relationship("Voter", back_populates="constituency")
	parties = db.relationship(
        "PartyConstituencyAssociation",
        back_populates="constituency")

	def dict(self):
		return {
			"id": self.id,
			"name": self.name
		}