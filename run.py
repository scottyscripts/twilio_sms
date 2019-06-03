from flask import Flask, render_template, request
import os
from twilio.rest import Client

TWILIO_ACCOUNT_SFID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
# must be valid twilio number including '+' and country code ( /+\d{11}/ )
SENDER = os.environ.get('TWILIO_NUMBER')

app = Flask(__name__)

@app.route('/message')
def message_form():
  return render_template('message_form.html', sender=SENDER[1:])

@app.route('/message/send', methods=['POST'])
def send():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message_text = request.form['message']
    recipient_country_code = request.form['recipient_country_code']
    recipient_10_digit_num = request.form['recipient_10_digit_num']

    recipient = f'+{recipient_country_code}{recipient_10_digit_num}'

    message = client.messages \
                    .create(
                         body=message_text,
                         from_=SENDER,
                         to=recipient
                     )

    return 'message sent'

if __name__ == "__main__":
  app.run(debug=True)
