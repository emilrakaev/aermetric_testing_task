class GeneralException(Exception):
    default_message = 'Something went wrong'

    def __init__(self, message=None):
        self.message = message if message else self.default_message


class FileParseException(GeneralException):
    default_message = 'Problem with parse'


class GenerateStatisticException(GeneralException):
    default_message = 'Problem with generate statistic'
