class FileUpload:

    def __init__(self, file):
        self.file = file

    def save_file(self, path):
        # if file is saved succesfull rm content of uploads folder
        return self.file.save(path)  # file is saved to uploads dir
