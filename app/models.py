from . import db


class Disciplina(db.Model):
    __tablename__ = 'disciplinas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True)
    professores = db.relationship('Professor', backref='disciplina',
                                  lazy='dynamic')

    def __repr__(self):
        return '<Disciplina %r>' % self.nome


class Professor(db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), index=True)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplinas.id'))

    def __repr__(self):
        return '<Professor %r>' % self.nome
