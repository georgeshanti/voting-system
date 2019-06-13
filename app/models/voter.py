from app import db

class Voter(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Unicode(128), nullable=False)
	age = db.Column(db.Unicode(128), nullable=False)
	address = db.Column(db.Unicode(512), nullable=False)
	constituency_id = db.Column(db.Integer, db.ForeignKey('constituency.id'), nullable=False)
	constituency = db.relationship("Constituency", back_populates="voters")
	voted = db.Column(db.Boolean, nullable=False, default=False)

	def dict(self):
		return {
			"id": self.id,
			"name": self.name,
			"age": self.age,
			"address": self.address,
			# "constituency_id": self.constituency.id,
			# "constituency_name": self.constituency.name,
			"voted": self.voted
		}
