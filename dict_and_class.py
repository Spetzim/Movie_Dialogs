from pymongo import MongoClient

client = MongoClient('mongodb://root:s3cr37@localhost:27027')
db = client.person_db

class Document():
    collection = None
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def save(self):
        return self.collection.insert_one(self.__dict__).inserted_id


class Person(Document):
    collection = db.person_col

class Car(Document):
    collection = db.cars

def main():
    p_dict = {
        'name': 'Asta',
        'age': 34,
        'music': 'Dance',
        'city': 'London'
    }
    p1 = Person(**p_dict)
    p1.save()
    car = {
        'Reg No': 'ABC 123',
        'Brand': 'Volvo'
    }
    c1 = Car(Reg_no='CBA 321', Brand='Opel')
    c1.save()
    #print(p1.__dict__)


if __name__ == '__main__':
    main()