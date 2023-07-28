def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError as e:
        print(f"Exception raised: {e}")
        
    
    # call the function with a custom message
    raise_exception_msg("This is a name exception.")
    