from odoo import models, fields, _, api
from odoo.exceptions import UserError, ValidationError

class Laboratory(models.Model):
    _name = 'lab.lab'
    _description = 'Laboratory Table'

    # patient_name = fields.Char(string='Patient')
    patient_id = fields.Many2one(comodel_name='patient.patient', string='Patient')
    date = fields.Date(string='Date')
    lab_check = fields.Text(string='Labrotary Check', readonly=False)
    age = fields.Integer(string='Age',related='patient_id.age')
    # test_id = fields.Many2one(comodel_name='test.test', string='Test')
    price = fields.Float(string='Price')
    test_ids = fields.One2many(comodel_name='test.test', inverse_name='lab_id', string='')
    line_ids = fields.One2many(comodel_name='lab.line', inverse_name='lab_id', string='')
    total = fields.Float(string='Total')
    

    @api.constrains('date')
    def _check_date(self):
        for record in self:
            if record.date:
                if record.date < fields.Date.today():
                    raise ValidationError("The date cannot be set in the past")
            else:
                pass

    state = fields.Selection(
        string='State',
        selection=[('draft', 'Draft'), ('confirmed', 'Confirmed'), ('cancel', 'Cancel')],
        default='draft',
        readonly=True,
    )

    
    @api.onchange('patient_id')
    def compute_price(self):
        # print('//////////////////----------------/////////////',self)
        self.price = self.patient_id.salary * 0.1 

    def action_confirm(self):
        self.write({'state':'confirmed'})

    def action_cancel(self):
        self.write({'state':'cancel'})

    def action_draft(self):
        self.write({'state':'draft'})


    @api.onchange('line_ids')
    def _onchange_test_ids(self):
        for rec in self:
            price_sum = 0 
            for record in rec.line_ids:
                price_sum += record.price
            rec.total = price_sum
    


class LabLine(models.Model):
    _name = 'lab.line'
    _description = 'Lab Lines'

    test_id = fields.Many2one(comodel_name='test.test', string='')
    lab_id = fields.Many2one(comodel_name='lab.lab', string='')
    price = fields.Float(string='Price')
    
    @api.onchange('test_id')
    def _onchange_test_id(self):
        self.price = self.test_id.price


    
            

class LaboratoryTest(models.Model):
    _name = 'test.test'
    _description = 'Laboratory Tests'

    name = fields.Char(string='Name')
    price = fields.Float(string='Price')
    lab_id = fields.Many2one(comodel_name='lab.lab', string='')
    
    