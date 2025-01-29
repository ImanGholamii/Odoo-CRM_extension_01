# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessError


class CustomLead(models.Model):
    _inherit = 'crm.lead'

    main_contact = fields.Boolean(string='Main Contact', stored=True, help="Define The Main Contact")


class CrmTag(models.Model):
    _inherit = 'crm.tag'

    @api.model
    def create(self, vals):
        if not self.env.user.has_group('custom_crm_lead_extension.custom_group_crm_tag_manager'):
            raise AccessError("You do not have permission to create a tag.")
        return super(CrmTag, self).create(vals)
