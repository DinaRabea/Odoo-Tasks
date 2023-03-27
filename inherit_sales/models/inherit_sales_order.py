from odoo import models, fields, api

class InheritSalesOrder(models.Model):
    _inherit='sale.order'

    custom_reference=fields.Char()


    @api.model
    def create(self, vals):
        if not vals.get('custom_reference'):
            vals['custom_reference']= vals['custom_reference']+'default custom reference'
        
        return super().create(vals)

