record_in_seconds = float(input())
metres = float(input())
time_in_seconds = float(input())

total_time = metres * time_in_seconds

delay = metres // 15

total_time = total_time + (delay * 12.5)

if record_in_seconds > total_time:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

elif record_in_seconds <= total_time:

    print(f"No, he failed! He was {(total_time - record_in_seconds):.2f} seconds slower.")
