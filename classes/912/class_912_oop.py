class Celular:
    def __init__(self, modelo='Modelo padrão'):
        self.modelo = modelo

    def display(self):
        print(self.modelo)

c = Celular()
c.display()