from orator import Model
from models.user import User
from orator.orm import belongs_to


class Job(Model):

    @belongs_to('user_id', 'id')
    def user(self):
        return User
