from flask import Flask
from app_package_folder.config import Config

def create_app(config_class_test=Config):
    
    app = Flask(__name__)
    app.config.from_object(config_class_test)

    from app_package_folder.routes import users
    from app_package_folder.errors_handling import bp
    
    app.register_blueprint(users)
    app.register_blueprint(bp)
    
    return app