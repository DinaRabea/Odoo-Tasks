from odoo import models , fields , api 
from odoo.exceptions import ValidationError

class CustomerCRM(models.Model):
    _inherit='res.partner'
    related_patient_id=fields.Many2one('hms.patient')

    @api.constrains('related_patient_id')
    def _check_email(self):
        for record in self:
          if record.email:
            if record.email == record.related_patient_id.email:
              raise ValidationError("Email already exit")
        
    
    def unlink(self):
        for record in self:
          if record.related_patient_id:
            raise ValidationError('You cant Delete this customer')
          return super(CustomerCRM, self).unlink()


    