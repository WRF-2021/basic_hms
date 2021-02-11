# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_diseases(models.Model):
    _name = 'medical.patient.diseases'
    
    pathelogh_id = fields.Many2one('medical.pathology', 'Enfermedad')
    status_of_the_disease = fields.Selection([('chronic','Crónica'),('status quo','Estatus Quo'),('healed','Sanado'), ('improving','Mejorando'), ('worsening', 'Empeoramiento') ], 'Estado de la enfermedad')
    is_active = fields.Boolean('Enfermedad activa')
    diagnosed_date = fields.Date('Fecha de diagnóstico')
    age = fields.Date('Edad al momento del diagnóstico')
    disease_severity = fields.Selection([('mild','Leve'), ('moderate','Moderado'), ('severe','Severo')], 'Gravedad')
    is_infectious = fields.Boolean('Enfermedad infecciosa', help = 'Check if the patient has an infectious / transmissible disease')
    short_comment = fields.Char('Observaciones')
    healed_date = fields.Date('Sanado')
    physician_id = fields.Many2one('medical.patient','Doctor')
    is_allergy = fields.Boolean('Enfermedad alérgica')
    is_infectious = fields.Boolean('Enfermedad infecciosa')
    allergy_type  = fields.Selection([('drug_allergy', 'Alergia a un medicamento'),('food_allergy', 'Alergia a la comida'),('misc', 'Misc')], 'Allergy_type')
    pregnancy_warning = fields.Boolean('Advertencia de embarazo')
    weeks_of_pregnancy = fields.Integer('Detectado en la semana del embarazo #')
    is_on_treatment = fields.Boolean('Actualmente en tratamiento')
    treatment_description = fields.Char('Descripción del tratamiento')
    date_start_treatment = fields.Date('Inicio del tratamiento')
    date_stop_treatment = fields.Date('Fin del tratamiento')
    psc_code_id = fields.Many2one('psc.code', 'Codigo')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:    