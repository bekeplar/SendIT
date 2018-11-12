import re
import string


class ValidUser:
    """Class to validate user attributes"""

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def valid_name(self):
        """
        Method validates a user's name
        :it always returns:
        True - if user's name is valid input
        False - if user's name input is not valid
        """

        if not self.name or self.name.isspace() or not isinstance(
                self.name, str):
            return False
        else:
            return True

    def valid_email(self):
        """
        Method validates a user's email
        :it has return:
        True - if email is valid
        False - if email is not valid
        """

        if not self.email or not re.match(
                r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email):
            return False
        else:
            return True

    def valid_password(self):
        """
        Method validates a user's password
        :it has to return:
        True - if password is valid
        False - if password is not valid
        """

        lower_case = re.search(r"[a-z]", self.password)
        upper_case = re.search(r"[A-Z]", self.password)
        numbers = re.search(r"[0-9]", self.password)

        if not self.password or not all((lower_case, upper_case, numbers))\
                or not len(self.password) > 4:
            return False
        else:
            return True

    @staticmethod
    def validate_punctuation(name):
        """
        Method to check for punctuation marks in a string.
        :returns:
        True if the string contains punctuation marks
        """
        result = ""
        for character in name:
            if character in string.punctuation:
                result += character
        if result:
            return True
        return False


 