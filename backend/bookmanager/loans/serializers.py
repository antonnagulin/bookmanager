from rest_framework import serializers
from loans.models import Loan
from datetime import date


class LoanSerializer(serializers.ModelSerializer):
    loan_date = serializers.DateField(format='%d.%m.%Y', input_formats=['%d.%m.%Y'], required=False)
    due_date = serializers.DateField(format='%d.%m.%Y', input_formats=['%d.%m.%Y'], required=False)
    return_date = serializers.DateField(format='%d.%m.%Y', input_formats=['%d.%m.%Y'], required=False)

    class Meta:
        model = Loan
        fields = '__all__'


    def create(self, validated_data):
        # Если loan_date не передан, ставим сегодняшнюю дату
        if 'loan_date' not in validated_data:
            validated_data['loan_date'] = date.today()

        return super().create(validated_data)
