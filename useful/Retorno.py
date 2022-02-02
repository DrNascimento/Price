import string


class Retorno:
    name_function = string.whitespace  # nome da função que retornou.
    data = string.whitespace
    message = string.whitespace

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, error):
        self._error = error

    @property
    def function_name(self):
        return self._function_name

    @function_name.setter
    def function_name(self, name):
        self._function_name = name

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    def __init__(self):
        self.error = None
        self.function_name = None
        self.data = None
        self.message = None

