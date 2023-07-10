from translator import englishToFrench, frenchToEnglish

class TestEnToFr(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertEqual(englishToFrench("dad"), "papa")

class TestFrToEn(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertEqual(frenchToEnglish("papa"), "dad")

unittest.main()