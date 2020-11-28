class Kit : 

    def __init__(
        self, 
        id, 
        model, 
        series, 
        release_year, 
        notes, 
        imageLink, 
        grade, 
        scale, 
        pbandai,
        variation
    ):
        self.__grade = grade
        self.__model = model
        self.__series = series
        self.__releaseYear = release_year
        self.__notes = notes
        self.__imageLink = imageLink
        self.__scale = scale
        self.__pbandai = pbandai
        self.__id = id
        self.__variation = variation
        
    def __series_to_wiki_link(self):
        return f'https://gundam.fandom.com/wiki/{self.__series.replace(" ","_")}' if self.__series != None else None

    def json(self):
        root = {
            "id":self.__id,
            "grade":self.__grade,
            "release-year":self.__releaseYear,
            "name":self.__model,
            "p-bandai":self.__pbandai,
            "series":self.__series if self.__series != "N/A" else None,
            "series-wiki": self.__series_to_wiki_link(),
            "info":{
                "scale":self.__scale
            }
        }
        if self.__notes != "" : root["info"]["notes"] = self.__notes
        if self.__imageLink != None : root["info"]["image-link"] = self.__imageLink 
        if self.__variation != None : root["info"]["variation"] = self.__variation  
        return root