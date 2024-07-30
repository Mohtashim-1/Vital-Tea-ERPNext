# Copyright (c) 2024, mohtashim and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Item(Document):
	def before_save(self):
        self.package_detail()

    def package_detail(self):
        self.custom_packaging_detail = str(self.weight_per_unit) +" X "+ str(self.custom_item_packing) 
        # doc.custom_packaging_detail = str(doc.weight_per_unit) +" X "+ str(doc.custom_item_packing)
        if self.weight_uom == "Gram":
            self.custom_weight_net_kgs =  (self.weight_per_unit * self.custom_item_packing) / 1000
            # frappe.msgprint("test")
        else:
            self.custom_weight_net_kgs =  (self.weight_per_unit * self.custom_item_packing)
            
        # custom_weight_gross_kgs

        # self.custom_weight_gross_kgs = self.custom_weight_net_kgs + (1.6)
            
        self.custom_weight_gross_kgs = self.custom_weight_net_kgs + self.custom_packaging_weight_kgs

        # lbs

        self.custom_lbs = self.weight_per_unit * 0.00220462

        # oz

        self.custom_oz = self.weight_per_unit * 0.035274
