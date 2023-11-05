from rest_framework import serializers


try:

    from home.models import Product
    from home.models import Account

except:
    pass 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Product
        except:
            pass    
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Account
        except:
            pass    
        fields = '__all__'

