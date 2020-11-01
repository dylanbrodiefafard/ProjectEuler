from solutions.BaseSolution import BaseSolution


class Solution19(BaseSolution):
    NUMBER = 19
    VERIFIED_ANSWER = 171
    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    D_BY_MONTH = [
        {'January': 0, 'February': 3, 'March': 3, 'April': 6, 'May': 1, 'June': 4, 'July': 6, 'August': 2,
         'September': 5, 'October': 0, 'November': 3, 'December': 5},
        {'January': 6, 'February': 2, 'March': 3, 'April': 6, 'May': 1, 'June': 4, 'July': 6, 'August': 2,
         'September': 5, 'October': 0, 'November': 3, 'December': 5}
    ]
    A_BY_CENTURY = {'17': 4, '18': 2, '19': 0, '20': 6, '21': 4, '22': 2, '23': 0, '24': 6, '25': 4, '26': 2}

    def run_tests(self, test_case):
        test_case.assertTrue(self.is_sunday_on_first_of_the_month(1920, 'August'))
        test_case.assertTrue(self.is_sunday_on_first_of_the_month(1965, 'August'))
        test_case.assertTrue(self.is_sunday_on_first_of_the_month(1996, 'September'))
        test_case.assertTrue(self.is_sunday_on_first_of_the_month(1996, 'December'))
        test_case.assertFalse(self.is_sunday_on_first_of_the_month(1996, 'January'))
        test_case.assertFalse(self.is_sunday_on_first_of_the_month(1920, 'January'))
        test_case.assertFalse(self.is_sunday_on_first_of_the_month(1965, 'May'))
        test_case.assertFalse(self.is_sunday_on_first_of_the_month(1996, 'April'))
        test_case.assertTrue(self.is_leap_year(1904))
        test_case.assertTrue(self.is_leap_year(1964))
        test_case.assertTrue(self.is_leap_year(1972))
        test_case.assertFalse(self.is_leap_year(1929))
        test_case.assertFalse(self.is_leap_year(2006))
        test_case.assertFalse(self.is_leap_year(2018))

    @staticmethod
    def is_sunday_on_first_of_the_month(year, month):
        digits = str(year)
        a = Solution19.A_BY_CENTURY[digits[:2]]
        b = int(digits[-2:])
        c = b // 4
        i = 1 if Solution19.is_leap_year(year) else 0
        d = Solution19.D_BY_MONTH[i][month]
        e = a + b + c + d + 1
        return e % 7 == 0

    @staticmethod
    def is_leap_year(year):
        if year % 4 == 0:
            if year % 100 == 0:
                return year % 400 == 0
            else:
                return True
        return False

    def get_answer(self):
        num_sundays_on_first_of_the_month = 0
        for year in range(1901, 2001):
            for month in self.MONTHS:
                if self.is_sunday_on_first_of_the_month(year, month):
                    num_sundays_on_first_of_the_month += 1
        return num_sundays_on_first_of_the_month


if __name__ == '__main__':
    Solution19().print_answer()
