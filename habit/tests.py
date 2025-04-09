from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование приложения habit"""

    def setUp(self):
        self.user1 = User.objects.create(email="user1@sky.pro")
        self.user2 = User.objects.create(email="user2@mail.com")

    def test_habit_create(self):
        """Тестирование создания привычки"""
        data = {
            "user": self.user1.pk,
            "place": "place1",
            "time": "2025-04-09T14:00:00+05:00",
            "action": "action1",
            "time_to_complete": 60,
            "periodicity": 1,
        }
        response = self.client.post("/habit/create/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "place": "place1",
                "time": "2025-04-09T14:00:00+05:00",
                "action": "action1",
                "is_pleasantly": False,
                "periodicity": 1,
                "reward": None,
                "time_to_complete": 60,
                "is_public": False,
                "user": 1,
                "associated_habit": None,
            },
        )

    def test_habit_list(self):
        """Тестирование списка привычек"""

        Habit.objects.create(
            user=1,
            place="place1",
            time="2025-04-09T14:00:00+05:00",
            action="action1",
            time_to_complete=60,
            periodicity=1,
        )
        response = self.client.get("/habit/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.json())
        # self.assertEqual(
        #     response.json(),
        #     [
        #         {
        #             "id": 1,
        #             "place": "place1",
        #             "time": "2025-04-09T14:00:00+05:00",
        #             "action": "action1",
        #             "is_pleasantly": False,
        #             "periodicity": 1,
        #             "reward": None,
        #             "time_to_complete": 60,
        #             "is_public": False,
        #             "user": 1,
        #             "associated_habit": None,
        #         }
        #     ]
        # )
