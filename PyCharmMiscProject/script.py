class order:
    def __init__(self,customer_name,items, total_amount, discount):
        self.customer_name = customer_name
        self.items = items
        self.__total_amount = total_amount
        self.__discount = discount

    def __calculate_final(self):
        return self.__total_amount - self.__discount

    def _get_admin_view (self):
        return{
            "customer": self.customer_name,
            "items": self.items,
            "total_amount":f"{ self.__total_amount}",
            "Discount": f"{self.__discount}",
            "Final Bill": f"{self.__calculate_final()}"

        }
    def get_customer_view(self):
        return{
            "customer": self.customer_name,
            "items": self.items,
            "Final Bill": self.__calculate_final()
        }

class adminportal:
    def show_order(self,order):
        return order._get_admin_view()

class customerapp:
    def show_order(self,order):
        return order.get_customer_view()

order = order("maadesh","pizza,burger",500,100)
admin = adminportal()
customer = customerapp()

print("admin view")
print (admin.show_order(order))

print("customer view")
print(customer.show_order(order))


