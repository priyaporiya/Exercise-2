'''Add new data members “parent”, “display_name”, and “products” (list of product objects) inside the category class.
•	Add a new member function to generate “display_name”.
•	“display_name” has the text value as below.
          1.	Vehicle category without parent then “Vehicle” 
          2.	Car category with “Vehicle” as a parent then “Vehicle > Car”
          3.	Petrol category with “Car” as a parent then “Vehicle > Car > Petrol”
•	Create 5 category objects with parent and child relation.
•	Create 3 product objects in each category.
•	Display Category with its Code, Display Name and all product details inside that category.
•	Display product list by category (group by category, order by category name).'''

class category:
    category_counter = 1000
    def __init__(self,name,parent=None):
        self.name = name
        self.code = category.category_counter
        category.category_counter += 1
        self.parent = parent
        self.product = []
        self.display_name = self.generate_display_name()

    def generate_display_name(self):
        if self.parent:
            return f"{self.parent.display_name} > {self.name}"
        return self.name

    def add_product(self,product):
        self.product.append(product)  

    def display_details(self):
        print(f"category code : {self.code} display name : {self.display_name}")
        print("products:")
        for product in self.product:
            print(f" - {product}")
        print("-"* 70)

class Product:
    def __init__(self,name,code,price):
        self.name = name
        self.code = code
        self.price = price

    def __str__(self):
        return f"Name : {self.name}, Code : {self.code}, Price : {self.price:2f}"
    
vehicle = category("vehicle")
car = category("car", vehicle)
#petrol = category("petrol", car)
bike = category("bike",vehicle)
#electric = category("electric",bike)
sedan = category("sedan",car)
sports_bike = category("sports_bike",bike)

vehicle.product = [Product("Truck", 1001,50000), Product("Bus",1002, 75000), Product("SUV",1003, 40000)]
car.product = [Product("Honda",1004, 25000), Product("Toyota",1005, 23000), Product("Ford Mustang",1006, 55000)]
bike.product = [Product("Yamaha",1007, 15000), Product("Honda CBR", 1008,17000), Product("Kawasaki Ninja",1009, 20000)]
sedan.product = [Product("BMW",1010, 60000), Product("Audi",1111, 65000), Product("Mercedes",1112, 70000)]
sports_bike.product = [Product("Ducati Panigale",1113, 25000), Product("KTM",1114, 8000), Product("Suzuki",1115, 16000)]

categories = [vehicle,car,bike,sedan,sports_bike]

print("Befor sort")
for category in categories:
    category.display_details()

for i in range(len(categories)):
    for j in range(len(categories)):
        if categories[i].name > categories[j].name:
            categories[i],categories[j] = categories[j],categories[i]

print("After sort")
for category in categories:
    category.display_details()

print("grouped product list by category")
for category in categories:
    print(f"category: {category.display_name}")
    for product in category.product:
            print(f" - {product}")
    print("-"* 70)


        
        


        