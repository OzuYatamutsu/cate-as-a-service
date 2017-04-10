from unittest import TestCase, main
from text import cateify

class TextTests(TestCase):
    def setUp(self):
        pass
    
    def test_can_cateify_normal_text(self):
        input = 'test'
        expected_result = 'ｔｅｓｔ'

        self.assertEqual(cateify(input), expected_result)

    def test_can_cateify_text_with_special_characters(self):
        input = 'test string\nnewline'
        expected_result = 'ｔｅｓｔ　ｓｔｒｉｎｇ\nｎｅｗｌｉｎｅ'

        self.assertEqual(cateify(input), expected_result)


if __name__ == '__main__':
    main()

