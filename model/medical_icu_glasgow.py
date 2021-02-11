# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date,datetime

class medical_icu_glasgow(models.Model):
    _name = 'medical.icu.glasgow'
    _rec_name = 'medical_inpatient_registration_id'

    medical_inpatient_registration_id = fields.Many2one('medical.inpatient.registration',string="Registration Code",required=True)
    evaluation_date = fields.Datetime(string="Fecha",required=True)
    glasgow_eyes = fields.Selection([('1','1 : No abre los ojos'),
                                     ('2','2 : Abre los ojos en respuesta a estímulos dolorosos'),
                                     ('3','3 : Abre los ojos para responder a la voz.'),
                                     ('4','4 : Oojos de pluma espontáneamente')],
                                    string="Ojos")
    glasgow_verbal = fields.Selection([('1','1 : No hace ningún sonido'),
                                       ('2','2 : Sonidos incomprensibles'),
                                       ('3','3 : Pronuncia palabras inapropiadas'),
                                       ('4','4 : Confundido desorientado'),
                                       ('5','5 : Orientado conversa normalmente')],
                                      string="Verbal")
    glasgow_motor = fields.Selection([('1','1 : No hace ningún movimiento'),
                                      ('2','2 : Extensión a estímulos dolorosos -respuesta desenfrenada'),
                                      ('3','3 : Flexión anormal a estímulos dolorosos (respuesta de decorticación)'),
                                      ('4','4 : Flexión / Retirada a estímulos dolorosos'),
                                      ('5','5 : Localiza estímulos dolorosos'),
                                      ('6','6 :Obedece los comandos')],
                                     string="Motor")
    glasgow = fields.Integer(string="Glasgow", compute='get_glas_score')

    @api.one
    @api.depends('glasgow_motor', 'glasgow_verbal', 'glasgow_eyes' )
    def get_glas_score(self):
        """ Calculates Sub total"""
        count = int(self.glasgow_eyes) + int(self.glasgow_motor)+ int(self.glasgow_verbal)
        self.glasgow = count

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
