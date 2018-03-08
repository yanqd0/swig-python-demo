import example


def test_echo():
    result = example.echo('message')
    assert isinstance(result, str)
    assert 'message' == result


def test_vector_int2str():
    data = example.vector_int2str([1, 2, 3])
    assert isinstance(data, tuple)
    assert ('1', '2', '3') == data


def test_reverse_map():
    str2int = example.Str2intMap()
    str2int['1'] = 1
    str2int['2'] = 2
    str2int['3'] = 3
    result = example.reverse_map(str2int)
    assert isinstance(result, example.Int2strMap)
    for key, value in result.items():
        assert str2int[value] == key
