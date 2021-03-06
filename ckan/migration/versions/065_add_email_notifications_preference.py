# encoding: utf-8

from sqlalchemy import *
from migrate import *

def upgrade(migrate_engine):
    metadata = MetaData()
    metadata.bind = migrate_engine
    migrate_engine.execute('''
ALTER TABLE "user"
    ADD COLUMN activity_streams_email_notifications BOOLEAN DEFAULT FALSE;
    ''')
