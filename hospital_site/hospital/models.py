from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator,MaxValueValidator
from multiselectfield import MultiSelectField


ROLE_CHOICES = (
    ('doctor', 'doctor'),
    ('patient', 'patient'),
    ('admin', 'admin'),
)


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True,blank=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                  MaxValueValidator(110)],
                                      null=True,blank=True)
    profile_picture = models.ImageField(upload_to='profile_images/')
    gender = models.BooleanField(default=False)




    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class Department(models.Model):
    department_name = models.CharField(max_length=32)
    level = models.PositiveSmallIntegerField(validators=[MinValueValidator(-5),
                                             MaxValueValidator(5)])


    def __str__(self):
        return self.department_name


class Specialty(models.Model):
    specialty_name = models.CharField(max_length=64)

    def __str__(self):
        return self.specialty_name


class Doctor(UserProfile):
    DAY_CHOICES =(
        ('ПН', 'ПН'),
        ('ВТ', 'ВТ'),
        ('СР', 'СР'),
        ('ЧТ', 'ЧТ'),
        ('ПТ', 'ПТ'),
        ('СБ', 'СБ'),
    )
    work_day = MultiSelectField(choices=DAY_CHOICES,max_choices=6,max_length=16)
    experience = models.PositiveSmallIntegerField(validators=[MaxValueValidator(50)])
    specialty = models.ManyToManyField(Specialty)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    service_price = models.PositiveSmallIntegerField(validators=[MaxValueValidator(200000)])
    role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='doctor')

    def __str__(self):
        return f'{self.first_name}, {self.specialty}'


    class Meta:
        verbose_name = "Doctor"


class Patient(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    emergence_contact = PhoneNumberField()
    BLOOD_CHOICES =(
        ('I+','I+'),
        ('I-', 'I-'),
        ('II+', 'II+'),
        ('II-', 'II-'),
        ('III+', 'III+'),
        ('III-', 'III-'),
        ('IV+', 'IV+'),
        ('IV-', 'IV-'),
    )
    blood_type = models.CharField( max_length=64,choices=BLOOD_CHOICES)
    role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='patient')


    def __str__(self):
        return f'{self.user.first_name}, {self.blood_type}'

    class Meta:
        verbose_name = "Patient"



class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_tame = models.DateTimeField()
    STATUS_CHOICES = (
        ('запланировано', 'запланировано'),
        ('завершено', 'завершено'),
        ('отменено', 'отменено'),
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES)


    def __str__(self):
        return f'{self.patient}, {self.doctor}, {self.date_tame}'


class MediaRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment = models.TextField()
    prescribed_medication = models.TextField()
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.patient}, {self.doctor}'


class Feedback(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i,str(i)) for i in range(1,6)],
                                              null=True, blank=True)
    comment = models.TextField(null=True, blank=True)


    def __str__(self):
        return f'{self.patient}'



class Ward(models.Model):
    TYPE_CHOICES = (
        ('Vip', 'Vip'),
        ('Simple', 'Simple'),
        ('Medium', 'Medium'),
    )

    type_ward = models.CharField(max_length=16, choices=TYPE_CHOICES)
    total_people = models.PositiveSmallIntegerField(validators=[MaxValueValidator(20)])
    current_people = models.PositiveSmallIntegerField(validators=[MaxValueValidator(20)])


    def __str__(self):
        return self.type_ward