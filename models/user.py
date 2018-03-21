from orator import Model
from orator.orm import has_many
from models.job import *


class User(Model):

    @has_many
    def job(self):
        return Job
