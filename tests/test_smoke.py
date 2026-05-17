import sys
import os

# allow imports from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.text_preprocessing import clean_text


def test_clean_text_basic():
    text = "Hello!!! This is a TEST review 😡"
    result = clean_text(text)

    assert isinstance(result, str)
    assert len(result) > 0