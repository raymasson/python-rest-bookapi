from waitress import serve
import falcon
import routes.bookRoutes

app = falcon.API()

routes.bookRoutes.add(app)

serve(app, host='localhost', port=5000)
