from django import forms
from django.contrib.auth.models import User
from django.forms import BaseFormSet
from django.forms.models import inlineformset_factory

from proj_orc.models import Orcamento,Zona

# FORMULÁRIOS

class ZonaForm(forms.ModelForm):
	idorc = forms.IntegerField(widget=forms.HiddenInput())
	class Meta:
		model = Zona
		fields=['nmformacao', 'nmzona', 'mdtopo', 'mdbase', 'cdzonacanhoneio', 'cdzonavedacao', 'cdzonafratura']
		exclude = ()

	def clean(self):
		orc = self.data['idorc']
		data = self.cleaned_data
		mdtopo = data['mdtopo']
		mdbase = data['mdbase']
		zonas = Zona.objects.filter(idorc=orc)
		prof_final = Orcamento.objects.get(id=orc).profundidade


		if not zonas:
			ultimabase = 0
		else:
			ultimabase = zonas.latest('id').mdbase

		#from ipdb import set_trace; set_trace()
		if (mdbase > prof_final):
			raise forms.ValidationError('A base deve ser menor que a profundidade final')

		if not (mdbase > mdtopo):
			raise forms.ValidationError('A base deve ser maior que a topo')

		if not (mdbase > ultimabase):
			raise forms.ValidationError('A base da nova zona deve ser maior que a anterior')

		if not (mdtopo > ultimabase):
			raise forms.ValidationError('O topo da nova zona deve ser maior que a base anterior')

		return data

# It's possible to extend Django ModelForm with extra fields. Imagine you have a custom User model and this ModelForm:

# class ProfileForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields = ['username', 'country', 'website', 'biography']
# Now, imagine you want to include an extra field (not present in your User model, lets say an image avatar). Extend your form by doing this:

# from django import forms

# class AvatarProfileForm(ProfileForm):

#     profile_avatar = forms.ImageField()

#     class Meta(ProfileForm.Meta):
#         fields = ProfileForm.Meta.fields + ('profile_avatar',)

# class Nova_zona_Form(forms.ModelForm):

# 	class Meta:
# 		model = Zona
# 		fields = '__all__'
# 		exclude = ()


# class ZonaFormSet(
#     forms.inlineformset_factory(Orcamento, Zona, 
  #fields=['nmformacao',
#             'nmzona',
#             'mdtopo',
#             'mdbase',
#             'cdzonacanhoneio',
#             'cdzonavedacao',
#             'cdzonafratura'])):

# 	def clean(self):
# 		# super(ZonaFormSet, self).clean()
# 		# if any(self.errors):
# 	 #         # Don't bother validating the formset unless each form is valid on its own
# 	 #         return

# 		if 'mdtopo' in self.cleaned_data:
# 			topo = self.cleaned_data['mdtopo']





    # def clean(self):
    #     variables = {}
    #     for form in self.formset:
    #         if form.is_valid() and 'formula_variable' in form.cleaned_data:
    #             variables[form.cleaned_data['formula_variable']] = 1

    #     if 'formula' in self.cleaned_data:
    #         formula = self.cleaned_data['formula']
    #         valid, msg = do_formula(formula, variables)
    #         if not valid:
    #             self._errors['formula'] = self.error_class([msg])
    #             del self.cleaned_data['formula']

    #     return self.cleaned_data





		#topo = self.cleaned_data[0]
	
		# topos = []
		# bases = []
		# #from ipdb import set_trace; set_trace()
		# for form in list(self.cleaned_data):
		# 	#from ipdb import set_trace; set_trace()
		# 	topo = form['mdtopo']
		# 	base = form['mdbase']
		# 	topos.append(topo)
		# 	bases.append(base)
		# 	# if self.can_delete and self._should_delete_form(form):
			# 	continue


		# from ipdb import set_trace; set_trace()
		# if topo in topos:
		# 	#from ipdb import set_trace; set_trace()
		# 	raise forms.ValidationError("Topos in a set must have distinct titles.")
	#     class CollectionTitleForm(forms.ModelForm):

#     class Meta:
#         model = CollectionTitle

# CollectionTitleFormSet = inlineformset_factory(
#     Collection, CollectionTitle, form=CollectionTitleForm,
#     fields=['name', 'language'], extra=1, can_delete=True
#     )


# class SellerResultForm(forms.ModelForm):

#     class Meta:
#         model = SellerResult
#         fields = ('month', 'year', 'result',)
#         widgets = {
#             'month': forms.Select(attrs={'class': 'form-control',}),
#             'year': forms.Select(attrs={'class': 'form-control',}),
#             'result': forms.TextInput(attrs={'class': 'form-control',}),
#         }

#     def has_changed(self): #used for saving data from initial
#         changed_data = super(SellerResultForm, self).has_changed()
#         return bool(self.initial or changed_data)

#     #no clean method here anymore

# class BaseSellerResultFormSet(BaseModelFormSet):
#     def clean(self):
#         super(BaseSellerResultFormSet, self).clean()

#         years = []
#         for form in self.forms:
#             year = form.cleaned_data['year']
#             years.append(year)
#         if years.count(2017) > 12:
#             raise forms.ValidationError('You selected more than 12 months for 2017')