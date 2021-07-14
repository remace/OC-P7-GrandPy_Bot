from parsing import parser


class TestSentenceparser:

    def setup_method(self):
        self.question = "connais-tu le palais idéal du facteur Cheval?"
        self.sp = parser.SentenceParser()

    def test_get_clean_sentence(self):
        assert self.sp.clean_sentence(self.question) == "connais palais idéal facteur cheval"
