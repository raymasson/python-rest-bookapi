import controllers.defaultController

def add(app): 
    app.add_route('/', controllers.defaultController.Default())