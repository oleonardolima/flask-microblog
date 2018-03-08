from flask import Flask

app = Flask(__name__)
#app variable is an instance of class Flask, it's a member of the app package created.
#__name__ variable is a predefined variable that is the name of the module used.

from app import routes
#The routes module needs to imports the app variable defined here, putting one reciprocal imports at the bottom avoids the errors of mutual references
