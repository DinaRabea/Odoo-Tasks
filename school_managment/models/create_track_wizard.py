from odoo import models, fields

class TrackWizard(models.TransientModel):
    _name="iti.trackwizard"
    name=fields.Char()
    description=fields.Text()

    def save_track_data(self):
        self.env['track.field'].create(
            {
               'name':self.name,
               'description':self.description
            }
        )

        std=self.env['student.field'].search([('state','=','accepted')])
        # delete student
        # std.unlink()

        # search
        # print(std)

    