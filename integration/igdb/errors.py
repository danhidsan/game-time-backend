class AuthorizationError(Exception):
    def __init__(self, message="Authorization Failure") -> None:
        super().__init__(message=message)