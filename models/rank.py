from odoo import models, fields, api, exceptions

class Rank(models.Model):
	_name = 'mymodule.rank'
	_rec_name = 'rank_name'

	rank_name = fields.Char(string = "Name", required = True)

	soldier_ids = fields.One2many(
		'mymodule.soldier', 'rank_id', string="Soldiers")
