from datetime import datetime
today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
with open("blank.txt", "a") as myfile:
    myfile.write(f"\nToday's Date in UTC is {today}")
    