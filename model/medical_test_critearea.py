# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
# classes under cofigration menu of laboratry 

class medical_test_critearea(models.Model):
    _name  = 'medical_test.critearea'

    test_id = fields.Many2one('medical.test_type',)
    name = fields.Char('Nombre',)
    seq = fields.Integer('Secuencia', default=1)
    medical_test_type_id = fields.Many2one ('medical.test_type', 'Tipo de prueba')
    medical_lab_id = fields.Many2one('medical.lab', 'Resultado de laboratorio médico')
    warning  = fields.Boolean('Advertencia')
    excluded  = fields.Boolean('Excluido')
    lower_limit = fields.Float('Límite inferior')
    upper_limit = fields.Float('Limite superior')
    lab_test_unit_id = fields.Many2one('medical.lab.test.units', 'Unidades')
    result = fields.Float('Resultado')
    result_text =  fields.Char('Texto de resultado')
    normal_range =  fields.Char('Rango normal')
    remark = fields.Text('Observaciones')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:    
