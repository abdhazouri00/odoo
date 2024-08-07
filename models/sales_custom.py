from odoo import models, fields, _, api



class sal(models.Model):
    _inherit = 'sale.order'

    info = fields.Char(string='other info')
    