# Sual 1 - 2

## Programlasdırma dillərinin ümumi iş prinsipi
Biz ümumilikdə kompüter proqramlarını yüksək səviyəli dillərdə yazırıq. Yüksək səviyəli dil, bizlər tərəfindən insan kimi başa düşülən dildir yəni bir sözlə biz yüksək səviyəli bir dildə kod yazarkən sanki bir insanla söhbət edirmişcəsinə kod yazırıq. Bizim yazdığımız kodlar qaynaq kodları adlandırlır.

Lakin, kompüter yüksək səviyəli dilləri başa düşə bilmir. O yalnız 0 və 1-lərdən ibarət olan ikilik say sistemində yazılmış proqramları başa düşür və bu maşın dili adlandırılır.

Qaynaq kodları maşın dilinə çevirmək üçün iki yoldan, "Tərtibçi"(Compiler) və "Tərcüməçi"(İnterpreter) istifadə olunur.

Həm tərtibçi həm də tərcüməçinin yüksək səviyəli dildə yazılmış kodları maşın dilinə çevirməsini kompüter başa düşür. Lakin bu metodların iş prinsiplərində fərqlər var.

## Tərcüməçi və Tərtibçinin iş prinsipləri arasındakı fərqlər
Tərcüməçi hər bir ifadəni bir-bir, Tərtibçi isə yazılmış kodu bütövlükdə yoxlayır və tam şəkildə maşın dilinə tərcümə edir.
Tərcüməçi adətən qaynaq kodu analiz etmək üçün az vaxt sərf edir, lakin ümumilikdə icra sürəti tərtibçidən daha yavaşdır. Tərtibçi isə adətən qaynaq kodu analiz üçün çox vaxt sərf edir, lakin ümumilikdə icra sürəti təcüməçidən sürətlidir.
Tərcüməçi aralıq obyekt kodlarını yaratmır, buna görə də yaddaş baxımından əl verişlidir. Amma tərtibçi bu obyekt kodlarını yaradır hansı ki sonralar əlaqələndirilməsi vacibdir, buna görə də daha çox yaddaş tələb edilir.
