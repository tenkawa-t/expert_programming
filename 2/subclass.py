class DistinctError(ValueError):
    """distinctdictに重複した値を追加したときに上がる例外"""


class distinctdict(dict):
    """重複した値が登録できない辞書"""
    def __setitem__(self, key, value):
        if value in self.values():
            if (
                (key in self and self[key] != value) or
                key not in self
            ):
                raise DistinctError(
                    "この値はすでに別のキーで登録されています"
                )
        super().__setitem__(key, value)


my = distinctdict()
my['key'] = 'value'
my['other_key'] = 'value'
my['other_key'] = 'value2'