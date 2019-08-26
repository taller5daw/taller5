import os
import sys
import django

# This is needed for Django to let us use its capabilities from here
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TallerGrup5.settings")
django.setup()

from libro.models import Autor, Libro, Autor_Libro

# Register to manage repeated entities (if any)
book_titles = set()
author_names = set()
books_authors = dict()

data_path = sys.argv[1]

with open(data_path, 'r', encoding='utf-8') as file:
    file.readline() # skip the header: titulo|autores|isbn|calificacion_promedio
    for line in file:
        line = line.strip()
        title, authors, isbn, mean_rate = line.split('|')
        authors = authors.split('-')
        mean_rate = float(mean_rate)

        if title not in book_titles:
            book_to_save = Libro()
            book_to_save.title = title
            book_to_save.isbn = isbn
            book_to_save.mean_rate = mean_rate
            book_to_save.save()
            book_titles.add(title)
        else:
            book_to_save = Libro.objects.filter(title=title)[0]
        
        for author in authors:
            if author not in author_names:
                author_to_save = Autor()
                author_to_save.nombre = author_to_save.apellido = author
                author_to_save.save()
                author_names.add(author)
            else:
                author_to_save = Autor.objects.filter(nombre=author)[0]
            
            books_authors[title] = books_authors.get(title, set())
            
            if author not in books_authors[title]:
                author_book_to_save = Autor_Libro()
                author_book_to_save.id_libro = book_to_save
                author_book_to_save.id_autor = author_to_save
                author_book_to_save.save()
                books_authors[title].add(author)
