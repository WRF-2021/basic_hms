# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class  medical_patient_pregnency(models.Model):
    _name = 'medical.patient.pregnency'

    gravida = fields.Integer('Embarazo #')
    lmp = fields.Integer('LMP')
    pdd = fields.Date('Fecha de parto de embarazo')
    patient_id= fields.Many2one('medical.patient','Paciente')
    current_pregnency = fields.Boolean('Embarazo actual')
    medical_patient_evolution_prental_ids = fields.One2many('medical.patient.prental.evoultion', 'pregnency_id', 'Evaluaciones perinatales de pacientes')
    medical_perinatal_ids = fields.One2many('medical.preinatal', 'pregnency_id', 'Perinatal médico ')
    puerperium_perental_ids = fields.One2many('medical.puerperium.monitor', 'pregnency_id', 'Monitor de puerperio')
    fetuses = fields.Boolean('Fetos')
    monozygotic = fields.Boolean('Monocigótico')
    igur = fields.Selection([('s','Simétrico'),('a','Asimétrico')], 'IGUR')
    warn = fields.Boolean('Advertencia')
    result = fields.Char('Resultado')
    pregnancy_end_date = fields.Date('Fecha de finalización del embarazo')
    pregnancy_end_result = fields.Char('Resultado final del embarazo')


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
