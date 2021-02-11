# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
 
from odoo import api, fields, models, _
 
class medical_patient_rounding(models.Model):
    _name = "medical.patient.rounding"
    _rec_name = 'medical_inpatient_registration'

    @api.onchange('right_pupil','left_pupil')
    def onchange_duration(self):
        if self.left_pupil == self.right_pupil:
            self.anisocoria = False
        else:
            self.anisocoria = True
     
    medical_inpatient_registration = fields.Many2one('medical.inpatient.registration',string="Código de registro",required=True)
    health_physician_id = fields.Many2one('medical.physician',string="Profesional de la salud",readonly=True)
    evaluation_start = fields.Datetime(string="Inicio",required=True)
    evaluation_end = fields.Datetime(string="Fin",required=True)
    environmental_assessment = fields.Char(string='Medio ambiente')
    icu_patient = fields.Boolean(string='ICU')
    warning = fields.Boolean(string='Advertencia')
    pain = fields.Boolean(string='Dolor')
    potty = fields.Boolean(string='Orinal')
    position = fields.Boolean(string='Posicion')
    proximity = fields.Boolean(string='Proximidad')
    pump = fields.Boolean(string='Zapatillas')
    personal_needs = fields.Boolean(string='Necesidades personales')
    temperature =fields.Float(string='Temperatura')
    systolic = fields.Integer(string="Presión sistólica")
    diastolic = fields.Integer(string='Presión diastólica')
    bpm = fields.Integer(string='Ritmo cardiaco')
    respiratory_rate = fields.Integer(string="La frecuencia respiratoria")
    osat = fields.Integer(string="Saturación de oxígeno")
    diuresis = fields.Integer(string="Diuresis")
    urinary_catheter = fields.Boolean(string="Catéter urinario")
    glycemia = fields.Integer(string="Glicemia")
    depression = fields.Boolean(string="Signos de depresión")
    evolution = fields.Selection([('n','Estatus Quo'),
                                  ('i','Mejorando'),
                                  ('w','Empeoramiento')],
                                 string="Evolución")
    round_summary = fields.Text(string="Resumen de la ronda")
    gcs = fields.Many2one("medical.icu.glasgow",string="GCS")
    right_pupil = fields.Integer(string="R")
    pupillary_reactivity = fields.Selection([('brisk','Enérgico'),
                                             ('sluggish','Lento'),
                                             ('nonreactive','No reactivo')],
                                            string="Reactividad pupilar")
    pupil_dilation = fields.Selection([('normal','Normanl'),
                                       ('miosis','Miosis'),
                                       ('mydriasis','Midriasis')],
                                      string="Dilatación de pupila")
    left_pupil = fields.Integer(string="l")
    anisocoria = fields.Boolean(string="Anisocoria")
    pupil_consensual_resp  = fields.Boolean(string=" Respuesta consensuada ")
    oxygen_mask = fields.Boolean(string='Mascara de oxigeno')
    respiration_type = fields.Selection([('regular','Regular'),
                                         ('deep','Profundo'),
                                         ('shallow','Superficial'),
                                         ('labored','Trabajado'),
                                         ('intercostal','Intercostal')],
                                        string="Respiración")
    peep = fields.Boolean(string='Peep')
    sce = fields.Boolean(string='SCE')
    lips_lesion = fields.Boolean(string="Lesión de labios")
    fio2  = fields.Integer(string="FiO2")
    trachea_alignment  = fields.Selection([('midline','Línea media'),
                                           ('right','Derecha desviada'),
                                           ('left','Izquierda desviada')],
                                          string=' Alineación traqueal')
    oral_mucosa_lesion = fields.Boolean(string=' Lesión de la mucosa oral ')
    chest_expansion = fields.Selection([('symmentric','Simétrico'),
                                        ('asymmentric','Asimétrico')],
                                       string="Expansión")
    paradoxical_expansion = fields.Boolean(string="Paradójico")
    tracheal_tug = fields.Boolean(string='Remolcador traqueal')
    xray = fields.Binary(string="Xray")
    chest_drainages = fields.One2many('medical.icu.chest_drainage','medical_patient_rounding_chest_drainage_id',string="Drenajes de pecho")
    ecg = fields.Many2one('medical.icu.ecg',string="ECG")
    venous_access = fields.Selection([('none','Ninguno'),
                                      ('central','Central Catheter'),
                                      ('peripheral','Peripheral')],
                                     string="Acceso venoso")
    swan_ganz = fields.Boolean(string='Swan Ganz')
    arterial_access = fields.Boolean(string='Acceso arterial')
    dialysis = fields.Boolean(string="Diálisis")
    edema = fields.Selection([('none','Ninguno'),
                              ('peripheral','Peripheral'),
                              ('anasarca','Anasarca')],
                             string='Edema')
    bacteremia = fields.Boolean(string="Bacteriemia")
    ssi = fields.Boolean(string='Infección en el lugar de la cirugía')
    wound_dehiscence = fields.Boolean(string='Dehiscencia de la herida')
    cellulitis = fields.Boolean(string="Celulitis")
    necrotizing_fasciitis = fields.Boolean(string=' La fascitis necrotizante')
    vomiting = fields.Selection([('none','Ninguno'),
                                 ('vomiting','Vómitos'),
                                 ('hematemesis','Hematemesis ')],
                                string="Vómitos")
    bowel_sounds = fields.Selection([('normal','Normal'),
                                     ('increased','Aumentado'),
                                     ('decreased','Disminuido'),
                                     ('absent','Ausente')],
                                    string="Sonidos intestinales")
    stools = fields.Selection([('normal','Normal'),
                               ('constipation','Estreñimiento'),
                               ('diarrhea','Diarrea'),
                               ('melena','Melena')],
                              string="Taburetes")
    peritonitis = fields.Boolean(string="Peritonitis")
    procedures_ids = fields.One2many('medical.rounding_procedure','medical_patient_rounding_procedure_id',string="Procedimientos")
    hospital_location_id = fields.Many2one('stock.location',string='Lugar de hospitalización')
    medicaments_ids = fields.One2many('medical.patient.rounding.medicament','medical_patient_rounding_medicament_id',string="Medicamentos")
    medical_supplies_ids = fields.One2many('medical.patient.rounding.medical_supply','medical_patient_rounding_medical_supply_id',string='Proveedor médico')
    vaccines_ids = fields.One2many('medical.patient.rounding.vaccine','medical_patient_rounding_vaccine_id',string='Vacunas')
    state = fields.Selection([('draft','Sequía'),
                              ('done','Hecho')],
                             string="Estado")

