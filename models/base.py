from  models import Service
from db.connect import mysql
from datetime import datetime

class Base:
  def __init__(self, **kwargs):
    self.table = kwargs['table']

  def sql(self, query):
    return mysql(query)

  def all(self, sup=""):
    return mysql("SELECT * FROM %s %s", (self.table, sup))

  def find(self, id):
    data = yield from mysql("SELECT * FROM %s WHERE id=%s", (self.table, id))
    for d in data:
      datum = d
    return datum

  def create(self, data):
    value = ""
    for d in data:
      value += "%s='%s'," % (d, data[d])
    value += "created_at='%s'," % datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    value += "updated_at='%s';"% datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    print("INSERT INTO", self.table, "SET", value)
    return mysql("INSERT INTO %s SET %s", (self.table, value))

  def update(self, id, data):
    value = ""
    for d in data:
      value += "%s='%s'," % (d, data[d])
    value += "updated_at='%s';"% datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    print(value)
    return mysql("UPDATE %s SET %s WHERE id=%s", (self.table, value, id))

