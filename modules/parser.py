import json
from realestateapi.models import Tenant


class Parser:

    def __init__(self, loaded_file):
        self.loaded_file = loaded_file
        self.tenants = self.get_tenants()

    def check_payments(self):
        for payment in self.loaded_file:
            for key, value in payment.items():
                self.is_match(key, value, payment)

    def is_match(self, k, val, payment):
        tenants = self.tenants
        for tenant in tenants:
            if k == 'Tegenrekening':
                if tenant.iban == val:
                    print('we have a fucking match', payment)

    def get_tenants(self):
        tenants = Tenant.query.all()
        return tenants


loaded_file = json.loads(open(
    "/Users/RaptorHezuzNinya/code/python/real_estate_API/data/csvjson.json").read())
p = Parser(loaded_file)
p.check_payments()
# p.get_tenants()
