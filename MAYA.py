
# ملف تشغيل للوحدة المشفرة MAYA.cpython-312.so
import MAYA

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(MAYA, 'main'):
    MAYA.main()
else:
    print("تم استيراد MAYA بنجاح، ولكن لا توجد دالة main للتشغيل.")
