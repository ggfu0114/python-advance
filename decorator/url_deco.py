


# The all the decorated will be executed when the module is loaded.
def url_register(url_path):
    def wrapper(func):
        print(f'Append url to server:{url_path} and func:{func.__name__}')
        return func
    return wrapper


@url_register('/photo')
def list_photos():
    print('list_photo')
    pass

@url_register('/album')
def list_albums():
    print('list_album')
    pass


# The above decorator use case is equal to 
def main_page():
    print('main_page')
    pass
f=url_register('/main')(main_page)
