from fastapi import HTTPException


class PlateNotFoundException(HTTPException):
    def __init__(self, message=None, status_code=400):
        super().__init__(status_code=status_code, detail=message)


class NoAccessException(HTTPException):
    def __init__(self, message=None, status_code=403):
        super().__init__(status_code=status_code, detail=message)


class UnauthorizedException(HTTPException):
    def __init__(self, message=None, status_code=401):
        super().__init__(status_code=status_code, detail=message)


class ConflictException(HTTPException):
    def __init__(self, message=None, status_code=409):
        super().__init__(status_code=status_code, detail=message)


class NotFoundException(HTTPException):
    def __init__(self, message=None, status_code=404):
        super().__init__(status_code=status_code, detail=message)
