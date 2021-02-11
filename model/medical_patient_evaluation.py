# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_patient_evaluation(models.Model):
	_name = 'medical.patient.evaluation'
	_rec_name = 'medical_patient_id' 

	patient_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Paciente")
	medical_patient_id = fields.Many2one('medical.patient',string="Paciente",required=True)
	start_evaluation = fields.Datetime(string="Iniciar evaluación")
	physician_partner_id = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string="Doctor")
	end_evaluation = fields.Datetime(string="Fin de la evaluación")
	evaluation_type= fields.Selection([
			('a', 'Ambulatorio(a)'),
			('e', 'Emergencia'),
			('i', 'Paciente interno'),
			('pa', 'Cita preestablecida'),
			('pc', 'Control periódico'),
			('p', 'Llamada telefónica'),
			('t', 'Telemedicina'),
		], string='Tipo')
	chief_complaint = fields.Char('Queja principal')
	information_source = fields.Char('Fuente')
	reliable_info = fields.Boolean('De confianza')
	present_illness = fields.Text(string='Enfermedad presente')
   
	weight = fields.Float(string='Peso (kg)',help='Peso en Kilos')
	height = fields.Float(string='Altura (cm)')
	abdominal_circ = fields.Float(string='Circunferencia abdominal')
	hip = fields.Float(string='Cadera')
	bmi = fields.Float(string='Índice de masa corporal')
	whr = fields.Float(string='WHR')
	head_circumference = fields.Float(string='Circunferencia de la cabeza')
	malnutrition = fields.Boolean('Desnutrición')
	dehydration = fields.Boolean('Deshidración')
	tag = fields.Integer(
			string='Nivel de triacilglicerol ',
			help='Nivel de triacilglicerol (triglicéridos). Puede ser aproximado'
		)
	is_tremor = fields.Boolean(
			string='Temblor',
			help='Marque esta casilla si el paciente muestra signos de temblores',
		)
	mood = fields.Selection([
			('n', 'Normal'),
			('s', 'Triste'),
			('f', 'Temor'),
			('r', 'Rabia'),
			('h', 'Feliz'),
			('d', 'Asco'),
			('e', 'Euforia'),
			('fl', 'Plano'),
		], string='Estado animico')
	glycemia = fields.Float(
			string='Glicemia',
			help='Último nivel de glucosa en sangre. Puede ser aproximado.')
	evaluation_summary = fields.Text(string='Resumen de evaluación')
	temperature = fields.Float(string='Temperatura (celsius)',
									help='Temperatura in celcius')
	osat = fields.Integer(string='Saturación de oxígeno',
							   help='Oxygen Saturation(arterial).')
	bpm = fields.Integer(string='Ritmo cardiaco',
							  help='Heart rate expressed in beats per minute')
	loc_eyes = fields.Selection([
			('1', 'No abre los ojos'),
			('2', 'Abre los ojos en respuesta a estímulos dolorosos.'),
			('3', 'Abre los ojos en respuesta a la voz.'),
			('4', 'Abre los ojos de forma espontánea'),
		], string='Glasgow - Ojos')
	loc_verbal = fields.Selection([
			('1', 'No hagas sonidos'),
			('2', 'Sonidos incomprensibles'),
			('3', 'Pronuncia palabras inapropiadas'),
			('4', 'Confundido, desorientado'),
			('5', 'Orientado, conversa normalmente'),
		], string='Glasgow - Verbal')
	loc_motor = fields.Selection([
			('1', 'No hagas movimiento'),
			('2', 'Extensión a estímulos dolorosos respuesta descerebrada'),
			('3', 'Flexión anormal a estímulos dolorosos respuesta de descerebración'),
			('4', 'Flexión / Retirada a estímulos dolorosos '),
			('5', 'Localiza estímulos dolorosos'),
			('6', 'Obedece los comandos'),
		], string='Glasgow - Motor')
	violent = fields.Boolean('Comportamiento violento')
	orientation = fields.Boolean('Orientación')
	memory = fields.Boolean('Memoria')
	knowledge_current_events = fields.Boolean('Conocimiento de la actualidad')
	judgment = fields.Boolean('Juicio')
	symptom_proctorrhagia = fields.Boolean('Polifagia')
	abstraction = fields.Boolean('Abstracción')
	vocabulary = fields.Boolean('Vocabulario')
	symptom_pain = fields.Boolean('Dolor')
	symptom_pain_intensity = fields.Integer('Intensidad del dolor')
	symptom_arthralgia = fields.Boolean('Artralgia')
	symptom_abdominal_pain = fields.Boolean('Dolor abdominal')
	symptom_thoracic_pain = fields.Boolean('Dolor torácico')
	symptom_pelvic_pain = fields.Boolean('Dolor pélvico')
	symptom_hoarseness = fields.Boolean('Hoarseness')
	symptom_sore_throat = fields.Boolean('Dolor de garganta')
	symptom_ear_discharge = fields.Boolean('Ear Discharge')
	symptom_chest_pain_excercise = fields.Boolean('Dolor de pecho solo con ejercicio')
	symptom_astenia = fields.Boolean('Astenia')
	symptom_weight_change = fields.Boolean('Cambio de peso repentino')
	symptom_hemoptysis = fields.Boolean('Hemoptysis')
	symptom_epistaxis = fields.Boolean('Epistaxis')
	symptom_rinorrhea = fields.Boolean('Rinorrhea')
	symptom_vomiting = fields.Boolean('Vomiting')
	symptom_polydipsia = fields.Boolean('Polydipsia')
	symptom_polyuria = fields.Boolean('Polyuria')
	symptom_vesical_tenesmus = fields.Boolean('Tenesmo vesical')
	symptom_dysuria = fields.Boolean('Dysuria')
	symptom_myalgia = fields.Boolean('Myalgia')
	symptom_cervical_pain = fields.Boolean('Dolor cervical')
	symptom_lumbar_pain = fields.Boolean('Dolor lumbar')
	symptom_headache = fields.Boolean('Dolor de cabeza')
	symptom_odynophagia = fields.Boolean('Odinofagia')
	symptom_otalgia = fields.Boolean('Otalgia')
	symptom_chest_pain = fields.Boolean('Dolor en el pecho')
	symptom_orthostatic_hypotension = fields.Boolean('Hipotensión ortostática')
	symptom_anorexia = fields.Boolean('Anorexia')
	symptom_abdominal_distension = fields.Boolean('Distensión abdominal')
	symptom_hematemesis = fields.Boolean('Hematemesis')
	symptom_gingival_bleeding = fields.Boolean('Sangrado gingival')
	symptom_nausea = fields.Boolean('Nausea')
	symptom_dysphagia = fields.Boolean('Disfagia')
	symptom_polyphagia = fields.Boolean('Polifagia')
	symptom_nocturia = fields.Boolean('Nocturia')
	symptom_pollakiuria = fields.Boolean('Pollaquiuria')
	symptom_mood_swings = fields.Boolean('Mood Swings')
	symptom_pruritus = fields.Boolean('Pruritus')
	symptom_disturb_sleep = fields.Boolean('Disturbed Sleep')
	symptom_orthopnea = fields.Boolean('Orthopnea')
	symptom_paresthesia = fields.Boolean('Paresthesia')
	symptom_dizziness = fields.Boolean('Dizziness')
	symptom_tinnitus = fields.Boolean('Tinnitus')
	symptom_eye_glasses = fields.Boolean('Eye glasses')
	symptom_diplopia = fields.Boolean('Diplopia')
	symptom_dysmenorrhea = fields.Boolean('Dysmenorrhea')
	symptom_metrorrhagia = fields.Boolean('Metrorrhagia')
	symptom_vaginal_discharge = fields.Boolean('Vaginal Discharge')
	symptom_diarrhea = fields.Boolean('Diarrhea')
	symptom_rectal_tenesmus = fields.Boolean('Rectal Tenesmus')
	symptom_sexual_dysfunction = fields.Boolean('Sexual Dysfunction')
	symptom_stress = fields.Boolean('Stressed-out')
	symptom_insomnia = fields.Boolean('Insomnia')
	symptom_dyspnea = fields.Boolean('Dyspnea')
	symptom_amnesia = fields.Boolean('Amnesia')
	symptom_paralysis = fields.Boolean('Paralysis')
	symptom_vertigo = fields.Boolean('Vertigo')
	symptom_syncope = fields.Boolean('Syncope')
	symptom_blurry_vision = fields.Boolean('Blurry vision')
	symptom_photophobia = fields.Boolean('Photophobia')
	symptom_amenorrhea = fields.Boolean('Amenorrhea')
	symptom_menorrhagia = fields.Boolean('Menorrhagia')
	symptom_urethral_discharge = fields.Boolean('Urethral Discharge')
	symptom_constipation = fields.Boolean('Constipation')
	symptom_melena = fields.Boolean('Melena')
	symptom_xerostomia = fields.Boolean('Xerostomia')
	calculation_ability = fields.Boolean('Calculation Ability')
	object_recognition = fields.Boolean('Object Recognition')
	praxis = fields.Boolean('Praxis')
	edema = fields.Boolean('Edema')
	petechiae = fields.Boolean('Petechiae')
	acropachy = fields.Boolean('Acropachy')
	miosis = fields.Boolean('Miosis')
	cough = fields.Boolean('Cough')
	arritmia = fields.Boolean('Arritmias')
	heart_extra_sounds = fields.Boolean('Heart Extra Sounds')
	ascites = fields.Boolean('Ascites')
	bronchophony = fields.Boolean('Bronchophony')
	cyanosis = fields.Boolean('Cyanosis')
	hematoma = fields.Boolean('Hematomas')
	nystagmus = fields.Boolean('Nystagmus')
	mydriasis = fields.Boolean('Mydriasis')
	palpebral_ptosis = fields.Boolean('Palpebral Ptosis')
	heart_murmurs = fields.Boolean('Heart Murmurs')
	jugular_engorgement = fields.Boolean('Tremor')
	lung_adventitious_sounds = fields.Boolean('Lung Adventitious sounds')
	increased_fremitus = fields.Boolean('Increased Fremitus')
	jaundice = fields.Boolean('Jaundice')
	breast_lump = fields.Boolean('Breast Lumps')
	nipple_inversion = fields.Boolean('Nipple Inversion')
	peau_dorange = fields.Boolean('Peau d orange')
	hypotonia = fields.Boolean('Hypotonia')
	masses = fields.Boolean('Masses')
	goiter = fields.Boolean('Goiter')
	xerosis = fields.Boolean('Xerosis')
	decreased_fremitus = fields.Boolean('Decreased Fremitus')
	lynphadenitis = fields.Boolean('Linphadenitis')
	breast_asymmetry = fields.Boolean('Breast Asymmetry')
	nipple_discharge = fields.Boolean('Nipple Discharge')
	gynecomastia = fields.Boolean('Gynecomastia')
	hypertonia = fields.Boolean('Hypertonia')
	pressure_ulcers = fields.Boolean('Pressure Ulcers')
	alopecia = fields.Boolean('Alopecia')
	erithema = fields.Boolean('Erithema')
	diagnosis_id = fields.Many2one('medical.pathology','Presumptive Diagnosis')
	ldl = fields.Integer(
			string='Last LDL',
			help='Last LDL Cholesterol reading. Can be approximative'
		)
	visit_type  = fields.Selection([('new','New Health Condition'),('follow','FollowUp'),('chronic','Chronic Condition ChechUp'),('child','Well Child Visit'),('women','Well Woman Visit'),('man','Well Man Visit')],string="Visit")
	urgency  = fields.Selection([('a', 'Normal'), ('b', 'Urgent'), ('c', 'Medical Emergency')],string='Urgency')
	systolic = fields.Integer('Systolic Pressure')
	diastolic = fields.Integer('Diastolic Pressure')
	respiratory_rate = fields.Integer('Respiratory Rate')
	signs_and_symptoms_ids = fields.One2many('medical.signs.and.sympotoms','patient_evaluation_id','Signs and Symptoms')
	hba1c = fields.Float('Glycated Hemoglobin')
	cholesterol_total = fields.Integer('Last Cholesterol')
	hdl = fields.Integer('Last HDL')
	ldl = fields.Integer('Last LDL')
	tags = fields.Integer('Last TAGs')
	loc = fields.Integer('Level of Consciousness')
	info_diagnosis = fields.Text(string='Information on Diagnosis')
	directions = fields.Text(string='Treatment Plan')
	user_id = fields.Many2one('res.users','Doctor user ID',readonly=True)
	medical_appointment_date_id = fields.Many2one('medical.appointment','Appointment Date')
	next_appointment_id = fields.Many2one('medical.appointment','Next Appointment')
	derived_from_physician_id = fields.Many2one('medical.physician','Derived from Doctor')
	derived_to_physician_id = fields.Many2one('medical.physician','Derived to Doctor')
	secondary_conditions_ids = fields.One2many('medical.secondary_condition','patient_evaluation_id','Secondary Conditions')
	diagnostic_hypothesis_ids = fields.One2many('medical.diagnostic_hypotesis','patient_evaluation_id','Procedures')
	procedure_ids = fields.One2many('medical.directions','patient_evaluation_id','Procedures')


