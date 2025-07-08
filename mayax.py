
# ملف تشغيل للوحدة المشفرة mayax.cpython-312.so
import mayax

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(mayax, 'main'):
    mayax.main()
else:
    print("تم استيراد mayax بنجاح، ولكن لا توجد دالة main للتشغيل.")
