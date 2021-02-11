# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_signs_and_sympotoms(models.Model):
    _name = 'medical.signs.and.sympotoms'
    _rec_name = 'pathology_id'

    patient_evaluation_id = fields.Many2one('medical.patient.evaluation','Evaluación del paciente')
    pathology_id = fields.Many2one('medical.pathology','Signo o síntoma')
    sign_or_symptom = fields.Selection([
            ('sign', 'Firmar'),
            ('symptom', 'Síntoma'),
        ], string='Subjetivo / objetivo')
    comments = fields.Char('Comentarios')


