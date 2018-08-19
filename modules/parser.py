import json
from realestateapi.models import Tenant, Payment
from realestateapi import db


class Parser:

    def __init__(self, loaded_file):
        self.loaded_file = loaded_file
        self.tenants = self.get_tenants()

    def loop_payments(self):
        for payment in self.loaded_file:
            for key, value in payment.items():
                self.is_match(key, value, payment)

    def is_match(self, k, val, payment):
        tenants = self.tenants
        for tenant in tenants:
            if k == 'Tegenrekening':
                if tenant.iban == val:
                    new_payment = Payment(
                        iban=payment['Tegenrekening'],
                        amount=float(str(payment['Bedrag (EUR)']).replace(",", ".")), account_holder=payment['Naam / Omschrijving'],
                        payment_json=payment,
                        date=str(payment['Datum']),
                        tenant_id=tenant.id
                    )
                    db.session.add(new_payment)
                    db.session.commit()

    @classmethod
    def get_tenants(self):
        tenants = Tenant.query.all()
        return tenants
