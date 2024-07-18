# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

READONLY_FIELD_STATES = {
    state: [('readonly', True)]
    for state in {'sale', 'done', 'cancel'}
}
LOCKED_FIELD_STATES = {
    state: [('readonly', True)]
    for state in {'done', 'cancel'}
}

INVOICE_STATUS = [
    ('upselling', 'Upselling Opportunity'),
    ('invoiced', 'Fully Invoiced'),
    ('to invoice', 'To Invoice'),
    ('no', 'Nothing to Invoice')
]
class sale_ext(models.Model):
    _inherit = 'sale.order'
    # _description = 'sale_ext.sale_ext'


    @api.model
    def default_get(self, fields_list):
        res = super(sale_ext, self).default_get(fields_list)
        default_partner = self.env['res.partner'].search([('is_default_picking', '=', True)], limit=1)
        if default_partner:
            res['partner_id'] = default_partner.id
        return res

    # partner_id = fields.Many2one(
    #     comodel_name='res.partner',
    #     string="Customer",
    #     required=False, readonly=False, change_default=True, index=True,
    #     tracking=1,
    #     states=READONLY_FIELD_STATES,
    #     domain="[('type', '!=', 'private'), ('company_id', 'in', (False, company_id))]")

    # partner_invoice_id = fields.Many2one(
    #     comodel_name='res.partner',
    #     string="Invoice Address",
    #     compute='_compute_partner_invoice_id',
    #     store=True, readonly=False, required=False, precompute=True,
    #     states=LOCKED_FIELD_STATES,
    #     domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    # partner_shipping_id = fields.Many2one(
    #     comodel_name='res.partner',
    #     string="Delivery Address",
    #     compute='_compute_partner_shipping_id',
    #     store=True, readonly=False, required=False, precompute=True,
    #     states=LOCKED_FIELD_STATES,
    #     domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_default_picking = fields.Boolean(string='Malzeme Toplama Carisi')

    @api.constrains('is_default_picking')
    def _check_unique_default_picking(self):
        if self.is_default_picking:
            existing = self.search([
                ('is_default_picking', '=', True),
                ('id', '!=', self.id)
            ])
            if existing:
                raise ValidationError('Sadece bir cari kartı malzeme toplama kartı olabilir.')

