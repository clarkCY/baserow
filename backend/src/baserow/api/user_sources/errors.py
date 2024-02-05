from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

ERROR_USER_SOURCE_DOES_NOT_EXIST = (
    "ERROR_USER_SOURCE_DOES_NOT_EXIST",
    HTTP_404_NOT_FOUND,
    "The requested user_source does not exist.",
)

ERROR_USER_SOURCE_NOT_IN_SAME_APPLICATION = (
    "ERROR_USER_SOURCE_NOT_IN_SAME_APPLICATION",
    HTTP_400_BAD_REQUEST,
    "The given user_sources do not belong to the same application.",
)


ERROR_AUTH_PROVIDER_TYPE_NOT_COMPATIBLE = (
    "ERROR_AUTH_PROVIDER_TYPE_NOT_COMPATIBLE",
    HTTP_400_BAD_REQUEST,
    "{e}",
)


ERROR_AUTH_PROVIDER_TYPE_DOES_NOT_EXIST = (
    "ERROR_AUTH_PROVIDER_TYPE_DOES_NOT_EXIST",
    HTTP_400_BAD_REQUEST,
    "{e}",
)


ERROR_AUTH_PROVIDER_CANT_BE_CREATED = (
    "ERROR_AUTH_PROVIDER_CANT_BE_CREATED",
    HTTP_400_BAD_REQUEST,
    "One of the auth provider can't be created.",
)
