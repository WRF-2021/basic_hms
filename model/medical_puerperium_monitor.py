# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_puerperium_monitor(models.Model):
    
    _name = 'medical.puerperium.monitor'
    
    pregnency_id = fields.Many2one('medical.patient.pregnency')
    date = fields.Datetime('Fecha y hora')
    systolic_pressure = fields.Integer('Presión sistólica')
    diastolic_pressure = fields.Integer('Presión diastólica')
    heart_freq = fields.Integer('Frecuencia cardiaca')
    temprature  = fields.Integer('Temperatura')
    fundal_height = fields.Integer('Altura del fondo uterino')
    lochia_amount = fields.Selection([('n','Normal'),('a','Abundante'),('h','Hemorragia'),],'Cantidad de loquios')
    lochia_color = fields.Selection([('r','Rubro'),('s','Seroso'),('a','Alba')], 'Color Loicha')
    loicha_order = fields.Selection([('n','Normal'), ('o','Ofensivo')],'Color Loicha')


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
