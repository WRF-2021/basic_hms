# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_pathology(models.Model):
    _name = 'medical.pathology'

    name = fields.Char(string="Nombre",required=True)
    code = fields.Char(string="Codigo")
    category_id = fields.Many2one('medical.pathology.category',string="Categoría de enfermedad")
    line_ids = fields.One2many('medical.pathology.group.member','disease_group_id',string="Grupo")
    chromosome = fields.Char(string="Cromosoma afectado")
    gene = fields.Char(string="Gene")
    protein = fields.Char(string="Proteína")
    info = fields.Text(string="Información extra")