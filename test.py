from orator import Model
from connect import db
from models.job import Job
from models.user import User

Model.set_connection_resolver(db)

person = User.where('id',  3).first()

print(person.name)


jobs = Job.all()
for job in jobs:
    print(job.user.name)
    print(job.name)

