from waitress import serve
import mongoengine as mongo
import falcon
import routes.bookRoutes as bookRoutes
import routes.defaultRoutes as defaultRoutes
import middlewares

app = falcon.API(middleware=[
    middlewares.JSONTranslator()
])

bookRoutes.add(app)
defaultRoutes.add(app)

mongo.connect('bookAPI')

serve(app, host='127.0.0.1', port=5000)
