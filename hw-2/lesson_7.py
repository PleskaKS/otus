from enum import Enum


class FileType(Enum):
    VIDEO = 1
    AUDIO = 2
    IMAGE = 3


class MediaFile:
    def __init__(self, file_type, name, size, created, owner, form):
        self.file_type = file_type
        self.name = name
        self.size = size
        self.created = created
        self.owner = owner
        self.form = form


class AudioFile(MediaFile):

    def __init__(self, time, file_type, name, size, created, owner, form, channel):
        super().__init__(file_type, name, size, created, owner, form)
        self.time = time
        self.channel = channel


class VideoFile(MediaFile):

    def __init__(self, file_type, name, size, created, owner, form, resolution, codecs, location=None):
        super().__init__(file_type, name, size, created, owner, form)
        self.resolution = resolution
        self.codecs = codecs
        self.location = location


class PhotoFile(MediaFile):

    def __init__(self, file_type, name, size, created, owner, form, depth, visibility=None):
        super().__init__(file_type, name, size, created, owner, form)
        self.visibility = visibility
        self.depth = depth


class LocalStorage:
    def __init__(self, path_file):
        self.path = path_file

    def save(self, file):
        """сохранить файл"""

    def delete(self, path):
        """удалить файл"""

    def update(self, file, path):
        """обновить файл"""


class ConnectStorage:
    def __init__(self, url, port, login, password):
        self.url = url
        self.port = port
        self.login = login
        self.password = password

    def connect(self):
        """создает подкдлючение к удаленному хранилищу"""

    def disconect(self):
        """закрывает подкдлючение к удаленному хранилищу"""

    def save(self, file, path):
        """сохранить файл"""

    def delete(self, path):
        """удалить файл"""

    def update(self, file, path):
        """обновить файл"""

    def convert(self, file_type, path):
        """конвертировать файл"""


class FileConverter:
    @staticmethod
    def convert(file_type: FileType, file):
        """конвертировать файл в указанный в параметре тип"""
        if file.file_type == FileType.VIDEO:
            return VideoFileUtils.convert(file, file_type)
        elif file.file_type == FileType.AUDIO:
            return AudioFileUtils.convert(file, file_type)
        elif file.file_type == FileType.IMAGE:
            return PhotoFileUtils.convert(file, file_type)
        else:
            Exception("Wrong type file!!!")


class VideoFileUtils:
    @staticmethod
    def prepare(file):
        """подготавливаем видео-файл под нужный формат, разрешение и размер"""
        return file

    @staticmethod
    def convert(file, file_type):
        """конвертируем файл в нужный тип"""
        if file_type == FileType.VIDEO:
            return file
        else:
            Exception("Wrong type file!!!")


class AudioFileUtils:
    @staticmethod
    def prepare(file):
        """подготавливаем аудио-файл под нужный формат, разрешение и размер"""
        return file

    @staticmethod
    def convert(file, file_type):
        """конвертируем файл в нужный тип"""
        if file_type == FileType.VIDEO:
            return file
        else:
            Exception("Wrong type file!!!")


class PhotoFileUtils:
    @staticmethod
    def prepare(file):
        """подготавливаем фото-файл под нужный формат, разрешение и размер"""
        return file

    @staticmethod
    def convert(file, file_type):
        """конвертируем файл в нужный тип"""
        if file_type == FileType.VIDEO:
            return file
        else:
            Exception("Wrong type file!!!")


class FileStorage:
    def __init__(self, url, port, login, password):
        self.connect = ConnectStorage(url, port, login, password)
        self.connect.connect()

    def __del__(self):
        self.connect.disconect()

    def save(self, file, path):
        prepare_file = self._prepare_file(file)
        self.connect.save(prepare_file, path)

    def delete(self, path):
        self.connect.delete(path)

    def update(self, file, path):
        prepare_file = self._prepare_file(file)
        self.connect.update(prepare_file, path)

    @staticmethod
    def _prepare_file(file: MediaFile):
        """Приводим файл к необходимым параметрам разрешения, максимального размера"""
        if file.file_type == FileType.VIDEO:
            return VideoFileUtils.prepare(file)
        elif file.file_type == FileType.AUDIO:
            return AudioFileUtils.prepare(file)
        elif file.file_type == FileType.IMAGE:
            return PhotoFileUtils.prepare(file)
        else:
            Exception("Wrong type file!!!")
