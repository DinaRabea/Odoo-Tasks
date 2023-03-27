from odoo import models , fields


class track(models.Model):
    _name='track.field'
    name=fields.Char()
    branch=fields.Char()
    info=fields.Text()
    description=fields.Html()
    capacity=fields.Integer()
    start_date=fields.Date()
    duration=fields.Float()
    is_opened=fields.Boolean()
    student_ids=fields.One2many(comodel_name='student.field',inverse_name='track_id')