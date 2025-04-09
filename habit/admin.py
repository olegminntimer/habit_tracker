from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "place",
        "time",
        "action",
        "is_pleasantly",
        "associated_habit",
        "periodicity",
        "reward",
        "is_public",
    )
