from uuid import uuid4
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()

def generate_uuid():
    """
    Génère un UUID unique sous forme de chaîne de caractères.

    :return: UUID généré.
    """
    return str(uuid4().hex)

# Modèles de base de données
class User(UserMixin, db.Model):
    """
    Modèle représentant un utilisateur du système.

    Chaque utilisateur est identifié de manière unique par un UUID.
    L'utilisateur dispose d'un nom d'utilisateur et d'un mot de passe haché pour des raisons de sécurité.

    :ivar id: UUID unique pour identifier l'utilisateur.
    :ivar username: Nom d'utilisateur, unique pour chaque utilisateur.
    :ivar hash_password: Mot de passe de l'utilisateur, stocké sous forme hachée pour des raisons de sécurité.
    """
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid, unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    hash_password = db.Column(db.String(80), nullable=False)
    
    def set_password(self, password):
        """
        Définit le mot de passe pour l'utilisateur et le stocke sous forme hachée.

        :param password: Mot de passe en clair à hacher et à stocker.
        """
        self.hash_password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """
        Vérifie si le mot de passe donné correspond au mot de passe haché de l'utilisateur.

        :param password: Le mot de passe à vérifier.
        :return: True si le mot de passe est correct, False sinon.
        """
        return bcrypt.check_password_hash(self.hash_password, password)

class Task(db.Model):
    """
    Modèle représentant une tâche à accomplir.

    La tâche contient un titre, une description optionnelle, un état indiquant si elle est terminée ou non, 
    ainsi qu'une date de création. Chaque tâche est identifiée de manière unique par un UUID.

    :ivar id: UUID unique pour identifier la tâche.
    :ivar title: Titre de la tâche.
    :ivar description: Description détaillée de la tâche (optionnelle).
    :ivar is_completed: Etat de la tâche, indiquant si elle est terminée (True) ou en cours (False).
    :ivar created_at: Date et heure de la création de la tâche.
    """
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid, unique=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
