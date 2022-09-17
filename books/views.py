from django.shortcuts import render
from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.views import View
from .forms import BookForms
import requests
import json

# Create your views here.

# Returns all th books in json format
@api_view(['GET','POST'])
def book_list(request):
    # get all the books
    if request.method =='GET':
        # retrive all the books
        books = Book.objects.all()
        # serialie the retrived data to json
        serializer = BookSerializer(books,many=True)
        # return json response
        return Response(serializer.data)

    # create a new record of book
    if request.method =='POST':
        # serialie the retrived data to json
        serializer = BookSerializer(data=request.data)
        # save the book in database
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def book_detail(request,id):
    # get a the book by requested id
    # if record does not exist return 404 
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # return details of book as response 
    if request.method =='GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    # Uptate the book 
    elif request.method =='PUT':
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    # delete book
    elif request.method =='DELETE':
        serializer = BookSerializer(book)
        print((serializer.data))
        book.delete()
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)


# code for front end

API_URL = 'http://127.0.0.1:8000/api/books/'
# Show all the books on dashboard 
def dashboard(request):
    books = requests.get(API_URL)
    books = json.loads(books.content)
    return render(request, 'dashboard.html',{'books':books})


# fetch and display book details
def book_details(request,pk):
    book = requests.get(API_URL+str(pk))
    book = json.loads(book.content)
    return render(request, 'book_details.html',{'book':book})

# deletes a book and returns book name
def book_delete(request,pk):
    book = requests.delete(API_URL+str(pk))
    return render(request, 'book_delete.html',{'book':book})

# metho to handle edit book form
def edit_view(request,pk):
    book = requests.get(API_URL+str(pk))
    book = json.loads(book.content)
    form = BookForms()
    return render(request, 'edit_book.html',{'form':form,'book':book})


# method not completed
def update_book(request):
        print(request.body.title)
        books = requests.get(API_URL)
        books = json.loads(books.content)
        return render(request, 'dashboard.html',{'books':books})
    

class AddbookView(View):
    def get(self,request):
        form = BookForms()
        return render(request, 'add_book.html',{'form':form})

    def post(self, request):
        form = BookForms(request.POST)
        if form.is_valid():
            form.save()
        books = requests.get('http://127.0.0.1:8000/api/books/')
        books = json.loads(books.content)
        return render(request, 'dashboard.html',{'books':books})
