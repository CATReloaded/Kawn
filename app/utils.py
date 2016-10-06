import peewee


def get_db(name, engine):
    """return a database instance using provided engine"""
    engine_class = getattr(peewee, engine)
    return engine_class(name)
