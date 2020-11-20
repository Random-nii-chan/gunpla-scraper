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
        self.grade = grade
        self.model = model
        self.series = series
        self.releaseYear = release_year
        self.notes = notes
        self.imageLink = imageLink
        self.scale = scale
        self.pbandai = pbandai
        self.id = id
        self.variation = variation
        
    def json(self):
        root = {
            "id":self.id,
            "grade":self.grade,
            "release-year":self.releaseYear,
            "name":self.model,
            "p-bandai":self.pbandai,
            "info":{
                "scale":self.scale,
                "series":self.series
            }
        }
        if self.notes != "" : root["info"]["notes"] = self.notes
        if self.imageLink != None : root["info"]["image-link"] = self.imageLink 
        if self.variation != None : root["info"]["variation"] = self.variation  
        return root