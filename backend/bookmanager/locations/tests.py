from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import LocationRoot, Rack, Section

class LocationsAPITest(APITestCase):

    def setUp(self):
        # Создаем тестовый корень (библиотеку)
        self.root1 = LocationRoot.objects.create(name="Библиотека 1", description="Главная")
        self.root2 = LocationRoot.objects.create(name="Библиотека 2", description="Вторичная")

        # Создаем тестовые стеллажи
        self.rack1 = Rack.objects.create(number="A1", root=self.root1)
        self.rack2 = Rack.objects.create(number="A2", root=self.root1)
        self.rack3 = Rack.objects.create(number="B1", root=self.root2)

        # Создаем тестовые секции
        self.section1 = Section.objects.create(number="1", rack=self.rack1)
        self.section2 = Section.objects.create(number="2", rack=self.rack1)
        self.section3 = Section.objects.create(number="1", rack=self.rack3)

    # ----------------- LocationRoot -----------------
    def test_get_all_roots(self):
        url = reverse('locations:root_list_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_root(self):
        url = reverse('locations:root_list_create')
        data = {"name": "Библиотека 3", "description": "Новая"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(LocationRoot.objects.count(), 3)

    # ----------------- Rack -----------------
    def test_get_all_racks(self):
        url = reverse('locations:rack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_racks_by_root(self):
        url = reverse('locations:root_racks', args=[self.root1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        # Проверяем что все racks принадлежат root1
        for rack in response.data:
            self.assertEqual(rack['root'], self.root1.id)

    def test_create_rack_with_root(self):
        url = reverse('locations:root_racks', args=[self.root2.id])
        data = {"number": "B2"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rack.objects.filter(root=self.root2).count(), 2)

    # ----------------- Section -----------------
    def test_get_all_sections(self):
        url = reverse('locations:section_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_sections_by_rack(self):
        url = reverse('locations:rack_sections', args=[self.rack1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        for section in response.data:
            self.assertEqual(section['rack'], self.rack1.id)

    def test_create_section_under_rack(self):
        url = reverse('locations:rack_sections', args=[self.rack3.id])
        data = {"number": "2"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Section.objects.filter(rack=self.rack3).count(), 2)

    # ----------------- DELETE tests -----------------
    def test_delete_rack(self):
        url = reverse('locations:rack_detail', args=[self.rack1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Rack.objects.filter(id=self.rack1.id).exists())

    def test_delete_section(self):
        url = reverse('locations:section_detail', args=[self.section1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Section.objects.filter(id=self.section1.id).exists())

    # ----------------- UPDATE tests (PUT) -----------------
    def test_update_root(self):
        url = reverse('locations:root_detail', args=[self.root1.id])
        data = {"name": "Библиотека 1 Обновленная", "description": "Главная Обновленная"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.root1.refresh_from_db()
        self.assertEqual(self.root1.name, "Библиотека 1 Обновленная")
        self.assertEqual(self.root1.description, "Главная Обновленная")

    def test_update_rack(self):
        url = reverse('locations:rack_detail', args=[self.rack1.id])
        data = {"number": "A1-Updated", "root": self.root1.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.rack1.refresh_from_db()
        self.assertEqual(self.rack1.number, "A1-Updated")

    def test_update_section(self):
        url = reverse('locations:section_detail', args=[self.section1.id])
        data = {"number": "1-Updated", "rack": self.rack1.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.section1.refresh_from_db()
        self.assertEqual(self.section1.number, "1-Updated")
