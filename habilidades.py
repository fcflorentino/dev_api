from flask_restful import Resource

lista_habilidades = ['Flask', 'PHP', 'Java', 'Python']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades