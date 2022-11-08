import functools


def mask_data(target_key: str, replace_with: str = "*"):
    """Replace the value of a dictionary with a 'masked' version."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            data_to_replace = func(*args, **kwargs)
            if target_key in data_to_replace.keys():
                data_to_replace[target_key] = replace_with
            return data_to_replace

        return wrapper

    return decorator


# TARGET FUNCTIONS
@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {"name": name, "age": age}


# TEST OUTPUT
print(get_user(name="Alice", age=30), get_user(name="Bob", age=25), sep="\n")
