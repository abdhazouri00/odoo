from odoo import models, fields, _, api



class hrEm(models.Model):
    _inherit = 'hr.employee'

    insurance = fields.Char(string='Insurance Company')
    