'''
TOD:
This class is a system used by staff, which should be able to manage online orders and update the inventory.

Those codes are just copied from the teacher's codes, so we need to modify it.

Some application case in the main sytem: (from teacher)

    def _authorise_discount(self, table, percent):
        username = input("Username: ")
        password = input("Password: ")

        price = None

        if self._admin_system.login(username, password):
            price = self._admin_system.apply_discount(table, percent)
            self._admin_system.logout()

        else:
            print("Login failed")

        return price
'''

class StaffSystem(object):

    def __init__(self, staff):
        self._logs = []
        self._staff = staff
        self._is_authenticated = False

    
    # Simulate login & logout (this will be different when using Flask and Flask-login)
    def login(self, username, password):
        if self._staff.authenticate(username, password):
            self._is_authenticated = True
            return True
        return False


    def logout(self):
        self._is_authenticated = False

    # View past discounts
    def view_log(self):
        if not self._is_authenticated:
            return

        for log in self._logs:
            print(log)


    @property
    def is_authenticated(self):
        return self._is_authenticated


class Staff(object):

    def __init__(self, username, password):
        self._username = username
        self._password = password


    def authenticate(self, username, password):
        if (self._username == username and self._password == password):
            return True
        else:
            return False