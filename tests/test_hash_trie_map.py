"""
Modified from the pyrsistent test suite.

Pre-modification, these were MIT licensed, and are copyright:

    Copyright (c) 2022 Tobias Gustafsson

    Permission is hereby granted, free of charge, to any person
    obtaining a copy of this software and associated documentation
    files (the "Software"), to deal in the Software without
    restriction, including without limitation the rights to use,
    copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following
    conditions:

    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.
"""
from collections.abc import Hashable, Mapping

import pytest
from rpds import HashTrieMap


def test_instance_of_hashable():
    assert isinstance(HashTrieMap(), Hashable)


def test_instance_of_map():
    assert isinstance(HashTrieMap(), Mapping)


def test_empty_initialization():
    a_map = HashTrieMap()
    assert len(a_map) == 0


def test_initialization_with_one_element():
    the_map = HashTrieMap({"a": 2})
    assert len(the_map) == 1
    assert the_map["a"] == 2
    assert "a" in the_map

    empty_map = the_map.remove("a")
    assert len(empty_map) == 0
    assert "a" not in empty_map


def test_get_non_existing_raises_key_error():
    m1 = HashTrieMap()
    with pytest.raises(KeyError) as error:
        m1["foo"]

    assert str(error.value) == "'foo'"


def test_remove_non_existing_element_raises_key_error():
    m1 = HashTrieMap(a=1)

    with pytest.raises(KeyError) as error:
        m1.remove("b")

    assert str(error.value) == "'b'"


def test_various_iterations():
    assert {"a", "b"} == set(HashTrieMap(a=1, b=2))
    assert ["a", "b"] == sorted(HashTrieMap(a=1, b=2).keys())
    assert [1, 2] == sorted(HashTrieMap(a=1, b=2).values())
    assert {("a", 1), ("b", 2)} == set(HashTrieMap(a=1, b=2).items())

    pm = HashTrieMap({str(k): k for k in range(100)})
    assert len(pm) == len(pm.keys())
    assert len(pm) == len(pm.values())
    assert len(pm) == len(pm.items())
    ks = pm.keys()
    assert all(k in pm for k in ks)
    assert all(k in ks for k in ks)
    us = pm.items()
    assert all(pm[k] == v for (k, v) in us)
    vs = pm.values()
    assert all(v in vs for v in vs)


def test_initialization_with_two_elements():
    map1 = HashTrieMap({"a": 2, "b": 3})
    assert len(map1) == 2
    assert map1["a"] == 2
    assert map1["b"] == 3

    map2 = map1.remove("a")
    assert "a" not in map2
    assert map2["b"] == 3