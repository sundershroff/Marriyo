from django.db import models
import random
# Create your models here.
def generate_unique_uid():
    return random.randint(100000, 999999)

class superadmin_data(models.Model):
    email = models.EmailField()
    password = models.TextField()

class emra_coin(models.Model):
    country = models.TextField()
    currency = models.TextField()
    emra_coin_value = models.TextField()

class external_expenses(models.Model):
    details = models.TextField()
    to = models.TextField()
    date = models.TextField()
    currency = models.TextField()
    amount = models.TextField()
    frequency = models.TextField()
    attachment = models.TextField()

class subscription(models.Model):
    Subscription_Country = models.TextField()
    Title_of_the_plan = models.TextField()
    Type_Of_Subscription = models.TextField()
    Amount_with_ad = models.IntegerField(null=True)
    Amount_without_ad = models.IntegerField(null=True)
    Validity = models.TextField(null=True)
    # Validity_to = models.DateField()
    Option1 = models.TextField(null=True)
    value1 = models.CharField(max_length=255,null=True,blank=True)
    Option2 = models.TextField(null=True)
    value2 = models.CharField(max_length=255,null=True,blank=True)
    Option3 = models.TextField(null=True)
    value3 = models.CharField(max_length=255,null=True,blank=True)

class commision(models.Model):
    title = models.TextField(null=True)
    country = models.TextField(null=True)
    commision_start = models.DateField(null=True)
    commision_end = models.DateField(null=True)
    to_whom = models.TextField(null=True)
    from_whom = models.TextField(null=True)
    for_what = models.TextField(null=True)
    how_many = models.TextField(null=True)
    subscription = models.TextField(null=True)
    commision = models.TextField(null=True)
    how_many_coin = models.TextField(null=True)
    how_many_views = models.TextField(null=True)
    
class third_party_user(models.Model):
    id = models.IntegerField(unique=True,primary_key=True, null=False)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_unique_uid()
        super().save(*args, **kwargs)
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    email = models.EmailField(null=True)
    phone_no = models.TextField(null=True)
    password = models.TextField(null=True)
    access_privilage = models.TextField(null=True)

class insentives_settings(models.Model):
    sales_target = models.TextField(null=True)
    Incentives_Amount_INR = models.TextField(null=True)
    Incentives_Amount_USD = models.TextField(null=True)
    
class pi_settings(models.Model):
    default_amount = models.TextField(null=True)
    to_Admin = models.TextField(null=True)
    to_investigator = models.TextField(null=True)
    
class pi_performance_calculation(models.Model):
    Calculation_Period = models.TextField(null=True)
    default_amount = models.TextField(null=True)
    fifty_Good_Review = models.TextField(null=True)
    eighty_Good_Review = models.TextField(null=True)
    fifty_bad_Review = models.TextField(null=True)
    eighty_bad_Review = models.TextField(null=True)
    
class dropdown(models.Model):
    country = models.TextField(null=True)
    cities = models.TextField(null=True)
    currency = models.TextField(null=True)
    marital_status = models.TextField(null=True)
    physical_status = models.TextField(null=True)
    cast = models.TextField(null=True)
    type_of_relationship = models.TextField(null=True)
    education = models.TextField(null=True)
    job_position = models.TextField(null=True)
    salary_range = models.TextField(null=True)
    intrest = models.TextField(null=True)
    no_intrest = models.TextField(null=True)
    complexion = models.TextField(null=True)
    food_taste = models.TextField(null=True)
    organs = models.TextField(null=True)
    familystatus = models.TextField(null=True)
    category = models.TextField(null=True)
    values = models.TextField(null=True)
    
class dummy_matching_list(models.Model):
    image = models.TextField(null=True)
    username = models.TextField(null=True)
    userid = models.TextField(null=True)
    tagline = models.TextField(null=True)

class fees_hiringmanager(models.Model):
    fees = models.TextField(null=True)

