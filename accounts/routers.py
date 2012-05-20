class AccountRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'accounts':
            return 'accounts'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'accounts':
            return 'accounts'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return False

    def allow_syncdb(self, db, model):
        if db == 'accounts':
            return model._meta.app_label == 'accounts'
        elif model._meta.app_label == 'accounts':
            return False
        return None
