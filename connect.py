from orator import DatabaseManager, Model

config = {
    'sqlite': {
        'driver': 'sqlite',
        'database': 'jobs.db',
        'prefix': ''
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)


