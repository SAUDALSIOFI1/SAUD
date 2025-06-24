import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
from datetime import datetime
import os
# تثبيت المكتبات عن طريق امر 
# إعداد التصميم العام للرسوم البيانية
sns.set_style("whitegrid")
sns.set_palette("husl")
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['axes.unicode_minus'] = False

# دالة لقراءة ملف Excel
def read_excel_file(file_path):
    """قراءة ملف Excel وإرجاع قاموس يحتوي على جميع الجداول"""
    sheets_dict = {}
    xls = pd.ExcelFile(file_path)
    
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        sheets_dict[sheet_name] = df
    
    return sheets_dict

# دالة لتحليل الجدول الرئيسي (جدول 1)
def analyze_main_table(df):
    """تحليل الجدول الرئيسي لمؤشرات سوق العمل"""
    print("\n" + "="*50)
    print("تحليل الجدول الرئيسي لمؤشرات سوق العمل")
    print("="*50)
    
    # التحقق من أبعاد DataFrame
    print(f"أبعاد الجدول: {df.shape}")
    
    try:
        # استخراج البيانات المهمة مع التحقق من وجود الأعمدة
        data = {
            'معدل البطالة': {
                'سعودي ذكور': df.iloc[8, 2] if df.shape[1] > 2 else 'غير متوفر',
                'سعودي إناث': df.iloc[8, 3] if df.shape[1] > 3 else 'غير متوفر',
                'سعودي إجمالي': df.iloc[8, 4] if df.shape[1] > 4 else 'غير متوفر',
                'غير سعودي ذكور': df.iloc[8, 5] if df.shape[1] > 5 else 'غير متوفر',
                'غير سعودي إناث': df.iloc[8, 6] if df.shape[1] > 6 else 'غير متوفر',
                'غير سعودي إجمالي': df.iloc[8, 7] if df.shape[1] > 7 else 'غير متوفر',
                'إجمالي ذكور': df.iloc[8, 8] if df.shape[1] > 8 else 'غير متوفر',
                'إجمالي إناث': df.iloc[8, 9] if df.shape[1] > 9 else 'غير متوفر',
                'إجمالي عام': df.iloc[8, 10] if df.shape[1] > 10 else 'غير متوفر'
            },
            'معدل المشتغلين من السكان في سن العمل': {
                'سعودي ذكور': df.iloc[9, 2] if df.shape[1] > 2 else 'غير متوفر',
                'سعودي إناث': df.iloc[9, 3] if df.shape[1] > 3 else 'غير متوفر',
                'سعودي إجمالي': df.iloc[9, 4] if df.shape[1] > 4 else 'غير متوفر',
                'غير سعودي ذكور': df.iloc[9, 5] if df.shape[1] > 5 else 'غير متوفر',
                'غير سعودي إناث': df.iloc[9, 6] if df.shape[1] > 6 else 'غير متوفر',
                'غير سعودي إجمالي': df.iloc[9, 7] if df.shape[1] > 7 else 'غير متوفر',
                'إجمالي ذكور': df.iloc[9, 8] if df.shape[1] > 8 else 'غير متوفر',
                'إجمالي إناث': df.iloc[9, 9] if df.shape[1] > 9 else 'غير متوفر',
                'إجمالي عام': df.iloc[9, 10] if df.shape[1] > 10 else 'غير متوفر'
            },
            'معدل المشاركة في القوى العاملة': {
                'سعودي ذكور': df.iloc[10, 2] if df.shape[1] > 2 else 'غير متوفر',
                'سعودي إناث': df.iloc[10, 3] if df.shape[1] > 3 else 'غير متوفر',
                'سعودي إجمالي': df.iloc[10, 4] if df.shape[1] > 4 else 'غير متوفر',
                'غير سعودي ذكور': df.iloc[10, 5] if df.shape[1] > 5 else 'غير متوفر',
                'غير سعودي إناث': df.iloc[10, 6] if df.shape[1] > 6 else 'غير متوفر',
                'غير سعودي إجمالي': df.iloc[10, 7] if df.shape[1] > 7 else 'غير متوفر',
                'إجمالي ذكور': df.iloc[10, 8] if df.shape[1] > 8 else 'غير متوفر',
                'إجمالي إناث': df.iloc[10, 9] if df.shape[1] > 9 else 'غير متوفر',
                'إجمالي عام': df.iloc[10, 10] if df.shape[1] > 10 else 'غير متوفر'
            }
        }
        
        # عرض النتائج
        for category, values in data.items():
            print(f"\n{category}:")
            for key, value in values.items():
                print(f"{key}: {value}")
        
        # رسم بياني لمعدل البطالة حسب الجنسية والجنس (فقط للبيانات المتوفرة)
        plt.figure(figsize=(12, 6))
        unemployment_data = {}
        
        if df.shape[1] > 4:
            unemployment_data['سعودي'] = [data['معدل البطالة']['سعودي ذكور'], data['معدل البطالة']['سعودي إناث']]
        if df.shape[1] > 7:
            unemployment_data['غير سعودي'] = [data['معدل البطالة']['غير سعودي ذكور'], data['معدل البطالة']['غير سعودي إناث']]
        if df.shape[1] > 9:
            unemployment_data['إجمالي'] = [data['معدل البطالة']['إجمالي ذكور'], data['معدل البطالة']['إجمالي إناث']]
        
        if unemployment_data:
            df_unemployment = pd.DataFrame(unemployment_data, index=['ذكور', 'إناث'])
            df_unemployment.plot(kind='bar', rot=0)
            plt.title('معدل البطالة حسب الجنسية والجنس - الربع الأول 2024')
            plt.ylabel('النسبة المئوية (%)')
            plt.xlabel('الجنس')
            plt.legend(title='الجنسية')
            plt.tight_layout()
            plt.savefig('unemployment_by_gender_nationality.png')
            plt.close()
            print("\nتم حفظ الرسم البياني لمعدل البطالة في ملف 'unemployment_by_gender_nationality.png'")
        else:
            print("\nلا توجد بيانات كافية لإنشاء الرسم البياني لمعدل البطالة")
            
    except Exception as e:
        print(f"\nحدث خطأ أثناء تحليل الجدول الرئيسي: {str(e)}")

# باقي الدوال تبقى كما هي بدون تغيير
# [يتبع باقي الكود كما هو مع تعديلات مشابهة للتحقق من الأبعاد في كل دالة]

# دالة رئيسية لتشغيل التحليل
def main():
    # قراءة ملف Excel
    file_path = 'LM tables_Q1_2024_AR_1.xlsx'
    
    if not os.path.exists(file_path):
        print(f"خطأ: الملف '{file_path}' غير موجود في المسار الحالي.")
        return
    
    print("جارٍ تحليل ملف إحصاءات سوق العمل...")
    sheets = read_excel_file(file_path)
    
    # عرض أسماء الجداول المتوفرة
    print("\nالجداول المتوفرة في الملف:")
    for sheet_name in sheets.keys():
        print(f"- {sheet_name}")
    
    # تحليل الجداول الرئيسية
    if '1' in sheets:
        analyze_main_table(sheets['1'])
    else:
        print("\nتحذير: الجدول الرئيسي (1) غير موجود في الملف")
    
    # [يتبع باقي الكود كما هو مع إضافة تحقق من وجود الجداول]
    
    print("\nتم الانتهاء من تحليل ملف إحصاءات سوق العمل!")

if __name__ == "__main__":
    main()