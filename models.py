from smartninja_nosql.odm import Model


class User(Model):
    def __init__(self, name, answer, email, password=None, session_token=None, **kwargs):
        self.name = name
        self.email = email
        self.password = password
        self.session_token = session_token
        self.answer = answer
        super().__init__(**kwargs)


