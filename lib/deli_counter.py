def line(deli):
    if len(deli) == 0:
       print("The line is currently empty.")
    else:
        customers = [str(deli.index(customer)+1)+". "+ customer for customer in deli]
         
        print(f'The line is currently: {" ".join(customers)}' )
   


def take_a_number(deli,name):
    deli.append(name)
    print(f"Welcome, {name}. You are number {len(deli)} in line." ) 



def now_serving(deli):
    if len(deli) > 1:
        print(f"Currently serving {deli[0]}.")
        deli.pop(0)
    else:
        print("There is nobody waiting to be served!")
    