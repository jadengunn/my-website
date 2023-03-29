from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def create_user(username, password):
    """
    Creates a new user with the given username and password.
    """
    user = User.objects.create_user(username=username, password=password)
    return user

def authenticate_user(username, password):
    """
    Authenticates the user with the given username and password.
    Returns the authenticated user object if successful, None otherwise.
    """
    user = authenticate(username=username, password=password)
    return user