import pytest

# Added to prevent ImportError: No module named 'posteat'
# https://stackoverflow.com/a/9806045/584134
# Please also note the difference between append and insert
import os
import inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
os.sys.path.insert(0, parent_dir)
# ---
from posteat.posteat import PostEat


class TestPostEat:
    def test_empty_list(self):
        """Test the emptiness of a list.
        See https://stackoverflow.com/questions/53513/best-way-to-check-if-a-list-is-empty
        """
        test_list = None
        with pytest.raises(TypeError):
            len(test_list) == 0
        test_list = []
        assert len(test_list) == 0
        test_list.append(43)
        assert len(test_list) > 0

    def test_use_module(self):
        posteat = PostEat()
        pass

    def test_insert(self):
        pass

    def test_get(self):
        pass
