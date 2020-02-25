from app.adaptor import file_routes as file
from app.domain.model import Usuario

print('Iniciando')

usuario = Usuario()

usuario.Username = 'nperez'

usuario.Nombre = 'Nicolas'

usuario.Apellido = 'Perez'

file.create_file('nombre.txt', usuario)

