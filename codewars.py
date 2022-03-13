def wrap(value):
    """
    A function wrap(value) that takes a value of arbitrary type and wraps it in
    Python Dict setting the 'value' key on the new Object
    or Dict to the passed-in value.
    wrapper_obj = wrap("my_wrapped_string");
    # wrapper_obj should be  {"value":"my_wrapped_string"}
    """
    print({'value': value})


value = "my_wrapped_string"  # "aBCdeF"
wrap(value)
