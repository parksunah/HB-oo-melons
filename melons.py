"""Classes for melon orders."""

class AbstractMelonOrder():
    ""
    base_price = 5
    country_code="USA"

    def __init__(self, species, qty):
        self.order_type = order_type
        self.country_code = country_code
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        if self.species == "Christmas melon":
            self.base_price *= 1.5

        total = (1 + self.tax) * self.qty * self.base_price

        return total
    
    def mark_shipped(self):
            """Record the fact than an order has been shipped."""

            self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = 'international'
    tax = 0.17 


    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""

        if self.qty <10:
            self.base_price += 3  

        return super().get_total()



class GovernmentMelonOrder(AbstractMelonOrder):
    """ A melon order for the US Government."""

    order_type = "Government"
    tax = 0.00

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)

        self.passed_inspection = False

    def get_total(self):

        return super().get_total() 

    def mark_inspection(self, passed=True):


        self.passed_inspection = True
