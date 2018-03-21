from orator.migrations import Migration


class CreateJobsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('jobs') as table:
            table.increments('id')
            table.string('name')
            table.integer('user_id').unsigned()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('jobs')
