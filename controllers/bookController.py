import falcon
import json

class Collection:
    def on_get(self, req, resp):
        try:  
            resp.body = json.dumps({'books': [{'id': 1, 'title': 'title 1'}, {'id': 2, 'title': 'title 2'}]})
        except Exception as ex: 
            resp.status = falcon.HTTP_500
            raise falcon.HTTPError(falcon.HTTP_500, 'Error', ex.message)
    
    def on_post(self, req, resp):
        resp.status = falcon.HTTP_201
        resp.body = json.dumps(req.stream.read())
        
class Item:
    def on_get(self, req, resp, bookId):
        resp.body = json.dumps({'id': 1, 'title': 'title 1'})

    def on_put(self, req, resp, bookId):
        try:
            resp.body = json.dumps({'id': 1, 'title': 'title 1'})
        except Exception as ex: 
            resp.status = falcon.HTTP_500
            raise falcon.HTTPError(falcon.HTTP_500, 'Error', ex.message)

    def on_delete(self, req, resp, bookId):
        try:
            resp.status = falcon.HTTP_204
            resp.body = 'Removed'
        except Exception as ex: 
            resp.status = falcon.HTTP_500
            raise falcon.HTTPError(falcon.HTTP_500, 'Error', ex.message)