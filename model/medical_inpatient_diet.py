# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_inpatient_diet(models.Model):
    _name = 'medical.inpatient.diet'

    diet_id = fields.Many2one('medical.diet.therapeutic',string='Dieta',required=True)
    remarks = fields.Text(string=' Observaciones / Direcciones ')
    medical_inpatient_registration_id = fields.Many2one('medical.inpatient.registration',string='Identificación del paciente hospitalizado')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
