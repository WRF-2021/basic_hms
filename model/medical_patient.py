# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta 

class medical_patient(models.Model):
    
    _name = 'medical.patient'
    _rec_name = 'patient_id'

    @api.onchange('patient_id')
    def _onchange_patient(self):
        '''
        The purpose of the method is to define a domain for the available
        purchase orders.
        '''
        address_id = self.patient_id
        self.partner_address_id = address_id

    @api.multi
    def print_report(self):
        return self.env.ref('basic_hms.report_print_patient_card').report_action(self)

    @api.depends('date_of_birth')
    def onchange_age(self):
        for rec in self:
            if rec.date_of_birth:
                d1 = rec.date_of_birth
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years) + "y" +" "+ str(rd.months) + "m" +" "+ str(rd.days) + "d"
            else:
                rec.age = "Sin fecha de nacimiento!!"

    
    patient_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Paciente", required= True)
    #Campo agregar por ariel para la info de familia
    medical_patient_familia_ids = fields.One2many('patient.familia','medical_patient_familia_id')
  
    name = fields.Char(string='Numero expediente', readonly=True)
    numero_identidad = fields.Char(string='Numero ID')
    last_name = fields.Char('Apellido')
    date_of_birth = fields.Date(string="Fecha de nacimiento")
    sex = fields.Selection([('m', 'Masculino'),('f', 'Femenino')], string ="Sexo")
    age = fields.Char(compute=onchange_age,string="Edad del paciente",store=True)
    critical_info = fields.Text(string="Información crítica para el paciente")
    photo = fields.Binary(string="Imagen")
    blood_type = fields.Selection([('A', 'A'),('B', 'B'),('AB', 'AB'),('O', 'O')], string ="Tipo de sangre")
    rh = fields.Selection([('-+', '+'),('--', '-')], string ="Rh")
    marital_status = fields.Selection([('s','Soltero'),('m','Casado'),('w','Viudo(a)'),('d','Divorciado(a)'),('x','Seperado(a)'),('ul','Union Libre') ],string='Estado Civil')
    deceased = fields.Boolean(string='Fallecido(a)')
    date_of_death = fields.Datetime(string="Fecha de muerte")
    cause_of_death = fields.Char(string='Causa de la muerte')
    receivable = fields.Float(string="Cuenta por cobrar", readonly=True)
    current_insurance_id = fields.Many2one('medical.insurance',string="Seguro")
    partner_address_id = fields.Many2one('res.partner', string="Direccion", )
    primary_care_physician_id = fields.Many2one('medical.physician', string="Doctor de atención primaria")
    patient_status = fields.Char(string="Estado de hospitalización",readonly=True)
    patient_disease_ids = fields.One2many('medical.patient.disease','patient_id')
    
    patient_psc_ids = fields.One2many('medical.patient.psc','patient_id')
    excercise = fields.Boolean(string='Ejercicio')
    excercise_minutes_day = fields.Integer(string="Minutos / día")
    sleep_hours = fields.Integer(string="Horas de sueño")
    sleep_during_daytime = fields.Boolean(string="Dormir durante el día")
    number_of_meals = fields.Integer(string="Comidas por dia")
    coffee = fields.Boolean('café')
    coffee_cups = fields.Integer(string='Tazas por día')
    eats_alone = fields.Boolean(string="Come solo")
    soft_drinks = fields.Boolean(string="Refrescos (azúcar)")
    salt = fields.Boolean(string="sal")
    diet = fields.Boolean(string=" Actualmente a dieta ")
    diet_info = fields.Integer(string=' Información de dieta ')
    general_info = fields.Text(string="Info")
    lifestyle_info = fields.Text('Información de estilo de vida')
    smoking = fields.Boolean(string="Fuma")
    smoking_number = fields.Integer(string="Cigarretes al día")
    ex_smoker = fields.Boolean(string="Ex-fumador")
    second_hand_smoker = fields.Boolean(string="Fumador pasivo")
    age_start_smoking = fields.Integer(string="La edad empezó a fumar")
    age_quit_smoking = fields.Integer(string="Edad para dejar de fumar")
    drug_usage = fields.Boolean(string='Hábitos de drogas')
    drug_iv = fields.Boolean(string='Usuario de drogas intravenosas')
    ex_drug_addict = fields.Boolean(string='Ex drogadicto')
    age_start_drugs = fields.Integer(string='Edad comenzó a tomar drogas')
    age_quit_drugs = fields.Integer(string="Edad dejar las drogas")
    alcohol = fields.Boolean(string="Bebidas Alcohol")
    ex_alcohol = fields.Boolean(string="Ex alcohólico")
    age_start_drinking = fields.Integer(string="La edad empezó a beber")
    age_quit_drinking = fields.Integer(string="Edad dejar de beber")
    alcohol_beer_number = fields.Integer(string="Cerveza / día")
    alcohol_wine_number = fields.Integer(string="Vino / día")
    alcohol_liquor_number = fields.Integer(string="Licor / día")
    cage_ids = fields.One2many('medical.patient.cage','patient_id')
    sex_oral = fields.Selection([('0','None'),
                                 ('1','Activo'),
                                 ('2','Pasivo'),
                                 ('3','Ambos')],string='Sexo oral')
    sex_anal = fields.Selection([('0','None'),
                                 ('1','Activo'),
                                 ('2','Pasivo'),
                                 ('3','Ambos')],string='Sexo anal')
    prostitute = fields.Boolean(string='Trabajador/a Sexual')
    sex_with_prostitutes = fields.Boolean(string=' Sexo con trabajador/a Sexual ')
    sexual_preferences = fields.Selection([
            ('h', 'Heterosexual'),
            ('g', 'Homosexual'),
            ('b', 'Bisexual'),
            ('t', 'Transexual'),
        ], 'Orientacion Sexual', sort=False)
    sexual_practices = fields.Selection([
            ('s', 'Safe / Protected sex'),
            ('r', 'Risky / Unprotected sex'),
        ], 'Practicas sexuales', sort=False)
    sexual_partners = fields.Selection([
            ('m', 'Monógamo'),
            ('t', 'Polígamo'),
        ], 'Parejas sexuales', sort=False)
    sexual_partners_number = fields.Integer('Número de parejas sexuales')
    first_sexual_encounter = fields.Integer('Edad primer encuentro sexual')
    anticonceptive = fields.Selection([
            ('0', 'Ninguno'),
            ('1', 'Píldora / Minipíldora'),
            ('2', 'Condón masculino'),
            ('3', 'Vasectomia'),
            ('4', 'Esterilización femenina'),
            ('5', 'Dispositivo intrauterino'),
            ('6', 'Método de retiro'),
            ('7', 'Conciencia del ciclo de la fertilidad'),
            ('8', 'Inyección anticonceptiva'),
            ('9', 'Parche de piel'),
            ('10', 'Condón femenino'),
            ('11', 'Implante Anticonceptivo'),
        ], 'Método anticonceptivo', sort=False)
    sexuality_info = fields.Text('Información extra')
    motorcycle_rider = fields.Boolean('Motociclista', help="The patient rides motorcycles")
    helmet = fields.Boolean('Usa casco', help="The patient uses the proper motorcycle helmet")
    traffic_laws = fields.Boolean('Obedece las leyes de tráfico', help="Check if the patient is a safe driver")
    car_revision = fields.Boolean('Revisión del coche', help="Maintain the vehicle. Do periodical checks - tires,breaks ...")
    car_seat_belt = fields.Boolean('Cinturón de seguridad', help="Safety measures when driving : safety belt")
    car_child_safety = fields.Boolean('Seguridad infantil en el automóvil', help="Safety measures when driving : child seats, proper seat belting, not seating on the front seat, ....")
    home_safety = fields.Boolean('Seguridad del hogar', help="Keep safety measures for kids in the kitchen, correct storage of chemicals, ...")
    fertile = fields.Boolean('Fértil')
    menarche = fields.Integer('Edad de la menarquia')
    menopausal = fields.Boolean('Menopáusico')
    menopause = fields.Integer('Edad de la menopausia')
    menstrual_history_ids = fields.One2many('medical.patient.menstrual.history','patient_id')
    breast_self_examination = fields.Boolean('Autoexamen de mama')
    mammography = fields.Boolean('Mamografía')
    pap_test = fields.Boolean('PAP test')
    last_pap_test = fields.Date('Last PAP test')
    colposcopy = fields.Boolean('Colposcopia')
    mammography_history_ids = fields.One2many('medical.patient.mammography.history','patient_id')
    pap_history_ids = fields.One2many('medical.patient.pap.history','patient_id')
    colposcopy_history_ids = fields.One2many('medical.patient.colposcopy.history','patient_id')
    pregnancies = fields.Integer('Embarazos')
    premature = fields.Integer('Prematuro')
    inmaduro = fields.Integer('Inmaduro')
    stillbirths = fields.Integer('Stillbirths')
    abortions = fields.Integer('Abortos')
    pregnancy_history_ids = fields.One2many('medical.patient.pregnency','patient_id')
    family_history_ids = fields.Many2many('medical.family.disease',string="Líneas de enfermedades familiares")
    perinatal_ids = fields.Many2many('medical.preinatal')
    ex_alcoholic = fields.Boolean('Ex alcohólico')
    currently_pregnant = fields.Boolean('Actualmente embarazada')
    born_alive = fields.Integer('Nacido Vivo')
    gpa = fields.Char('Ultimo embarazo')
    works_at_home = fields.Boolean('Trabaja en casa')
    colposcopy_last = fields.Date('Última colposcopia')
    mammography_last = fields.Date('Última mamografía')
    notas_embarazo = fields.Text(string="Información extra")
    ses = fields.Selection([
            (None, ''),
            ('0', 'Bajo'),
            ('1', 'Bajo medio'),
            ('2', 'Medio'),
            ('3', 'Medio-alto'),
            ('4', 'Alto'),
        ], 'Nivel Social', help="SES - Socioeconomic Status", sort=False)
    education = fields.Selection([('o','None'),('1','Escuela primaria incompleta'),
                                  ('2','Escuela primaria'),
                                  ('3','Escuela secundaria incompleta'),
                                  ('4','Escuela secundaria'),
                                  ('5','Universidad')],string='Nivel Educativo')
    housing = fields.Selection([
            (None, ''),
            ('0', 'vivienda de materiales de desechos'),
            ('1', 'Pequeño, hacinamiento con buenas condiciones.'),
            ('2', 'Vivienda pequeña de madera/adobe/bahareque.'),
            ('3', 'Pequeño, piso de tierra y/o fogón.'),
            ('4', 'Cómodas y buenas condiciones sanitarias'),
            ('5', 'Amplias y excelentes condiciones sanitarias.'),
            ('6', 'Lujo y excelentes condiciones sanitarias'),
        ], 'Condiciones de vivienda', help="Housing and sanitary living conditions", sort=False)
    works = fields.Boolean('Trabajos')
    hours_outside = fields.Integer('Horas fuera de casa', help="Number of hours a day the patient spend outside the house")
    hostile_area = fields.Boolean('Zona hostil')
    notes = fields.Text(string="Información extra")
    sewers = fields.Boolean('Alcantarillas Sanitarias')
    water = fields.Boolean('Agua potable')
    trash = fields.Boolean('Recolección de basura')
    electricity = fields.Boolean('Suministro eléctrico')
    gas = fields.Boolean('Fecalismo al aire libre')
    telephone = fields.Boolean('Teléfono')
    television = fields.Boolean('Letrinas')
    internet = fields.Boolean('Internet')
    single_parent= fields.Boolean('Familia monoparental')
    domestic_violence = fields.Boolean('Domestic violence')
    working_children = fields.Boolean('Niños trabajadores')
    teenage_pregnancy = fields.Boolean('Embarazo en la adolescencia')
    sexual_abuse = fields.Boolean('Abuso sexual')
    drug_addiction = fields.Boolean('Drogadicción')
    school_withdrawal = fields.Boolean('Retiro escolar')
    prison_past = fields.Boolean('Ha estado en prisión')
    prison_current = fields.Boolean('Está actualmente en prisión')
    relative_in_prison = fields.Boolean('Pariente en prisión', help="Check if someone from the nuclear family - parents sibblings  is or has been in prison")
    fam_apgar_help = fields.Selection([
            (None, ''),
            ('0', 'Ninguno'),
            ('1', 'Moderadamente'),
            ('2', 'Mucho'),
        ], 'Ayuda de la familia',
            help="Is the patient satisfied with the level of help coming from the family when there is a problem ?", sort=False)
    fam_apgar_discussion = fields.Selection([
            (None, ''),
            ('0', 'Ninguno'),
            ('1', 'Moderadamente'),
            ('2', 'Mucho'),
        ], 'Discusión de problemas',
            help="Is the patient satisfied with the level talking over the problems as family ?", sort=False)
    fam_apgar_decisions = fields.Selection([
            (None, ''),
            ('0', 'Ninguno'),
            ('1', 'Moderadamente'),
            ('2', 'Mucho'),
        ], 'Toma de decisiones',
            help="Is the patient satisfied with the level of making important decisions as a group ?", sort=False)
    fam_apgar_timesharing = fields.Selection([
            (None, ''),
            ('0', 'Ninguno'),
            ('1', 'Moderadamente'),
            ('2', 'Mucho'),
        ], 'Tiempo compartido',
            help="Is the patient satisfied with the level of time that they spend together ?", sort=False)
    fam_apgar_affection = fields.Selection([
            (None, ''),
            ('0', 'Ninguno'),
            ('1', 'Moderadamente'),
            ('2', 'Mucho'),
        ], 'Afecto familiar',
            help="Is the patient satisfied with the level of affection coming from the family ?", sort=False)
    fam_apgar_score = fields.Integer('Puntuación', help="Total Family APGAR 7 - 10 : Functional Family 4 - 6  : Some level of disfunction \n"
                                          "0 - 3  : Severe disfunctional family \n")
    lab_test_ids = fields.One2many('medical.patient.lab.test','patient_id')
    fertile = fields.Boolean('Fértil')
    menarche_age  = fields.Integer('Edad de la menarquia')
    menopausal = fields.Boolean('Menopausico')
    pap_test_last = fields.Date('Last PAP Test')
    colposcopy = fields.Boolean('Colposcopia')
    gravida = fields.Integer('Embarazos')
    medical_vaccination_ids = fields.One2many('medical.vaccination','medical_patient_vaccines_id')
    medical_appointments_ids = fields.One2many('medical.appointment','patient_id',string='Appointments')
    lastname = fields.Char('Apellido')
    report_date = fields.Date('Fecha',default = datetime.today().date())
    medication_ids = fields.One2many('medical.patient.medication1','medical_patient_medication_id')
    deaths_2nd_week = fields.Integer('Fallecido después de la segunda semana')
    deaths_1st_week = fields.Integer('Fallecido después de la 1ra semana')
    full_term = fields.Integer('A término')
    ses_notes = fields.Text('Notas')
    seguridad_notes = fields.Text('Notas')

    @api.model
    def create(self,val):
        appointment = self._context.get('appointment_id')
        res_partner_obj = self.env['res.partner']
        if appointment:
            val_1 = {'name': self.env['res.partner'].browse(val['patient_id']).name}
            patient= res_partner_obj.create(val_1)
            val.update({'patient_id': patient.id})
        if val.get('date_of_birth'):
            dt = val.get('date_of_birth')
            d1 = datetime.strptime(str(dt), "%Y-%m-%d").date()
            d2 = datetime.today().date()
            rd = relativedelta(d2, d1)
            age = str(rd.years) + "y" +" "+ str(rd.months) + "m" +" "+ str(rd.days) + "d"
            val.update({'age':age} )

        patient_id  = self.env['ir.sequence'].next_by_code('medical.patient')
        if patient_id:
            val.update({
                        'name':patient_id,
                       })
        result = super(medical_patient, self).create(val)
        return result

# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
