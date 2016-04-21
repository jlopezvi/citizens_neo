from py2neo import neo4j
class NotFoundError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)

def getGraph() :
     return neo4j.GraphDatabaseService("http://127.0.0.1:7474/db/data")
