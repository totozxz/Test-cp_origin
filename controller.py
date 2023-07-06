class controller:
    async def calculation(self) :
        vat = self.vat + 1
        addVat = self.price * vat
        data = { 
            "price_per_unit_include_vat" : addVat,
            "total_price_include_vat": addVat * self.amount
            }
        return data
