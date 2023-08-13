

class Base:
 

    # attributes:
    __nb_objects = 0
    # a private class attribute called _nb_objects which is initalized as zero.

    def __init__(self, id=None):
        # inisantiate the initalization init method
        if id != None:
            # if id is not None we give the public value to id else we increment the private instance _nb_objects and give it to id.
            self.id = id
        else:
            #increment the private instance
            Base.__nb_objects += 1
            self.id = Base. __nb_objects 
