import unittest


class YearTestCase(unittest.TestCase):

    def test_year_leap(self):

        for year in (2000, 2016, 1916):
            with self.subTest(year=year):
                self.assertTrue(is_year_leap(year),
                                "{} на самом деле високосный".format(year))

    def test_year_notleap(self):

        for year in (1900, 2014, 2001):
            with self.subTest(year=year):
                self.assertFalse(is_year_leap(year),
                                 "{} на самом деле не високосный".format(year))



def is_year_leap(year):
    
    if year % 100 != 0:
        if year % 4 == 0:
            return True
        
    else:
        if year % 400 == 0:
            return True
        
    return False


if __name__ == "__main__":
    unittest.main()
