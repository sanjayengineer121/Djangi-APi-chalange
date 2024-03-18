Django Code Challenge
Varsha Shriram Bhosale
Varsha Shriram Bhosale
Mar 11
Thank you for your application as a Python Developer. To proceed with the assessment, please create a Django project with the following features -

Objective: 

 The API implementation at a publicly accessible location.
Create a Python/ DRF (Django rest framework) website with Git-based source control with the ability to: 
 Retrieval of books meeting zero or more filter criteria. You can use either a PostgreSQL database dump or a MySQL dump of books for data from the mentioned repository.
Each query should return the following:
The number of books meeting the criteria
A list of book objects, each of which contains the following: 
          Title of the book
          Information about the author
          Genre
          Language
          Subject(s)
          Bookshelf(s)
          A list of links to download the book in the available formats (mime-types)
3. The following rules apply:
In case the number of books that meet the criteria exceeds 20, the API should
return only 20 books at a time and support the means of retrieving the next sets
of 20 books till all books are retrieved.
The books should be returned in descending order of popularity, as measured by
the number of downloads.
Data should be returned in a JSON format.
4. The following filter criteria should be supported:
Book ID numbers specified as Project Gutenberg ID numbers.
Language
Mime-type
Topic - topic should filter on either ‘subject’ or ‘bookshelf’ or both. Case-insensitive partial matches should be supported. e.g. ‘topic=child’ should among others, return books from the bookshelf ‘Children’s Literature’ and from the subject ‘Child education’.
Author - Case-insensitive partial matches should be supported.
Title - Case-insensitive partial matches should be supported.
Multiple filter criteria should be permitted in each API call and multiple filter
values should be allowed for each criterion. e.g. an API call should be able to
filter on ‘language=en,fr’ and ‘topic=child, infant’.

 5. Bonus: Show test coverage for the project.


Assessment Criteria:

1) Can the candidate produce an appropriate database model, do they understand how the Django ORM works? ; 

2) Do they understand Test-Driven Development? 

3) Do they have an understanding of Django REST framework and can use it as per requirements?
    

You should share your completed project as a repo on GitHub on the mentioned date. Looking forward to your solution.
