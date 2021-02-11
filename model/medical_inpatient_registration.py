# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date,datetime

class medical_inpatient_registration(models.Model):
    _name = 'medical.inpatient.registration'

    name = fields.Char(string="Código de registro", copy=False, readonly=True, index=True)
    patient_id = fields.Many2one('medical.patient',string="Paciente",required=True)
    hospitalization_date = fields.Datetime(string="Fecha de hospitalización",required=True)
    discharge_date = fields.Datetime(string="Fecha de alta prevista",required=True)
    attending_physician_id = fields.Many2one('medical.physician',string="Médico asistente")
    operating_physician_id = fields.Many2one('medical.physician',string="Médico Operador")
    admission_type = fields.Selection([('routine','Rutina'),('maternity','Maternidad'),('elective','Electivo'),('urgent','Urgente'),('emergency','Emergencia  ')],required=True,string="Tipo de admisión")
    medical_pathology_id = fields.Many2one('medical.pathology',string="Motivo de admision")
    info = fields.Text(string="Información extra")
    bed_transfers_ids = fields.One2many('bed.transfer','inpatient_id',string='Cama de transferencia',readonly=True)
    medical_diet_belief_id = fields.Many2one('medical.diet.belief',string='Creencia')
    therapeutic_diets_ids = fields.One2many('medical.inpatient.diet','medical_inpatient_registration_id',string='Dietas_terapéuticas')
    diet_vegetarian = fields.Selection([('none','Ninguno'),('vegetarian','Vegetariano'),('lacto','Lacto vegetariano'),('lactoovo','Lacto-Ovo-Vegetarian'),('pescetarian','Pescetarian'),('vegan','Vegano')],string="Vegetariano")
    nutrition_notes = fields.Text(string="Notas nutricionales / Direcciones")
    state = fields.Selection([('free','Gratis'),('confirmed','Confirmado'),('hospitalized','Hospitalizado'),('cancel','Cancelado'),('done','Hecho')],string="Estado",default="free")
    nursing_plan = fields.Text(string="Plan de enfermería")
    discharge_plan = fields.Text(string="Plan de alta")
    icu = fields.Boolean(string="ICU")
    medication_ids = fields.One2many('medical.inpatient.medication','medical_inpatient_registration_id',string='Medicamento')

    @api.model
    def default_get(self, fields):
        result = super(medical_inpatient_registration, self).default_get(fields)
        patient_id  = self.env['ir.sequence'].next_by_code('medical.inpatient.registration')
        if patient_id:
            result.update({
                        'name':patient_id,
                       })
        return result

    @api.multi
    def registration_confirm(self):
        self.write({'state': 'confirmed'})

    @api.multi
    def registration_admission(self):
        self.write({'state': 'hospitalized'})

    @api.multi
    def registration_cancel(self):
        self.write({'state': 'cancel'})

    @api.multi
    def patient_discharge(self):
        self.write({'state': 'done'})


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
