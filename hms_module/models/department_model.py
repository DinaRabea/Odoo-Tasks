from odoo import models, fields

class department(models.Model):
    _name="hms.department"
    name=fields.Char()
    capacity=fields.Integer()
    is_opened=fields.Boolean()
    patient_ids=fields.One2many('hms.patient', 'dept_id')


   