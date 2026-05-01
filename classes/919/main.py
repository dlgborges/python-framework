import os

def criar_arquitetura():
    pastas = [
        './pasta_escola/models',
        './pasta_escola/models/database',
        './pasta_escola/controller',
        './pasta_escola/view',
        './pasta_escola/teste'
    ]


    for pasta in pastas:
        os.makedirs(pasta, exist_ok=True)
        with open(os.path.join(pasta, '__init__.py'), 'w') as f:
            pass
    print('Arquitetura criada')

criar_arquitetura()