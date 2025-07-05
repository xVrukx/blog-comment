#imports
import json
from django.http import JsonResponse
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from content.models import *

#--------------------------------------------------------------------------------------------------
#for handeling registration
@csrf_exempt
def register_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            if not all([username, email, password]):
                return JsonResponse({"error": "All fields are required"}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username already exists"}, status=400)

            user = User.objects.create_user(username=username, email=email, password=password)
            return JsonResponse({"message": "User registered successfully"}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    return JsonResponse({"error": "Only POST method allowed"}, status=405)

#--------------------------------------------------------------------------------------------------
#for handeling login
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            if not all([username, password]):
                return JsonResponse({"error": "Username and password required"}, status=400)

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"message": "Login successful"}, status=200)
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    return JsonResponse({"error": "Only POST method allowed"}, status=405)

#--------------------------------------------------------------------------------------------------
# for handeling post 
@csrf_exempt
def create_post(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Authentication required"}, status=401)

        try:
            data = json.loads(request.body)
            title = data.get("title")
            content = data.get("content")

            if not all([title, content]):
                return JsonResponse({"error": "Title and content required"}, status=400)

            post = Post.objects.create(author=request.user, title=title, content=content)
            return JsonResponse({"message": "Post created successfully", "post_id": post.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Only POST method allowed"}, status=405)

@csrf_exempt
def get_all_posts(request):
    if request.method == "GET":
        posts = Post.objects.all().order_by("-created_at")
        post_list = []

        for post in posts:
            post_list.append({
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "author": post.author.username,
                "created_at": post.created_at.strftime("%Y-%m-%d %H:%M:%S")
            })

        return JsonResponse({"posts": post_list}, status=200)
    return JsonResponse({"error": "GET method only"}, status=405)

@csrf_exempt
def get_post_detail(request, id):
    if request.method == "GET":
        try:
            post = Post.objects.get(id=id)
            comments = Comment.objects.filter(post=post)

            comment_list = []
            for comment in comments:
                comment_list.append({
                    "user": comment.user.username,
                    "text": comment.text,
                    "created_at": comment.created_at.strftime("%Y-%m-%d %H:%M:%S")
                })

            return JsonResponse({
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "author": post.author.username,
                "created_at": post.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "comments": comment_list
            }, status=200)

        except Post.DoesNotExist:
            return JsonResponse({"error": "Post not found"}, status=404)
    return JsonResponse({"error": "GET method only"}, status=405)

#--------------------------------------------------------------------------------------------------
#for handeling comments
@csrf_exempt
def add_comment(request, id):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Authentication required"}, status=401)

        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return JsonResponse({"error": "Post not found"}, status=404)

        try:
            data = json.loads(request.body)
            text = data.get("text")

            if not text:
                return JsonResponse({"error": "Text field is required"}, status=400)

            comment = Comment.objects.create(post=post, user=request.user, text=text)
            return JsonResponse({"message": "Comment added", "comment_id": comment.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Only POST allowed"}, status=405)