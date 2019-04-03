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

    def __init__(self, staff, staff_details: dict):
        self._staff = staff
        self._staff_details = staff_details
        self._is_authenticated = False

    
    # Simulate login & logout (this will be different when using Flask and Flask-login)
    def login(self, username, password):
        if self._staff.authenticate(username, password):
            self._is_authenticated = True
            return True
        return False

    def add_staff(self,username,password):
      #  if username in self._staff_details
       #     print('User-name already taken, please enter another username')
        #else
            self._staff_details{username} = password


    @property
    def is_authenticated(self):
        return self._is_authenticated
    
    @property
    def staff_details(self):
        return self.staff_details


class Staff(object):

    def __init__(self, username, password):
        self._username = username
        self._password = password


    def authenticate(self, username, password):
        if (self._username == username and self._password == password):
            return True
        else:
            return False
