import pandas as pd
import os
import uuid
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']

        try:
            # Read Excel file
            df = pd.read_excel(file)

            # Sanitize column names
            df.rename(columns=lambda x: x.strip().replace(" ", "_"), inplace=True)

            # Calculate total and average
            df["Total"] = df["Sub1"] + df["Sub2"] + df["Sub3"]
            df["Average"] = df["Total"] / 3

            # Result logic
            df["Result"] = df.apply(
                lambda row: "Passed" if row["Sub1"] >= 40 and row["Sub2"] >= 40 and row["Sub3"] >= 40 else "Failed",
                axis=1
            )

            # Separate passed and failed students
            passed_df = df[df["Result"] == "Passed"]
            failed_df = df[df["Result"] == "Failed"]

            # Create folder if doesn't exist
            export_path = os.path.join(settings.MEDIA_ROOT, 'exports')
            os.makedirs(export_path, exist_ok=True)

            # Generate unique filenames
            passed_file = os.path.join(export_path, f'passed_{uuid.uuid4().hex}.xlsx')
            failed_file = os.path.join(export_path, f'failed_{uuid.uuid4().hex}.xlsx')

            # Save files
            passed_df.to_excel(passed_file, index=False)
            failed_df.to_excel(failed_file, index=False)

            # Save just the file names to pass to template
            context = {
                'message': 'File processed successfully!',
                'passed_file': os.path.basename(passed_file),
                'failed_file': os.path.basename(failed_file),
                'table_data': df.to_dict(orient='records')
            }

            return render(request, 'marks/upload.html', context)

        except Exception as e:
            return render(request, 'marks/upload.html', {'message': f'Error: {str(e)}'})

    return render(request, 'marks/upload.html')
