# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_preinatal(models.Model):
    
    _name = 'medical.preinatal'
    
    pregnency_id = fields.Many2one('medical.patient.pregnency', 'Embarazo', )
    gestational_weeks = fields.Integer('Semanas gestacionales')
    admission_date = fields.Date('Fecha de admisión')
    code  = fields.Char('Codigo')
    labour_mode = fields.Selection([('n','Normal'),('i','Inducido'),('c','Cesárea')], 'Modo de trabajo')
    fetus_presentation = fields.Selection([('n','Correcto'),
                                         ('o','Occipucio / Postrior cefálico'),
                                         ('fb','Frank Breech'),
                                         ('cb','Nalgas completas'),
                                         ('tl','Mentira transversal'),
                                         ('fu','Footling Lie')], 'Presentación del feto')
    monitor_ids = fields.One2many('medical.perinatal.monitor','medical_perinatal_id')
    dystocia = fields.Boolean('Distocia')
    episiotomy = fields.Boolean('Episiotomía')
    lacerations = fields.Selection([('p','Perinial'),
                                      ('v','Vaginal'),
                                      ('c','Cervical'),
                                      ('bl', 'Broad Ligament'),
                                      ('vl','Vulvar'),
                                      ('r','Rectal'),
                                      ('br','Blader'),
                                      ('u','Ureteral'),  ],'Laceraciones')
    
    
    hematoma = fields.Selection( [('v','Vaginal'), ('vl','Vulvar'),('r','Retropericional')], 'Hematoma')
    plancenta_incomplete = fields.Boolean('Placenta incompleta')
    retained_placenta = fields.Boolean('Placenta retenida')
    abruptio_placentae = fields.Boolean('Desprendimiento de placenta')
    
       

    notes= fields.Text('Notas')


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
