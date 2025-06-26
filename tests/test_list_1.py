from pydantic import TypeAdapter
import pytest
from sqlalchemy import text

from src.candies.schemas import CandySchema
from src.candies.service import CandiesService
from src.db import Base, engine
from src.candies.models import Candies #Нужна чтобы прогнался этот фаил из-за Base

from src.config import settings

#Фикстура для подготовки среды
@pytest.fixture(scope="session", autouse=True)#прогнать фикстуру перед первым тестов в скоупе, scope:session-все прогоны тестов, package - на уровне папки, module-уровень файла, function(default)-уровень функции
def setup_db():
    print(f"{settings.DB_NAME=}")
    assert settings.MODE == "TEST"
    print("Перед созданием БД")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("После создания БД")




@pytest.fixture() #Если scope = модуль, то перед самым первом тестом фикстура прогонится, а при последующих не будет.
def empty_candies():
    CandiesService.delete_all()
    with engine.connect() as conn:
        if engine.dialect.name == "postgresql":
            conn.execute(text("ALTER SEQUENCE candies_id_seq RESTART WITH 1"))
        elif engine.dialect.name == "sqlite":
            conn.execute(text("DELETE FROM sqlite_sequence WHERE name='candies'"))
        conn.commit()

#Фикстура для заполнения тестовых данных(Лучше не делать autouse=True, а явно передавать где это нужно)
@pytest.fixture()
def candies():
    candies = [
        CandySchema(title="candy1", owner="Даниил"),
        CandySchema(title="candy2", state="eaten"),
        CandySchema(title="candy3", state="half"),
    ]
    return candies #Возвращает данные. Поэтому она из-за автоюза отработает перед тестом, но данные никак не передаст. Нужно явно передавать возвращаемую фикстуру в тест-функцию

#@pytest.mark.usefixtures("empty_candies") на классе заставит pytest вызывать фикстуру empty_candies перед каждым тестовым методом в этом классе, даже если у самой фикстуры autouse=False.
@pytest.mark.usefixtures("empty_candies") 
class TestCandies:
    def test_count_candies(self, candies):
        for candy in candies:
            CandiesService.add(candy)

        assert CandiesService.count() == 3

    def test_list_candies(self, candies):
        for candy in candies:
            CandiesService.add(candy)
        candies_py = [c.model_dump(exclude={"id"}) for c in candies]
        all_candies = CandiesService.list()

        for added_candy in all_candies:
            assert added_candy in candies_py