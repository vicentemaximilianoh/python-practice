
import json


class ExistingUserError(Exception):
    pass


class User:
    __name = ''
    __password = ''
    __file_name = "users.json"

    def __init__(self, name, password):
        self.__name = name
        self.__password = password

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_type(self):
        print("User")

    # Private methods
    def __get_users(self):
        self.__init_file()

        # Como buscar usuario en el json
        f = open(self.__file_name, "r")
        content = f.read()
        users = json.loads(content)
        f.close()

        return users

    def __init_file(self):
        try:
            with open(self.__file_name) as f:
                return json.load(f)
        except FileNotFoundError:
            f = open(self.__file_name, "a")
            f.write(json.dumps([]))
            f.close()

            f = open(self.__file_name, "r")
            return json.load(f)

    # Public methods

    def create(self):

        # Agregar comprobacion si ya existe usuario con ese nombre aca
        users = self.__get_users()

        found_user = None
        for user_in_list in users:
            if user_in_list['username'] == self.__name:
                found_user = user_in_list
                break

        if (found_user != None):
            raise ExistingUserError

        new_user = {'username': self.__name, 'password': self.__password}
        users.append(new_user)

        f = open(self.__file_name, "w")
        f.write(json.dumps(users))
        f.close()

    def login(self):
        users = self.__get_users()

        user_exists = None
        for user_in_list in users:
            if user_in_list['username'] == self.__name and user_in_list['password'] == self.__password:
                user_exists = user_in_list
                break

        return user_exists
