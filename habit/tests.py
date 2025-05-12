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
            user=self.user1,
            place="place2",
            time="2025-04-09T14:00:00+05:00",
            action="action2",
            time_to_complete=60,
            periodicity=1,
        )
        response = self.client.get("/habit/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 3,
                        "place": "place2",
                        "time": "2025-04-09T14:00:00+05:00",
                        "action": "action2",
                        "is_pleasantly": False,
                        "periodicity": 1,
                        "reward": None,
                        "time_to_complete": 60,
                        "is_public": False,
                        "user": 5,
                        "associated_habit": None,
                    }
                ],
            },
        )
        self.assertTrue(Habit.objects.all().exists())

    def test_habit_public_list(self):
        """Тест публичных привычек"""

        Habit.objects.create(
            user=self.user1,
            place="place3",
            time="2025-04-09T14:00:00+05:00",
            action="action3",
            time_to_complete=60,
            is_public=True,
            periodicity=1,
        )
        Habit.objects.create(
            user=self.user2,
            place="place4",
            time="2025-04-10T14:00:00+05:00",
            action="action4",
            time_to_complete=70,
            is_public=True,
            periodicity=2,
        )
        response = self.client.get("/public/")
        self.assertEqual(
            response.json(),
            {
                "count": 2,
                "next": None,
                "previous": None,
                "results": [
                    {"action": "action3", "is_pleasantly": False},
                    {"action": "action4", "is_pleasantly": False},
                ],
            },
        )

    def test_habit_retrieve(self):
        """Тест просмотра привычки"""

        Habit.objects.create(
            user=self.user1,
            place="place5",
            time="2025-04-09T14:00:00+05:00",
            action="action5",
            time_to_complete=60,
            is_public=True,
            periodicity=1,
        )
        response = self.client.get("/habit/6/")
        self.assertEqual(
            response.json(),
            {
                "id": 6,
                "place": "place5",
                "time": "2025-04-09T14:00:00+05:00",
                "action": "action5",
                "is_pleasantly": False,
                "periodicity": 1,
                "reward": None,
                "time_to_complete": 60,
                "is_public": True,
                "user": 9,
                "associated_habit": None,
            },
        )

    def test_habit_update(self):
        """Тест изменения привычки"""

        Habit.objects.create(
            user=self.user2,
            place="place6",
            time="2025-04-09T14:00:00+05:00",
            action="action6",
            time_to_complete=10,
            is_public=True,
            periodicity=5,
        )
        data = {
            "place": "place7",
            "time": "2025-04-09T14:00:00+05:00",
            "action": "action7",
            "is_pleasantly": False,
            "periodicity": 1,
            "time_to_complete": 100,
            "is_public": True,
        }
        response = self.client.patch("/habit/update/7/", data=data)
        self.assertEqual(
            response.json(),
            {
                "id": 7,
                "place": "place7",
                "time": "2025-04-09T14:00:00+05:00",
                "action": "action7",
                "is_pleasantly": False,
                "periodicity": 1,
                "reward": None,
                "time_to_complete": 100,
                "is_public": True,
                "user": 12,
                "associated_habit": None,
            },
        )

    def test_habit_delete(self):
        """Тест изменения привычки"""

        Habit.objects.create(
            user=self.user2,
            place="place7",
            time="2025-04-09T14:00:00+05:00",
            action="action7",
            time_to_complete=110,
            is_public=True,
            periodicity=6,
        )
        self.assertEqual(
            Habit.objects.all().count(),
            1
        )
