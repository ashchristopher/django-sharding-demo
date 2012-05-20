class RecordRouter(object):

    def db_for_read(self, model, **hints):
        return None

    def db_for_write(self, model, **hints):
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return False

    def allow_syncdb(self, db, model):
        if db.startswith('shard'):
            return model._meta.app_label == 'records'
        elif model._meta.app_label == 'records':
            return False
        return None
