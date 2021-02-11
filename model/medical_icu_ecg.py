# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date,datetime


class medical_icu_ecg(models.Model):
    _name = 'medical.icu.ecg'
    _rec_name = 'medical_inpatient_registration_id'

    ecg_date = fields.Datetime(string="Fecha",requied=True)
    medical_inpatient_registration_id = fields.Many2one('medical.inpatient.registration',string="Código de registro",required=True)
    lead = fields.Selection([('i','|'),('ii','||'),('iii','|||'),('avf','aVF'),('avr','aVR'),('avl','aVL'),('v1','V1'),('v2','V2'),('v3','V3'),('v4','V4'),('v5','V5'),('v6','V6')])
    axis = fields.Selection([('normal','Normal'),('left','Desviación izquierda'),('right','Right Deviation'),('extreme_right','Extreme Right Deviation')],string="Eje",required=True)
    rate = fields.Integer(string="Velocidad",required="True")
    pacemaker = fields.Selection([('sa','sinus Node'),('av','Atrioventricular'),('pk','purkinje')],string="Marcapasos",required=True)
    rhythm = fields.Selection([('regular','Regular'),('irregular','Irregular')],string="Ritmo",required=True)
    pr =fields.Integer(string="PR",required=True)
    qrs = fields.Integer(string="QRS",required=True)
    qt = fields.Integer(string="QT",required=True)
    st_segment = fields.Selection([('normal','Normal'),('depressed','Depressed'),('elevated','Elevated')],string="Segmento ST",required=True)
    twave_inversion = fields.Boolean(string="Inversión de onda T")
    interpretation = fields.Char(string="Interpretación",required=True,size=256)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
