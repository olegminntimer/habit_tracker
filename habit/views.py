from rest_framework import generics

from habit.models import Habit
from habit.paginators import HabitPagination
from habit.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateAPIView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
