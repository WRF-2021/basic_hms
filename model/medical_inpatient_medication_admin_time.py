# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date,datetime

class medical_inpatient_medication_admin_time(models.Model):
    _name = 'medical.inpatient.medication.admin.time'

    admin_time = fields.Datetime(string='Fecha')
    dose = fields.Float(string='Dosis')
    remarks = fields.Text(string='Observaciones')
    medical_inpatient_admin_time_id = fields.Many2one('medical.physician',string='Profesional de la salud')
    dose_unit = fields.Many2one('medical.dose.unit',string='Dosis Unidad')
    medical_inpatient_admin_time_medicament_id = fields.Many2one('medical.inpatient.medication',string='Hora de administración')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
