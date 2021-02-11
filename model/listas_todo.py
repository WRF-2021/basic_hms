# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import date
from datetime import datetime
from datetime import *
import datetime
from odoo.exceptions import UserError, ValidationError
                      

tipo_parto = [
    ('1', 'Vaginal'),
    ('2', 'Vaginal con ayuda medicamentos'),
    ('3', 'Vaginal con forceps'),
    ('4', 'Cesarea'),
]


class creacion_listas_Todo(models.Model):
    _name = "lista_ruta_administracion"
    _order = 'nombre_cartera'
    _rec_name = 'nombre_cartera'

    #Esta herencia funciona para que se pueda mostrar el pie de pagina en los formularios con las notas y poder enviar correos
    _inherit = ['mail.thread', 'mail.activity.mixin']
                                   
    nombre_cartera = fields.Text("Ruta de administracion")
    
    _sql_constraints = [
        ('name_uniq', 'unique (nombre_cartera)', "El nombre de la ruta ya existe !"),
    ]



class mediacament_lista(models.Model):
    _inherit = 'medical.patient.medication1'
    
    tipo_ruta_admin = fields.Many2one('lista_ruta_administracion', 
                                   string="Ruta de administracion", 
                                   ondelete='cascade', 
                                   index=True)


class creacion_listas_drogas(models.Model):
    _name = "lista_drogas"
    _order = 'nombre_cartera'
    _rec_name = 'nombre_cartera'

    #Esta herencia funciona para que se pueda mostrar el pie de pagina en los formularios con las notas y poder enviar correos
    _inherit = ['mail.thread', 'mail.activity.mixin']
                                   
    nombre_cartera = fields.Text("Tipo Droga")
    
    _sql_constraints = [
        ('name_uniq', 'unique (nombre_cartera)', "El nombre de esta droga ya existe!"),
    ]

class creacion_infertilidad(models.Model):
    _name = "tipo_infertilidad"
    _order = 'nombre_cartera'
    _rec_name = 'nombre_cartera'

    #Esta herencia funciona para que se pueda mostrar el pie de pagina en los formularios con las notas y poder enviar correos
    _inherit = ['mail.thread', 'mail.activity.mixin']
                                   
    nombre_cartera = fields.Text("Tipo infertilidad")
    
    _sql_constraints = [
        ('name_uniq', 'unique (nombre_cartera)', "El nombre de esta infertilidad ya existe!"),
    ]

class creacion_aborto(models.Model):
    _name = "tipo_aborto"
    _order = 'nombre_cartera'
    _rec_name = 'nombre_cartera'

    #Esta herencia funciona para que se pueda mostrar el pie de pagina en los formularios con las notas y poder enviar correos
    _inherit = ['mail.thread', 'mail.activity.mixin']
                                   
    nombre_cartera = fields.Text("Tipo Aborto")
    
    _sql_constraints = [
        ('name_uniq', 'unique (nombre_cartera)', "El nombre de este aborto ya existe!"),
    ]

class mediacament_Drilista(models.Model):
    _inherit = 'medical.patient'
    
    tipo_drogas_admin = fields.Many2one('lista_drogas', 
                                        string="Tipo Drogas", 
                                        ondelete='cascade', 
                                        index=True)

    notas_Drogas = fields.Text('Observaciones')
 
    tipo_parto =  fields.Selection(tipo_parto, string='Tipo parto', index=True, default=tipo_parto[0][0]) 
    
    tipo_infertilidad_admin = fields.Many2one('tipo_infertilidad', 
                                        string="Tipo Infertilidad", 
                                        ondelete='cascade', 
                                        index=True)
    
    tipo_aborto_admin = fields.Many2one('tipo_aborto', 
                                        string="Tipo Aborto", 
                                        ondelete='cascade', 
                                        index=True)
    