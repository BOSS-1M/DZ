
# ملف تشغيل للوحدة المشفرة ox.cpython-312.so
import ox

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(ox, 'main'):
    ox.main()
else:
    print("تم استيراد ox بنجاح، ولكن لا توجد دالة main للتشغيل.")
