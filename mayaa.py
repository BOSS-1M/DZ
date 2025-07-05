
# ملف تشغيل للوحدة المشفرة mayaa.cpython-312.so
import mayaa

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(mayaa, 'main'):
    mayaa.main()
else:
    print("تم استيراد mayaa بنجاح، ولكن لا توجد دالة main للتشغيل.")
