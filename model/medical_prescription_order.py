# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_prescription_order(models.Model):
    _name = "medical.prescription.order"

    name = fields.Char('ID de prescripción')
    patient_id = fields.Many2one('medical.patient','ID del paciente')
    prescription_date = fields.Datetime('Fecha de prescripción', default=fields.Datetime.now)
    user_id = fields.Many2one('res.users','Login User',readonly=True, default=lambda self: self.env.user)
    no_invoice = fields.Boolean('Exención de factura')
    inv_id = fields.Many2one('account.invoice','Factura')
    invoice_to_insurer = fields.Boolean('Factura al seguro')
    doctor_id = fields.Many2one('medical.physician','Doctor que prescribe')
    medical_appointment_id = fields.Many2one('medical.appointment','Cita')
    state = fields.Selection([('invoiced','To Invoiced'),('tobe','To Be Invoiced')], 'Estado de la factura')
    pharmacy_partner_id = fields.Many2one('res.partner',domain=[('is_pharmacy','=',True)], string='Farmacia')
    prescription_line_ids = fields.One2many('medical.prescription.line','name','Línea de prescripción')
    invoice_done= fields.Boolean('Factura completada')
    notes = fields.Text('Nota de prescripción')
    appointment_id = fields.Many2one('medical.appointment')
    is_invoiced = fields.Boolean(copy=False,default = False)
    insurer_id = fields.Many2one('medical.insurance', 'Aseguradora')
    is_shipped = fields.Boolean(default  =  False,copy=False)


    @api.model
    def create(self , vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('medical.prescription.order') or '/'
        return super(medical_prescription_order, self).create(vals)


    @api.multi
    def prescription_report(self):
        return self.env.ref('basic_hms.report_print_prescription').report_action(self)

    @api.onchange('name')
    def onchange_name(self):
        ins_obj = self.env['medical.insurance']
        ins_record = ins_obj.search([('medical_insurance_partner_id', '=', self.patient_id.patient_id.id)])
        self.insurer_id = ins_record.id or False

    @api.onchange('name')
    def onchange_p_name(self):
        self.pricelist_id = 1 or False


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
