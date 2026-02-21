import pandas as pd


def save_advanced_data(data_list, filename):
    if not data_list:
        print("❌ No data to save.")
        return

    # التأكد من أن الامتداد هو xlsx
    if not filename.endswith('.xlsx'):
        filename = filename.rsplit('.', 1)[0] + '.xlsx'

    # تحويل القائمة إلى Pandas DataFrame
    df = pd.DataFrame(data_list)

    # استخدام ExcelWriter لتنسيق الملف
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Jobs')

        # مهارة إضافية: ضبط عرض الأعمدة تلقائياً لتناسب المحتوى
        worksheet = writer.sheets['Jobs']
        for idx, col in enumerate(df.columns):
            max_len = max(df[col].astype(str).map(len).max(), len(col)) + 2
            worksheet.column_dimensions[chr(65 + idx)].width = min(max_len, 50)  # حد أقصى 50 للجمالية

    print(f"🎉 Excel file saved successfully: {filename}")

