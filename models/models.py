# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class relaciones(models.Model):
#     _name = 'relaciones.relaciones'
#     _description = 'relaciones.relaciones'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100





from odoo import models, fields, api

class alumno(models.Model):
	_name = 'relaciones.alumno'
	_description = 'model alumno'

	name = fields.Char('DNI',required=True)
	nombre = fields.Char(string='Nombre',required=True)



class asignatura(models.Model):
	_name = 'relaciones.asignatura'
	_description = 'model asignatura'

	name = fields.Char('Código',required=True)
	nombre = fields.Char(string='Asignatura',required=True)



class tutor(models.Model):
	_name = 'relaciones.tutor'
	_description = 'model tutor'

	name = fields.Char('DNI',required=True)
	nombre = fields.Char(string='Tutor',required=True)
