from lxml import etree

class ConfigParser:

    def __init__(self, file_path):
        self.file_path = file_path

    @property
    def config(self):
        if hasattr(self, '_config'):
            return self._config
        self._config = open()
