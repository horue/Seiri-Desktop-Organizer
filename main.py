from organizer import main
import time

while True:
    try:
        main()
        time.sleep(2)
    except Exception as e:
        print(f'Unexpected error: {e}')