class StructError(Exception):
    pass


class StackEmptyError(StructError):
    pass


class QueueEmptyError(StructError):
    pass


class ObjectIsNoneError(StructError):
    pass
