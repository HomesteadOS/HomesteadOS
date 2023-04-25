from django.test import TestCase
from home.models import Homestead

# Create your tests here.
class HomesteadTest(TestCase):
    def setUp(self) -> None:
        Homestead.objects.create(name="Mermaid Of Fire", description="The one, the only, the MERMAID OF FIRE")
        Homestead.objects.create(name="Valhalla", description="Feast, Fight, ...")


    def test_homestead_has_name(self) -> None:
        mermaid = Homestead.objects.get(name="Mermaid Of Fire")
        valhalla = Homestead.objects.get(name="Valhalla")
        self.assertEqual(mermaid.name, "Mermaid Of Fire")
        self.assertEqual(valhalla.name, "Valhalla")

