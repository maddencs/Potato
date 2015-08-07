from . import Field


class OneToOne(Field):
    constraints = list()
    
    def __init__(self, model, required=False):
        super().__init__()
        try:
            self.model = model
            self.required = required
        except:
            raise Exception('OneToOne field requires a model!')

        if(required):
           self.constraints.append('NOT NULL')
        else:
            self.constraints.append('NULL')

    def sql(self):
        return self.model.__name__ + '_id integer ' + ' '.join(self.constraints) + ' REFERENCES ' + self.model.__name__
