from models import Todo, db
from faker import Faker
from app import app

fake = Faker()

with app.app_context():
    Todo.query.delete()
    db.session.commit()

    todo = []

    for item in range(10):
        does = Todo(
            title = f'The {fake.sentence()}',
            completed = fake.boolean()
        )
        todo.append(does)

        db.session.add(does)
        db.session.commit()