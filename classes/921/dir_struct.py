import os

p = input("Nome do projeto: ")

pastas = [
    "app/models",
    "app/viewmodels",
    "app/views",
    "templates"
]

arquivos = [
    "app/__init__.py",
    "app/models/cep_model.py",
    "app/viewmodels/cep_viewmodel.py",
    "app/views/cep_view.py",
    "templates/index.html",
    "run.py",
    "config.py"
]

for pasta in pastas:
    os.makedirs(f"{p}/{pasta}", exist_ok=True)

for arquivo in arquivos:
    open(f"{p}/{arquivo}", "w").close()

print("Estrutura MVVM criada.")