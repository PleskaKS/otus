from enum import Enum


class FileType(Enum):
    """Объявляем класс "FileType", который содержит возможные варианты типов файлов """
    VIDEO = 1
    """видеофайл"""
    AUDIO = 2
    """аудиофайл"""
    IMAGE = 3
    """изображение"""


class MediaFile:
    """Объявляем класс "MediaFile", который будет родтельским и содержит атрибуты,
    относящиеся к файлу независимо от его типа"""

    def __init__(self, file_type, name, size, created, owner, form):
        """Инициализируем атрибуты, которые будут определять состояние объекта, созданого при помощи конструтора
        класса """
        self.file_type = file_type
        """тип файла"""
        self.name = name
        """имя файла"""
        self.size = size
        """размер файла"""
        self.created = created
        """дата создания"""
        self.owner = owner
        """владелец"""


class AudioFile(MediaFile):
    """Класс-наследник от класса "MediaFile", в котором дополнительно инициализируем атрибуты:
    длительность аудиио файла и аудиоканал"""

    def __init__(self, time, file_type, name, size, created, owner, form, channel):
        """вызываем методы базого класса"""
        super().__init__(file_type, name, size, created, owner, form)
        """добавляем аргументы, характерные для аудифайла"""
        self.time = time
        self.channel = channel


class VideoFile(MediaFile):
    """Класс-наследник от класса "MediaFile", в котором дополнительно инициализируем атрибуты:
    разрешение, кодирование, местоположение видеосьемки"""

    def __init__(self, file_type, name, size, created, owner, form, resolution, codecs, location=None):
        """вызываем методы базого класса"""
        super().__init__(file_type, name, size, created, owner, form)
        self.resolution = resolution
        self.codecs = codecs
        self.location = location


class PhotoFile(MediaFile):
    """Класс-наследник от класса "MediaFile", в котором дополнительно инициализируем атрибуты:
    прозрачность, глубина"""

    def __init__(self, file_type, name, size, created, owner, form, depth, visibility=None):
        super().__init__(file_type, name, size, created, owner, form)
        """вызываем методы базого класса"""
        self.visibility = visibility
        self.depth = depth


class LocalStorage:
    """Объявляем класс с методами для локального хранилища с атрибутом путь"""
    def __init__(self, path_file):
        self.path = path_file

    def save(self, file):
        """Этот метод сохраняет файл в локальное хранилище, с аргументом - файл"""

    def delete(self, path):
        """Этот метод удаляет файл из локального хранилища, необходимо передать агрумент - путь к файлу"""

    def update(self, file, path):
        """Этот метод обновяет файл, принимает аргументы: файл, путь к файлу"""


class ConnectStorage:
    """Объявляем класс для работы с удаленным хранилищем, в инициализуем необходимы для подлючения аргументы:
    урл, порт, логин и пароль"""
    def __init__(self, url, port, login, password):
        self.url = url
        self.port = port
        self.login = login
        self.password = password

    def connect(self):
        """Метод создает подкдлючение к удаленному хранилищу"""

    def disconect(self):
        """Метод закрывает подкдлючение к удаленному хранилищу"""

    def save(self, file, path):
        """Этот метод позволит сохранить файл в удаленном хранилище, принимает аргументы: сам файл и путь"""

    def delete(self, path):
        """Этот метод позволит удалить файл в удаленном хранилище, принимает аргумент: путь к файлу"""

    def update(self, file, path):
        """Этот метод обновляет файл в удаленном хранилище, принимает аргументы: файл, путь"""

    def convert(self, file_type, path):
        """Этот метод конвертирует файл в удаленном хранилище, принимает аргументы: формат, в который надо
        конвектировать файл и путь к файлу"""


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
    """Объявляем класс "FileStorage", который будет содержит функции,
    относящиеся к хранилищу файлов"""
    def __init__(self, url, port, login, password):
        """подключение к хранилиу по урлу с логопассом"""
        self.connect = ConnectStorage(url, port, login, password)
        self.connect.connect()

    def __del__(self):
        """разрыв соединения подключения к хранилиу"""
        self.connect.disconect()

    def save(self, file, path):
        """метод позволит сохранить файл в хранилище"""
        prepare_file = self._prepare_file(file)
        self.connect.save(prepare_file, path)

    def delete(self, path):
        """метод позволит удалить файл из хранилища """
        self.connect.delete(path)

    def update(self, file, path):
        """изменить файл в хранилище"""
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
