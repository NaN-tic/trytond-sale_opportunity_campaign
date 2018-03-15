from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['InvoiceLine']


class InvoiceLine:
    __name__ = 'account.invoice.line'
    __metaclass__ = PoolMeta
    sale_opportunity_campaign = fields.Many2One('sale.opportunity.campaign',
        'Campaign')
