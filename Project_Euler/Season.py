import unittest


class SeasonTestCase(unittest.TestCase):

    def test_season(self):
        seasons = [None, 'зима', 'зима', 'весна', 'весна', 'весна',
                   'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']

        for month in range(1, 13):
            with self.subTest(month=month):
                self.assertEqual(season(month).lower(), seasons[month])

                

def season(month):
    
    seasons = {'winter': (12, 1, 2),
               'spring': (3, 4, 5),
               'summer': (6, 7, 8),
               'autumn': (9, 10, 11)}

    if month in seasons['winter']: return 'зима'

    elif month in seasons['spring']: return 'весна'

    elif month in seasons['summer']: return 'лето'

    elif month in seasons['autumn']: return 'осень'

    else: return 'wtf?'



if __name__ == "__main__":
    unittest.main()
               
