from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Loan
from .serializers import LoanSerializer
from django.utils import timezone

@api_view(['GET', 'POST'])
def loan_list_create(request):
    if request.method == 'GET':
        loans = Loan.objects.select_related('book', 'reader').all()
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def loan_return(request, pk):
    try:
        loan = Loan.objects.get(pk=pk)
    except Loan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if loan.return_date:
        return Response(
            {"error": "Книга уже возвращена"},
            status=status.HTTP_400_BAD_REQUEST
        )

    loan.return_date = timezone.now().date()
    loan.save()
    # Обновим available_copies через save()
    return Response({"message": "Книга успешно возвращена"}, status=status.HTTP_200_OK)
