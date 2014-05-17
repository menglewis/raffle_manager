import random
from raffle import db

class Raffle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return '<Raffle %s>' % self.name

    def get_winner(self):
        entries = []
        if self.raffle_entries:
            for entry in self.raffle_entries:
                entries.extend((entry.name,)*entry.quantity)
            return random.choice(entries)
        return None

class RaffleEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    quantity = db.Column(db.Integer)
    raffle_id = db.Column(db.Integer, db.ForeignKey('raffle.id'))
    raffle = db.relationship('Raffle', backref='raffle_entries')

    def __repr__(self):
        return '<RaffleEntry %s: %s>' % (self.name, self.quantity)
