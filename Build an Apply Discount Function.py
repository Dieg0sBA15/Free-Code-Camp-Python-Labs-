#Defininf a function called "apply_discount" with two parametters: price and discount
def apply_discount(price, discount):
  #If conditional where the inputs needs to be a number 
    if not isinstance(price, (int, float)) or isinstance(price, bool):
      #Return output if the input is not a number 
        return ("The price should be a number")
  #If discount where the inputs needs to be a number 
    elif not isinstance(discount,(int,float)) or isinstance(price, bool):
      #Return output if the input is not a number 
        return("The discount should be a number")
      #Conditional where if price is less or equal than 0 then return an alert
    elif price <= 0:
        return("The price should be greater than 0")
    #Conditional where if discount is less than 0 then return an alert
    elif discount < 0:
        return("The discount should be between 0 and 100")
    #Conditional (will progress later)
    elif 
