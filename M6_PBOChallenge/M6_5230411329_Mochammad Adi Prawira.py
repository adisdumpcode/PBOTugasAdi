import datetime

class Order:
    def __init__(self, id, nama, detail):
        self.id = id
        self.nama = nama
        self.detail = datetime.datetime.now()
        self.deliveries = []

    def setorder(self):
        print(f"id: {self.id}, nama: {self.nama}, detail: {self.detail}")

    def __str__(self):
        return f"Order(id: {self.id}, nama: {self.nama}, detail: {self.detail})"

    def add_delivery(self, delivery):
        self.deliveries.append(delivery)
    
    def display_order(self):
        print(f"Order ID: {self.id}, nama: {self.nama}, dibuat: {self.detail}")
        if self.deliveries:
            for delivery in self.deliveries:
                print(f"  - {delivery.processDelivery()}")
        else:
            print("  Tidak ada yang terkait dengan pengiriman tersebut .")

    


class Delivery:
    def __init__(self, id, nama, detail):
        self.id = id
        self.nama = nama
        self.detail = detail


    def processDelivery(self):
        return f"Delivery(id: {self.id}, nama: {self.nama}, detail: {self.detail})"

    def __str__(self):
        deliveries_str = ', '.join(str(d) for d in self.deliveries)
        return f"Order(id: {self.id}, nama: {self.nama}, dibuat: {self.detail}, pesanan: [{deliveries_str}])"

def menu():
    orders = {}
    deliveries = {}  

    while True:
        print("\n--- Pesantar ---")
        print("1. Buat Pesanan")
        print("2. Buat Pengiriman")
        print("3. Tambah Pengiriman ke Pesanan")
        print("4. Liat pesanan dan pengiriman")
        print("5. Keluar")
        choice = input("Masukkan pilihan: ")

        if choice == '1':
            # Create a new order
            order_id = int(input("Enter Order ID: "))
            customer_name = input("Masukkan nama pelanggan: ")
            details = input("Enter Order Details: ").split(', ')
            orders[order_id] = Order(order_id, customer_name, details)
            print("Pesanan sudah dibuat.")

        elif choice == '2':
            # Create a new delivery
            delivery_id = int(input("Enter Delivery ID: "))
            service_name = input("Enter Delivery Service Name: ")
            delivery_details = input("Enter Delivery Details: ")
            deliveries[delivery_id] = Delivery(delivery_id, service_name, delivery_details)
            print("Delivery created successfully.")

        elif choice == '3':
            # Add a delivery to an order
            order_id = int(input("Enter Order ID to add delivery: "))
            if order_id not in orders:
                print("Order not found.")
                continue
            delivery_id = int(input("Enter Delivery ID to add to this order: "))
            if delivery_id not in deliveries:
                print("Delivery not found.")
                continue
            orders[order_id].add_delivery(deliveries[delivery_id])
            print("Delivery added to order successfully.")

        elif choice == '4':
            # Display all orders and their associated deliveries
            if not orders:
                print("No orders to display.")
            for order in orders.values():
                order.display_order()

        elif choice == '5':
            print("Keluar dari program")
            break
        else:
            print("Ivalid, masukkan lagi")

menu()

