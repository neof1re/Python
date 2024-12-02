import time

def auto_stop_stopwatch(duration):
    print("Секундомер запущен и остановится через 10 секунд.")
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        elapsed_time = time.time() - start_time
        print(f"Прошло времени: {int(elapsed_time)} секунд")
        time.sleep(1)

    print(f"Секундомер остановлен. Прошло времени: {duration} секунд.")

if __name__ == "__main__":
    auto_stop_stopwatch(10)