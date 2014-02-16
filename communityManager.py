from utils import NotFoundError

def saveCommunity(community):
    try:
       __getCommunity(community)
       app.logger.debug("community %s already exists" % community)
       return "Community %s already exists" % community
    except NotFoundError as e:
       __newCommunity(community)
       return "Community %s was successfully added" % community

def __getCommunity(communityName):
    communityFound = __getCommunityIndex().get("name", communityName)
    if communityFound :
         return communityFound[0]
    raise NotFoundError("Community named %s does not exist" % communityName)

def __addToUsersIndex(email, newUser) :
     getGraph().get_or_create_index(neo4j.Node, "Users").add("email", email, newUser)

def __getCommunityIndex(name, newCommunity):
    get_or_create_index(neo4j.Node, "Communities").add("name", name, newCommunity)
