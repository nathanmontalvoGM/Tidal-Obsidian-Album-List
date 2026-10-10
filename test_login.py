import tidalapi

session = tidalapi.Session()
session.login_oauth_simple()

# If login worked:
print(f"Logged in as: {session.user.name}")
print(f"User ID: {session.user.id}")