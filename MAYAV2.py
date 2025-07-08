
# ملف تشغيل للوحدة المشفرة MAYAV2.cpython-312.so
import MAYAV2

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(MAYAV2, 'main'):
    MAYAV2.main()
else:
    print("تم استيراد MAYAV2 بنجاح، ولكن لا توجد دالة main للتشغيل.")
