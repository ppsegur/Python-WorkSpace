### Type Hints

my_string_variable = "Hello, World!"
print(my_string_variable)
print(type(my_string_variable))


# Aquí podemos ver la facilidad de cambio de tipado (O tipado dinámico)
# de nuestraas variables en python
my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

# Al usar type hints, podemos especificar el tipo de dato que queremos que
# Reailzar esto ayudará a enternderse emjor 
my_ttyped_variable : str = "Hello, World!"
print(my_ttyped_variable)
print(type(my_ttyped_variable))
#Pero se puede ver que igualmente se puede cambiar el tipo de dato aun asi 
my_ttyped_variable = 5
print(my_ttyped_variable)
print(type(my_ttyped_variable))



#Esto será un tipado débil en Python
#Pero se puede hacer uso de type hints para especificar el tipo de dato
my_string_variable: int = "Hello, World!"
print(my_string_variable)
print(type(my_string_variable))

#Funciones especiales
my_integer_variable:int  = 5
