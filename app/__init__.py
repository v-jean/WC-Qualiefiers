from flask import Flask
from config import config_dict

def app_factory(mode_config):
    app = Flask(__name__)
    app.config.from_object(config_dict[mode_config])
    app.template_folder = "html"

    from .main import main_bp
    app.register_blueprint(main_bp)

    return app