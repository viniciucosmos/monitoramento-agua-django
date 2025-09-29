from rest_framework import serializers 
from .models import Leituras 

class LeiturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leituras
        fields = ['id', 'temperatura', 'ph', 'tds', 'data_hora']

    #Validação -  ph entre 0 e 14
    def validate_ph(self, value):
        if not (0 <= value <= 14):
            raise serializers.ValidationError("O valor de pH deve estar entre 0 e 14")
        return value
     #Validação -  temp entre -10 e 100
    def validate_temperatura(self, value):
        if not (-10 <= value <= 100):
            raise serializers.ValidationError("Temperatura fora do intervalo permitido (-10 a 100°C)")
        return value
    
    #Validação -  tds entre 0 e 2000
    def validate_tds(self, value):
        if not (0 <= value <= 2000):
            raise serializers.ValidationError("TDS deve estar entre 0 e 2000 ppm.")
        return value