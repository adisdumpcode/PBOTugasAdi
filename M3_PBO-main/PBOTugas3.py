class Menu:
    def __init__(self):
        self.makan = []
        self.minum = []

    def tambahmakan(self, food_name, price):
        self.makan.append((food_name, price))

    def tambah(self, drink_name, price):
        """Add a drink item to the menu."""
        self.minum.append((drink_name, price))

    def tampilmakanmenu(self):
        """Display the food menu."""
        if not self.foods:
            print("No food items available.")
        else:
            print("\n--- Food Menu ---")
            for index, (food, price) in enumerate(self.foods, start=1):
                print(f"{index}. {food} - ${price:.2f}")

    def tampilminummenu(self):
        """Display the drink menu."""
        if not self.drinks:
            print("No minum items available.")
        else:
            print("\n---Menu minum ---")
            for index, (minum, harga) in enumerate(self.minum, start=1):
                print(f"{index}. {minum} - ${harga:.2f}")

    def tampilitem(self):
        while True:
            choice = input("\nPilih Tambah (makan/minum/keluar): ").lower()
            if choice == "exit":
                break
            name = input(f"Enter the name of the {choice}: ")
            harga = float(input(f"Enter the price of the {choice}: $"))
            if choice == "food":
                self.tambahmakan(name, harga)
            elif choice == "drink":
                self.tambahminum(name, harga)
            else:
                print("Invalid, pilih makan, minum, atau keluar'.")

# Create an instance of Menu
menu = Menu()

# Adding some default foods and drinks
menu.tambahmakan("Pizza", 8.99)
menu.tambahmakan("Burger", 5.99)
menu.tambahmakan("cola", 1.99)
menu.tambahmakan("air", 0.99)

# Show the current menus
menu.tampilmakanmenu()
menu.tampilminummenu()

# Allow the user to add more items
menu.tampilitem()

# Show the updated menus
menu.tampilmakanmenu()
menu.tampilminummenu()
