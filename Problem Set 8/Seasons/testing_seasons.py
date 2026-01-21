import seasons


class MockDate(seasons.date):
    @classmethod
    def today(cls):
        return cls(2000, 1, 2)


def test_get_minutes_one_day(monkeypatch):
    monkeypatch.setattr(seasons, "date", MockDate)
    assert seasons.get_minutes(seasons.date(2000, 1, 1)) == 1440


def test_get_minutes_two_days(monkeypatch):
    monkeypatch.setattr(seasons, "date", MockDate)
    assert seasons.get_minutes(seasons.date(1999, 12, 31)) == 2880


def test_convert_to_words():
    assert (
        seasons.convert_to_words(525600)
        == "Five hundred twenty-five thousand, six hundred minutes"
    )

