from . import Field

class IntField(Field):
    name = 'Integer Field'
    sql_type = 'integer'
    null = False

    def sql(self, field_name):
        return self.sql_type + ' CHECK ' + '(' + field_name + '<' + str(self.maximum) + ')'


