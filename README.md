<<<<<<< HEAD
HNGx Internship
REST API with Basic CRUD Operation.
Description
A CRUD API (Create, Read, Update, and Delete) is a type of API that allows users to perform basic operations on data. These operations are typically performed on resources, which can be anything from simple data objects to complex entities. CRUD APIs are used in a variety of applications, including web applications, mobile apps, and desktop applications. They are also used by developers to build other APIs and services. The purpose of a CRUD API is to provide a simple and efficient way to manage data. By using a CRUD API, developers can avoid having to write their own code to perform basic operations on data. This can save time and effort, and it can also help to Here are some examples of how CRUD APIs can be used: A web application might use a CRUD API to allow users to create, read, update, and delete their accounts.
* A mobile app might use a CRUD API to allow users to add, remove, and edit items in their shopping cart.
* A desktop application might use a CRUD API to allow users to manage their contacts or appointments. CRUD APIs are a powerful tool that can be used to simplify the development and management of applications that need to interact with data.
Prerequisites
List of prerequisites or dependencies that users need to have installed before setting up and running your API. For example:
* Python (version 3.7 or higher)
* Django (Django==3.2.21)
* Django REST framework (djangorestframework==3.14.0)



Installation

Detailed instructions on how to install and set up your API. Include steps like:
1. Clone the repository: 
git clone https://github.com/Abubakarauta/hngxStageTwo.git

2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. Install the required packages:
      pip install -r requirements.txt
4. Set up the database:
      python manage.py migrate
5. Create a superuser (for admin access):
      python manage.py createsuperuser
      
Start the development server:
python manage.py runserver
Access the API at http://127.0.0.1:8000/.




API Endpoints
List and explain the available API endpoints, including their purposes and any required parameters. 

Endpoint		Method				Description

/api/			GET				Retrieve a list of persons
/api/			POST				Create a new person
/api/user_id		GET				Retrieve a specific person by ID		
/api/user_id		PUT                             Update a specific person by ID		
/api/user_id		DELETE				Delete a specific person



Examples for retrieving, creating, and updating a person using Postman:

Retrieving a List of All Persons (GET Request)
* URL: http://127.0.0.1:8000/api/
* Method: GET
In Postman:
1. Create a new request.
2. Set the request type to "GET."
3. Enter the API URL: http://127.0.0.1:8000/api/
4. Click "Send."
This will show you a list of all persons in your API.

Creating a New Person (POST Request)
* URL: http://127.0.0.1:8000/api/
* Method: POST
* Headers: Content-Type: application/json
* Request Body:
{
    "name": "John Doe"
}

In Postman:
1. Create a new request.
2. Set the request type to "POST."
3. Enter the API URL: http://127.0.0.1:8000/api/
4. In the Headers section, add a header with Content-Type as the key and application/json as the value.
5. In the Body section, select "raw" and enter the JSON request body shown above.
6. Click "Send."
This will create a new person with the name "John Doe."


Updating a Person (PUT Request)
* URL: http://127.0.0.1:8000/api/<person_id>/ (Replace <person_id> with the ID of the person you want to update)
* Method: PUT
* Headers: Content-Type: application/json
* Request Body:
      {"name": "Updated Name"}

In Postman:
1. Create a new request.
2. Set the request type to "PUT."
3. Enter the API URL with the person's ID you want to update (e.g., http://127.0.0.1:8000/api/1/).
4. In the Headers section, add a header with Content-Type as the key and application/json as the value.
5. In the Body section, select "raw" and enter the JSON request body shown above with the updated name.
6. Click "Send."
This will update the person's name to "Updated Name."

Contact Information
GitHub repository https://github.com/Abubakarauta/hngStageTwo

=======
HNGx Internship
REST API with Basic CRUD Operation.
Description
A CRUD API (Create, Read, Update, and Delete) is a type of API that allows users to perform basic operations on data. These operations are typically performed on resources, which can be anything from simple data objects to complex entities. CRUD APIs are used in a variety of applications, including web applications, mobile apps, and desktop applications. They are also used by developers to build other APIs and services. The purpose of a CRUD API is to provide a simple and efficient way to manage data. By using a CRUD API, developers can avoid having to write their own code to perform basic operations on data. This can save time and effort, and it can also help to Here are some examples of how CRUD APIs can be used: A web application might use a CRUD API to allow users to create, read, update, and delete their accounts.
* A mobile app might use a CRUD API to allow users to add, remove, and edit items in their shopping cart.
* A desktop application might use a CRUD API to allow users to manage their contacts or appointments. CRUD APIs are a powerful tool that can be used to simplify the development and management of applications that need to interact with data.
Prerequisites
List of prerequisites or dependencies that users need to have installed before setting up and running your API. For example:
* Python (version 3.7 or higher)
* Django (Django==3.2.21)
* Django REST framework (djangorestframework==3.14.0)



Installation

Detailed instructions on how to install and set up your API. Include steps like:
1. Clone the repository: 
git clone https://github.com/Abubakarauta/hngxStageTwo.git

2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. Install the required packages:
      pip install -r requirements.txt
4. Set up the database:
      python manage.py migrate
5. Create a superuser (for admin access):
      python manage.py createsuperuser
      
Start the development server:
python manage.py runserver
Access the API at http://127.0.0.1:8000/.




API Endpoints
List and explain the available API endpoints, including their purposes and any required parameters. 

Endpoint		Method				Description

/api/			GET				Retrieve a list of persons
/api/			POST				Create a new person
/api/user_id		GET				Retrieve a specific person by ID		
/api/user_id		PUT                             Update a specific person by ID		
/api/user_id		DELETE				Delete a specific person



Examples for retrieving, creating, and updating a person using Postman:

Retrieving a List of All Persons (GET Request)
* URL: http://127.0.0.1:8000/api/
* Method: GET
In Postman:
1. Create a new request.
2. Set the request type to "GET."
3. Enter the API URL: http://127.0.0.1:8000/api/
4. Click "Send."
This will show you a list of all persons in your API.

Creating a New Person (POST Request)
* URL: http://127.0.0.1:8000/api/
* Method: POST
* Headers: Content-Type: application/json
* Request Body:
{
    "name": "John Doe"
}

In Postman:
1. Create a new request.
2. Set the request type to "POST."
3. Enter the API URL: http://127.0.0.1:8000/api/
4. In the Headers section, add a header with Content-Type as the key and application/json as the value.
5. In the Body section, select "raw" and enter the JSON request body shown above.
6. Click "Send."
This will create a new person with the name "John Doe."


Updating a Person (PUT Request)
* URL: http://127.0.0.1:8000/api/<person_id>/ (Replace <person_id> with the ID of the person you want to update)
* Method: PUT
* Headers: Content-Type: application/json
* Request Body:
      {"name": "Updated Name"}

In Postman:
1. Create a new request.
2. Set the request type to "PUT."
3. Enter the API URL with the person's ID you want to update (e.g., http://127.0.0.1:8000/api/1/).
4. In the Headers section, add a header with Content-Type as the key and application/json as the value.
5. In the Body section, select "raw" and enter the JSON request body shown above with the updated name.
6. Click "Send."
This will update the person's name to "Updated Name."

Contact Information
GitHub repository https://github.com/Abubakarauta/hngStageTwo

>>>>>>> 799116b5167c1ebf05d25e75048451d651f53421
