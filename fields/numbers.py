class Field(object):

    def __init__(self, maximum=None, minimum=None):
        self.maximum = maximum
        self.minimum = minimum


class IntField(Field):
    name = 'Integer Field'
    sql_type = 'integer'
    null = False

    def sql(self, field_name):
        return sql_type + ' CHECK ' + '(' + field_name + '<' + self.maximum


