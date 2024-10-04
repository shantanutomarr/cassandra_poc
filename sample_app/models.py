import uuid

from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


class Book(DjangoCassandraModel):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    title = columns.Text(required=True)
    author = columns.Text(required=True)
    published_year = columns.Integer()
