from rest_framework.serializers import ModelSerializer

from habit.models import Habit
from habit.validators import (
    AssociatedHabitOnlyPleasantly,
    AssociatedHabitOrReward,
    MaxPeriodicity,
    MaxTimeToComplete,
    PleasantlyHabitNoRewardNoAssociatedHabit,
)


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            AssociatedHabitOrReward(),
            MaxTimeToComplete(),
            AssociatedHabitOnlyPleasantly(),
            PleasantlyHabitNoRewardNoAssociatedHabit(),
            MaxPeriodicity(),
        ]


class PublicHabitSerializer(ModelSerializer):

    class Meta:
        model = Habit
        fields = (
            "action",
            "is_pleasantly",
        )
