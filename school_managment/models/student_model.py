from odoo import models , fields  , api
from odoo.exceptions import ValidationError
import re
from datetime import datetime

class student(models.Model):
    _name='student.field'
    name=fields.Char()
    email=fields.Char()
    age=fields.Integer()
    info=fields.Text()
    salary=fields.Float()
    birthdate=fields.Date()
    interview_time=fields.Datetime()
    description=fields.Html()
    is_accepted=fields.Boolean()
    image=fields.Image()
    gender=fields.Selection(
        [
          ('Male','male'),
          ('Female','female')
        ]
    )
    ###############################################################
    # computed field 
    computed_age=fields.Integer(compute="computed_agee")

    @api.depends('birthdate')
    def computed_agee(self):
        for record in self:
            if record.birthdate:
                record.computed_age=datetime.now().year - record.birthdate.year
            else:
                record.computed_age=0
    ################################################################
    # uniqe constrains
    _sql_constraints = [ ('unique_name','UNIQUE(email)','Email Already Exists'),
                         ('check_salary','CHECK(salary >10)','salary must be greater than 10') ]


    ################################################################
    track_id=fields.Many2one('track.field')
    branch=fields.Char(related='track_id.branch',store=True)
    skills_ids=fields.Many2many('skill.field')
    state=fields.Selection(
        [
           ('new','New'),
           ('interviewing','Interviewing'),
           ('accepted','Accepted'),
           ('rejcted','Rejcted')
        ], default="new"
    )

    def set_to_interviewing(self):
        self.state="interviewing"
    
    def set_to_new(self):
        self.state="new"

    def set_to_accepted(self):
        self.state="accepted"

    def set_to_rejcted(self):
        self.state="rejcted"
    
    # make validation in email field
    @api.constrains('email')
    def check_email(self):
        # pattern = '^(?!.*[^\w\s]).{1,64}@(?=.{1,255}\.)(?=.{1,255}$)(?!\d)[\w\-\.]{1,255}(?<!\.)$'
        for record in self:
            # if record.email and not re.match(pattern, record.email):
            if '@gmail.com' not in record.email:
                raise ValidationError("Enter valid email")
            


    #to change the behavior of create function
    @api.model
    def create(self,vals):
        if '@' not in vals['email']:
            vals['email'] = vals['email']+'@gmail.com'
        return super().create(vals)
    
    def write(self,vals):
        if vals.get('email') and '@gmail.com' not in vals['email']:
            vals['email']=vals['email'] +'@gmail.com'
        return super().write(vals)