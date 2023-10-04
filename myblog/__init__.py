
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
app = Flask(__name__)

def create_app():
    # Cargar configuraciones
    app.config.from_object('config.DevelopmentConfig')
    # Inicializar la base de datos
    init_db(app, db)
    # Configurar Flask-Migrate
    migrate = Migrate(app, db)
    return app

#Importar las views
from myblog.views.auth import auth
app.register_blueprint(auth)

from myblog.views.blog import blog
app.register_blueprint(blog)

def init_db(app, db):
    db.init_app(app)
    with app.app_context():
        db.create_all()


from myblog.views.comentario import comentario
app.register_blueprint(comentario)
