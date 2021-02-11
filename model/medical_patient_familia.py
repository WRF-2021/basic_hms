# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta 

class medical_patient_familia(models.Model):
    
    _name = 'patient.familia'
    

    relative_type = fields.Selection([('Aunty', 'Tío'),
                                      ('Brother', 'Hermano'),
                                      ('Daughter', 'Hija'),
                                      ('Father', 'Padre'),
                                      ('conyuge', 'Conyuge'),
                                      ('Mother', 'Madre'),
                                      ('Sister', 'Hermana'),
                                      ('Son', 'Hijo'), ('Uncle', 'Tia'),
                                      ('Other', 'Otros')],
                                     string='Tipo Parentesco', required=True)
    name = fields.Char(string='Nombre', required=True)
    fecha_nacimiento = fields.Date(string='Fecha Nacimiento')
    occupation = fields.Char(string='Ocupacion')
    gender = fields.Selection([('Male', 'Masculino'), ('Female', 'Femenino')], string='Sexo')
    active = fields.Boolean(string='Active', default=True)
    medical_patient_familia_id = fields.Many2one('medical.patient',string="Paciente")

    #paciente_id = fields.Many2one('hr.applicant', 'Applicant Ref', ondelete='cascade')  