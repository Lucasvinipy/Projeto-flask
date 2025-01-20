from flask import Flask 
from routes.home import home_route
from routes.clientes import cliente_route

app = Flask(__name__)
app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix = '/clientes')

app.run(debug=True)