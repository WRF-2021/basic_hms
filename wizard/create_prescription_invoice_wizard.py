# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
from odoo.exceptions import Warning

class create_prescription_invoice(models.TransientModel):
    _name = 'create.prescription.invoice'

    @api.multi
    def create_prescription_invoice(self):
        active_ids = self._context.get('active_ids')
        active_ids = active_ids or False
        lab_req_obj = self.env['medical.prescription.order']
        
        #Modelo factura
        #account_invoice_obj  = self.env['account.invoice']
        account_invoice_obj  = self.env['sale.order']
        #modelo linea de factura
        #account_invoice_line_obj = self.env['account.invoice.line']
        account_invoice_line_obj = self.env['sale.order.line']

        ir_property_obj = self.env['ir.property']
        inv_list =[]
        lab_reqs = lab_req_obj.browse(active_ids)
        for lab_req in lab_reqs:
            if len(lab_req.prescription_line_ids) < 1:
                self.env.user.notify_warning(message='Se requiere al menos una línea de productos.')
                break
                #raise Warning('Se requiere al menos una línea de productos.')

            if lab_req.is_invoiced == True:
                self.env.user.notify_info(message='Esta orden de venta ya esta creada')
                break
                #raise Warning('Esta orden de venta ya esta creada.')
            
            
            invoice_vals = {
            'origin': lab_req.name or '',
            'reference': False,
            'partner_id': lab_req.patient_id.patient_id.id,
            'validity_date': date.today(),
            'partner_shipping_id':lab_req.patient_id.patient_id.id,
            'currency_id':lab_req.patient_id.patient_id.currency_id.id ,
            'payment_term_id': False,
            'fiscal_position_id': lab_req.patient_id.patient_id.property_account_position_id.id,
            'note': "Orden de venta creada a partir de una prescripcion médica",
            'company_id':lab_req.patient_id.patient_id.company_id.id or False ,
            }

            res = account_invoice_obj.create(invoice_vals)
            for p_line in lab_req.prescription_line_ids: 
            
                tax_ids = []
                taxes = p_line.medicament_id.product_id.taxes_id.filtered(lambda r: not p_line.medicament_id.product_id.company_id or r.company_id == p_line.medicament_id.product_id.company_id)
                tax_ids = taxes.ids
                
                invoice_line_vals = {
                    'product_id':p_line.medicament_id.product_id.id ,
                    'name': p_line.medicament_id.product_id.display_name or '',
                    'product_uom_qty': p_line.quantity,
                    'price_unit':p_line.medicament_id.product_id.lst_price,
                    'tax_id': [(6, 0, tax_ids)],
                    'order_id': res.id,
                    }

                account_invoice_line_obj.create(invoice_line_vals)  
            
            if res:
               lab_reqs.write({'is_invoiced': True})
               #raise Warning('0rden de venta creada correctamente.')
               self.env.user.notify_success(message='0rden de venta creada correctamente.')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
