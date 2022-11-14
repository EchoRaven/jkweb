from flask import Flask
import config
from exts import db, mail
from flask_cors import CORS
from blueprints import user_bp, home_bp, write_bp, comment_bp, search_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config)
CORS(app, supports_credentials=True)
db.init_app(app)
mail.init_app(app)
app.register_blueprint(user_bp)
app.register_blueprint(home_bp)
app.register_blueprint(write_bp)
app.register_blueprint(comment_bp)
app.register_blueprint(search_bp)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
