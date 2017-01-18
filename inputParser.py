import csv

class inputParser():
    def __init__ (self, inputfile):
        with open(inputfile) as csvfile:
            reader = csv.DictReader(csvfile,delimiter=';')
            self.fieldnames = reader.fieldnames
            self.rows = list(reader)

    def getKeys(self):
        return self.fieldnames

    def getValue(self,rownumber, key):
        if rownumber < len(self.rows):
            return self.rows[rownumber][key]

    def isElemetLeft(self,rownumber):
        if rownumber < len(self.rows) -1 :
            return 1
        else:
            return 0

