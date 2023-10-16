import tempfile


class ContextManager:
    def __init__(self):
        self.file = tempfile.TemporaryFile(mode='r+')

    def __enter__(self):
        return self

    def repeat(self):
        self.file.seek(0)
        content = self.file.read()
        self.file.write(content)

    def write(self, msg):
        self.file.seek(0)
        content = self.file.read()
        self.file.seek(0)
        self.file.write(msg)
        self.file.write(content)

    def show(self):
        self.file.seek(0)
        print(self.file.read())

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.seek(0)
        print(f"Количество символов: {len(self.file.read())}")
        self.file.close()
