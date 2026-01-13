from flask import Flask
from flask_cors import CORS

def create_app():
    from trivia.routes.categories import categories_bp
    from trivia.routes.questions import questions_bp
    from trivia.routes.scores import scores_bp
    app = Flask(__name__)
    CORS(app) # CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})  # Adjust as needed"}) React app origin

    app.register_blueprint(categories_bp)
    app.register_blueprint(questions_bp)
    app.register_blueprint(scores_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


# To run the app using Flask CLI, use the command:
#flask --app trivia.app:create_app run

# To activate venv: 
# source trivia/Scripts/activate