#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from gui.models import News,Report
from django.utils.translation import gettext as _

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'imagen', 'resumen','content',)
        labels = {
            'title': _('Título'),
        }
        error_messages = {
            'title': {
                'required': _("El campo 'Título' es requerido"),
            },
            'imagen': {
                'required': _("Una 'Imagen' es requerida"),
            },
            'resumen': {
                'required': _("El campo 'Resumen' es requerido"),
            },
            'content': {
                'required': _("El campo 'Contenido' es requerido"),
            },
        }

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('title', 'fileReport',)
        error_messages = {
            'title': {
                'required': _("El campo 'Título' es requerido"),
            },
            'fileReport': {
                'required': _("Un 'Documento' es requerido"),
            },
        }