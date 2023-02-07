class Prime:

    @classmethod
    def _prime(cls, keypad_strokes):
        text = ""
        # Key indexing for 100 keys
        _keys = {"2": "0",
                 "3": "1",
                 "5": "2",
                 "7": "3",
                 "11": "4",
                 "13": "5",
                 "17": "6",
                 "19": "7",
                 "23": "8",
                 "29": "9",
                 "31": "10",
                 "37": "11",
                 "41": "12",
                 "43": "13",
                 "47": "14",
                 "53": "15",
                 "59": "16",
                 "61": "17",
                 "67": "18",
                 "71": "19",
                 "73": "20",
                 "79": "21",
                 "83": "22",
                 "89": "23",
                 "97": "24",
                 "101": "25",
                 "103": "26",
                 "107": "27",
                 "109": "28",
                 "113": "29",
                 "127": "30",
                 "131": "31",
                 "137": "32",
                 "139": "33",
                 "149": "34",
                 "151": "35",
                 "157": "36",
                 "163": "37",
                 "167": "38",
                 "173": "39",
                 "179": "40",
                 "181": "41",
                 "191": "42",
                 "193": "43",
                 "197": "44",
                 "199": "45",
                 "211": "46",
                 "223": "47",
                 "227": "48",
                 "229": "49",
                 "233": "50",
                 "239": "51",
                 "241": "52",
                 "251": "53",
                 "257": "54",
                 "263": "55",
                 "269": "56",
                 "271": "57",
                 "277": "58",
                 "281": "59",
                 "283": "60",
                 "293": "61",
                 "307": "62",
                 "311": "63",
                 "313": "64",
                 "317": "65",
                 "331": "66",
                 "337": "67",
                 "347": "68",
                 "349": "69",
                 "353": "70",
                 "359": "71",
                 "367": "72",
                 "373": "73",
                 "379": "74",
                 "383": "75",
                 "389": "76",
                 "397": "77",
                 "401": "78",
                 "409": "79",
                 "419": "80",
                 "421": "81",
                 "431": "82",
                 "433": "83",
                 "439": "84",
                 "443": "85",
                 "449": "86",
                 "457": "87",
                 "461": "88",
                 "463": "89",
                 "467": "90",
                 "479": "91",
                 "487": "92",
                 "491": "93",
                 "499": "94",
                 "503": "95",
                 "509": "96",
                 "521": "97",
                 "523": "98",
                 "541": "99"
                 }
        for i in keypad_strokes.split():
            text += (_keys[i])
        return text

    @classmethod
    def decrypt(cls, message, key=None):
        """Decrypts Prime Indexing Cypher :  
        Valid if every number present is a prime number
        Indexed to the position of prime number
        Dictionary Generator at https://pastebin.com/7wXNapM5

        Args:
            message (str): encrypted text

        Returns:
            dict: {"Prime indexing" : [output]}
        """
        try:
            prime = cls._prime(message)
        except:
            prime = "N/A"
        return {"Prime indexing": prime}
