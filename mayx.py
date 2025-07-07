
# ملف تشغيل للوحدة المشفرة mayx.cpython-312.so
import mayx

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(mayx, 'main'):
    mayx.main()
else:
    print("تم استيراد mayx بنجاح، ولكن لا توجد دالة main للتشغيل.")
