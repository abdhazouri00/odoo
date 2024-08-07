from odoo import models, fields, _, api
from odoo.exceptions import UserError, ValidationError

class Patients(models.Model):
    _name = 'patient.patient'
    _description = 'Patients Table'

    name = fields.Char(string='Patient Name', required=True)
    age = fields.Integer(string='Age')
    id_patient = fields.Char(string='Patient ID', size=10)
    mobile = fields.Char(string='Mobile Number', size=10)
    history = fields.Text(string='History')
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female'),])
    new_patient = fields.Boolean(string='New', default=False)
    copatient_id = fields.Many2one(comodel_name='copatient.copatient', string='Copatient')
    salary = fields.Float(string='Salary')
    diabate = fields.Boolean(string='Diabate')
    diabate_accum = fields.Float(string='Accomulative')
    blood_pressure = fields.Boolean(string='Blood Pressure')
    
    
    @api.constrains('age')
    def _check_age(self):
        for record in self:
            if record.age > 15:
                ValidationError('Patient can not be older than 15')

    
    
    _sql_constraints = [
        (
            'patient_identifier',
            'UNIQUE(id_patient)',
            _('Patient ID should be unique')
        )
    ]


    
    class Copatients(models.Model):
        _name = 'copatient.copatient'
        _description = 'Copatients Table'

        name = fields.Char(string='Name')
        
    
    
    
    
    
    
    
    