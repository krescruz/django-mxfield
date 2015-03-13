from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _

import validators

class CURPField(CharField):
	default_validators = [validators.CURPValidator()]
	description = _("CURP")

	def __init__(self, *args, **kwargs):
		kwargs['max_length'] = 18
		super(CURPField, self).__init__(*args, **kwargs)
