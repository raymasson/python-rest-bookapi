import falcon
import json
from models.bookModel import Book

class Collection:
    def on_get(self, req, resp):
        try:  
            resp.body = Book.objects.all().to_json()
        except Exception as ex: 
            resp.status = falcon.HTTP_500
            raise falcon.HTTPError(falcon.HTTP_500, 'Error', ex.message)
    
    def on_post(self, req, resp):
        data = req.context['data']
        book = Book(**data).save()
        resp.body = book.to_json()
        resp.status = falcon.HTTP_201
        
class Item:
    def on_get(self, req, resp, bookId):
        resp.body = Book.objects(id=bookId).to_json()

    def on_put(self, req, resp, bookId):
        try:
            data = req.context['data']
            data['id'] = bookId
            book = Book(**data).save()
            resp.body = book.to_json()
        except Exception as ex: 
            resp.status = falcon.HTTP_500
            raise falcon.HTTPError(falcon.HTTP_500, 'Error', ex.message)

    def on_delete(self, req, resp, bookId):
        try:
            Book.objects(id=bookId).delete()
            resp.status = falcon.HTTP_204
            resp.body = 'Removed'
        except Exception as ex: 
            resp.status = falcon.HTTP_500
            raise falcon.HTTPError(falcon.HTTP_500, 'Error', ex.message)