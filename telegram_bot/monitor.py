import subprocess

if __name__ == '__main__':
    while True:
        try:
            subprocess.run(["/home/str/30ise/.venv/bin/python", "/home/str/30ise/start_all_bot.py"])
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Ошибка: {e}")
