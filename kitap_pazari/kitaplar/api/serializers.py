
from rest_framework import serializers
from kitaplar.models import Kitap, Yorum

class YorumSerializer(serializers.ModelSerializer):
   comment_own = serializers.StringRelatedField(read_only=True)
   class Meta:
      model = Yorum
      # fields = '__all__'
      exclude = ['kitap']



class KitapSerializer(serializers.ModelSerializer):
   comment = YorumSerializer(many=True, read_only=True)
   class Meta:
      model = Kitap
      fields = '__all__'

