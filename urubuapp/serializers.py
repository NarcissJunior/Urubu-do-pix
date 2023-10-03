from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		user_model = UserModel
		fields = ('id', 'name')

class WalletSerializer(serializers.HyperlinkedModelSerialize):
    class Meta:
        wallet_model = WalletModel