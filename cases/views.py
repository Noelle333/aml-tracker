from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.db.models import Count
from .models import Case
import csv

# Lista spraw z paginacją
def case_list(request):
    cases = Case.objects.all().order_by('-created_at')
    paginator = Paginator(cases, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cases/case_list.html', {'page_obj': page_obj})

# Szczegóły sprawy
def case_detail(request, pk):
    case = get_object_or_404(Case, pk=pk)
    return render(request, 'cases/case_detail.html', {'case': case})

# Dodawanie nowej sprawy
def add_case(request):
    if request.method == 'POST':
        Case.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            country=request.POST.get('country'),
            account_number=request.POST.get('account_number'),
            status=request.POST.get('status'),
            description=request.POST.get('description', '')
        )
        return redirect('case_list')
    return render(request, 'cases/add_case.html')

# Aktualizacja statusu
def update_case_status(request, pk):
    case = get_object_or_404(Case, pk=pk)
    if request.method == 'POST':
        case.status = request.POST.get('status')
        case.save()
    return redirect('case_list')

# Eksport do CSV
def export_cases_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="aml_cases.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Country', 'Account', 'Status', 'Created At'])

    for case in Case.objects.all():
        writer.writerow([case.first_name, case.last_name, case.country, case.account_number, case.status, case.created_at])

    return response

# Wykres Chart.js
def cases_chart(request):
    data = Case.objects.values('status').annotate(count=Count('id'))
    labels = [d['status'] for d in data]
    counts = [d['count'] for d in data]
    return render(request, 'cases/cases_chart.html', {'labels': labels, 'data': counts})
    

