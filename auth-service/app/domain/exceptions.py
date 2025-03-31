class UserAlreadyExistsError(Exception):
    def __init__(self, email: str):
        self.email = email
        self.message = f"User with email {self.email} already exists."
        super().__init__(self.message)

class UserNotFoundError(Exception):
    def __init__(self, email: str):
        self.email = email
        self.message = f"User with email {self.email} not found."
        super().__init__(self.message)
