from django.urls import path

from measurement.views import ReadChangeSensorView, ListCreateSensorsView, AddMeasurementView

urlpatterns = [
    path('sensors/', ListCreateSensorsView.as_view()),
    path('sensors/<pk>/', ReadChangeSensorView.as_view()),
    path('measurement/', AddMeasurementView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
