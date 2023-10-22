from bs4 import BeautifulSoup
import smtplib
import requests
import lxml

# Web scraping section
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'
accept_language = 'en-US,en;q=0.9'
item_to_track = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'

# Email section
my_email = 'gtuvshin369@gmail.com'
password = 'vjvljjlgyfkibsba'


def send_email(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="gtuvshin369@gmail.com",
            msg=f'Subject:Low Price Alert!\n\n {message}'
        )


def check_price(desired_price: float):
    headers = {
        'User-Agent': user_agent,
        'Accept-Language': accept_language
    }

    response = requests.get(url=item_to_track, headers=headers)
    response.raise_for_status()
    contents = response.text

    soup = BeautifulSoup(contents, 'lxml')

    price_float = float(soup.find(name='span', class_='a-offscreen').text.replace('$', ''))
    item_name = soup.find(name='span', class_='a-size-large product-title-word-break').text.encode('utf-8').strip()

    if price_float < desired_price:
        print('Sending email')
        send_email(f'{item_name.decode("utf-8")} is now ${price_float}')
        print('Sent email')
    else:
        print('Price is still higher than desired value')


check_price(100)

