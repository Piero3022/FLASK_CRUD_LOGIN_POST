from datetime import datetime
from myblog import db

class Coment(db.Model):
    __tablename__ = 'coments'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, author, body, post_id) -> None:
        self.author = author or 'Foraneo'
        self.body = body
        self.post_id = post_id

    def __repr__(self) -> str:
        return f'Coment: {self.title}'
