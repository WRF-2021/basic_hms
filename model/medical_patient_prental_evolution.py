# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_prental_evolution(models.Model):   
    
    _name = 'medical.patient.prental.evoultion'

    pregnency_id = fields.Many2one('medical.patient.pregnency', )
    evoultion_date = fields.Date('Fecha', required = True) 
    gestational_weeks = fields.Integer('Semanas de gestación', required = True)
    hypertansion = fields.Boolean('Hipertensión')
    preclampsia = fields.Boolean('Preeclampsia') 
    overweight = fields.Boolean('Exceso de peso')
    diabetes= fields.Boolean('Diabetes') 
    placenta_previa = fields.Boolean('Placenta previa')
    invasive_placentation = fields.Selection([('normal_decidua','Decidua normal'),
                                              ('accreta','Accreta'),
                                              ('increta','Increta'),
                                              ('percreta','Precreta')])
    vasa_previa = fields.Boolean('Vasa Previa') 
    fundel_weight = fields.Integer('Peso Fundel')
    fetus_heart_rate = fields.Integer('Frecuencia cardíaca del feto')
    efw = fields.Integer('EFW')
    bpd = fields.Integer('BPD')
    hc = fields.Integer('HC')
    ac = fields.Integer('AC')
    fl = fields.Integer('FL')


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
