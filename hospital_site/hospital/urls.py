from .views import *
from django.urls import path, include
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users'),
router.register(r'departament', DepartmentViewSet, basename='departament'),
router.register(r'specialty', SpecialtyViewSet, basename='specialty'),
# router.register(r'patient', PatientViewSet, basename='patient'),
# router.register(r'appointment', AppointmentViewSet, basename='appointment'),
# router.register(r'media_record', MediaRecordViewSet, basename='media_record'),
# router.register(r'feedback', FeedbackViewSet, basename='feedback'),
router.register(r'ward', WardViewSet, basename='ward'),
urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('doctor/', DoctorListAPIView.as_view(), name='doctor_list'),
    path('doctor/<int:pk>/', DoctorDetailAPIView.as_view(), name='doctor_detail'),
    path('doctor/create/', DoctorCreteAPIView.as_view(), name='question_create'),
    path('doctor/create/<int:pk>/', DoctorEDITAPIView.as_view(), name='question_edit'),
    path('appointment/create/', AppointmentCreateAPIVIew.as_view(), name='question_create'),
    path('appointment/create/<int:pk>/', AppointmentEDITAPIVIew.as_view(), name='question_edit'),
    path('mediarecord/create/', MediaRecordCreateAPIVIew.as_view(), name='question_create'),
    path('mediarecord/create/<int:pk>/', MediaRecordEDITAPIVIew.as_view(), name='question_edit'),
    path('feedback/create/', FeedbackCreteAPIView.as_view(), name='question_create'),
    path('feedback/create/<int:pk>/', FeedbackEDITAPIView.as_view(), name='question_edit'),
    ]

