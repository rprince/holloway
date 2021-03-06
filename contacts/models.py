from django.db import models
import jsonfield

class Contact(models.Model):
    owner = models.ForeignKey("auth.User")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    fields = jsonfield.JSONField()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    @property
    def name(self):
        return "%s %s" % (self.first_name, self.last_name)

    @property
    def all_fields(self):
        """ A list of tuples - including the default data and custom fields """
        yield ("name", self.name)
        yield ("first_name", self.first_name)
        yield ("last_name", self.last_name)
        yield ("email", self.email)

        for i in self.fields.items():
            yield i
    

class Group(models.Model):
    owner = models.ForeignKey("auth.User")
    name = models.CharField(max_length=100)
    description = models.TextField()
    contacts = models.ManyToManyField(Contact, related_name="groups")
