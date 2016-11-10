import falcon
import json
import sys

class Collection:
    def on_get(self, req, resp):
        try:  
            resp.body = json.dumps({'books': [{'id': 1, 'title': 'title 1'}, {'id': 2, 'title': 'title 2'}]})
        except: 
            resp.status = falcon.HTTP_500
            print sys.exc_info()
    
    def on_post(self, req, resp):
        resp.status = falcon.HTTP_201
        resp.body = json.dumps({'id': 1, 'title': 'title 1'})

class Item:
    def on_get(self, req, resp, bookId):
        print bookId
        resp.body = json.dumps({'id': 1, 'title': 'title 1'})


app = falcon.API()

app.add_route('/api/books', Collection())
app.add_route('/api/books/{bookId}', Item())

from waitress import serve

serve(app, host='127.0.0.1', port=5000)  # it is the same if i use serve(srv3)
