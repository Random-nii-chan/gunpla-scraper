class Kit : 
    """
    number,
    model,
    series,
    yenPrice,
    releaseDate,
    notes
    """

    def __init__(self, args, imageLink, grade):
        self.grade = grade
        self.number = args[0]
        self.model = args[1]
        self.series = args[2]
        self.yenPrice = args[3]
        self.releaseDate = args[4]
        self.notes = args[5]
        self.imageLink = imageLink

    def __str__(self):
        return f'{self.grade}-{self.number} : {self.model}, from {self.series}, released {self.releaseDate}, priced at {self.yenPrice} yen. {self.notes}\n.\n{self.imageLink}'