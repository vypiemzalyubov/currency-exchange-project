from fastapi import HTTPException, status


class CurrencyException(HTTPException):
    status_code = 500
    detail = 'Internal error'

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(CurrencyException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'User already exist'


class IncorrectEmailOrPasswordException(CurrencyException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Incorrect email or username'


class ExpiredTokenException(CurrencyException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Token expired'


class TokenAbsentException(CurrencyException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Token absent'


class IncorrectTokenFormatException(CurrencyException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Incorrect token format'


class UserNotPresentException(CurrencyException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'User not present'
