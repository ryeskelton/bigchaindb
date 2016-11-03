def test_backend_factory_returns_the_expected_factory():
    from bigchaindb.db import get_backend_factory
    from bigchaindb.db.rethinkdb.factory import RethinkDBFactory

    backend_config = {
        'engine': 'rethinkdb',
        'host': 'localhost',
        'port': 28015,
        'dbname': 'test'
    }

    factory = get_backend_factory(**backend_config)
    assert isinstance(factory, RethinkDBFactory)
