from odoo import api, fields, models


class AccountJournalInherit(models.Model):
    _inherit = "account.journal"

    sucursal = fields.Integer(
        string="Sucursal",
        default="1",
    )
    terminal = fields.Integer(
        string="Terminal",
        default="1",
    )
    FE_sequence_id = fields.Many2one(
        comodel_name="ir.sequence",
        string="Electronic Invoice Sequence",
    )
    TE_sequence_id = fields.Many2one(
        comodel_name="ir.sequence",
        string="Electronic Ticket Sequence",
    )
    FEE_sequence_id = fields.Many2one(
        comodel_name="ir.sequence",
        string="Sequence of Electronic Export Invoices",
    )
    NC_sequence_id = fields.Many2one(
        comodel_name="ir.sequence",
        string="Sequence of Electronic Credit Notes",
    )
    ND_sequence_id = fields.Many2one(
        comodel_name="ir.sequence",
        string="Electronic Debit Notes Sequence",
    )
    to_process = fields.Boolean(
        default=True,
        help="If is checked, the documents related to this journal will be sended to the API (staging or production, based on company configuration)",
    )

    sequence_id = fields.Many2one('ir.sequence', string='Secuencia.')
    sequence_refund_id = fields.Many2one('ir.sequence', string='Secuencia Rect.')

    @api.model
    def set_sequences(self):
        pass