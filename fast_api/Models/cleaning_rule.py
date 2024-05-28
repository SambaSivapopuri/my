from db.db import db
class Designation_the_study:
    def __init__(self, **kwargs) :
        self.data=kwargs
    def save(self):
        db.Designation_the_study.insert_one(self.data)
    @classmethod
    def findall(self):
        return db.Designation_the_study.find()
    @classmethod
    def data_filter(self,**data):
        if data:
            return db.Designation_the_study.find_one(data)
        return {"data":" Check Input value or validations"}