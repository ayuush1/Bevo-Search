import os.path
import base64
import csv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels and retrieves all messages received by specific email addresses.
    Saves the results in a CSV file.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API to list labels
        service = build("gmail", "v1", credentials=creds)
        
        # Specify the email addresses to filter messages received by
        specific_emails = ["ayush.pokharel8@gmail.com"]
        query = " OR ".join([f"to:{email}" for email in specific_emails])

        results = service.users().messages().list(
            userId="me",
            labelIds=["INBOX"],
            q=query,
            maxResults=5
        ).execute()

        messages = results.get("messages", [])

        # Define the path for saving the CSV file
        csv_path = "./emails_received.csv"

        with open(csv_path, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            # Write the header row
            writer.writerow(["From", "Subject", "Message"])

            if not messages:
                print("No messages received by the specified email addresses.")
            else:
                for message in messages:
                    msg = service.users().messages().get(userId="me", id=message["id"]).execute()
                    email_data = msg["payload"]["headers"]

                    from_name = ""
                    subject = ""
                    for values in email_data:
                        if values["name"] == "From":
                            from_name = values["value"]
                        if values["name"] == "Subject":
                            subject = values["value"]

                    # Get the email body content (text/plain or text/html)
                    message_content = ""
                    for part in msg["payload"].get("parts", []):
                        if part["mimeType"] in ["text/plain", "text/html"]:
                            data = base64.urlsafe_b64decode(part["body"]["data"]).decode("utf-8")
                            message_content = data
                            break  # Get only the first text part

                    # Write row data into the CSV
                    writer.writerow([from_name, subject, message_content])

            print(f"Email data saved to {csv_path}")

    except HttpError as error:
        # Handle errors from the Gmail API
        print(f"An error occurred: {error}")

if __name__ == "__main__":
  main()
