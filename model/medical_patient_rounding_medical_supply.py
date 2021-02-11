# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_patient_rounding_medical_supply(models.Model):
    _name = 'medical.patient.rounding.medical_supply'
    
    product_id = fields.Many2one('product.product',string="Suplemento médico",required=True)
    short_comment = fields.Char(string='Comentarios')
    quantity = fields.Integer(string="Cantidad")
    lot_id = fields.Many2one('stock.production.lot',string='Lote',required=True)
    medical_patient_rounding_medical_supply_id = fields.Many2one('medical.patient.rounding',string=" Suministros médicos ")

