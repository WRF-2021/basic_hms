# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_prescription_line(models.Model):
    _name = "medical.prescription.line"

    name = fields.Many2one('medical.prescription.order','ID de prescripción')
    medicament_id = fields.Many2one('medical.medicament','Medicamento')
    indication = fields.Char('Indicación')
    allow_substitution = fields.Boolean('Permitir sustitución')
    form = fields.Char('Formulario')
    prnt = fields.Boolean('Impresión')
    route = fields.Char('Ruta de administración')
    end_treatement  = fields.Datetime('Ruta de administración')
    dose = fields.Float('Dosis')
    dose_unit_id = fields.Many2one('medical.dose.unit', 'Unidad de dosis')
    qty = fields.Integer('x')
    medication_dosage_id = fields.Many2one('medical.medication.dosage','Frecuencia')
    admin_times = fields.Char('Horas de administración', size = 128)
    frequency = fields.Integer('Frecuencia')
    frequency_unit = fields.Selection([('seconds','Segundos'),('minutes','Minutos'),('hours','hours'),('days','Dias'),('weeks','Semanas'),('wr','Cuando se requiere')], 'Unidad')
    duration = fields.Integer('Treatment Duration')
    duration_period = fields.Selection([('minutes','Minutos'),('hours','Horas'),('days','Dias'),('months','Meses'),('years','Años'),('indefine','Indefinido')],'Periodo de tratamiento')
    quantity = fields.Integer('Cantidad')
    review = fields.Datetime('revisión')
    refills = fields.Integer('Recargas#')
    short_comment = fields.Char('Comentario', size=128 )
    end_treatment = fields.Datetime('Fin del tratamiento')
    start_treatment = fields.Datetime('Inicio del tratamiento')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
