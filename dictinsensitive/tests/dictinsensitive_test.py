from unittest import TestCase
from dictinsensitive import DictInsensitive


class DictInsensitiveUnitTestCase(TestCase):
    def test_not_iterable(self):
        test = 1

        with self.assertRaises(TypeError):
            DictInsensitive(test)

    def test_iterable_but_not_dict(self):
        test = (1, 2)

        with self.assertRaises(TypeError):
            DictInsensitive(test)

    def test_getitem(self):
        test = DictInsensitive()
        test['test'] = 1

        self.assertEqual(test['Test'], 1)
        self.assertEqual(test['TEst'], 1)
        self.assertEqual(test['TEST'], 1)

    def test_delitem(self):
        test = DictInsensitive()

        test['test'] = 1
        del test['test']
        self.assertIsNone(test.get('test'))

        test['test'] = 1
        del test['Test']
        self.assertIsNone(test.get('test'))

        test['test'] = 1
        del test['TEST']
        self.assertIsNone(test.get('test'))

    def test_keys(self):
        test = DictInsensitive()

        test['test1'] = 1
        test['test2'] = 2

        self.assertTrue('test1' in test.keys())
        self.assertTrue('test2' in test.keys())

    def test_mapping(self):
        test = DictInsensitive([('test1', 1), ('test2', 2)])

        self.assertEqual(test['test1'], 1)
        self.assertEqual(test['test2'], 2)

    def test_dict_to_insensitive(self):
        original = {'test1': 1, 'test2': 2}
        insensitive = DictInsensitive(original)

        for key, value in insensitive.items():
            self.assertEqual(original[key], insensitive[key])
