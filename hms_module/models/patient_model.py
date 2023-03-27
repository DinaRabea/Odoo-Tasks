from odoo import models , fields , api
from datetime import datetime

class patient(models.Model):
    _name="hms.patient"
    _rec_name="f_name"
    f_name=fields.Char()
    l_name=fields.Char()
    b_date=fields.Date()
    history=fields.Html()
    cr_ratio=fields.Float()
    blood_typr=fields.Selection(
        [
           ('a','A'),
           ('b','B'),
           ('o','O'),
        ]
    )
    pcr=fields.Boolean(default=False)
    image=fields.Image()
    address=fields.Text()
    age=fields.Integer()
    dept_id=fields.Many2one('hms.department')
    name_dept=fields.Char(related='dept_id.name')
    capacity=fields.Integer(related='dept_id.capacity')
    doc_ids=fields.Many2many('hms.doctor','patient_ids')
    state=fields.Selection(
        [
           ('undetermined','Undetermined'),
           ('good','Good'),
           ('fair','Fair'),
           ('serious','Serious')
        ], default="undetermined"
    )


    @api.onchange('b_date')
    def _onchange_age(self):
        if self.b_date:
            self.age=datetime.now().year - self.b_date.year
            return{
                'warning':{
                            'title':"age Changed",
                            'massage':"age has been changed"
                }
            }
        
    def set_to_good(self):
        self.state="good"

    def set_to_fair(self):
        self.state="fair"

    def set_to_undetermined(self):
        self.state="undetermined"
    
    def set_to_serious(self):
        self.state="serious"
    

    
    @api.onchange('b_date')
    def change_pcr(self):
     if self.b_date:
        self.age=datetime.now().year-self.b_date.year
        if self.age < 30:
            self.pcr=True
            return{
                'warning':{
                            'title':"pcr checked",
                            'massage':"PCR has been Checked"
                }
            }

    # adding email for patient
    email=fields.Char(required=True)
    _sql_constraints=[
         ('unique_email','UNIQUE(email)','Email Already Exists'),
    ] 

