from datetime import datetime
today = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
with open("blank.txt", "a+") as myfile:
    myfile.write(f"Today's Date is {today}\n")
    myfile.seek(0)
    print(myfile.read())
