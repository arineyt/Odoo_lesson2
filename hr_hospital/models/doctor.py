# -*- coding: utf-8 -*-
from odoo import models, fields

class HospitalDoctor(models.Model):
    """A class used to represent a Doctor"""
    _name = 'hospital.doctor'
    _description = "Hospital doctor"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
