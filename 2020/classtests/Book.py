class Book:

    #constructor method
    def __init__(self, title, pageCount, wordsInPage, author, publisher, publishDate):
        self.title = title
        self.pageCount = pageCount
        self.wordsInPage = wordsInPage
        self.author = author
        self.publisher = publisher
        self.publishDate = publishDate

    def calculateWordCount(self, pageCount, wordsInPage):
        total = pageCount * wordsInPage
        print(total)


#calculate number of words in a book with nb pages & nb words per page
nameOfTheWind = Book("The Name of the Wind", 900, 600, "Pat Rothfuss", "Daw Edition", 2011)
print(nameOfTheWind.pageCount)
nameOfTheWind.calculateWordCount(nameOfTheWind.pageCount, nameOfTheWind.wordsInPage)
