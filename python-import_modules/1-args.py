import sys

def print_arguments():
    num_arguments = len(sys.argv) - 1
    if num_arguments == 0:
        print("0 arguments.")
        return
    print(f"{num_arguments} argument{'s' if num_arguments > 1 else ''}:")
    for i, arg in enumerate(sys.argv [1:], ):
        print(f"{i+1}: {arg}")
        
if __name__ =="__main__":
    print_arguments()
           
    