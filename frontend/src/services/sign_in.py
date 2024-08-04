from typing import Tuple
import httpx

from src.models.models import SignInModel


async def sign_in(url, data: SignInModel) -> Tuple[dict[str, str], bool]:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url=url, data=data.model_dump())
            if response.status_code == 200:
                return response.json(), True
            else:
                return response.json(), False
    except httpx.HTTPStatusError as e:
        print(e)
    except Exception as e:
        print(e)
