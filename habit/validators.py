from rest_framework import serializers

from habit.models import Habit


class AssociatedHabitOrReward:
    """Исключает одновременный выбор связанной привычки и указания вознаграждения."""

    def __call__(self, value):
        if value.get("associated_habit") and value.get("reward"):
            raise serializers.ValidationError(
                "Невозможен одновременный выбор связанной привычки и указания вознаграждения."
            )


class MaxTimeToComplete:
    """Время выполнения должно быть не больше 120 секунд."""

    def __call__(self, value):
        if value.get("time_to_complete") > 120:
            raise serializers.ValidationError("Время на выполнение должно быть меньше 120 секунд.")


class AssociatedHabitOnlyPleasantly:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки."""

    def __call__(self, value):
        if value.get("associated_habit"):
            associated_habit = Habit.objects.get(pk=value.get("associated_habit").id)
            if not associated_habit.is_pleasantly:
                raise serializers.ValidationError(
                    "В связанные привычки могут попадать только привычки с признаком приятной привычки."
                )


class PleasantlyHabitNoRewardNoAssociatedHabit:
    """У приятной привычки не может быть вознаграждения или связанной привычки."""

    def __call__(self, value):
        if value.get("is_pleasantly") and any([value.get("reward"), value.get("associated_habit")]):
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки."
            )


class MaxPeriodicity:
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней."""

    def __call__(self, value):
        if value.get("periodicity") > 7:
            raise serializers.ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")
