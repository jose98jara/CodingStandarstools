"""Modulo de carrito de compras para calcular el precio"""

class Item:
    """Clase Item para el carro de compras"""

    def __init__(self, name, price, qty):
        """Inicialización de items"""
        self.name = name
        self.price = price
        self.qty = qty
        self.category = "general"
        self.env_fee = 0

    def get_total(self):
        """Calculate the total price for this item."""
        return self.price * self.qty

    def get_total_with_discount(self):
        """Calculate the discounted total price for this item."""
        return self.price * self.qty * 0.6


class ShoppingCart:
    """Class representing a shopping cart."""

    def __init__(self):
        """Initialize the shopping cart with an empty item list and default rates."""
        self.items = []
        self.tax_rate = 0.08
        self.member_discount = 0.05
        self.big_spender_discount = 10
        self.coupon_discount = 0.15
        self.currency = "USD"

    def add_item(self, item):
        """Add an item to the shopping cart."""
        self.items.append(item)

    def calculate_subtotal(self):
        """Calculate the subtotal of all items in the cart."""
        subtotal = 0
        for item in self.items:
            subtotal += item.get_total()
        return subtotal

    def apply_discounts(self, subtotal, is_member, has_coupon):
        """Descuento según membresia y cupones"""
        if is_member:
            subtotal -= subtotal * self.member_discount

        if subtotal > 100:
            subtotal -= self.big_spender_discount

        if has_coupon:
            subtotal -= subtotal * self.coupon_discount 

        return subtotal

    def calculate_total(self, is_member, has_coupon):
        """Calculo total considerando descuentos"""
        subtotal = self.calculate_subtotal()

        for item in self.items:
            if item.category == "electronics":
                subtotal += item.qty * 5 

        subtotal = self.apply_discounts(subtotal, is_member, has_coupon)

        total = subtotal + (subtotal * self.tax_rate)

        if has_coupon:
            total -= total * self.coupon_discount

        return total


def main():
    """Funcionalidad principal """
    cart = ShoppingCart()
    item1 = Item("Apple", 1.5, 10)
    item2 = Item("Banana", 0.5, 5)
    item3 = Item("Laptop", 1000, 1)

    item3.category = "electronics"

    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)

    is_member = True
    has_coupon = True

    total = cart.calculate_total(is_member, has_coupon)

    if total < 0:
        print("Error in calculation!")
    else:
        print("The total price is: $" + str(round(total, 2)))


if __name__ == "__main__":
    main()
