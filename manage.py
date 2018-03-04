#!/usr/bin/env python
import os
import sys


class SWord:
    """单词,带上例句"""

    def __init__(self, word, meaning, sentence_en, sentence_ch):
        self.word = word
        self.meaning = meaning
        self.sentence_en = sentence_en
        self.sentence_ch = sentence_ch

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VocabularyLearning.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
