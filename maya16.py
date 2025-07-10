
# ملف تشغيل للوحدة المشفرة maya16.cpython-312.so
import maya16

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(maya16, 'main'):
    maya16.main()
else:
    print("تم استيراد maya16 بنجاح، ولكن لا توجد دالة main للتشغيل.")
