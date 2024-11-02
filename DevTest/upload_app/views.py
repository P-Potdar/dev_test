# upload_app/views.py
import pandas as pd
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import FileUploadForm
from django.conf import settings
from django.http import HttpResponse

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file) if file.name.endswith('.xlsx') else pd.read_csv(file)

            # Generate summary report
            state_counts = data['Cust State'].value_counts().to_dict()
            avg_dpd = data['DPD'].mean()
            max_dpd = data['DPD'].max()
            summary = f"Summary Report:\n\nTotal Entries: {len(data)}\nAverage DPD: {avg_dpd}\nMaximum DPD: {max_dpd}\n\nState Counts:\n"
            for state, count in state_counts.items():
                summary += f"{state}: {count}\n"

            # Send email
            send_mail(
                subject=f'Python Assignment - {request.user.get_full_name()}',
                message=summary,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['tech@themedius.ai']
            )

            return HttpResponse("File uploaded and summary sent successfully.")
    else:
        form = FileUploadForm()
    return render(request, 'upload_app/upload.html', {'form': form})
