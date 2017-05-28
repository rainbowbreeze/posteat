import pytest

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

    def test_insert(self):
        pass

    def test_get(self):
        pass
