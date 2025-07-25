from contextlib import contextmanager
from unittest.mock import patch


@contextmanager
def patcher(*args: tuple, **kwargs: dict):
    args_list = list(args)
    arg = args_list.pop(0)
    class_ref = arg[0]
    method = arg[1]
    operations = arg[2]
    with patch.object(class_ref, method, **operations) as mock_x:
        kwargs.update({f"{class_ref.__name__}.{method}": mock_x})
        if not args_list:
            yield list(kwargs.items())
        else:
            with patcher(*args_list, **kwargs) as patches:
                yield patches
