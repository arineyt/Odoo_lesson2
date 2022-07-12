# -*- coding: utf-8 -*-
from odoo import models, fields

class HospitalDiagnosis(models.Model):
    """A class used to represent a Pdiagnosis"""
    _name = 'hospital.diagnosis'
    _description = "Hospital diagnosis"

    name = fields.Char(string='Name', required=True)
    state = fields.Selection([('bad', 'Bad'), ('good', 'Good')], string='State')
