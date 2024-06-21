from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

pokemon_egg_groups = Table(
    'pokemon_egg_groups',
    Base.metadata,
    Column('pokemon_id', Integer, ForeignKey('pokemons.id')),
    Column('egg_group_id', Integer, ForeignKey('egg_groups.id'))
)

class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    base_experience = Column(Integer)
    height = Column(Integer)
    weight = Column(Integer)
    egg_groups = relationship("EggGroup",
                              secondary="pokemon_egg_groups",
                              back_populates="pokemons",
                              cascade="all, delete")

class EggGroup(Base):
    __tablename__ = "egg_groups"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    pokemons = relationship("Pokemon",
                            secondary="pokemon_egg_groups",
                            back_populates="egg_groups")