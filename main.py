import pandas


df = pandas.read_csv('hotels.csv',dtype={'id':str})
df_card = pandas.read_csv('cards.csv', dtype= str).to_dict(orient='records')
df_card_security = pandas.read_csv('card_security.csv', dtype=str)
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
    @classmethod
    def get_hotel_count(cls,data):
        return len(data)

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
class SecureCreditCard(CreditCard):
    def authenticate(self,give_pass):
        password = df_card_security.loc[df_card_security['number']==self.number,'password'].squeeze()
        if password == give_pass:
            return True
        else:
            return False
class SpaReservation(ReservationTicket):
    def spa_resevation(self):
        content = f"""
                Thank you for your spa reservation!
                Here are you booking data:
                Name:{self.customer_name}
                Hotel:{self.hotel.hotel_name}
                """
        return content
print(df)
hotel_id = input("Enter the ID of the hotel ")
hotel = Hotel(hotel_id)
print(Hotel.get_hotel_count(data=df))
#
# if hotel.available():
#     credit_card = SecureCreditCard(number='1234')
#     if credit_card.valid(expiration='12/26',holder='JOHN SMITH',cvc='123'):
#         if credit_card.authenticate(give_pass = 'mypass'):
#             hotel.book()
#             name = input("Enter you name ")
#             reseration_ticket = SpaReservation(name,hotel)
#             print(reseration_ticket.generate())
#             spa_reservation = str(input('Do you want spa package '))
#             if spa_reservation == 'yes':
#                 print(reseration_ticket.spa_resevation())
#             else:
#                 print('ok')
#         else:
#             print('Not correct password')
#     else:
#         print('There was a problem with payment')
# else:
#     print('Hotel is not free ')
