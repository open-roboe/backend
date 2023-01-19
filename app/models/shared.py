import uuid

class UUIDString(str):
    """ UUIDv4 string

    This is a custom pydantic data type, for
    a UUIDv4 string
    https://pydantic-docs.helpmanual.io/usage/types/#custom-data-types
    https://stackoverflow.com/a/69740271
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(
            pattern='^[A-F0-9a-f]{8}(-[A-F0-9a-f]{4}){3}-[A-F0-9a-f]{12}$',
            examples=['4a33135d-8aa3-47ba-bcfd-faa297b7fb5b'],
        )

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError('string required')
        u = uuid.UUID(v)
        return cls(f'{v}')
