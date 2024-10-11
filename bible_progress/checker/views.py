from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Book, ReadChapter



def index(request):
    def submit(request):
        if request.method == "POST":
            chapter = request.POST.get("chapter_id")
            book = request.POST.get("book_id")
            return JsonResponse({'status': 'success'})
    
    sub = "Liv"

    chapter = Book.objects.filter()
    if request.method == "POST":
        book_id = request.POST["book_id"]
        chapter = request.POST["chapter_id"]
        chapter_checked = ReadChapter.objects.filter(user_sub=sub, book=book_id, chapter=chapter)
        if chapter_checked:
            chapter_checked.delete()
            chapter_checked = None
        else: 
            book = Book.objects.filter(id=book_id).first()
            chapter_checked = ReadChapter(user_sub=sub, book=book, chapter=chapter)
            chapter_checked.save()
            
    # most_read = ReadChapter.most_read_books()
    # print(most_read)
    # for entry in most_read:
    #     for key in entry.items():
    #         most_read_list = []
    #         most_read_list.append(key)
    #         print(most_read_list)
    #     return most_read_list



    
    context = {
        "session" : request.session.get("user"),
        "total_chapter_count" : ReadChapter.total_percentage(),
        "most_read" : ReadChapter.most_read_books(),
        "books" : [
            {
                "id": book.id,
                "book_chapter_percentage" : ReadChapter.book_percentage(book.id),
                "name": book.name,
                "chapters": 
                    [ 
                        {
                            "number": i, 
                            "chapter_checked": 
                                "checked"
                                if ReadChapter.objects.filter(chapter=i, book=book, user_sub=sub).count() > 0
                                else "",                            
                        }       
                        for i in
                        range(1, (book.chapters_number)+1)
                    ],
            }
            for book in Book.objects.order_by("id")
        ],

    }
    return render(request, "index.html", context)