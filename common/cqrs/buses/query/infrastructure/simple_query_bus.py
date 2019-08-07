from common.cqrs.buses.query.domain.query import Query
from common.cqrs.buses.query.domain.query_bus import QueryBus
from common.cqrs.buses.query.domain.query_handler import QueryHandler


class SimpleQueryBus(QueryBus):
    def register(self, handler: QueryHandler):
        pass

    def handle(self, query: Query):
        pass
