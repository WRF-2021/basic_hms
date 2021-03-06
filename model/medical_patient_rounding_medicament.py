# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_patient_rounding_medicament(models.Model):
    _name = 'medical.patient.rounding.medicament'
    
    medicament_id = fields.Many2one('medical.medicament',string='Medicamento',required=True)
    quantity = fields.Integer(string="Cantidad")
    lot_id = fields.Many2one('stock.production.lot',string='Lote',required=True)
    short_comment = fields.Char(string='Comentarios')
    product_id = fields.Many2one('product.product',string='Producto')
    medical_patient_rounding_medicament_id = fields.Many2one('medical.patient.rounding',string="Medicamentos") 

