"""
a script that lists all State objects from the database hbtn_0e_6_usa

script should take 3 arguments: mysql username, mysql password and database name
must use the module SQLAlchemy
must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""


from model_state import Base, State
from sqlalchemy import (engine)


if __name__ == '__main__':
    engine = cr
