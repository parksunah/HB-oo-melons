"""Classes for melon orders."""

class AbstractMelonOrder():

    def __init__(self, species, qty, order_type, tax=.05):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.tax = tax
        self.order_type = order_type
        self.shipped = False    

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "christmas melon":
            base_price = base_price * 1.5
        
        # if self.order_type == "international" and self.qty <10:
        #     base_price += 3

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "domestic", 0.08)



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):

        total = super().get_total()

        if self.qty < 10:
            total += 3        

        return total
