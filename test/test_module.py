from test.CSSTest.modules.hidden import HiddenModule
from utils import HoraceTestObject
from CSSTest.modules.paragraph import ParagraphSectionModule


class TestModule(HoraceTestObject):
    driver = None

    def test_text(self):
        webModule = ParagraphSectionModule(self.driver)
        self.assertEqual(webModule.text, 'Lorem ipsum dolor sit amet, test link adipiscing elit. Nullam dignissim convallis est. Quisque aliquam. Donec faucibus. Nunc iaculis suscipit dui. Nam sit amet sem. Aliquam libero nisi, imperdiet at, tincidunt nec, gravida vehicula, nisl. Praesent mattis, massa quis luctus fermentum, turpis mi volutpat justo, eu volutpat enim diam eget metus. Maecenas ornare tortor. Donec sed tellus eget sapien fringilla nonummy. Mauris a ante. Suspendisse quam sem, consequat at, commodo vitae, feugiat in, nunc. Morbi imperdiet augue quis tellus.\nLorem ipsum dolor sit amet, emphasis consectetuer adipiscing elit. Nullam dignissim convallis est. Quisque aliquam. Donec faucibus. Nunc iaculis suscipit dui. Nam sit amet sem. Aliquam libero nisi, imperdiet at, tincidunt nec, gravida vehicula, nisl. Praesent mattis, massa quis luctus fermentum, turpis mi volutpat justo, eu volutpat enim diam eget metus. Maecenas ornare tortor. Donec sed tellus eget sapien fringilla nonummy. Mauris a ante. Suspendisse quam sem, consequat at, commodo vitae, feugiat in, nunc. Morbi imperdiet augue quis tellus.')

    def test_required(self):
        webModule = ParagraphSectionModule(self.driver)
        self.assertTrue(webModule.displayed)
        webModule = HiddenModule(self.driver, required=True)
        self.assertFalse(webModule.displayed)

    def test_content(self):
        webModule = ParagraphSectionModule(self.driver)
        self.assertEqual(len(webModule.paragraphs), 2)
        self.assertEqual(webModule.paragraphs[1].id, 'second')

    def test_content_with_custom_base_selector(self):
        webModule = ParagraphSectionModule(self.driver, selector='#formSection')
        self.assertEqual(len(webModule.paragraphs), 9)
