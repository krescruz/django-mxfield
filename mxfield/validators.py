#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _

@deconstructible
class CURPValidator(validators.RegexValidator):
	regex = re.compile(r'^([A-Z][A,E,I,O,U,X][A-Z]{2}[0-9]{2}[0-1][0-9][0-3][0-9][M,H][A-Z]{2}[B,C,D,F,G,H,J,K,L,M,N,Ñ,P,Q,R,S,T,V,W,X,Y,Z]{3}[0-9,A-Z][0-9])$', re.IGNORECASE)
	message = _('Enter a valid CURP.')