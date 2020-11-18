class Kit : 
    """
    number,
    model,
    series,
    yenPrice,
    releaseDate,
    notes
    """

    def __init__(self, args, imageLink, grade, scale):
        self.grade = grade
        self.number = args[0]
        self.model = args[1]
        self.series = args[2]
        self.price = args[3]
        self.releaseYear = args[4]
        self.notes = args[5]
        self.imageLink = imageLink
        self.scale = scale
        
    def json(self):
        if self.imageLink != None :
            return {"id":"test","grade":self.grade,"release_year":self.releaseYear,"name":self.model,"info":{"scale":self.scale,"series":self.series,"notes":self.notes,"image_links":[self.imageLink]}}
        else :
            return {"id":"test","grade":self.grade,"release_year":self.releaseYear,"name":self.model,"info":{"scale":self.scale,"series":self.series,"notes":self.notes,"image_links":[]}}

    def __str__(self):
        return f'{self.grade}-{self.number} : {self.model}, from {self.series}, released {self.releaseYear}, priced at {self.price} yen. {self.notes}\n{self.imageLink}'