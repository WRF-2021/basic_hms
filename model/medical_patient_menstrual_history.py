# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_menstrual_history(models.Model):

    _name = 'medical.patient.menstrual.history'
    
    patient_id = fields.Many2one('medical.patient', 'Paciente')
    evolution_id = fields.Many2one('medical.patient.evaluation','Evaluacion')
    evoultion_date = fields.Date('Fecha')
    lmp = fields.Integer('LMP', required= True)
    lmp_length = fields.Integer('LMP Longitud', required= True )
    is_regular = fields.Boolean('IS Regular')
    dysmenorrhea = fields.Boolean('Dismenorrea')
    frequency = fields.Selection([('amenorrhea','Amenorrea'),
                                  ('oligomenorrhea','Oligomenorrea'),
                                  ('eumenorrhea','Eumenorrea'),
                                  ('pollymenohea','Polimenorrea')])
    volume  = fields.Selection([('hopomenorrhea','hipomenorrea'),
                                ('normal','Normal'),
                                ('menorrhagia','Menorragia') ])


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
