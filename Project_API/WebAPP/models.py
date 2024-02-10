from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    ssc_score = models.IntegerField()
    percentage = models.IntegerField()
    speciliation = models.CharField(max_length=100)
    degree_score = models.IntegerField()
    company = models.CharField(max_length=100, null=True)
    experience = models.IntegerField()

    def set_SSC_details(self, first_name, ssc_score, percentage):
        self.first_name = first_name
        self.ssc_score = ssc_score
        self.percentage = percentage

    def set_Degree_details(self, specilization, degree_score):
        self.specilization = specilization
        self.degree_score = degree_score

    def set_Job_details(self, company, experience):
        self.company = company
        self.experience = experience
