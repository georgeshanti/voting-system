from app import db
import app.models as models
from app.models.party import PartyConstituencyAssociation

db.create_all()

voter_1 = models.Voter(name="Rohit Varma", age=24, address="Flat no. 12H, Twilight towers, Ernakulam")
voter_2 = models.Voter(name="Thomas Philip", age=40, address="Flat no. 13H, Twilight towers, Ernakulam")
voter_3 = models.Voter(name="Ivan Abraham", age=32, address="VNRA 24, Vazhakkala")
voter_4 = models.Voter(name="VP Devassia", age=54, address="Govt. Model Engg College")
voter_5 = models.Voter(name="Vinu Thomas", age=18, address="Karimakkad")
voter_6 = models.Voter(name="George Punoose", age=42, address="Opp. High Court")
voter_7 = models.Voter(name="Pareedh Muhammed", age=65, address="Chembummukku")

party_1 = models.Party(name="National Party 1")
party_2 = models.Party(name="National Party 2")
party_3 = models.Party(name="National Party 3")

constituency_1 = models.Constituency(name="Ernakulam")
constituency_2 = models.Constituency(name="Alleppey")

constituency_1.voters.append(voter_1)
constituency_1.voters.append(voter_3)
constituency_1.voters.append(voter_5)
constituency_1.voters.append(voter_7)
a_1 = PartyConstituencyAssociation()
a_1.party = party_1
constituency_1.parties.append(a_1)
a_2 = PartyConstituencyAssociation()
a_2.party = party_2
constituency_1.parties.append(a_2)
a_3 = PartyConstituencyAssociation()
a_3.party = party_3
constituency_1.parties.append(a_3)

constituency_2.voters.append(voter_2)
constituency_2.voters.append(voter_4)
constituency_2.voters.append(voter_6)
a_4 = PartyConstituencyAssociation()
a_4.party = party_1
constituency_2.parties.append(a_4)
a_5 = PartyConstituencyAssociation()
a_5.party = party_3
constituency_2.parties.append(a_5)

db.session.add(voter_1)
db.session.add(voter_2)

db.session.add(constituency_1)
db.session.add(constituency_2)

db.session.add(party_1)
db.session.add(party_2)
db.session.add(party_3)

db.session.commit()
