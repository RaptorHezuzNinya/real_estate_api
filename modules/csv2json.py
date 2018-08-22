import csv


class Csv2json:

    def __init__(self, path):
        self.path = path
        self.convert()

    def convert(self):
        with open(self.path) as cfile:
            reader = csv.DictReader(cfile)
            dict_list = []
            for line in reader:
                dict_list.append(line)
            self.dict_list = dict_list

    def get_json(self):
        return self.dict_list
