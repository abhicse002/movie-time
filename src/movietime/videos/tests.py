from django.test import TestCase
from .models import Videos
# Create your tests here.


class VideoModelTestCase(TestCase):
    def setUp(self):
        #creates a seperate test database for us and adds it
        Videos.objects.create(title="Zoo video", description="Zoo Videos", videos_id="001" )
    #start with test_
    def test_valid_title(self):
        title = "Zoo video"
        qs = Videos.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_valid_desc(self):
        desc = "Zoo Videos"
        qs = Videos.objects.filter(description=desc)
        self.assertTrue(qs.exists())

    


