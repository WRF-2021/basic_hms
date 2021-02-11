# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_medicament(models.Model):
  
    _name = 'medical.medicament'
    _rec_name = 'product_id'

    @api.multi
    @api.depends('product_id')
    def onchange_product(self):
        for each in self:
            if each:
                self.qty_available = self.product_id.qty_available
                self.price = self.product_id.lst_price
            else:
                self.qty_available = 0
                self.price = 0.0

    product_id  = fields.Many2one('product.product', 'Nombre')
    therapeutic_action = fields.Char('Efecto terapéutico', help = 'Therapeutic action')
    price = fields.Float(compute=onchange_product,string='Precio',store=True)
    qty_available = fields.Integer(compute=onchange_product,string='Cantidad disponible',store=True)
    indications = fields.Text('Indicaciones')
    active_component = fields.Char(string="Componente activo")
    presentation = fields.Text('Presentación')
    composition = fields.Text('Composición')
    dosage = fields.Text('Instrucciones de dosificación')
    pregnancy = fields.Text('Embarazo')
    overdosage = fields.Text('Sobredosis')
    pregnancy_warning = fields.Boolean('Advertencia de embarazo')
    pregnancy_category = fields.Selection([('a','A'),('b','B'), ('c','C'), ('d', 'D'), ('x', 'X'), ('n','N')], help = """"** FDA Pregancy Categories ***CATEGORY A :Adequate and well-controlled human studies have failed to demonstrate a risk to the fetus in the first trimester of pregnancy (and there is no evidence of risk in later trimesters)CATEGORY B : Animal reproduction studies have failed todemonstrate a risk to the fetus and there are no adequate and well-controlled studies in pregnant women OR Animal studies have shown an adverse effect, but adequate and well-controlled studies in pregnant women have failed to demonstrate a risk to the fetus in any trimester.

CATEGORY C : Animal reproduction studies have shown an adverse effect on the fetus and there are no adequate and well-controlled studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks. 

 CATEGORY D : There is positive evidence of human fetal  risk based on adverse reaction data from investigational or marketing experience or studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.

CATEGORY X : Studies in animals or humans have demonstrated fetal abnormalities and/or there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience, and the risks involved in use of the drug in pregnant women clearly outweigh potential benefits.

CATEGORY N : Not yet classified""")

    adverse_reaction = fields.Text('Adverse Reactions')
    storage = fields.Text('Condición de almacenamiento')
    notes = fields.Text('Información extra')

