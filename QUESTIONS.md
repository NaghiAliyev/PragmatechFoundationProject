# Cavablar

## 1.Jinja template nədir? Necə istifadə olunur?

### Jinja nədir:
Jinja Python proqramlama dili üçün yardılmış bir veb şablonu yaratma maşınıdır. HTML səhifələrində Python bənzəri kodların yazılmasını təmin edir və əsas ütünlüklərindən biri HTML daxilində methodları argumentləri ilə çağırılmasıdır. Jinja version 2 yayımlandıqdan sonra sıx istifadə olduğuna görə Jinja 2 adlandırılıb, Jinja 2 Flaskın defolt şablon maşınıdır.
### Jinja necə istifadə olunur:
Jinja-nın tətbiq olunması üçün lazım olan xüsusi bir fayl strukturu vardır, əgər biz bu fayl strukturundakı adlar əvəzinə fərqli adlardan istifadə etmək istəyiriksə bu zaman Jinja daxilində defolt fayl adlarını dəyişdirməliyik. Defolt fayl adlarına misal olaraq bizim Python faylında dəyişdirdiyimiz hissələr "templates" faylında olur, bir digəri isə dəyişməyən faylların saxlandığı "static" faylıdır.

## 2.Database migration nədir və necə istifadə olunur?

### Database migration nədir:
Flaskda data migration üçün "flask_migrate" adlanan extension-dan istifadə olunur. "flask_migrate" "sqlalchemy" əsaslı database modelləri köçürmə (migrate) etmək üçündür.
### Flask-Migrate necə istifadə olunur:
"flask_migrate" paketini yükləmək üçün istifadə olunan terminal əmri: "pip install Flask-Migrate".
Paketi yüklədikdən sonra istifadə etmək üçün birinci əsas əmrlərimizi yazdığımız Python faylında  "migrate = Migrate(app, db)" əmrini yazmalıyıq burada app obyekti bizim flask app-imizdir, db obyekti isə sqlalchemy obyektidir, bundan sonra isə migrations faylının bizim application faylında yaranması üçün "flask db init" terminal əmrindən istifadə olunur.Dəyişikliklərin aşakar olunması üçün "flask db migrate -m 'Initial migration.' " terminal əmrindən istifadə edirik, dırnaq içərisində yazılan görülən işlər barəsində məlumat xarakteri daşıyan mətndir və sonda köçürmənin tamamlanması üçün "flask db upgrade" terminal əmrindən istifadə olunur.
