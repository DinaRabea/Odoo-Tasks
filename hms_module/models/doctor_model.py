from odoo import models, fields

class doctor(models.Model):
    _name="hms.doctor"
    name=fields.Char()
    b_date=fields.Date()
    age=fields.Integer()
    history=fields.Html()
    image=fields.Image()
    address=fields.Text()
    patient_ids=fields.Many2many('hms.patient')