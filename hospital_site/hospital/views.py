from .filters import DoctorFilter
from .models import *
from .serializers import *
from rest_framework import viewsets,generics,status
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import PostPagination
# from .permissions import CreateAppointment,CreateDoctor
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response




class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class =DepartmentSerializer

class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer


class DoctorListAPIView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorListSerializer
    filter_backends = [ SearchFilter, OrderingFilter]
    filterset_class = DoctorFilter
    search_fields = ['specialty', ]
    ordering_fields = ['service_price', ]




class DoctorDetailAPIView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer


class DoctorCreteAPIView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer
    # permission_classes = [CreateDoctor]


class DoctorEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    pagination_class = PostPagination

class AppointmentListAPIVIew(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentDetailAPIVIew(generics.RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentCreateAPIVIew(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentCreateSerializer
    # pagination_class = CreateAppointment


class AppointmentEDITAPIVIew(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class MediaRecordListAPIView(generics.ListAPIView):
    queryset = MediaRecord.objects.all()
    serializer_class = MediaRecordListSerializer

class MediaRecordCreateAPIVIew(generics.RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class MediaRecordEDITAPIVIew(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer



class MediaRecordDetailAPIView(generics.RetrieveAPIView):
    queryset = MediaRecord.objects.all()
    serializer_class = MediaRecordDetailSerializer


class FeedbackListAPIView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackListSerializer



class FeedbackDetailAPIView(generics.RetrieveAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackDetailSerializer


class FeedbackCreteAPIView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackDetailSerializer


class FeedbackEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackDetailSerializer

class WardViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer