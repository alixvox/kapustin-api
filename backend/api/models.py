from api.extensions import db

class Works(db.Model):
    __tablename__ = 'works'

    opus_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    recording_exists = db.Column(db.Boolean, nullable=False)
    length = db.Column(db.String, nullable=True)
    youtube_link = db.Column(db.String, nullable=True)
    num_instruments = db.Column(db.Integer, nullable=False)
    instruments = db.Column(db.String, nullable=True)
    num_sections = db.Column(db.Integer, nullable=False)
    section_names = db.Column(db.String, nullable=True)
    referenced_work = db.Column(db.String, nullable=True)

    def json(self):
        return {
            'opus_id': self.opus_id,
            'title': self.title,
            'type': self.type,
            'year': self.year,
            'recording_exists': self.recording_exists,
            'length': self.length,
            'youtube_link': self.youtube_link,
            'num_instruments': self.num_instruments,
            'instruments': self.instruments,
            'num_sections': self.num_sections,
            'section_names': self.section_names,
            'referenced_work': self.referenced_work
        }

class User(db.Model):
    __tablename__ = 'users'

    userID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def json(self):
        return {
            'userID': self.userID,
            'username': self.username,
            'email': self.email
        }
