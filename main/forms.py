from django import forms
from .models import Nurse, Patient

class AddPatient(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ('p_id','bed','condition',)

class EditPatient(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ('p_id','bed','condition',)

class DeletePatient(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ('p_id',)




class AddNurse(forms.ModelForm):
	class Meta:
		model = Nurse
		fields = ('name','number',)

class EditNurse(forms.ModelForm):
	class Meta:
		model = Nurse
		fields = ('name','number',)

class DeleteNurse(forms.ModelForm):
	class Meta:
		model = Nurse
		fields = ('name',)
