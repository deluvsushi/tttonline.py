import requests
from time import time

class TTTOnline:
	def __init__(self):
		self.api = "https://keralamedia.online/crisscross"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Linux; Android 7.1.2; SM-G9880 Build/RP1A.2007201.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36",
			"x-requested-with": "com.web.tictactoeonlineplayers2"
		}
		self.player_id = None

	def check_username(self, username: str):
		return requests.get(
			f"{self.api}/check_username.php?pname={username}",
			headers=self.headers).json()

	def get_country(self):
		return requests.get(
			f"{self.api}/get_country.php",
			headers=self.headers).json()

	def get_date(self):
		return requests.get(
			f"{self.api}/get_date.php",
			headers=self.headers).json()

	def login(self, email: str):
		response = requests.get(
			f"{self.api}/login_user.php?pemail={email}",
			headers=self.headers).text
		self.player_id = response.split(":*")[0]
		return response

	def check_ban(self, player_id: int):
		return requests.get(
			f"{self.api}/check_ban.php?pid={player_id}",
			headers=self.headers).json()

	def update_profile(
			self,
			username: str,
			player_id: int,
			picture: str = "profiles/icon_add.png",
			score: int = 0,
			cs: int = 0,
			country_code: str = "sk"):
		return requests.get(
			f"{self.api}/update_pid.php?name={username}&pic={picture}&score={score}&pid={player_id}&cs={cs}&flager=https://flagcdn.com/48x36/{country_code}.png&city=NA",
			headers=self.headers).text

	def get_recent_players(self):
		return requests.get(
			f"{self.api}/get_recent.php",
			headers=self.headers).json()

	def get_player_defeats(self, player_id: int):
		return requests.get(
			f"{self.api}/get_defeats.php?pid={player_id}",
			headers=self.headers).json()		

	def get_top_20(self):
		return requests.get(
			f"{self.api}/get_top_20.php",
			headers=self.headers).text

	def get_player_email(self, player_id: int):
		return requests.get(
			f"{self.api}/get_email.php?pid={player_id}",
			headers=self.headers).json()

	def check_email(self, email: str):
		return requests.get(
			f"{self.api}/check_email.php?cemail={email}",
			headers=self.headers).json()

	def send_token(self, username: str, email: str):
		return requests.get(
			f"{self.api}/send_token.php?pemail={email}&pname={username}",
			headers=self.headers).json()

	def set_champions(self, player_id: int):
		return requests.get(
			f"{self.api}/set_champions.php?pid1={player_id}&pid2={player_id}",
			headers=self.headers).json()

	def set_email(self, player_id: int, email: str):
		return requests.get(
			f"{self.api}/set_final_email.php?pemail={email}&pid={player_id}",
			headers=self.headers).text
