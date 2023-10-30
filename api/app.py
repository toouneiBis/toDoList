from flask import Flask
import api.routes as routes
import os
from api.models import db, bcrypt, User
from flask_login import LoginManager

# Chemin absolu du dossier courant
basedir = os.path.abspath(os.path.dirname(__file__))

# Initialisation de l'application Flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialisation des extensions
db.init_app(app)
bcrypt.init_app(app)

# Configuration du gestionnaire de connexion
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    """
    Charge un utilisateur à partir de l'ID utilisateur.

    :param user_id: ID de l'utilisateur à charger.
    :return: Retourne l'objet utilisateur correspondant à l'ID.
    """
    return User.query.get(user_id)

with app.app_context():
    """
    Contexte d'application pour effectuer des opérations sur la base de données.
    """
    print('table created')
    db.create_all()
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print('admin user created')

# Initialisation des routes
routes.init_app(app)

if __name__ == '__main__':
    """
    Point d'entrée principal de l'application.
    """
    app.run(debug=True)
