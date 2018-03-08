from app import app

#The "@app.route()" below are decorators(Python feature), a decorator modifies the function that follows it.
@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!"
