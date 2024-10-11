from django.db import models
import operator

# Create your models here.
from django.db import models

# Create your models here.

bible_chapters = 1189

class Main(models.Model):
    """ definition of shape of model. """
    name = models.CharField(max_length=50)
    
    def  __str__(self) -> str:
        return f"({self.id}) {self.name}"

class Book(models.Model):
    """ book values """
    name = models.CharField(max_length=50)
    chapters_number = models.IntegerField()
    

        
        
    def  __str__(self) -> str:
        return f"({self.id}) {self.name} {self.chapters_number}"
    
class ReadChapter(models.Model):
    """ which chapters has the user read???"""
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    chapter = models.IntegerField()
    user_sub = models.CharField(max_length=100, default="") 
    
    
    
    def total_percentage():
        chapter_count = ReadChapter.objects.count()
        total_chapters = chapter_count / bible_chapters
        total_chapter_percentage = int(total_chapters*100)

        return total_chapter_percentage
    
    def book_percentage(book_id):
        sub = "Liv"
        book = Book.objects.filter(id=book_id).first()
        count_of_chapters_read_in_this_book = ReadChapter.objects.filter(book=book_id, user_sub=sub).count()
        chapters = book.chapters_number
        book_chapter_percentage = int((count_of_chapters_read_in_this_book*100) / chapters)
        return book_chapter_percentage


    def most_read_books():
        query_books=ReadChapter.objects.values("book__name").annotate(count=models.Count("book")).order_by("-count")
        result = [{x['book__name']: x['count']} for x in query_books.all()[:3]]
        return result
                    
    

        
        
    
class User():
    def __init__(self) -> None:
        self.name = models.CharField(max_length=50)
        # self.chapter_progress = models.IntegerField()

        
    

class Maths(Book, User):
    def __init__(self, name, chapters, chapter) -> None:
        super().__init__(name, chapters, chapter)
        
    
        
    
    def book_progress():
        book_progress = Book.chapters_number / Book.chapter_progress
        
    def bible_progress():
        for book in Book.objects:
            bible_progress = bible_chapters / User.chapter_progress
        print(bible_progress)


class Checkbox():
    def __init__(self, book, chapter) -> None:
        self.name = book
        self.chapter = chapter
