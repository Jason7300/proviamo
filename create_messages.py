from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import random

# This function allow us to create an HTML message to send
# You can edit all fields of message using HTML syntax

def create_item_html(items):
    response = []
    print(f'{5 * "*"} Creating post {5 * "*"}')

    # Shuffling items
    random.shuffle(items)

    # Iterate over items
    for item in items:
        # If item has an active offer
        if 'off' in item:
            # Creating buy button
            keyboard = [
                [InlineKeyboardButton("π Acquista ora π", callback_data='buy', url=item["url"])],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Creating message body

            html = ""
            html += f"π <b>{item['title']}</b> π\n\n"

            if 'description' in list(item.keys()):
                html += f"{item['description']}\n"

            html += f"<a href='{item['image']}'>&#8205</a>\n"

            if 'savings' in list(item.keys()):
                html += f"β Non piΓΉ: {item['original_price']}β¬ β\n\n"

            html += f"π° <b>Al prezzo di: {item['price']}</b> π°\n\n"

            if 'savings' in list(item.keys()):
                html += f"β <b>Risparmi: {item['savings']}β¬</b> β\n\n"

            html += f"<b><a href='{item['url']}'></a></b>"

            response.append(html)
            response.append(reply_markup)
    return response
