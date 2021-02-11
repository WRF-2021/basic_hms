# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_pediatrics_growth_charts_who(models.Model):
    _name = 'medical.pediatrics.growth.charts.who'
    
    name = fields.Selection([
                             ('l/h-f-a','Longitud / altura para la edad'),
                             ('w-f-a','Peso por edad'),
                             ('bmi-f-a','Índice de masa corporal para la edad (IMC para la edad)')],
                            string='Indicador')
    sex = fields.Selection([('m','Masculino'),('f','Femenino ')],string='Genero')
    measure = fields.Selection([('p','percentil'),('z','Puntuaciones Z')],string='Medida')
    type = fields.Char(string="Tipo")
    month = fields.Integer(string="Meses")
    value = fields.Float(string='Valor')