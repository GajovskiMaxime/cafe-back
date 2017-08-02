from cafe.exceptions.file.file_exception import FileException


class FileFormatException(FileException):

    def __init__(self, file_path, err):
        self.status_code = 400
        self.file_path = file_path
        self.err = err
        self.message = "Bad format for file : {}.".format(self.file_path)

    @property
    def serialize(self):
        return {
            'status':       self.status_code,
            'file_path':    self.file_path,
            'err':          self.err,
            'message':      self.message
        }
