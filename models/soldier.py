from odoo import models, fields, api, exceptions

class Soldier(models.Model):
	_name = 'mymodule.soldier'
	_rec_name = 'full_name'

	full_name = fields.Char(string = "Full name", required = True)
	birthdate = fields.Date(string = "Date of birth", required = True)

	rank_id = fields.Many2one('mymodule.rank',
        ondelete='set null', string="Rank", index=True)

