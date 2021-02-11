# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_icu_chest_drainage(models.Model):
    _name = 'medical.icu.chest_drainage'

    location = fields.Selection([('rl','Right Pleura'),
                                 ('ll','Left Pleura'),
                                 ('mediastinum','Mediastinum')],
                                string='Location')
    suction = fields.Boolean(string="Succión")
    suction_pressure = fields.Integer(string="cm H2O")
    fluid_volumme = fields.Integer(string="Volume")
    fluid_aspect = fields.Selection([('serous','Seroso'),
                                     ('bloody','Sangriento'),
                                     ('chylous','Quiloso'),
                                     ('purulent','Purulento')],
                                    string="Aspecto")
    oscillation = fields.Boolean(string='Oscilación')
    air_leak = fields.Boolean(string='Fuga de aire')
    remarks = fields.Char(string="Observaciones")
    medical_patient_rounding_chest_drainage_id = fields.Many2one('medical.patient.rounding',string="Drenaje torácico")

