import controllers.bookController

def add(app): 
    app.add_route('/api/books', controllers.bookController.Collection())
    app.add_route('/api/books/{bookId}', controllers.bookController.Item())
