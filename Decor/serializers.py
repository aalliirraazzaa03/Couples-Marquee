from rest_framework import serializers
from Events.models import Event
from .models import Decor
from .models import Decor, DecorImage

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class DecorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decor
        fields = '__all__'


from .models import Decor
class DecorSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Decor
        fields = ['id', 'Date', 'DJ_amount', 'Cool_fire_count', 'Cool_fire_amount', 'ice_pot_count', 'ice_pot_amount']



# from rest_framework import serializers
from .models import DecorImage

class DecorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecorImage
        fields = ['id', 'image', 'uploaded_at']
