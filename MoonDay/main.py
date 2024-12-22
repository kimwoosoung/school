from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import ephem
from datetime import datetime, timedelta

app = FastAPI()

def get_moon_phase(date):
    moon = ephem.Moon(date)
    phase = moon.phase

    if phase < 1.0:
        moon_emoji = "🌑" 
        phase_name = "New Moon"
    elif phase < 7.4:
        moon_emoji = "🌒" 
        phase_name = "Waxing Crescent"
    elif phase < 14.8:
        moon_emoji = "🌓"
        phase_name = "First Quarter"
    elif phase < 22.1:
        moon_emoji = "🌔" 
        phase_name = "Waxing Gibbous"
    elif phase < 29.5:
        moon_emoji = "🌕" 
        phase_name = "Full Moon"
    elif phase < 36.9:
        moon_emoji = "🌖" 
        phase_name = "Waning Gibbous"
    elif phase < 44.3:
        moon_emoji = "🌗" 
        phase_name = "Last Quarter"
    else:
        moon_emoji = "🌘"
        phase_name = "Waning Crescent"

    return moon_emoji, phase_name, phase

@app.get("/", response_class=HTMLResponse)
async def show_moon():
    today = datetime.now()
    tomorrow = today + timedelta(days=1)

    today_moon_emoji, today_phase_name, today_phase = get_moon_phase(today)
    tomorrow_moon_emoji, tomorrow_phase_name, tomorrow_phase = get_moon_phase(tomorrow)

    html_content = f"""
    <html>
        <head>
            <title>오늘과 내일의 달 모양</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    background-image: url('https://i1.sndcdn.com/artworks-eTPnNF3ZSx0xVsFi-XO0z2g-t500x500.jpg');
                    background-size: cover;
                    background-position: center;
                    color: white;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }}
                .content {{
                    text-align: center;
                }}
                h1, h2 {{
                    color: #fff;
                }}
                .moon {{
                    font-size: 80px;
                    text-align: center;
                    display: block;
                    margin: 10px 0;
                }}
                .today-moon {{
                    font-size: 120px;
                    color: #FFD700;
                }}
                .tomorrow-moon {{
                    font-size: 50px;
                    color: #B0B0B0;
                }}
                .phase-name {{
                    font-size: 20px;
                    color: #888;
                }}
                .phase-percentage {{
                    font-size: 18px;
                    color: #ccc;
                }}
                .moon-container {{
                    margin-bottom: 50px;
                }}
            </style>
        </head>
        <body>
            <div class="content">
                <h1>오늘과 내일의 달 모양</h1>
                <div class="moon-container">
                    <h2>오늘의 달 ({today.strftime('%Y-%m-%d')})</h2>
                    <div class="moon today-moon">{today_moon_emoji}</div>
                    <p class="phase-name">{today_phase_name}</p>
                    <p class="phase-percentage">달의 단계: {today_phase:.1f}%</p>
                </div>
                <div class="moon-container">
                    <h2>내일의 달 ({tomorrow.strftime('%Y-%m-%d')})</h2>
                    <div class="moon tomorrow-moon">{tomorrow_moon_emoji}</div>
                    <p class="phase-name">{tomorrow_phase_name}</p>
                    <p class="phase-percentage">달의 단계: {tomorrow_phase:.1f}%</p>
                </div>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
