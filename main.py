import pandas


df = pandas.read_csv('hotels.csv',dtype={'id':str})
df_card = pandas.read_csv('cards.csv', dtype= str).to_dict(orient='records')
class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()
    def book(self):
        """Book a hotel by changing its availability to no"""
        availability = df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv',index = False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        print(availability)
        if availability=="yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self,customer_name,hotel_obect):
        self.customer_name = customer_name
        self.hotel = hotel_obect
    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name:{self.customer_name}
        Hotel:{self.hotel.hotel_name}
        """
        return content
class CreditCard():
    def __init__(self,number):
        self.number = number
    def valid(self,expiration,holder,cvc):
        card_data = {'number':self.number,'expiration':expiration,'holder':holder,'cvc':cvc}
        if  card_data in df_card:
            return True
        else:
            return False


print(df)
hotel_id = input("Enter the ID of the hotel ")
hotel = Hotel(hotel_id)

if hotel.available():
    credit_card = CreditCard(number='1234')
    if credit_card.valid(expiration='12/26',holder='JOHN SMITH',cvc='123'):
        hotel.book()
        name = input("Enter you name ")
        reseration_ticket = ReservationTicket(name,hotel)
        print(reseration_ticket.generate())
    else:
        print('There was a problem with payment')
else:
    print('Hotel is not free ')
