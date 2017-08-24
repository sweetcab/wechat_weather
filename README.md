# wechat_weather
This application is implmented to query the real time weather, which is deployed on Raspberry Pi and is connected to wechat.

## Usage
<p>1. To start the application:</p>
<pre><code>python weather_app.py
</code></pre>

<p>2. Scan the QR code with wechat. Accept on your mobile wechat and you will find "filehelper" in your list.</p>

<p>3. Query with the following commands:</p>
<pre><code>Beijing         # The current weather in Beijing
Beijing now     # The current weather in Beijing
Beijing tom     # The weather of tommorow in Beijing
Beijing days    # Three days forecast for Beijing
Beijing next    # Next few hours forecast for Beijing
Beijing week    # One week forecast for Beijing
</code></pre>

## Library dependencies
The following python libararies are needed:

<pre><code>PyOWM       # A Python wrapper around the OpenWeatherMap API
pytz        # World Timezone Definitions for Python
tzlocal     # tzinfo object for the local timezone
itchat      # A complete and graceful API for Wechat. 
</code></pre>


