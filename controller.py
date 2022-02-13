from google_play_scraper import app


def get_developer(app_id: str):
    result: str
    try:
        rs = app(app_id)
        result = rs.get("developerId")
    except Exception as e:
        result = "Unknown"
        print(e)
    return result
