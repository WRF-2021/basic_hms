# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_perinatal_monitor(models.Model):
    
    _name = 'medical.perinatal.monitor'
    
    medical_perinatal_id = fields.Many2one('medical.perinatal.monitor')
    date  = fields.Date('Fecha')
    systolic = fields.Integer('Presión sistólica')
    diastolic = fields.Integer('Presión diastólica')
    mothers_heart_freq = fields.Integer('Frecuencia del corazón de las madres')
    consentration = fields.Integer('Concentración')
    cervix_dilation = fields.Integer('Dilatación del cuello uterino')  
    fundel_height = fields.Integer('Altura del fondo uterino ')
    fetus_presentation = fields.Selection([('n','Correcto'),
                                         ('o','Occipucio / Postrior cefálico'),
                                         ('fb','Frank Breech'),
                                         ('cb','Nalgas completas'),
                                         ('tl','Mentira transversal'),
                                         ('fu','Footling Lie')], 'Presentación del feto')
    f_freq = fields.Integer('Frecuencia cardíaca del feto')
    bleeding = fields.Boolean('Sangrado')
    meconium = fields.Boolean('Meconio')
    notes = fields.Char('Notas')


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
