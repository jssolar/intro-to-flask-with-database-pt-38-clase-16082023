from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Task(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean(), default=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "label": self.label,
            "done": self.done
        }