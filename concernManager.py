from userManagement import __getUserByEmail
from utils import NotFoundError,getGraph

def addConcernToUser(current, concern):
    title = concern.get('title')
    description = concern.get('description')
    user = __getUserByEmail(current)
    newConcern, = getGraph().create({"title" : title, "description" : description})
    __addConcernToIndex(title, newConcern)
    getGraph().create((user, "CREATES", newConcern))

def __addConcernToIndex(title,newConcern):
    return getGraph().get_or_create_index(neo4j.Node, "Concernss").add("title",title,newConcern)
    
    
def deleteConcern(id):
    concern = getGraph().node(id)
    concern.delete()

def getAllConcerns(email):
    print "getAllConcerns"
    currentUser = __getUserByEmail(email)
    rels = list(getGraph().match(start_node=currentUser, rel_type="CREATES"))
    concerns = []
    for rel in rels:
        concernss.append(rel.end_node.get_properties())
        #print getGraph().node(rel.end_node)
    return concerns

