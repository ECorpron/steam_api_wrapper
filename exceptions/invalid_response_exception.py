class InvalidResponseException(Exception):
    pass


raise InvalidResponseException("Response Code is not 200")
