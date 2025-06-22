
# ملف تشغيل للوحدة المشفرة red.cpython-312.so
import red

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(red, 'main'):
    red.main()
else:
    print("تم استيراد red بنجاح، ولكن لا توجد دالة main للتشغيل.")
