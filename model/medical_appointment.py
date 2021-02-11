# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
#from datetime import datetime, date
from datetime import datetime, timedelta
from odoo.exceptions import UserError

class medical_appointment(models.Model):
    _name = "medical.appointment"
    _inherit = 'mail.thread'

    name = fields.Char(string="ID de cita", readonly=True ,copy=True)
    is_invoiced = fields.Boolean(copy=False,default = False)
    institution_partner_id = fields.Many2one('res.partner',domain=[('is_institution','=',True)],string="Centro de salud")
    inpatient_registration_id = fields.Many2one('medical.inpatient.registration',string="Registro de pacientes hospitalizados")
    patient_status = fields.Selection([
            ('ambulatory', 'Ambulatory'),
            ('outpatient', 'Paciente externo'),
            ('inpatient', 'Paciente interno'),
        ], 'Estado del paciente', sort=False,default='outpatient')
    patient_id = fields.Many2one('medical.patient','Paciente',required=True)
    urgency_level = fields.Selection([
            ('a', 'Normal'),
            ('b', 'Urgente'),
            ('c', 'Emergencia Medica'),
        ], 'Nivel de urgencia', sort=False,default="b")
    appointment_date = fields.Datetime('Día de la cita',required=True,default = fields.Datetime.now)
    appointment_end = fields.Datetime('Fin de la cita',required=True)
    doctor_id = fields.Many2one('medical.physician','Médico',required=True)
    no_invoice = fields.Boolean(string='Exento Factura',default=True)
    validity_status = fields.Selection([
            ('invoice', 'Factura'),
            ('tobe', 'A facturar'),
        ], 'Estado', sort=False,readonly=True,default='tobe')
    appointment_validity_date = fields.Datetime('Fecha de validez')
    consultations_id = fields.Many2one('product.product','Servicio de consulta',required=True)
    comments = fields.Text(string="Info")
    state = fields.Selection([('draft','Borrador'),('confirmed','Confirmado'),('cancel','Cancelado'),('done','Hecho')],string="Estado",default='draft')
    invoice_to_insurer = fields.Boolean('Factura al seguro')
    medical_patient_psc_ids = fields.Many2many('medical.patient.psc',string='Lista de verificación de síntomas pediátricos')
    medical_prescription_order_ids = fields.One2many('medical.prescription.order','appointment_id',string='Prescripción')
    insurer_id = fields.Many2one('medical.insurance','Aseguradora')
    duration = fields.Integer('Duración')

    @api.onchange('patient_id')
    def onchange_name(self):
        ins_obj = self.env['medical.insurance']
        ins_record = ins_obj.search([('medical_insurance_partner_id', '=', self.patient_id.patient_id.id)])
        if len(ins_record)>=1:
            self.insurer_id = ins_record[0].id
        else:
            self.insurer_id = False

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('medical.appointment') or 'APT'
        msg_body = 'Appointment created'
        self.message_post(body=msg_body)
        result = super(medical_appointment, self).create(vals)
        return result

    @api.onchange('inpatient_registration_id')
    def onchange_patient(self):
        if not self.inpatient_registration_id:
            self.patient_id = ""
        inpatient_obj = self.env['medical.inpatient.registration'].browse(self.inpatient_registration_id.id)
        self.patient_id = inpatient_obj.id

    @api.multi
    def confirm(self):
        self.write({'state': 'confirmed'})

    @api.multi
    def done(self):
        self.write({'state': 'done'})

    @api.multi
    def cancel(self):
        self.write({'state': 'cancel'})

    @api.multi
    def print_prescription(self):
        return self.env.ref('basic_hms.report_print_prescription').report_action(self)


    @api.multi
    def view_patient_invoice(self):
        self.write({'state': 'cancel'})

    @api.multi
    def create_invoice(self):
        lab_req_obj = self.env['medical.appointment']
        account_invoice_obj  = self.env['account.invoice']
        account_invoice_line_obj = self.env['account.invoice.line']

        lab_req = lab_req_obj
        if lab_req.is_invoiced == True:
            raise UserError(_(' La factura ya existe'))
        if lab_req.no_invoice == False:
            res = account_invoice_obj.create({'partner_id': lab_req.patient_id.patient_id.id,
                                                   'date_invoice': date.today(),
                                             'account_id':lab_req.patient_id.patient_id.property_account_receivable_id.id,
                                             })

            res1 = account_invoice_line_obj.create({'product_id':lab_req.consultations_id.id ,
                                             'product_uom': lab_req.consultations_id.uom_id.id,
                                             'name': lab_req.consultations_id.name,
                                             'product_uom_qty':1,
                                             'price_unit':lab_req.consultations_id.lst_price,
                                             'account_id': lab_req.patient_id.patient_id.property_account_receivable_id.id,
                                             'invoice_id': res.id})

            if res:
                lab_req.write({'is_invoiced': True})
                imd = self.env['ir.model.data']
                action = imd.xmlid_to_object('account.action_invoice_tree1')
                list_view_id = imd.xmlid_to_res_id('account.view_order_form')
                result = {
                                'name': action.name,
                                'help': action.help,
                                'type': action.type,
                                'views': [ [list_view_id,'form' ]],
                                'target': action.target,
                                'context': action.context,
                                'res_model': action.res_model,
                                'res_id':res.id,
                            }
                if res:
                    result['domain'] = "[('id','=',%s)]" % res.id
        else:
             raise UserError(_(' La cita está exenta de factura'))
        return result

        
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
