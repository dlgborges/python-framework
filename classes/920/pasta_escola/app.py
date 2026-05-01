from flask import Flask
from controllers.tarefa_controllers import tarefa_bp

app = Flask(__name__, template_folder='views/templates', static_folder='static')
app.register_blueprint(tarefa_bp)

if __name__ == '__main__':
    app.run(debug=True)