from django.shortcuts import render,redirect
from django.db import models
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from django.conf import settings
from django.conf.urls.static import static
import os
import json
        
def load_data():
    try:
        with open('books.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"data": {"books": []}}

def save_data(data):
    with open('books.json', 'w') as file:
        json.dump(data, file, indent=2)
        

def home(request):
    mydat = load_data()
    data = mydat["data"]["books"]
    return render(request,'home.html',{'data':data})

def getbooks(request):
    mydat = load_data()
    data = mydat["data"]["books"]
    return JsonResponse(data, safe=False)

def get_books_by_language(request):
    mydat = load_data() 
    language = request.GET.get('lang', '')  
    books = mydat.get("data", {}).get("books", []) 
    
    if language:
        filtered_books = [book for book in books if book.get('Language', '').lower() == language.lower()]
    else:
        filtered_books = books
    
    return JsonResponse({'books': filtered_books})

def get_books_by_genre(request):
    mydat = load_data()
    genre = request.GET.get('genre', '') 
    books = mydat.get("data", {}).get("books", []) 
    
    if genre:
        filtered_books = [book for book in books if book.get('Genre', '').lower() == genre.lower()]
    else:
        filtered_books = books
    
    return JsonResponse({'books': filtered_books})

def get_booksBYLIMT(request):
    offset = int(request.GET.get('offset', 0))
    limit = int(request.GET.get('limit', 20))

    all_books = load_data()["data"]["books"]

    books_subset = all_books[offset:offset + limit]

    has_more = len(all_books) > offset + limit

    response_data = {
        'books': books_subset,
        'has_more': has_more
    }

    return JsonResponse(response_data)

@csrf_exempt 
def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        image_path = request.FILES.get('image_path')
        description = request.POST.get('description')
        genre = request.POST.get('genre')
        language = request.POST.get('language')
        subjects = request.POST.getlist('subjects[]')  
        bookshelves = request.POST.getlist('bookshelves[]') 

        if name and author and description and genre and language:  # Assuming these are required fields
            # Append new book data to the existing data
            mydat = load_data()
            new_id = len(mydat["data"]["books"]) + 1
            
            new_book = {
                'id': str(new_id),
                'name': name,
                'author': author,
                'image_path': image_path,
                'description': description,
                'genre': genre,
                'language': language,
                'subjects': subjects,
                'bookshelves': bookshelves
            }
            
            mydat["data"]["books"].append(new_book)
            save_data(mydat)

            return JsonResponse({'message': 'Book added successfully'}, status=201)
        else:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def get_books_by_genandlang(request):
    mydat = load_data()  
    language = request.GET.get('lang', '')
    genre = request.GET.get('genre', '')  
    books = mydat.get("data", {}).get("books", [])  
    
    filtered_books = books
    if language:
        filtered_books = [book for book in filtered_books if book.get('Language', '').lower() == language.lower()]
    if genre:
        filtered_books = [book for book in filtered_books if book.get('Genre', '').lower() == genre.lower()]
    
    return JsonResponse({'books': filtered_books})


def adddata(request):
    mydat = load_data()
    new_id = len(mydat["data"]["books"]) + 1
        
    newdata = {
        'id': str(new_id),
        "name": name,
        "author": author,
        "image_path": file_path,
        "description": desc,
        "Genre":Genre,
        "Language":Language,
        "Subject(s)":subject,
        "Bookshelf(s)":Bookshelf
        }
        
       
    mydat["data"]["books"].append(newdata)

    save_data(mydat)
    
def create(request):
    
    if request.method == 'POST' and 'image' in request.FILES:
        image_file = request.FILES['image']
        name=request.POST.get('name')
        author=request.POST.get('author')
        desc=request.POST.get('desc')
        Genre=request.POST.get('Genre')
        Language=request.POST.get('Language')
        subject=request.POST.get('subject')
        Bookshelf=request.POST.get('Bookshelf')
        
        upload_folder = os.path.join(settings.BASE_DIR, 'myapp', 'static', 'media')
        file_path = os.path.normpath(os.path.join(upload_folder, image_file.name))
        
        os.makedirs(upload_folder, exist_ok=True)
        
        with open(file_path, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)

         
        print("File path:", file_path)
        
        file_path=f'static/media/{image_file.name}'
        print(file_path)
        mydat = load_data()
        new_id = len(mydat["data"]["books"]) + 1
        
        newdata = {
        'id': str(new_id),
        "name": name,
        "author": author,
        "image_path": file_path,
        "description": desc,
        "Genre":Genre,
        "Language":Language,
        "Subject(s)":subject,
        "Bookshelf(s)":Bookshelf
        }
        
       
        mydat["data"]["books"].append(newdata)

        save_data(mydat)


    return render(request,'create.html')

def search(request):
    mydat = load_data()
    data = mydat["data"]["books"]
    if request.method=="POST":
        searchcontent=request.POST.get('searchcontent')
        print(searchcontent)
        
        person = next((person for person in mydat["data"]["books"] if person['name'] == searchcontent), None)
        if person is None:
            return jsonify({'error': 'Person not found'}), 404
        else:
            print(person)
            return render(request,'found.html',{'data':data,'person':person})
    return render(request,'search.html',{'data':data})