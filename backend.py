import requests


API_KEY = "bfb6db37ddda9a196d0f7667fd2d434a"


def get_data(city, forecast_days=None):
	url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
	response = requests.get(url)
	data = response.json()
	# Filtering Data by FORECAST DAYS
	filtered_data = data["list"]
	num_value = 8 * forecast_days
	filtered_data = filtered_data[:num_value]
	# Filtering Data by CHOICE
	return filtered_data


if __name__=="__main__":
	print(get_data(city="Seoul", forecast_days=3))