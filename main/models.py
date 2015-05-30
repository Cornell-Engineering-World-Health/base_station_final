from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# Create your models here.
class Nurse(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

    @classmethod
    def add(cls, n, num):
        try:
            nurse = Nurse.objects.get(name=n)
            print("Exists Already")
        except:
            Nurse.objects.create(name=n, number=num)

    @classmethod
    def delete(cls, n):
        try:
            Nurse.objects.filter(name=n).delete()
        except:
            print("Does not exists")

    @classmethod
    def edit(cls, n, new_num):
        try:
            nurse = Nurse.objects.get(name=n)
            if (new_num != ""): nurse.number = new_num
            nurse.save()
        except:
            print("Does not exist")

    @classmethod
    def listAll(cls):
    	html_out = "<table class='table table-striped' align='center'>"
    	html_out += "<thead><th>Name</th><th>Phone #</th></thead><tbody>"

    	nurses = Nurse.objects.order_by('name')

    	if (not nurses) : return "<h3>No nurses</h3>"

    	for nurse in nurses:
    		name = nurse.name
    		number = nurse.number
    		html_out += "<tr>"
    		html_out += "<td>" + name + "</td>"
    		html_out += "<td>" + number + "</td>"
    		html_out += "</tr>"

    	html_out += "</tbody></table>"

    	return html_out

    def __str__(self):
    	return self.name + " & " + self.number 


class Patient(models.Model):
    p_id = models.CharField(max_length=10)
    bed = models.CharField(max_length=10)
    condition = models.IntegerField(validators=[MinValueValidator(-1),MaxValueValidator(1)])
    update = models.DateTimeField(default=datetime.now, blank=True)

    @classmethod
    def add(cls, p, b, c):
        try:
            patient = Patient.objects.get(p_id=p)
            print("Exists Already")
        except:
            Patient.objects.create(p_id=p, bed=b, condition=c)

    @classmethod
    def delete(cls, p):
        try:
            Patient.objects.filter(p_id=p).delete()
        except:
            print("Does not exists")
    	

    @classmethod
    def edit(cls, p, new_b, new_c):
        try:
            print("p: " + p )
            patient = Patient.objects.get(p_id=p)
	    print("Edit Made0")
            if (new_b != ""): patient.bed = new_b
            print("Edit Made1")
            if (new_c != ""): patient.condition = int(new_c)
            print("Edit Made2")
            patient.update = datetime.now()
	    print("Edit Made3")
            patient.save()
	    print("Edit Made")
        except:
            print("Does not exist")


    @classmethod
    def listAll(cls):
    	html_out = "<table class='table table-striped' align='center'>"
    	html_out += "<thead><th>ID</th><th>Bed</th><th>Condition</th><th>Last Update</th></thead><tbody>"

    	patients = Patient.objects.order_by('p_id')

    	if (not patients) : return "<h3>No patients</h3>"

        for patient in patients:
            p = patient.p_id
            b = patient.bed
            c = patient.condition
            u = patient.update
            html_out += "<tr>"
            html_out += "<td>" + p + "</td>"
            html_out += "<td>" + b + "</td>"
            html_out += "<td>" + Patient.cond(c) + "</td>"
            html_out += "<td>" + u.strftime('%m/%d/%Y %H:%M:%S') + "</td>"
            html_out += "</tr>"

    	html_out += "</tbody></table>"

    	return html_out

    @classmethod
    def cond(cls,c):
        if c == 1:
            return "Stable"
        elif c == -1:
            return "Critical"
        else:
            return "Intermediate"


	def __str__(self):
		return self.p_id + " & " + self.bed + " & " + self.condition