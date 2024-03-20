class Book():
    def __init__(self):
        self.name = "No name"
        self.author = "No author"
        self.pageCount = 0
    
    def ShowInfo(self):
        print("Назва " + self.name)
        print("Автор " + self.author)
        print("Кількість сторінок " + str(self.pageCount))
        
class ChronikuNarnii(Book):
    def __init__(self):
        super().__init__()
        self.name = "Chroniku Narnii"
        self.author = "author1"
        self.pageCount = 800
        
class LydunaAmphibia(Book):
    def __init__(self):
        super().__init__()
        self.name = "Lyduna Amphibia"
        self.author = "author2"
        self.pageCount = 600
        
class PodorojGullivera(Book):
    def __init__(self):
        super().__init__()
        self.name = "Podoroj Gullivera"
        self.author = "author3"
        self.pageCount = 700
        
class OstrovuVOkeani(Book):
    def __init__(self):
        super().__init__()
        self.name = "Ostrovu V Okeani"
        self.author = "author4"
        self.pageCount = 600
        
class ZlochunIKara(Book):
    def __init__(self):
        super().__init__()
        self.name = "Zlochun I Kara"
        self.author = "author5"
        self.pageCount = 800
        
class LydunaVKoruchnovomyKostymi(Book):
    def __init__(self):
        super().__init__()
        self.name = "Lyduna V Koruchnovomy Kostymi"
        self.author = "author6"
        self.pageCount = 400
        
class VbuvstvoNaVyluciMorg(Book):
    def __init__(self):
        super().__init__()
        self.name = "Vbuvstvo Na Vyluci Morg"
        self.author = "author7"
        self.pageCount = 500
        
class Fantacy(ChronikuNarnii, LydunaAmphibia):
    def __init__(self):
        super().__init__()
        self.ganre = "Fantacy"
        
    def ShowInfo(self):
        print("Назва " + self.name)
        print("Автор " + self.author)
        print("Кількість сторінок " + str(self.pageCount))
        print("Жанр " + self.ganre)
        
class Adventure(PodorojGullivera, OstrovuVOkeani):
    def __init__(self):
        super().__init__()
        self.ganre = "Adventure"
        
    def ShowInfo(self):
        print("Назва " + self.name)
        print("Автор " + self.author)
        print("Кількість сторінок " + str(self.pageCount))
        print("Жанр " + self.ganre)
        
class Detective(ZlochunIKara, LydunaAmphibia, VbuvstvoNaVyluciMorg):
    def __init__(self):
        super().__init__()
        self.ganre = "Detective"
        
    def ShowInfo(self):
        print("Назва " + self.name)
        print("Автор " + self.author)
        print("Кількість сторінок " + str(self.pageCount))
        print("Жанр " + self.ganre)
        

item1 = Fantacy()
item2 = Adventure()
item3 = Detective()
item1.ShowInfo()
print("")
item2.ShowInfo()
print("")
item3.ShowInfo()
print("")

item4 = ChronikuNarnii()
item5 = Book()
item4.ShowInfo()
print("")
item5.ShowInfo()
print("")