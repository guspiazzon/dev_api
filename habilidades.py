from flask_restful import Resource


lista_habilidades = ['Python', 'Java', 'Flask', 'Django',
               'PHP', 'HTML', 'CSS', 'VB', 'Delphi'
               'Angular', 'Kotlin', 'Ruby']
class Habilidades(Resource):
    def get(self):
        return lista_habilidades
