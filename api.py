import os


class ChangeDir:
    def __init__(self, path):
        self.path = path
        self._cwd = None

    def __enter__(self):
        self._cwd = os.getcwd()
        os.chdir(self.path)

    def __exit__(self, *exc):
        os.chdir(self._cwd)
