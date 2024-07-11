import time
import datetime

current_time = time.time()
#print(f"Current time in seconds since the epoch: {current_time}\n")

formatted_time_with_commas = f"{current_time:,.7f}"
formatted_time_scientific = f"{current_time:.2e}"
print(f"Seconds since January 1, 1970: {formatted_time_with_commas} or {formatted_time_scientific} in scientific notation")