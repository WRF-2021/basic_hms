# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_family_disease(models.Model):
    _name = 'medical.family.disease'
    _rec_name = 'medical_pathology_id'

    medical_pathology_id = fields.Many2one('medical.pathology', 'Enfermedad',required=True)
    relative = fields.Selection([('m','Mama'), ('f','Papa'), ('b', 'Hermano'), ('s', 'Hermana'), ('a', 'Tía'), ('u', 'Tio'), ('ne', 'Sobrino'), ('ni', 'Sobrina'), ('gf', 'Abuelo'), ('gm', 'GrandMother')],string="Pariente")
    metrnal = fields.Selection([('m', 'Maternal'),('p', 'Paternal')],string="Pariente")


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: