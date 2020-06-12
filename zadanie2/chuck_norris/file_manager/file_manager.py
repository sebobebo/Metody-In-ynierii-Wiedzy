class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def update_file(self, text_data):
        f = open(self.file_name, 'a')
        f.write(text_data)
        f.close()

    def read_file(self):
        f = open(self.file_name, 'r')
        text = f.read()
        f.close()
        return text