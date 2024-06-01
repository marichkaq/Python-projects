user_db = {
    'user1': 'password',
    'user2': 'securepassword'
}

def require_auth(func):
    def wrapper(username, *args, **kwargs):
        if username in user_db:
            return func(username, *args, **kwargs)
        else:
            return "User not authenticated"
    return wrapper

def add_or_update_user(username, password):
    user_db[username] = password

if __name__ == '__main__':
    @require_auth
    def protected_function(username):
        return f"Welcome {username}!"

    # Tests:
    print(protected_function('user1')) #should print: Welcome user1!
    print(protected_function('user3')) #should print: User not authenticated

    add_or_update_user('user3', 'password123')
    print(protected_function('user3')) #should print: Welcome user3!
