def get_zodiac(self):
    current = self.birthdate.split(".")
    day = int(current[0])
    month = current[1]

    def gzfdb(zodiac):
        return Zodiac.objects.filter(zodiac=zodiac)[0]
if month == '12':
    self.zodiac = gzfdb('Sagittarius') if (day < 22) else gzfdb('Capricorn')
elif month == '01':
    self.zodiac = gzfdb('Capricorn') if (day < 20) else gzfdb('Aquarius')
elif month == '02':
    self.zodiac = gzfdb('Aquarius') if (day < 19) else gzfdb('Pisces')
elif month == '03':
    self.zodiac = gzfdb('Pisces') if (day < 21) else gzfdb('Aries')
elif month == '04':
    self.zodiac = gzfdb('Aries') if (day < 20) else gzfdb('Taurus')
elif month == '05':
    self.zodiac = gzfdb('Taurus') if (day < 21) else gzfdb('Gemini')
elif month == '06':
    self.zodiac = gzfdb('Gemini') if (day < 21) else gzfdb('Cancer')
elif month == '07':
    self.zodiac = gzfdb('Cancer') if (day < 23) else gzfdb('Leo')
elif month == '08':
    self.zodiac = gzfdb('Leo') if (day < 23) else gzfdb('Virgo')
elif month == '09':
    self.zodiac = gzfdb('Virgo') if (day < 23) else gzfdb('Libra')
elif month == '10':
    self.zodiac = gzfdb('Libra') if (day < 23) else gzfdb('Scorpio')
elif month == '11':
    self.zodiac = gzfdb('Scorpio') if (day < 22) else gzfdb('Sagittarius')

    first_zodiac_dict = {
        '12':('Sagittarius'),
        '01':('Capricorn'),
        '02':('Aquarius'),
        '03':('Pisces'),
        '04':('Aries'),
        '05':('Taurus'),
        '06':('Gemini'),
        '07':('Cancer'),
        '08':('Leo'),
        '09':('Virgo'),
        '10':('Libra'),
        '11':('Scorpio')
    }
    second_zodiac_dict = {
        '12':('Capricorn'),
        '01': ('Aquarius'),
        '02': ('Pisces'),
        '03': ('Aries'),
        '04': ('Taurus'),
        '05': ('Gemini'),
        '06': ('Cancer'),
        '07': ('Leo'),
        '08': ('Virgo'),
        '09': ('Libra'),
        '10': ('Scorpio'),
        '11': ('Sagittarius')
    }