class EmptyError(ValueError):
    pass

class TemaMusical():
    def __init__(self, codigo=None, nombre=None, duracion=0, interprete=None):
        self.codigo = codigo
        self.nombre = nombre
        self.duracion = duracion
        self.interprete = interprete
    
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self,value):
        if value == '':
            raise EmptyError('El codigo no puede estar vacio...')
        else:
            self._codigo = value
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,value):
        if value == '':
            raise EmptyError('El nombre no puede estar vacio...')
        else:
            self._nombre = value
    
    @property
    def duracion(self):
        return self._duracion
    
    @duracion.setter
    def duracion(self,value):
        if value < 0:
            raise ValueError('La duracion no puede ser negativa...')
        else:
            self._duracion = value
    
    @property
    def interprete(self):
        return self._interprete

    @interprete.setter
    def interprete(self,value):
        if value == '':
            raise EmptyError('El interprete no puede estar vacio...')
        else:
            self._interprete = value
    
    def input(self,codigo=False):
        if codigo == False:
            c=input('Ingrese Codigo: ')
            self._codigo=c
        n=input('Ingrese Nombre: ')
        d=int(input('Ingrese Duracion: '))
        i=input('Ingrese Interprete: ')
        self._nombre=n
        self._duracion=d
        self._interprete=i
