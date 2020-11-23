class Series:

    def __init__(self,id,name,wikiLink):
        self.id = id
        self.name = name
        self.wikiLink = wikiLink

    def json(self):
        return {
            "id":self.id,
            "name":self.name,
            "wiki-link":self.wikiLink
        }