from abc import abstractmethod

from common.cqrs.buses.query.domain.query import Query
from common.cqrs.buses.query.domain.query_handler import QueryHandler


class QueryBus:
    @abstractmethod
    def register(self, handler: QueryHandler): raise NotImplementedError

    @abstractmethod
    def handle(self, query: Query): raise NotImplementedError
