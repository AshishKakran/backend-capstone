from rest_framework import serializers
from restaurant.models import Menu, Booking
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'Title', 'Price', 'Inventory']
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'Name', 'No_of_guests', 'Booking_date']
        read_only_fields = ['id']
        extra_kwargs = {
            'Name': {'required': True},
            'No_of_guests': {'required': True},
            'Booking_date': {'required': True}
        }