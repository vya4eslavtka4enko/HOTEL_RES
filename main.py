import pandas


df = pandas.read_csv('hotels.csv',dtype={'id':str})

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

print(df)
hotel_id = input("Enter the ID of the hotel ")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input("Enter you name ")
    reseration_ticket = ReservationTicket(name,hotel)
    print(reseration_ticket.generate())
else:
    print('Hotel is not free ')
