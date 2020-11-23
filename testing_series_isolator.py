import unittest
import series_isolator as SI
from series import Series
from id_manager import IdManager as IDM

class SeriesIsolatorTest(unittest.TestCase):

    def test_urlConversion(self):
        self.assertEqual(SI.series_to_wiki_link("Mobile Suit Gundam"),"https://gundam.fandom.com/wiki/Mobile_Suit_Gundam")

    def test_creationSeries(self):
        dict = {
            "id": 0,
            "grade": "RG",
            "release-year": 2010,
            "name": "RX-78-2 Gundam",
            "p-bandai": False,
            "info": {
                "scale": "1/144",
                "series": "Mobile Suit Gundam",
                "notes": "First release from the Universal Century timeline. Features the Core Block Transformation and Combination System. Includes fully transformable FF-X7 Core Fighter, a non-transformable Core Block, and an Amuro Ray figurine. Kits from RG-01 to RG-13 use a base adapter that is compatible with Action Base 2 only.",
                "image-link": "https://static.wikia.nocookie.net/gundam/images/2/29/RX782_Gundam_-_RG_Boxart.jpg/revision/latest?cb=20111226174639"
            }
        }
        expected = {"id":0,"name":"Mobile Suit Gundam","wiki-link":"https://gundam.fandom.com/wiki/Mobile_Suit_Gundam"}
        name = dict["info"]["series"]
        wiki_link = SI.series_to_wiki_link(name)
        self.assertEqual(Series(0,name,wiki_link).json(),expected)
    
    def test_seriesConversion(self):
        dict = {
            "id": 0,
            "grade": "RG",
            "release-year": 2010,
            "name": "RX-78-2 Gundam",
            "p-bandai": False,
            "info": {
                "scale": "1/144",
                "series": "Mobile Suit Gundam",
                "notes": "First release from the Universal Century timeline. Features the Core Block Transformation and Combination System. Includes fully transformable FF-X7 Core Fighter, a non-transformable Core Block, and an Amuro Ray figurine. Kits from RG-01 to RG-13 use a base adapter that is compatible with Action Base 2 only.",
                "image-link": "https://static.wikia.nocookie.net/gundam/images/2/29/RX782_Gundam_-_RG_Boxart.jpg/revision/latest?cb=20111226174639"
            }
        }
        expected = {
            "id":0,
            "name":"Mobile Suit Gundam",
            "wiki-link":"https://gundam.fandom.com/wiki/Mobile_Suit_Gundam"
        }
        self.assertEqual(SI.convert_to_series(dict["info"]["series"],0),expected)

    def test_isolation(self):
        list = [
            {
                "id": 3,
                "grade": "RG",
                "release-year": 2011,
                "name": "MS-06F Zaku II",
                "p-bandai": False,
                "info": {
                    "scale": "1/144",
                    "series": "Mobile Suit Gundam",
                    "notes": "Parts and color variant of RG-02. Includes left open hand, right trigger hand, and Zeon pilot figurine.",
                    "image-link": "https://static.wikia.nocookie.net/gundam/images/b/b5/Rg-1-144-ms-06f.jpg/revision/latest?cb=20111017085248"
                }
            },
            {
                "id": 2,
                "grade": "RG",
                "release-year": 2011,
                "name": "GAT-X105 Aile Strike Gundam",
                "p-bandai": False,
                "info": {
                    "scale": "1/144",
                    "series": "Mobile Suit Gundam SEED",
                    "notes": "First release from the Cosmic Era timeline. Includes Kira Yamato figurine.",
                    "image-link": "https://static.wikia.nocookie.net/gundam/images/5/5e/Rg_aile_strike.jpg/revision/latest?cb=20111016193301"
                }
            }
        ]
        expected = [
            {
                "id":0,
                "name":"Mobile Suit Gundam",
                "wiki-link":"https://gundam.fandom.com/wiki/Mobile_Suit_Gundam"
            },{
                "id":1,
                "name":"Mobile Suit Gundam SEED",
                "wiki-link":"https://gundam.fandom.com/wiki/Mobile_Suit_Gundam_SEED"
            }
        ]
        id_manager = IDM()
        self.assertEqual(SI.isolate(list,id_manager),expected)
    
    def test_isolationSeveralTimesSameSeries(self):
        list = [
            {
                "id": 3,
                "grade": "RG",
                "release-year": 2011,
                "name": "MS-06F Zaku II",
                "p-bandai": False,
                "info": {
                    "scale": "1/144",
                    "series": "Mobile Suit Gundam",
                    "notes": "Parts and color variant of RG-02. Includes left open hand, right trigger hand, and Zeon pilot figurine.",
                    "image-link": "https://static.wikia.nocookie.net/gundam/images/b/b5/Rg-1-144-ms-06f.jpg/revision/latest?cb=20111017085248"
                }
            },
            {
                "id": 2,
                "grade": "RG",
                "release-year": 2011,
                "name": "GAT-X105 Aile Strike Gundam",
                "p-bandai": False,
                "info": {
                    "scale": "1/144",
                    "series": "Mobile Suit Gundam SEED",
                    "notes": "First release from the Cosmic Era timeline. Includes Kira Yamato figurine.",
                    "image-link": "https://static.wikia.nocookie.net/gundam/images/5/5e/Rg_aile_strike.jpg/revision/latest?cb=20111016193301"
                }
            },{
                "id": 105,
                "grade": "RG",
                "release-year": 2015,
                "name": "MS-06S Zaku II (Char Aznable's Custom) Ver. GUNDAM docks at Singapore",
                "p-bandai": False,
                "series": "Mobile Suit Gundam",
                "info": {
                    "scale": "1/144",
                    "notes": "Gundam Docks at Singapore exclusive re-release of RG-02 with special marking sheet.",
                    "image-link": "https://static.wikia.nocookie.net/gundam/images/5/5b/RG-CharZaku-SG.jpg/revision/latest?cb=20150802043435"
                }
            }
        ]
        expected = [
            {
                "id":0,
                "name":"Mobile Suit Gundam",
                "wiki-link":"https://gundam.fandom.com/wiki/Mobile_Suit_Gundam"
            },{
                "id":1,
                "name":"Mobile Suit Gundam SEED",
                "wiki-link":"https://gundam.fandom.com/wiki/Mobile_Suit_Gundam_SEED"
            }
        ]
        id_manager = IDM()
        self.assertEqual(SI.isolate(list,id_manager),expected)

if __name__ == '__main__':
    unittest.main()