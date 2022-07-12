# -*- coding: utf-8 -*-
from odoo import models, fields

class HospitalCard(models.Model):
    """A class used to represent a Patient Card"""
    _name = 'hospital.card'
    _description = "Patient Card"

    name = fields.Char(string='Name', required=True)
    pages = fields.Integer(string='Pages')
