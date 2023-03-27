from odoo import models, fields

class skill(models.Model):
    _name="skill.field"
    name=fields.Char()

    std_ids=fields.Many2many('student.field')