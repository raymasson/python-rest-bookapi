class Default:
    def on_get(self, req, resp):
        resp.body = 'Welcome to my Python REST API!'
        