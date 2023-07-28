def raise_exception():
    try:
        raise TypeError("This is a type exception.")
    except TypeError as e:
        print(f"Exception raised: {e}")
       
       
    # call the function
    raise_exception() 