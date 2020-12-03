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
        if self.__series != None:
            return f'https://gundam.fandom.com/wiki/{self.__series.replace(" ","_")}'
        else:
            return None

    def json(self):
        return {
            "id":self.__id,
            "release-year":self.__releaseYear,
            "name":self.__model,
            "p-bandai":self.__pbandai,
            "grade":self.__grade,
            "scale":self.__scale,
            "series": {
                "name":self.__series if self.__series != "N/A" else None,
                "wiki-link":self.__series_to_wiki_link()
            },
            "info":{
                "variation":self.__variation,
                "notes": self.__notes if self.__notes != "" else None,
                "image-link":self.__imageLink
            }
        }