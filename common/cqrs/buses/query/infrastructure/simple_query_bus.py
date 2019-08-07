import inspect

from common.cqrs.buses.query.domain.query import Query
from common.cqrs.buses.query.domain.query_bus import QueryBus
from common.cqrs.buses.query.domain.query_handler import QueryHandler


class SimpleQueryBus(QueryBus):
    __handlers = {}

    def register(self, handler: QueryHandler):
        queryType = inspect.signature(handler.on).parameters["query"].annotation
        self.__handlers[queryType] = handler

    def handle(self, query: Query):
        queryType = type(query)
        return self.__handlers[queryType].on(query)
