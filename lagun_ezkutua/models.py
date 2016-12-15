from django.db import models
from django.forms import ModelForm,Form
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms.extras import SelectDateWidget
import datetime
#from  django.contrib.admin.widgets import AdminDateWidget

# Create your models here.

class Kuadrilla (models.Model):
    lagun_kopurua = models.IntegerField()
    data = models.DateField(null=True,default = datetime.date.today())
    dirua = models.IntegerField()
    def __str__(self):
        return str(self.id)

class Laguna (models.Model):
    kuadri = models.ForeignKey(Kuadrilla, on_delete=models.CASCADE)
    izena = models.CharField(max_length = 200)
    eposta = models.EmailField()
    lagun_ezk = models.CharField(max_length=200,null=True)

class KuadrillaForm(ModelForm):
    class Meta:
        model = Kuadrilla
        fields = ["lagun_kopurua","data","dirua"]
        labels = {'lagun_kopurua': _("Zenbat lagun zarete?"),"data":_("Noiz egingo da opari banaketa?"),"dirua":_("Zenbat diru?"),}
        widgets = {"data":SelectDateWidget()}


class LagunaForm(Form):
    # izena = forms.CharField()
    # eposta = forms.EmailField()

    def __init__(self, *args, **kwargs):
        self.extra = kwargs.pop('extra')
        super(LagunaForm, self).__init__(*args, **kwargs)

        for i in range(0,self.extra):
            self.fields['izena_%s' % i] = forms.CharField()
            self.fields['eposta_%s' % i] = forms.EmailField()

    def extra_lagunak(self):
        for i in range(0,self.extra):
            yield (self.cleaned_data['izena_'+str(i)],self.cleaned_data['eposta_'+str(i)])
        # for name, value in self.cleaned_data.items():
        #     if name.startswith('izena_') or name.startswith('eposta'):
        #         yield (self.fields[name].label, value)

