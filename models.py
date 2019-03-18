from smartninja_nosql.odm import Model


class User(Model):
    def __init__(self, name, email, password=None, session_token=None, **kwargs):
        self.name = name
        self.email = email
        self.password = password
        self.session_token = session_token
        super().__init__(**kwargs)