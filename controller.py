from google_play_scraper import app


async def get_developer(app_id: str):
    result = await app(app_id)
    return result.get("developerId")
