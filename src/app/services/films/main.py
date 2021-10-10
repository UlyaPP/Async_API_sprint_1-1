from logging import getLogger

from app.elastic import IndexNameEnum
from app.services.base import (
    BaseService,
    MethodEnum,
    exc_handled,
)
from app.services.films.exceptions import BaseFilmsServiceError
from app.services.films.schemas import FilmSchema
from app.services.schemas import DocSchema

logger = getLogger(__name__)


class FilmsService(BaseService):
    # @cached()  # TODO
    @exc_handled(logger, BaseFilmsServiceError)
    async def get_by_id(self, film_id: str) -> FilmSchema | None:
        doc = await self._request(
            method=MethodEnum.get.value, index=IndexNameEnum.movies.value, id=film_id
        )
        return FilmSchema(**DocSchema(**doc).source)
