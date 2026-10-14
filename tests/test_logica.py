import os
import tempfile
import unittest

from app import datos, logica


class TestLogica(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
        self.tmp.close()
        os.remove(self.tmp.name)
        datos.ARCHIVO = self.tmp.name

    def tearDown(self):
        if os.path.exists(self.tmp.name):
            os.remove(self.tmp.name)

    def test_promedio_sin_notas(self):
        self.assertEqual(logica.promedio(), 0)

    def test_promedio_con_notas(self):
        logica.registrar("Ana", 9)
        logica.registrar("Luis", 7)
        self.assertAlmostEqual(logica.promedio(), 8.0)

    def test_nota_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            logica.registrar("Ana", 11)


if __name__ == "__main__":
    unittest.main()
