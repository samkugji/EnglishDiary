from django.core.urlresolvers import reverse

from rest_framework import status

from diaries.models import Diary
from .base import DiaryBaseTestCase


class DiaryAPIViewTestCase(DiaryBaseTestCase):

    def test_create_diary(self):

        test_create_url = reverse('api:diary:create')
        test_datetime = '2016/07/02'
        test_content = 'Today I realy want to write diary!'
        test_data = {
            'datetime': test_datetime,
            'content': test_content,
        }
        response = self.client.post(
            test_create_url,
            test_data,
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(
            Diary.objects.count(),
            1,
        )
        self.assertEqual(
            Diary.objects.get().datetime,
            test_datetime,
        )
        self.assertEqual(
            Diary.objects.get().content,
            test_content,
        )
        self.assertEqual(
            response.data.get("result"),
            True,
        )

    def test_get_diary(self):
        year = "2016"
        month = "07"
        day = "02"
        test_datetime = year + "/" + month + "/" + day
        test_content = 'Today I realy want to read diary!'

        # Create a diary
        self.diary = self.user.diary_set.create(
            content=test_content,
            datetime=test_datetime,
        )

        test_detail_url = reverse(
            'api:diary:detail',
            kwargs={
                "year": year,
                "month": month,
                "day": day,
            },
        )

        response = self.client.get(
            test_detail_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(
            response.data.get("content"),
            test_content,
        )

    def test_delete_diary(self):
        year = "2016"
        month = "07"
        day = "02"
        test_datetime = year + "/" + month + "/" + day
        test_content = 'Today I realy want to delete diary!'

        # Create a diary
        self.diary = self.user.diary_set.create(
            content=test_content,
            datetime=test_datetime,
        )

        test_delete_url = reverse(
            'api:diary:detail',
            kwargs={
                "year": year,
                "month": month,
                "day": day,
            },
        )

        response = self.client.delete(
            test_delete_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(
            Diary.objects.count(),
            0,
        )

        def test_search_korean_in_diary_content(self):
            test_create_url = reverse('api:diary:create')
            test_datetime = '2016/07/02'
            test_content = 'Today I 정말 want to write diary!'
            test_data = {
                'datetime': test_datetime,
                'content': test_content,
            }
            response = self.client.post(
                test_create_url,
                test_data,
            )
            self.assertEqual(
                response.status_code,
                status.HTTP_201_CREATED,
            )
            self.assertEqual(
                Diary.objects.count(),
                0,
            )
            self.assertEqual(
                Diary.objects.get().datetime,
                test_datetime,
            )
            self.assertEqual(
                response.data.get("result"),
                False,
            )