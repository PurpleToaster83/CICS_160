class view_counter:
    __private_counter = 0 # mangled variable
    def visit(self):
        self.__private_counter += 1
        print(self.__private_counter, "total viewers")

my_website_c = view_counter()
my_website_c.visit()
my_website_c.visit()

print(my_website_c.__private_counter) # throws error