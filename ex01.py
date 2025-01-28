from sqlalchemy import create_engine

"""
https://docs.sqlalchemy.org/en/20/core/engines.html

engine = create_engine("postgresql://scott:tiger@localhost/mydatabase")
engine = create_engine("mysql://scott:tiger@localhost/foo")

# sqlite://<nohostname>/<path>
# where <path> is relative:
engine = create_engine("sqlite:///foo.db")
"""

# conectar ao SQLite em memoria
engine = create_engine('sqlite://meubanco.br', echo=True)

print("Conexão OK")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    senha = Column(String)

# criar as tabelas no banco de dados
Base.metadata.create_all(engine)
    