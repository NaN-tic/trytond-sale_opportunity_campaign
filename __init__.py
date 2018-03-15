# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .opportunity import *
import invoice


def register():
    Pool.register(
        Campaign,
        ProductCampaign,
        PartyCampaign,
        Opportunity,
        CreateCampaignStart,
        invoice.InvoiceLine,
        module='sale_opportunity_campaign', type_='model')
    Pool.register(
        CreateCampaign,
        module='sale_opportunity_campaign', type_='wizard')
