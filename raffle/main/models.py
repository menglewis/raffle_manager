from raffle import db

class Raffle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return '<Raffle %s>' % self.name

class RaffleEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    quantity = db.Column(db.Integer)
    raffle_id = db.Column(db.Integer, db.ForeignKey('raffle.id'))
    raffle = db.relationship('Raffle', backref='raffle_entries')

    def __repr__(self):
        return '<RaffleEntry %s: %s>' % (self.name, self.quantity)
