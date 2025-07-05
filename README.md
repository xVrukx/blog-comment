📝 Blog + Comment System (Without DRF)
A medium-high level blogging API built with core Django, featuring user authentication, blog post creation, and comment functionality — all implemented without Django REST Framework (DRF). Responses are returned using JsonResponse, and the system uses only function-based views.

🚀 Features
✅ User Registration & Login (Session-based)

✅ Create Blog Posts (Authenticated)

✅ View All Blog Posts

✅ View Detailed Post with Comments

✅ Add Comments to Posts (Authenticated)

❌ No DRF or serializers used

✅ JsonResponse-only API

✅ Function-Based Views

✅ Error Handling for invalid input and missing records

🔧 Tech Stack
Backend: Django (Core only, no DRF)

Database: SQLite

Auth: Django's built-in authentication system

Views: Function-based views

API Format: JSON using JsonResponse

📦 Models
🔹 User
Django's built-in User model

🔹 Post
author = ForeignKey(User)
title = CharField
content = TextField
created_at = DateTimeField(auto_now_add=True)

🔹 Comment
post = ForeignKey(Post)
user = ForeignKey(User)
text = TextField
created_at = DateTimeField(auto_now_add=True)
📂 API Endpoints

✅ User
POST /api/register/
{
  "username": "John",
  "email": "john@example.com",
  "password": "123456"
}
POST /api/login/
{
  "username": "John",
  "password": "123456"
}

✅ Posts
POST /api/create-post/ (Authentication Required)
{
  "title": "My First Blog",
  "content": "Hello, world!"
}
GET /api/posts/
Returns list of all posts with author usernames.

GET /api/post/<id>/
Returns detailed post info along with its comments.

✅ Comments
POST /api/post/<id>/comment/ (Authentication Required)
{
  "text": "Great post!"
}

🛠️ Setup Instructions
Clone the repo

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-folder>

Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Run migrations
python manage.py migrate

Run server
python manage.py runserver

🧪 API Testing Tips
Use Thunder Client or Postman

Set header: Content-Type: application/json

For authenticated requests, use the returned sessionid cookie from /api/login/

📌 Constraints Followed
No Django REST Framework (DRF)

Function-based views only

JsonResponse used manually

Proper error handling and structure

Auth required for protected endpoints

📚 License
This project is open-source and free to use under the MIT License.
