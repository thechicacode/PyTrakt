"""All Trakt related errors that are worth processing. Note that 412 response
codes are ignored because the only requests that this library sends out are
guaranteed to have the application/json MIME type set.
"""

__author__ = 'Jon Nappi'
__all__ = ['TraktException', 'OAuthException', 'ForbiddenException',
           'NotFoundException', 'ConflictException', 'ProcessException',
           'RateLimitException', 'TraktInternalException', 'TraktUnavailable']


class TraktException(BaseException):
    """Base Exception type for trakt module"""
    http_code = message = None

    def __str__(self):
        return self.message


class OAuthException(TraktException):
    """TraktException type to be raised when a 401 return code is recieved"""
    http_code = 401

    def __init__(self):
        self.message = 'Unauthorized - OAuth must be provided'


class ForbiddenException(TraktException):
    """TraktException type to be raised when a 403 return code is recieved"""
    http_code = 403

    def __init__(self):
        self.message = 'Forbidden - invalid API key or unapproved app'


class NotFoundException(TraktException):
    """TraktException type to be raised when a 404 return code is recieved"""
    http_code = 404

    def __init__(self):
        self.message = 'Not Found - method exists, but no record found'


class ConflictException(TraktException):
    """TraktException type to be raised when a 409 return code is recieved"""
    http_code = 409

    def __init__(self):
        self.message = 'Conflict - resource already created'


class ProcessException(TraktException):
    """TraktException type to be raised when a 422 return code is recieved"""
    http_code = 422

    def __init__(self):
        self.message = 'Unprocessable Entity - validation errors'


class RateLimitException(TraktException):
    """TraktException type to be raised when a 429 return code is recieved"""
    http_code = 429

    def __init__(self):
        self.message = 'Rate Limit Exceeded'


class TraktInternalException(TraktException):
    """TraktException type to be raised when a 500 error is raised"""
    http_code = 500

    def __init__(self):
        self.message = 'Internal Server Error'


class TraktUnavailable(TraktException):
    """TraktException type to be raised when a 503 error is raised"""
    http_code = 503

    def __init__(self):
        self.message = 'Trakt Unavailable - server overloaded'
