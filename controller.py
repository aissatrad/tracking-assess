from google_play_scraper import app


def get_developer(app_id: str):
    return app(app_id).get("developerId")



