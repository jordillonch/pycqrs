from abc import abstractmethod

from common.cqrs.buses.query.domain.query import Query


class QueryHandler:
    @abstractmethod
    def on(self, query: Query): raise NotImplementedError
