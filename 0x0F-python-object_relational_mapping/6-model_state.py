#!/usr/bin/python3
""" a script that takes in arguments and displays all values in the statestable of hbtn_0e_0_usa where name matches the argument.But this time, write one that is safe from MySQL injections!  """
import sys
from mode_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
