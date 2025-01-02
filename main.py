from datetime import date
import pandas as pd
from send_email import send_email

URL="EmailAutomator.csv"

def load_df(url):
    parse_dates=["Due_date","Reminder_date"]
    df=pd.read_csv(url,parse_dates=parse_dates)
    return df

def query_data_and_send_emails(df):
    present=date.today()
    email_counter=0
    for _,row in df.iterrows():
        if (present>=row['Reminder_date'].date()) and (row["Has_paid"]=="no"):
            send_email(
                subj=f"[Coding in Fun] Invoice:{row['Invoice_no']}",
                recv=row["Email"],
                name=row["Name"],
                due_date=row["Due_date"].strftime("%d, %b %Y"),
                invoice_no=row["Invoice_no"],
                amt=row["Amount"],
            )
            email_counter+=1
    return f"Total Emails Sent:{email_counter}"
df=load_df(URL)
result=query_data_and_send_emails(df)
print(result)