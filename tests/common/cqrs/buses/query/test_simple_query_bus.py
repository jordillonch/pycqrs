import unittest
from dataclasses import dataclass

from common.cqrs.buses.query.domain.query import Query
from common.cqrs.buses.query.domain.query_handler import QueryHandler
from common.cqrs.buses.query.infrastructure.simple_query_bus import SimpleQueryBus


class MyTestCase(unittest.TestCase):
    __query_bus = SimpleQueryBus()

    def test_simple_query_bus(self):
        handler = TestQueryHandler()
        query = TestQuery("foo")
        self.__query_bus.register(handler)
        self.__query_bus.handle(query)
        self.assertEqual(handler.last_value, "foo")


@dataclass
class TestQuery(Query):
    some_value: str


class TestQueryHandler(QueryHandler):
    __last_value: str

    def on(self, query: TestQuery):
        self.__last_value = query.some_value

    @property
    def last_value(self): return self.__last_value


if __name__ == '__main__':
    unittest.main()
