from __future__ import unicode_literals
from django.db import models
import bcrypt

class AccountManager(models.Manager):

	# def validate(self, form_data):
	# 	print "validating {}".format(form_data)
	# 	return False	


	def create_acct (self, form_data):
		account = self.create(    
			name =   form_data['name'],
			number = form_data['number'],
			due =    form_data['due'],
			amount = form_data['amount'],
		)
		return account



class Account(models.Model):
	name = models.CharField(max_length=45)
	number = models.CharField(max_length=45)
	due = models.DateTimeField(max_length=45)
	amount = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = AccountManager()

	def __str__(self):
		return "{} {} {} {}".format(self.name, self.number, self.due, self.amount)

