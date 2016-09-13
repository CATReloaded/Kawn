import sys

from app import App


DEBUG = App.config['DEBUG']

def handle_command():
    try:
        command = sys.argv[1]
        if command in ['runserver',]:
            if command == 'runserver':
                App.run(debug=DEBUG)
        else:
            print("Command Not Found, Avaliable commands [runserver,]")
    except IndexError:
        print("Available commands are:\n\trunserver")


if __name__ == '__main__':
    handle_command()
