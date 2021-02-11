# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
# classes under  menu of laboratry 

class medical_patient_psc(models.Model):
    _name = 'medical.patient.psc'
    _rec_name = 'patient_id'

    @api.model
    def default_get(self,fields):
        result = super(medical_patient_psc, self).default_get(fields)
        
        result.update({
                        'user_id':self._uid,
                       })
        return result

    appointment_id = fields.Many2one('medical.appointment',"Citas")
    patient_id = fields.Many2one('medical.patient','Paciente', required = True) 
    evaluation_start = fields.Datetime('Fecha ', required = True, default=fields.Datetime.now)
    psc_total = fields.Integer('PCS Total')
    user_id = fields.Many2one('res.users','Profesional de la salud', default=lambda self: self.env.user)
    notes = fields.Text('Notas') 
    #selection field 
    psc_aches_pains = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Se queja de dolores y molestias')
    psc_absent_from_school = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Ausente de la escuela')
    psc_act_as_younger = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Actúa más joven que los niños de su edad')
    psc_acts_as_driven_by_motor = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Actúa como impulsado por un motor')
    psc_afraid_of_new_situations = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Tiene miedo a nuevas situaciones.')
    psc_blames_others = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Culpa a otros por sus problemas')
    psc_daydreams_too_much = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Sueña despierto demasiado')
    psc_distracted_easily = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Distraerse fácilmente')
    psc_does_not_get_people_feelings = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'No hace sentir a la gente')
    psc_does_not_listen_to_rules = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'No escucha las reglas')
    psc_does_not_show_feelings = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'No muestra sentimientos')
    psc_down_on_self = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Está deprimido por sí mismo')
    psc_feels_hopeless = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Se siente desesperado')
    psc_feels_is_bad_child = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Se siente mal')
    psc_fidgety =fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Inquieto, incapaz de sentarse quieto')
    psc_fights_with_others = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Peleas con otros niños(as)')
    psc_gets_hurt_2 = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Se lastima con frecuencia')
    psc_having_less_fun = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Parece divertirse menos')
    psc_irritable_angry = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Es irritable, enojado')
    psc_less_interested_in_friends = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Menos interesado en los amigos')
    psc_less_interest_in_school = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Menos interesado en la escuela')
    psc_refuses_to_share = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Se niega a compartir')
    psc_sad_unhappy = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Se siente triste, infeliz')
    psc_school_grades_dropping = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Las calificaciones escolares caen')
    psc_spend_time_alone = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Pasa más tiempo solo')
    psc_takes_things_from_others = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Toma cosas que no le pertenecen')
    psc_takes_unnecesary_risks = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Toma riesgos innecesarios')
    psc_teases_others = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Se burla de los demás')
    psc_tires_easily = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Se cansa fácilmente, tiene poca energía')
    psc_trouble_concentrating = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Tiene problemas para concentrarse')
    psc_trouble_sleeping = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Tiene problemas para dormir')
    psc_trouble_with_teacher = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Tiene problemas con el maestro(a)')
    psc_gets_hurt_often = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Se lastima a menudo')
    psc_visit_doctor_finds_ok = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Visita al médico con el médico y no encuentra nada malo')
    psc_wants_to_be_with_parents = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Quiere estar contigo más que antes')
    psc_worries_a_lot = fields.Selection([('0', 'Nunca'),('1', 'A veces'),('2', 'A menudo')], 'Se preocupa mucho')
    
    @api.onchange('psc_aches_pains', 
                  'psc_absent_from_school',
                   'psc_act_as_younger', 'psc_acts_as_driven_by_motor',
                    'psc_afraid_of_new_situations', 
                    'psc_blames_others','psc_teases_others',
                     'psc_daydreams_too_much', 'psc_tires_easily',
                     'psc_distracted_easily','psc_trouble_concentrating',
                     'psc_trouble_sleeping','psc_trouble_with_teacher',
                     'psc_visit_doctor_finds_ok', 'psc_wants_to_be_with_parents',
                     'psc_worries_a_lot',
                      'psc_does_not_get_people_feelings', 'psc_does_not_listen_to_rules', 
                      'psc_does_not_show_feelings', 'psc_down_on_self',
                       'psc_feels_hopeless','psc_feels_is_bad_child',
                       'psc_fidgety','psc_fights_with_others', 
                       'psc_gets_hurt_often', 'psc_having_less_fun', 'psc_irritable_angry', 
                      'psc_less_interested_in_friends', 'psc_less_interest_in_school',
                       'psc_refuses_to_share', 'psc_sad_unhappy', 
                       'psc_school_grades_dropping', 'psc_spend_time_alone', 
                       'psc_takes_things_from_others', 'psc_takes_unnecesary_risks', )
    def onchange_selections(self):
        self.psc_total = int(self.psc_aches_pains)+int(self.psc_absent_from_school) + int(self.psc_act_as_younger) +int(self.psc_acts_as_driven_by_motor)  + int(self.psc_afraid_of_new_situations) +int(self.psc_blames_others) + int(self.psc_teases_others) + int(self.psc_daydreams_too_much)+int(self.psc_tires_easily)+ int(self.psc_distracted_easily)+ int(self.psc_trouble_concentrating)+ int(self.psc_trouble_sleeping)+ int(self.psc_trouble_with_teacher)+ int(self.psc_visit_doctor_finds_ok)++int(self.psc_wants_to_be_with_parents) + int(self.psc_worries_a_lot)+ int(self.psc_does_not_get_people_feelings)+int(self.psc_down_on_self)+ int(self.psc_feels_hopeless)+ int(self.psc_feels_is_bad_child)+int(self.psc_fidgety)+ int(self.psc_fights_with_others)+ int(self.psc_gets_hurt_often)+ int(self.psc_having_less_fun)+ int(self.psc_irritable_angry) + int(self.psc_less_interested_in_friends)+int(self.psc_less_interest_in_school)+ int(self.psc_refuses_to_share)+ int(self.psc_sad_unhappy) +int(self.psc_school_grades_dropping) + int(self.psc_spend_time_alone) + int(self.psc_takes_things_from_others)+int(self.psc_takes_unnecesary_risks)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:    








