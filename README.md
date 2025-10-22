# WattsTap - Flask приложение для Unity WebGL

Flask веб-приложение для развертывания Unity WebGL билда на Render.com.

## 🚀 Быстрый старт

### Локальная разработка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/denisislamov/WattsTapDeploy.git
cd WattsTapDeploy
```

2. Создайте виртуальное окружение и установите зависимости:
```bash
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Поместите файлы Unity WebGL билда в папку `unity_build/`:
```
unity_build/
├── Build.loader.js
├── Build.data
├── Build.framework.js
└── Build.wasm
```

4. Запустите приложение:
```bash
python app.py
```

Приложение будет доступно по адресу: http://localhost:5000

## 📦 Создание Unity WebGL билда

1. Откройте ваш Unity проект
2. **File** → **Build Settings**
3. Выберите платформу **WebGL**
4. Нажмите **Build**
5. Скопируйте файлы из папки `Build/` в `unity_build/`

Подробнее см. `unity_build/README.md`

## 🌐 Развертывание на Render.com

### Способ 1: Автоматическое развертывание (рекомендуется)

1. Запушьте код в GitHub:
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. Перейдите на [Render.com](https://render.com) и войдите
3. Нажмите **New** → **Web Service**
4. Подключите ваш GitHub репозиторий: `https://github.com/denisislamov/WattsTapDeploy.git`
5. Настройки будут автоматически подтянуты из `render.yaml`
6. Нажмите **Create Web Service**

### Способ 2: Ручная настройка

1. На Render.com создайте новый **Web Service**
2. Подключите GitHub репозиторий
3. Настройте параметры:
   - **Name**: wattstap (или любое другое имя)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free (или выберите другой план)

4. Нажмите **Create Web Service**

## 📁 Структура проекта

```
WattsTapDeploy/
├── app.py                 # Основное Flask приложение
├── requirements.txt       # Python зависимости
├── render.yaml           # Конфигурация для Render.com
├── .gitignore            # Игнорируемые файлы
├── README.md             # Этот файл
├── templates/
│   └── index.html        # HTML шаблон для Unity
└── unity_build/          # Unity WebGL билд файлы
    ├── README.md
    ├── Build.loader.js
    ├── Build.data
    ├── Build.framework.js
    └── Build.wasm
```

## 🔧 Конфигурация

### Переменные окружения

Приложение автоматически использует порт из переменной `PORT` (устанавливается Render.com).
Для локальной разработки используется порт 5000.

### Изменение настроек Unity билда

Если ваши файлы Unity имеют другие имена, измените пути в `templates/index.html`:
```javascript
var config = {
    dataUrl: buildUrl + "/YourBuild.data",
    frameworkUrl: buildUrl + "/YourBuild.framework.js",
    codeUrl: buildUrl + "/YourBuild.wasm",
    // ...
};
```

## 🛠️ Endpoints

- `/` - Главная страница с Unity WebGL билдом
- `/unity_build/<filename>` - Обслуживание файлов Unity билда
- `/health` - Health check endpoint (для мониторинга)

## ⚠️ Важные замечания

1. **Размер файлов**: Unity WebGL билды могут быть большими. Убедитесь, что Git LFS настроен, если файлы превышают 100MB.

2. **Бесплатный план Render**: На бесплатном плане сервис засыпает после 15 минут неактивности. Первая загрузка после пробуждения может занять 30-60 секунд.

3. **CORS**: Приложение настроено для корректной работы с Unity WebGL без проблем CORS.

4. **Компрессия**: Убедитесь, что в Unity включена Gzip компрессия для WebGL билда.

## 📝 Лицензия

Этот проект создан для развертывания Unity приложения WattsTap.

## 🤝 Поддержка

Если возникли проблемы:
1. Проверьте логи на Render.com
2. Убедитесь, что все файлы Unity билда загружены корректно
3. Проверьте, что `requirements.txt` содержит все необходимые зависимости

## 🔄 Обновление билда

Для обновления Unity билда:
1. Замените файлы в папке `unity_build/`
2. Закоммитьте и запушьте изменения:
```bash
git add unity_build/
git commit -m "Update Unity build"
git push origin main
```
3. Render автоматически пересоберет и задеплоит новую версию


