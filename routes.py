# Using redirect route instead of simple routes since it supports strict_slash
# Simple route: http://webapp-improved.appspot.com/guide/routing.html#simple-routes
# RedirectRoute: http://webapp-improved.appspot.com/api/webapp2_extras/routes.html#webapp2_extras.routes.RedirectRoute
from webapp2 import Route
from webapp2_extras.routes import RedirectRoute
from web import handlers
import utils

secure_scheme = 'https'

_routes = [

    # Show Home page
    RedirectRoute('/', handlers.MainPage, name='main', strict_slash=True),
]

def get_routes():
    return _routes


def add_routes(app):
    if app.debug:
        secure_scheme = 'http'
    for r in _routes:
        app.router.add(r)
