# converts a camelCase input to snake_case.

def camel_to_snake(camel_str):
    snake_str = ""
    for char in camel_str:
         if char.isupper():
            snake_str += "_"
            snake_str += char.lower()
         else:       
            snake_str += char
    return snake_str
    
def main():
    print(camel_to_snake(input("enter camelCase: ")))

main()