import httpx

from src.models.models import SignUpModel


async def sign_up(url, json_data: SignUpModel) -> bool:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url=url, json=json_data.model_dump())
            if response.status_code == 201:
                print(response.text)
                return True
            else:
                print(response.text)
                return False
    except httpx.HTTPStatusError as e:
        print(e)
        return False
    except Exception as e:
        print(e)
        return False
