from django.contrib import admin
from django import forms

from anoneyes.models import Patient, EthnicGroup, Management, Outcome

class ManagementAdminForm(forms.ModelForm):
    class Meta:
        model = Management
        widgets = {
                   'comments': forms.TextInput
        }

class ManagementAdmin(admin.ModelAdmin):
    pass

admin.site.register(Management, ManagementAdmin)

class OutcomeAdminForm(forms.ModelForm):
    class Meta:
        model = Outcome
        widgets = {
                   'visual_acuity_right': forms.TextInput(attrs={'size':'10'}),
                   'visual_acuity_left': forms.TextInput(attrs={'size':'10'}),
                   'visual_acuity_both': forms.TextInput(attrs={'size':'10'}),
        }

class OutcomeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Outcome, OutcomeAdmin)

class EthnicGroupAdmin(admin.ModelAdmin):
    pass

admin.site.register(EthnicGroup, EthnicGroupAdmin)

class ManagementInline(admin.TabularInline):
    extra = 0
    model = Management
    form = ManagementAdminForm

class OutcomeInline(admin.TabularInline):
    extra = 0
    model = Outcome
    form = OutcomeAdminForm

class PatientAdminForm(forms.ModelForm):
    class Meta:
        model = Patient
        widgets = {
                   'postcode': forms.TextInput(attrs={'size':'10'}),
                   'visual_acuity_right': forms.TextInput(attrs={'size':'10'}),
                   'visual_acuity_left': forms.TextInput(attrs={'size':'10'}),
                   'visual_acuity_both': forms.TextInput(attrs={'size':'10'}),
        }

class PatientAdmin(admin.ModelAdmin):
    form = PatientAdminForm
    fieldsets = (
                 (None, {
                         'fields': ('sex', 'dob', 'postcode', 'ethnic_group', 'consanguinity')
                         }),
                 ('Baseline Assessment', {
                         'fields': ('eye', 'diagnosis', ('lens_status_right', 'lens_extraction_date_right'), ('lens_status_left', 'lens_extraction_date_left'),
                                    ('visual_acuity_date', 'visual_acuity_method'), ('visual_acuity_right', 'visual_acuity_left', 'visual_acuity_both'))
                         }),
    )
    inlines = [
        ManagementInline,
        OutcomeInline,
    ]

admin.site.register(Patient, PatientAdmin)
