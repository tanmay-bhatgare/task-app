import httpx
from src.models.models import TaskCreateModel


async def create_task(
    url: str,
    token: str,
    json_data: TaskCreateModel,
) -> bool:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url=f"{url}",
                json=json_data.model_dump(),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {token}",
                },
            )
            if response.status_code == 201:
                return True
            else:
                print(response.status_code, response.text)
                return False
    except httpx.RequestError as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return False
